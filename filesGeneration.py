import ctypes
import json
import re
import sys
from pathlib import WindowsPath, Path
from typing import Any, Dict, List, Union

# -----------------------------------------
RAYPYC_FOLDER_PATH = Path(__file__).parent / 'raypyc'
DYNAMIC_LIBRARIES_PATH = RAYPYC_FOLDER_PATH / 'libs'

wrapped_defines_names = []

wrapped_colors_names = []

wrapped_enums_names = []

wrapped_structures_names = []
wrapped_structures_names_stub = []

wrapped_aliases_names = []

wrapped_functions_names_stub = []

if sys.platform == 'linux':
	_raylib_dynamic_library_name = 'libraylib.so'
else:  # windows
	_raylib_dynamic_library_name = 'raylib.dll'

if sys.platform == 'linux':
	_raypyc_extra_functions_name = 'raypyc_extra_functions.so'
else:  # windows
	_raypyc_extra_functions_name = 'raypyc_extra_functions.dll'

_raylib_dynamic_library = ctypes.cdll.LoadLibrary(str(DYNAMIC_LIBRARIES_PATH / _raylib_dynamic_library_name))
_raypyc_extra_functions = ctypes.cdll.LoadLibrary(str(DYNAMIC_LIBRARIES_PATH / _raypyc_extra_functions_name))


# -----------------------------------------


# -----------------------------------------
def find_char_in_str(string: str, char: str) -> List[int]:
	"""get the indexes of a char in a string"""
	return [i for i, ltr in enumerate(string) if ltr == char]


def underscore(_string: str) -> str:
	_string = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', _string)
	_string = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', _string)
	_string = _string.replace("-", "_")
	return _string.lower()


def is_string_contained_in_list(_string: str, _list: List[str]) -> bool:
	for _item in _list:
		if _item in _string:
			return True
	return False


def generate_file(file_path: WindowsPath) -> None:
	if Path(file_path).exists():
		with open(Path(file_path), "w"):  # if the file exists we clean it
			pass
	else:
		print(f"the {file_path} doesn't exist, regenerating a new one")
		with open(file_path, "x"):
			pass


def add_text_to_file(file_path: WindowsPath, _string: str) -> None:
	with open(Path(file_path), "a") as file:
		file.write(_string)


def convert_c_type_to_python_type(c_type_string: str) -> str:
	"""convert c type string to ctype type sting"""
	c_string_to_ctypes_string = {
		'bool': 'c_bool',  # C type: _Bool  Python type: bool (1)
		'char': 'c_char',  # C type: char  Python type: 1-character bytes object
		'wchar_t': 'c_wchar',  # C type: wchar_t  Python type: 1-character string
		# 'char': c_byte,  # C type: char  Python type: int
		'unsignedchar': 'c_ubyte',  # C type: unsigned char  Python type: int
		'short': 'c_short',  # C type: short  Python  # type: int
		'unsignedshort': 'c_ushort',  # C type: unsigned short  Python type: int
		'int': 'c_int',  # C type: int  Python type: int
		'unsignedint': 'c_uint',  # C type: unsigned int  Python type: int
		'long': 'c_long',  # C type: long  Python type: int
		'unsignedlong': 'c_ulong',  # C type: unsigned long  Python type: int
		'uint64': 'c_longlong',  # C type: __int64 or long-long  Python type: int
		'unsigneduint64': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
		'unsignedlonglong': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
		'size_t': 'c_size_t',  # C type: unsigned size_t  Python type: int
		'ssize_t': 'c_ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
		'float': 'c_float',  # C type: float  Python type: float
		'double': 'c_double',  # C type: double  Python type: float
		'longdouble': 'c_longdouble',  # C type: long double  Python type: float
		'char*': 'c_char_p',  # C type: char* (NUL terminated)  Python type: bytes object or None
		'wchar_t*': 'c_wchar_p',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
		'void*': 'c_void_p',  # C type: wchar_t* (NUL terminated)  Python type: int or None
		'void': 'None',  # C type: void  Python type: None
	}

	c_type_string = c_type_string.replace(' ', '').replace('const', '')  # remove spaces, and "const" because there isn't really a const type in python...
	is_array = ']' in c_type_string
	pointer_level = c_type_string.count("*")

	if c_type_string == 'void':  # void shouldn't be in the form of ctypes.None
		return "None"

	if c_type_string in c_string_to_ctypes_string:  # "regular" value not a pointer or an array
		return "ctypes." + c_string_to_ctypes_string[c_type_string]

	if is_array and pointer_level > 0:  # array of pointers to structures
		type_of_array = c_type_string.split('[')[0]
		array_size = c_type_string.split('[')[1][:-1]
		type_of_array_without_pointers = type_of_array.replace('*', '')
		if type_of_array in c_string_to_ctypes_string:  # basic type pointer (int*, char*, float*, ...)
			return f"ctypes.{c_string_to_ctypes_string[type_of_array]} * {array_size}"
		if type_of_array_without_pointers in c_string_to_ctypes_string:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
			type_of_array_end = c_string_to_ctypes_string[type_of_array_without_pointers]
			for i in range(pointer_level):
				type_of_array_end = f"ctypes.POINTER({type_of_array_end})"
			return f"ctypes.{type_of_array_end} * {array_size}"
		else:  # a struct array pointer level 1+ or just a pointer level 1
			type_of_array_end = type_of_array_without_pointers
			for i in range(pointer_level):
				type_of_array_end = f"ctypes.POINTER({type_of_array_end})"
			return f"{type_of_array_end} * {array_size}"
	elif is_array:
		type_of_array = c_type_string.split('[')[0]
		array_size = c_type_string.split('[')[1][:-1]
		if type_of_array in c_string_to_ctypes_string:  # basic type array (int, char, float, ...)
			return f"ctypes.{c_string_to_ctypes_string[type_of_array]} * {array_size}"
		else:  # a struct array
			return f"{type_of_array} * {array_size}"
	elif pointer_level > 0:
		type_without_pointers = c_type_string.replace('*', '')
		if c_type_string in c_string_to_ctypes_string:  # basic type pointer (int*, char*, float*, ...)
			return f"ctypes.{c_string_to_ctypes_string[c_type_string]}"
		if type_without_pointers in c_string_to_ctypes_string:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
			type_of_pointer_end = "ctypes." + c_string_to_ctypes_string[type_without_pointers]
			for i in range(pointer_level):
				type_of_pointer_end = f"ctypes.POINTER({type_of_pointer_end})"
			return f"{type_of_pointer_end}"
		else:  # a struct pointer level 1+ or just a pointer level 1
			type_of_pointer_end = c_type_string.replace('*', '')
			for i in range(pointer_level):
				type_of_pointer_end = f"ctypes.POINTER({type_of_pointer_end})"
			return f"{type_of_pointer_end}"

	return c_type_string  # a struct


# -----------------------------------------
def generate_color_code(define_data: Dict[str, Union[str, float, int]], for_stub: bool = False) -> str:
	if define_data['type'] == "COLOR":
		ints_array_string = define_data['value'].split('{')[1].split('}')[0].replace(' ', '').split(',')
		temp = f"{define_data['name']}: raypyc.structures.Color"
		if not for_stub:
			temp += f" = raypyc.structures.Color({ints_array_string[0]}, {ints_array_string[1]}, {ints_array_string[2]}, {ints_array_string[3]})"
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp
	else:
		return ""


def generate_define_code(define_data: Dict[str, Union[str, float, int]], for_stub: bool = False) -> str:
	if not define_data['type'] in ["FLOAT_MATH", "FLOAT", "DOUBLE", "STRING", "INT"]:
		return ""

	elif define_data['type'] == "FLOAT_MATH":
		temp = f"{define_data['name']}: float"
		if not for_stub:
			temp += f" = {define_data['value'].replace('f', '')}"
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp

	elif define_data['type'] == "INT":
		temp = f"{define_data['name']}: int"
		if not for_stub:
			temp += f" = {define_data['value']}"
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp

	elif define_data['type'] in ["DOUBLE", "FLOAT"]:
		temp = f"{define_data['name']}: float"
		if not for_stub:
			temp += f" = {define_data['value']}"
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp

	elif define_data['type'] == "STRING":
		temp = f"{define_data['name']}: str"
		if not for_stub:
			temp += f" = \"{define_data['value']}\""
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp
	else:
		return ""


def generate_dummy_struct_code(struct_name: str, bytes_size: int, for_stub: bool = False) -> str:
	_string = f"class {struct_name}(ctypes.Structure):\n\t\"\"\"dummy structure\"\"\"\n"
	if not for_stub:
		_string += f"\t_fields_ = [\n\t\t(\"buffer\", ctypes.c_byte * {bytes_size})\n\t]\n\n"
	else:
		_string += f"\t@property\n\tdef buffer(self) -> ctypes.c_byte * {bytes_size}:\n"
		_string += f"\t\t...\n\n"
		_string += f"\t@buffer.setter\n\tdef buffer(self, i: ctypes.c_byte * {bytes_size}) -> None:\n"
		_string += f"\t\t...\n\n"

	return _string


def generate_struct_code(struct_data: Dict[str, Union[str, List[Dict[str, str]]]], for_stub: bool = False) -> str:
	_string = ""
	struct_fields = ""
	struct_setters_getters_string = ""
	_string += f"class {struct_data['name']}(ctypes.Structure):\n\t\"\"\"{struct_data['description']}\"\"\"\n"

	if not for_stub:
		struct_fields = "\t_fields_ = [\n"
		for struct_data_field in struct_data['fields']:
			struct_fields += f"\t\t('{struct_data_field['name']}', {convert_c_type_to_python_type(struct_data_field['type'])}),"
			if struct_data_field['description'] != "":
				struct_fields += f"  # {struct_data_field['description']}"
			struct_fields += '\n'
		temp = find_char_in_str(struct_fields, ',')
		if len(temp) != 0:
			struct_fields = struct_fields[: temp[-1]] + struct_fields[temp[-1] + 1:]
		struct_fields += '\t]\n\n'
	_string += struct_fields

	if for_stub:
		for struct_data_field in struct_data['fields']:
			use_type = convert_c_type_to_python_type(struct_data_field['type'])
			struct_setters_getters_string += f"\t@property\n\tdef {struct_data_field['name']}(self) -> {use_type}:\n"
			struct_setters_getters_string += f"\t\t...\n\n"
			struct_setters_getters_string += f"\t@{struct_data_field['name']}.setter\n\tdef {struct_data_field['name']}(self, i: {use_type}) -> None:\n"
			struct_setters_getters_string += f"\t\t...\n\n"
	_string += struct_setters_getters_string

	return _string


def generate_alias_code(alias_name: str, object_name: str) -> str:
	return f"{alias_name} = {object_name}\n"


def generate_enum_code(enum_data, for_stub=False):
	_string = ""
	_string += f"class {enum_data['name']}(enum.IntEnum):\n"
	if enum_data['description'] != '':
		_string += f"\t\"\"\"{enum_data['description']}\"\"\"\n"

	for value in enum_data['values']:
		_string += f"\t{value['name']}: int"
		if not for_stub:
			_string += f" = {value['value']}"
		if value['description'] != '':
			_string += f"  # {value['description']}"
		_string += "\n"

	_string += "\n"

	return _string


def generate_function_signature_code(function_data: Dict[str, Union[str, List[Dict[str, str]]]]) -> str:
	function_string = f"def {function_data['name']}("
	if 'params' in function_data.keys():  # only return stuff
		for param in function_data['params']:
			function_string += f"{param['name']}: {convert_c_type_to_python_type(param['type'])}, "

		function_string = function_string[:-2]

	function_string += ") -> "
	function_string += f"{convert_c_type_to_python_type(function_data['returnType'])}:\n\t\"\"\"{function_data['description']}\"\"\"\n\t...\n\n"

	return function_string


# -----------------------------------------
def generate_colors_code(defines_api: List[Dict[str, Union[str, float, int]]], for_stub: bool = False) -> str:
	_string = ""
	for define in defines_api:
		if for_stub or define['name'] not in wrapped_defines_names:
			color_string_logic = generate_color_code(define, for_stub)
			if color_string_logic != "":
				wrapped_defines_names.append(define['name'])
				color_string_logic += "\n"

			_string += color_string_logic
	return _string


def generate_defines_code(defines_api: List[Dict[str, Union[str, float, int]]], for_stub: bool = False) -> str:
	_string = ""
	for define in defines_api:
		if for_stub or define['name'] not in wrapped_defines_names:
			define_string_logic = generate_define_code(define, for_stub)
			if define_string_logic != "":
				wrapped_defines_names.append(define['name'])
				define_string_logic += "\n"

			_string += define_string_logic
	return _string


def generate_dummy_structs_code(names: List[str], for_stub: bool = False) -> str:
	_string = ""
	for name in names:
		function_of_size = _raypyc_extra_functions.__getattr__(f"Get{name}Size")
		function_of_size.argtypes = None
		function_of_size.restype = ctypes.c_int

		dummy_struct_code = generate_dummy_struct_code(name, int(function_of_size()), for_stub)
		if dummy_struct_code != "":
			dummy_struct_code += "\n"

		_string += dummy_struct_code
	return _string


def generate_structs_aliases_code(structs_api: List[Union[Dict[str, Union[str, List[Dict[str, str]]]], Any]], aliases_api: List[Union[Dict[str, str], Any]], for_stub: bool = False) -> str:
	_string = ""
	if not for_stub:
		_wrapped_structures_names = wrapped_structures_names
	else:
		_wrapped_structures_names = wrapped_structures_names_stub
	for struct in structs_api:
		if struct['name'] not in _wrapped_structures_names:
			struct_string_logic = generate_struct_code(struct, for_stub)
			if struct_string_logic != "":
				_wrapped_structures_names.append(struct['name'])
				struct_string_logic += "\n"

			_string += struct_string_logic

			for alias in aliases_api:
				if struct['name'] == alias['type']:
					if alias['name'] not in _wrapped_structures_names:
						alias_string_logic = ""
						alias_string_logic += generate_alias_code(alias['name'], struct['name'])
						if alias_string_logic != "":
							_wrapped_structures_names.append(alias['name'])
						alias_string_logic += "\n\n"

						_string += alias_string_logic

	return _string


def generate_structures_dictionary_code(wrapped_structures: List[str], for_stub: bool = False) -> str:
	if not for_stub:
		dictionary_sting = "__structs = {\n"
		for struct in wrapped_structures:
			dictionary_sting += f"\t\"{struct}\": {struct},\n"
		dictionary_sting = dictionary_sting[:-2]
		dictionary_sting += "\n}\n"
		return dictionary_sting
	else:
		dictionary_sting = "__structs: dict[str, Type["
		for struct in wrapped_structures:
			dictionary_sting += f"{struct} | "
		dictionary_sting = dictionary_sting[:-3]
		dictionary_sting += "]] = {\n\t...\n}\n"
		return dictionary_sting


def generate_enums_code(enums_api, for_stub=False):
	_string = ""
	for enum in enums_api:
		if for_stub or enum['name'] not in wrapped_enums_names:
			enum_string_logic = generate_enum_code(enum, for_stub)
			if enum_string_logic != "":
				wrapped_enums_names.append(enum['name'])
				enum_string_logic += "\n"

			_string += enum_string_logic
	return _string


def check_for_functions_that_can_wrap(functions_api: List[Union[Any, Dict[str, Union[str, List[Dict[str, str]]]], Dict[str, str]]]) -> List[Union[Any, Dict[str, Union[str, List[Dict[str, str]]]], Dict[str, str]]]:
	functions_that_can_be_wrap = []
	functions_that_cant_be_wrap = []

	for function in functions_api:
		do_wrapper_this_function = True
		if 'params' in function.keys():
			for function_param in function['params']:
				if is_string_contained_in_list(function_param['type'], ['Sound', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']):
					do_wrapper_this_function = False
					break

		if do_wrapper_this_function:
			if is_string_contained_in_list(function['returnType'], ['Sound', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']):
				do_wrapper_this_function = False

		if do_wrapper_this_function:
			functions_that_can_be_wrap.append(function)
		else:
			functions_that_cant_be_wrap.append(function)

	return functions_that_can_be_wrap


def generate_functions_code(functions_set: List[Union[Any, Dict[str, Union[str, List[Dict[str, str]]]], Dict[str, str]]]) -> str:
	_string = ""
	for function in functions_set:
		if function['name'] not in wrapped_functions_names_stub:
			wrapped_functions_names_stub.append(function['name'])
			function_copy = function.copy()
			name_of_function = underscore(function['name']).replace('3_d', '_3d').replace('2_d', '_2d').replace('vector_2', 'vector2_').replace('vector_3', 'vector3_')
			function_copy['name'] = name_of_function
			_string += generate_function_signature_code(function_copy)
	return _string


# -----------------------------------------

# load config data
with open(Path(RAYPYC_FOLDER_PATH / 'config_api.json')) as reader:
	config_api = json.load(reader)

config_api_defines = config_api['defines']
config_api_structs = config_api['structs']
config_api_aliases = config_api['aliases']
config_api_enums = config_api['enums']
config_api_functions = config_api['functions']

# load rlgl data
with open(Path(RAYPYC_FOLDER_PATH / 'rlgl_api.json')) as reader:
	rlgl_api = json.load(reader)

rlgl_api_defines = rlgl_api['defines']
rlgl_api_structs = rlgl_api['structs']
rlgl_api_aliases = rlgl_api['aliases']
rlgl_api_enums = rlgl_api['enums']
rlgl_api_functions = rlgl_api['functions']

# load raylib data
with open(Path(RAYPYC_FOLDER_PATH / 'raylib_api.json')) as reader:
	raylib_api = json.load(reader)

raylib_api_defines = raylib_api['defines']
raylib_api_structs = raylib_api['structs']
raylib_api_aliases = raylib_api['aliases']
raylib_api_enums = raylib_api['enums']
raylib_api_functions = raylib_api['functions']

# load raymath data
with open(Path(RAYPYC_FOLDER_PATH / 'raymath_api.json')) as reader:
	raymath_api = json.load(reader)

raymath_api_defines = raymath_api['defines']
raymath_api_structs = raymath_api['structs']
raymath_api_aliases = raymath_api['aliases']
raymath_api_enums = raymath_api['enums']
raymath_api_functions = raymath_api['functions']

# load raygui data
with open(Path(RAYPYC_FOLDER_PATH / 'raygui_api.json')) as reader:
	raygui_api = json.load(reader)

raygui_api_defines = raygui_api['defines']
raygui_api_structs = raygui_api['structs']
raygui_api_aliases = raygui_api['aliases']
raygui_api_enums = raygui_api['enums']
raygui_api_functions = raygui_api['functions']

# -----------------------------------------
# note that we have to generate the none stub-code first, because we need all the wrapped_*_names lists to be updated first
# -----------------------------------------

# generate colors files and add import stuff
generate_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py')
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', 'import raypyc\n\n\n')
generate_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi')
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', 'import raypyc\n\n\n')

# generate colors code and add colors code to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', generate_colors_code(config_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', generate_colors_code(rlgl_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', generate_colors_code(raylib_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', generate_colors_code(raymath_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', generate_colors_code(raygui_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', generate_colors_code(config_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', generate_colors_code(rlgl_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', generate_colors_code(raylib_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', generate_colors_code(raymath_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', generate_colors_code(raygui_api_defines, for_stub=True))
# -----------------------------------------

# generate defines files
generate_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py')
generate_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi')

# generate defines code ans add defines code to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py', generate_defines_code(config_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py', generate_defines_code(rlgl_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py', generate_defines_code(raylib_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py', generate_defines_code(raymath_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.py', generate_defines_code(raygui_api_defines, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi', generate_defines_code(config_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi', generate_defines_code(rlgl_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi', generate_defines_code(raylib_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi', generate_defines_code(raymath_api_defines, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'defines/__init__.pyi', generate_defines_code(raygui_api_defines, for_stub=True))
# -----------------------------------------

# generate structures files and add import stuff
generate_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py')
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', 'import ctypes\nfrom raypyc.defines import *\n\n\n')
generate_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi')
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', 'import ctypes\nfrom raypyc.defines import *\nfrom typing import Type\n\n\n')

# generate dummy structures code and add dummy structures code to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_dummy_structs_code(['rAudioBuffer', 'rAudioProcessor'], for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_dummy_structs_code(['rAudioBuffer', 'rAudioProcessor'], for_stub=True))

# generate structures code add structures code to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structs_aliases_code(config_api_structs, config_api_aliases, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structs_aliases_code(rlgl_api_structs, rlgl_api_aliases, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structs_aliases_code(raylib_api_structs, raylib_api_aliases, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structs_aliases_code(raymath_api_structs, raymath_api_aliases, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structs_aliases_code(raygui_api_structs, raygui_api_aliases, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structs_aliases_code(config_api_structs, config_api_aliases, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structs_aliases_code(rlgl_api_structs, rlgl_api_aliases, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structs_aliases_code(raylib_api_structs, raylib_api_aliases, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structs_aliases_code(raymath_api_structs, raymath_api_aliases, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structs_aliases_code(raygui_api_structs, raygui_api_aliases, for_stub=True))

# generate structures-dictionary code and add structures-dictionary to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.py', generate_structures_dictionary_code(wrapped_structures_names, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'structures/__init__.pyi', generate_structures_dictionary_code(wrapped_structures_names_stub, for_stub=True))
# -----------------------------------------

# generate enums files and add import stuff
generate_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py')
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', 'import enum\n\n\n')
generate_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi')
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', 'import enum\n\n\n')

# generate enums code and add enums code to files
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', generate_enums_code(config_api_enums, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', generate_enums_code(rlgl_api_enums, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', generate_enums_code(raylib_api_enums, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', generate_enums_code(raymath_api_enums, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.py', generate_enums_code(raygui_api_enums, for_stub=False))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', generate_enums_code(config_api_enums, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', generate_enums_code(rlgl_api_enums, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', generate_enums_code(raylib_api_enums, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', generate_enums_code(raymath_api_enums, for_stub=True))
add_text_to_file(RAYPYC_FOLDER_PATH / 'enums/__init__.pyi', generate_enums_code(raygui_api_enums, for_stub=True))

# -----------------------------------------

generate_file(RAYPYC_FOLDER_PATH / '__init__.pyi')
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', 'import ctypes\nfrom raypyc.defines import *\nfrom raypyc.defines import *\nfrom raypyc.colors import *\nfrom raypyc.enums import *\nfrom raypyc.structures import *\n\n\n')

# check what function can be wrapped
config_functions_to_wrapped = check_for_functions_that_can_wrap(config_api_functions)
rlgl_functions_to_wrapped = check_for_functions_that_can_wrap(rlgl_api_functions)
raylib_functions_to_wrapped = check_for_functions_that_can_wrap(raylib_api_functions)
raymath_functions_to_wrapped = check_for_functions_that_can_wrap(raymath_api_functions)
raygui_functions_to_wrapped = check_for_functions_that_can_wrap(raygui_api_functions)

# add the functions signature strings files
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', generate_functions_code(config_functions_to_wrapped))
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', generate_functions_code(rlgl_functions_to_wrapped))
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', generate_functions_code(raylib_functions_to_wrapped))
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', generate_functions_code(raymath_functions_to_wrapped))
add_text_to_file(RAYPYC_FOLDER_PATH / '__init__.pyi', generate_functions_code(raygui_functions_to_wrapped))
