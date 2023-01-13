import ctypes
import json
import sys
from pathlib import Path

# -----------------------------------------
RAYPYC_FOLDER_PATH = Path(__file__).parent / 'raypyc'
DYNAMIC_LIBRARIES_PATH = Path(__file__).parent / 'raypyc/libs'

wrapped_defines_names = []

wrapped_colors_names = []

wrapped_enums_names = []

wrapped_structures_names = []

wrapped_aliases_names = []

wrapped_functions_names_pyi = []

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
def indent_string(string: str, indent_by: int) -> str:
	"""return a string that indented in the start of the string and in every \\n of the string"""
	return '\t' * indent_by + string.replace('\n', '\n\t' * indent_by)


def generate_file(file_path):
	if Path(file_path).exists():
		with open(Path(file_path), "w"):  # if the file exists we clean it
			pass
	else:
		print(f"the {file_path} doesn't exist, regenerating a new one")
		with open(file_path, "x"):
			pass


def add_text_to_file(file_path, _string):
	with open(Path(file_path), "a") as file:
		file.write(_string)


def convert_c_type_string_to_ctypes_type_sting(c_type_string):
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
def generate_color_code(define_data, for_stub=False):
	if define_data['type'] == "COLOR":
		ints_array_string = define_data['value'].split('{')[1].split('}')[0].replace(' ', '').split(',')
		temp = f"{define_data['name']}: raypyc.structures.Color"
		if not for_stub:
			temp += f" = raypyc.structures.Color({ints_array_string[0]}, {ints_array_string[1]}, {ints_array_string[2]}, {ints_array_string[3]})"
		temp += f"{('  # ' + define_data['description']) if define_data['description'] != '' else ''}"
		return temp
	else:
		return ""


# -----------------------------------------
def generate_colors_code(defines_api, for_stub=False):
	_string = ""
	for define in defines_api:
		if for_stub or define['name'] not in wrapped_defines_names:
			wrapped_defines_names.append(define['name'])
			define_string_logic = generate_color_code(define, for_stub)
			if define_string_logic != "":
				define_string_logic += "\n"

			_string += define_string_logic
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

# generate colors files and add import stuff
generate_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py')
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.py', 'import raypyc\n\n\n')
generate_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi')
add_text_to_file(RAYPYC_FOLDER_PATH / 'colors/__init__.pyi', 'import raypyc\n\n\n')

# generate colors code add colors code to files
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
