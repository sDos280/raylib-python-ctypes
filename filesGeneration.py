import ctypes
import json
import sys
from pathlib import Path

# -----------------------------------------
LIBRARY_FOLDER_PATH = Path(__file__).parent / 'raypyc'
JSON_FOLDER_PATH = Path(__file__).parent / 'raypyc'
DYNAMIC_LIBRARIES_PATH = Path(__file__).parent / 'raypyc/libs'

wrapped_defines_names = []

wrapped_colors_names = []

wrapped_enums_names = []

wrapped_structures_names = []

wrapped_functions_names = []

if sys.platform == 'linux':
	_raylib_dynamic_library_name = 'libraylib.so'
else:  # windows
	_raylib_dynamic_library_name = 'raylib.dll'

if sys.platform == 'linux':
	_raypyc_extra_functions_name = 'raypyc_extra_functions.so'
else:  # windows
	_raypyc_extra_functions_name = 'raypyc_extra_functions.dll'

_raypyc_extra_functions = ctypes.cdll.LoadLibrary(str(DYNAMIC_LIBRARIES_PATH / _raypyc_extra_functions_name))


# -----------------------------------------

def indent_string(string: str, indent_by: int) -> str:
	"""return a string that indented in the start of the string and in every \\n of the string"""
	return '\t' * indent_by + string.replace('\n', '\n\t' * indent_by)


def generate_file(file_path):
	if Path(file_path).exists():
		with open(Path(file_path), "w"):
			pass
	else:
		print(f"the {file_path} doesn't exist, regenerating a new one")
		with open(file_path, "x"):
			pass
		with open(Path(file_path), "w"):
			pass


def add_text_to_file(file_path, _string):
	with open(Path(file_path), "a") as file:
		file.write(_string)


def generate_define_code(define_data):
	if define_data['type'] not in ["FLOAT_MATH", "FLOAT", "DOUBLE", "STRING", "INT"]:
		return ""
	elif define_data['type'] == "FLOAT_MATH":
		return f"DEF {define_data['name']} = {define_data['value'].replace('f', '')}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
	elif define_data['type'] in ["INT"]:
		return f"DEF {define_data['name']} = {define_data['value']}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
	elif define_data['type'] in ["DOUBLE", "FLOAT"]:
		return f"DEF {define_data['name']} = {define_data['value']}{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
	elif define_data['type'] == "STRING":
		return f"DEF {define_data['name']} = \"{define_data['value']}\"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
	else:
		return ""


def generate_defines_code(defines_api):
	_string = ""
	for define in defines_api:
		if define['name'] not in wrapped_defines_names:
			wrapped_defines_names.append(define['name'])
			define_string_logic = generate_define_code(define)
			if define_string_logic != "":
				define_string_logic += "\n"

			_string += define_string_logic
	return _string


def generate_enum_code(enum_data):
	_string = ('#  ' + enum_data['description'] + '\n') if enum_data['description'] != '' else ''
	_string += f"cdef enum {enum_data['name']}:\n"
	for index, value in enumerate(enum_data['values']):
		_description = ('  #  ' + value['description'] + '\n') if value['description'] != '' else '\n'
		_string += f"\t{value['name']} = {value['value']},"
		if index == len(enum_data['values']) - 1:
			_string = _string[:-1]
		_string += _description
	return _string


def generate_enums_code(enums_api):
	_string = ""
	for enum in enums_api:
		if enum['name'] not in wrapped_enums_names:
			wrapped_enums_names.append(enum['name'])
			enum_string_logic = generate_enum_code(enum)
			if enum_string_logic != "":
				enum_string_logic += "\n\n"

			_string += enum_string_logic
	return _string


def generate_dummy_struct_code(struct_name, bytes_size):
	return f"#  dummy structure\nctypedef struct {struct_name}:\n\tsigned char[{bytes_size}] data;\n"


def generate_dummy_structs_code(names):
	_string = ""
	for name in names:
		function_of_size = _raypyc_extra_functions.__getattr__(f"Get{name}Size")
		function_of_size.argtypes = None
		function_of_size.restype = ctypes.c_int

		dummy_struct_code = generate_dummy_struct_code(name, int(function_of_size()))
		if dummy_struct_code != "":
			dummy_struct_code += "\n\n"

		_string += dummy_struct_code
	return _string


def generate_struct_code(struct_data):
	_string = f"#  {struct_data['description']}\nctypedef struct {struct_data['name']}:\n"
	for field in struct_data['fields']:
		_string += f"\t{field['type'] if field['type'] != 'bool' else 'bint'} {field['name']};{('  # ' + field['description']) if field['description'] != '' else ''}\n"
	return _string


def generate_alias_code(alias_data):
	_description = ('#  ' + alias_data['description'] + '\n') if alias_data['description'] != '' else ''
	return f"{_description}ctypedef {alias_data['type']} {alias_data['name']}\n"


def generate_structs_code(structs_api, aliases_api):
	_string = ""
	for struct in structs_api:
		if struct['name'] not in wrapped_structures_names:
			wrapped_structures_names.append(struct['name'])
			struct_string_logic = generate_struct_code(struct)
			if struct_string_logic != "":
				struct_string_logic += "\n"

			_string += struct_string_logic
		for alias in aliases_api:
			if struct['name'] == alias['type']:
				if alias['name'] not in wrapped_structures_names:
					wrapped_structures_names.append(alias['name'])
					alias_string_logic = generate_alias_code(alias)
					if alias_string_logic != "":
						alias_string_logic += "\n"

					_string += alias_string_logic
	return _string


def generate_function_code(function_data):
	_string = function_data['returnType'] if function_data['returnType'] != 'bool' else 'bint'
	_string += ' ' + function_data['name'] + '('
	parameters = function_data.get('params')

	if parameters is None:

		_string += ');' + (('  # ' + function_data['description']) if function_data['description'] != '' else '')
		_string += '\n'
		return _string
	else:
		for parameter in parameters:
			if parameter['type'] in ['SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback', 'AudioCallback', '...']:
				return ''
			_temp = True
			_string += f"{parameter['type'] if parameter['type'] != 'bool' else 'bint'} {parameter['name']}, "
		_string = _string[:-2]
		_string += ');'
		_string += ('  # ' + function_data['description']) if function_data['description'] != '' else ''
		_string += '\n'
		return _string


def generate_functions_code(functions_api):
	_string = ""
	for function in functions_api:
		if function['name'] not in wrapped_functions_names:
			wrapped_functions_names.append(function['name'])
			_string += generate_function_code(function)
	return _string


# -----------------------------------------
# load config data
with open(Path(JSON_FOLDER_PATH / 'config_api.json')) as reader:
	config_api = json.load(reader)

config_api_defines = config_api['defines']
config_api_structs = config_api['structs']
config_api_aliases = config_api['aliases']
config_api_enums = config_api['enums']
config_api_functions = config_api['functions']
# -----------------------------------------

# -----------------------------------------
# load rlgl data
with open(Path(JSON_FOLDER_PATH / 'rlgl_api.json')) as reader:
	rlgl_api = json.load(reader)

rlgl_api_defines = rlgl_api['defines']
rlgl_api_structs = rlgl_api['structs']
rlgl_api_aliases = rlgl_api['aliases']
rlgl_api_enums = rlgl_api['enums']
rlgl_api_functions = rlgl_api['functions']
# -----------------------------------------

# -----------------------------------------
# load raylib data
with open(Path(JSON_FOLDER_PATH / 'raylib_api.json')) as reader:
	raylib_api = json.load(reader)

raylib_api_defines = raylib_api['defines']
raylib_api_structs = raylib_api['structs']
raylib_api_aliases = raylib_api['aliases']
raylib_api_enums = raylib_api['enums']
raylib_api_functions = raylib_api['functions']
# -----------------------------------------

# -----------------------------------------
# load raymath data
with open(Path(JSON_FOLDER_PATH / 'raymath_api.json')) as reader:
	raymath_api = json.load(reader)

raymath_api_defines = raymath_api['defines']
raymath_api_structs = raymath_api['structs']
raymath_api_aliases = raymath_api['aliases']
raymath_api_enums = raymath_api['enums']
raymath_api_functions = raymath_api['functions']
# -----------------------------------------

# -----------------------------------------
# load raygui data
with open(Path(JSON_FOLDER_PATH / 'raygui_api.json')) as reader:
	raygui_api = json.load(reader)

raygui_api_defines = raygui_api['defines']
raygui_api_structs = raygui_api['structs']
raygui_api_aliases = raygui_api['aliases']
raygui_api_enums = raygui_api['enums']
raygui_api_functions = raygui_api['functions']
# -----------------------------------------

config_defines_code = generate_defines_code(config_api_defines)
rlgl_defines_code = generate_defines_code(rlgl_api_defines)
raylib_defines_code = generate_defines_code(raylib_api_defines)
raymath_defines_code = generate_defines_code(raymath_api_defines)
raygui_defines_code = generate_defines_code(raygui_api_defines)

config_enums_code = generate_enums_code(config_api_enums)
rlgl_enums_code = generate_enums_code(rlgl_api_enums)
raylib_enums_code = generate_enums_code(raylib_api_enums)
raymath_enums_code = generate_enums_code(raymath_api_enums)
raygui_enums_code = generate_enums_code(raygui_api_enums)

dummy_structs_code = indent_string(generate_dummy_structs_code(['rAudioBuffer', 'rAudioProcessor']), 1) + "\n"
config_structs_code = indent_string(generate_structs_code(config_api_structs, config_api_aliases), 1) + "\n"
rlgl_structs_code = indent_string(generate_structs_code(rlgl_api_structs, rlgl_api_aliases), 1) + "\n"
raylib_structs_code = indent_string(generate_structs_code(raylib_api_structs, raylib_api_aliases), 1) + "\n"
raymath_structs_code = indent_string(generate_structs_code(raymath_api_structs, raymath_api_aliases), 1) + "\n"
raygui_structs_code = indent_string(generate_structs_code(raygui_api_structs, raygui_api_aliases), 1) + "\n"

config_functions_code = indent_string(generate_functions_code(config_api_functions), 1) + "\n"
rlgl_functions_code = indent_string(generate_functions_code(rlgl_api_functions), 1) + "\n"
raylib_functions_code = indent_string(generate_functions_code(raylib_api_functions), 1) + "\n"
raymath_functions_code = indent_string(generate_functions_code(raymath_api_functions), 1) + "\n"
raygui_functions_code = indent_string(generate_functions_code(raygui_api_functions), 1)[:-1] + "\n"

generate_file(LIBRARY_FOLDER_PATH / '__init__.pxd')

add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', config_defines_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', rlgl_defines_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raylib_defines_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raymath_defines_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raygui_defines_code)

add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', config_enums_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', rlgl_enums_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raylib_enums_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raymath_enums_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raygui_enums_code)

add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', 'cdef extern from "config.h":\n')
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', dummy_structs_code)  # we add the dummy structs earliest as possible
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', config_structs_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', config_functions_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', 'cdef extern from "rlgl.h":\n')
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', rlgl_structs_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', rlgl_functions_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', 'cdef extern from "raylib.h":\n')
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raylib_structs_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raylib_functions_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', 'cdef extern from "raymath.h":\n')
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raymath_structs_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raymath_functions_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', 'cdef extern from "raygui.h":\n')
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raygui_structs_code)
add_text_to_file(LIBRARY_FOLDER_PATH / '__init__.pxd', raygui_functions_code)
