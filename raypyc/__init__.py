import ctypes
import json
import pathlib
import re
import sys
import platform

import raypyc.structures
from raypyc.colors import *
from raypyc.defines import *
from raypyc.enums import *
from raypyc.structures import *

# -----------------------------------------
wrapped_functions_names = []

current_module = __import__(__name__)

DYNAMIC_LIBRARIES_PATH = pathlib.Path(__file__).parent / 'libs'

if sys.platform == 'emscripten':
	dllname = 'wasmraylib.so'
elif sys.platform == 'linux':
	dllname = 'libraylib.so'
elif platform.machine() == 'aarch64': # pydroid
	dllname = 'libraylibandroid.so'
else:  # windows
	dllname = 'raylib.dll'

_raylib_dynamic_library = ctypes.cdll.LoadLibrary(str(pathlib.Path(__file__).parent / DYNAMIC_LIBRARIES_PATH / dllname))


# -----------------------------------------

def evaluate_c_type_string_to_python_type(c_type_string):
	c_string_to_ctypes_string = {
		'bool': ctypes.c_bool,  # C type: _Bool  Python type: bool (1)
		'char': ctypes.c_char,  # C type: char  Python type: 1-character bytes object
		'wchar_t': ctypes.c_wchar,  # C type: wchar_t  Python type: 1-character string
		# 'char': c_byte,  # C type: char  Python type: int
		'unsignedchar': ctypes.c_ubyte,  # C type: unsigned char  Python type: int
		'short': ctypes.c_short,  # C type: short  Python  # type: int
		'unsignedshort': ctypes.c_ushort,  # C type: unsigned short  Python type: int
		'int': ctypes.c_int,  # C type: int  Python type: int
		'unsignedint': ctypes.c_uint,  # C type: unsigned int  Python type: int
		'long': ctypes.c_long,  # C type: long  Python type: int
		'unsignedlong': ctypes.c_ulong,  # C type: unsigned long  Python type: int
		'uint64': ctypes.c_longlong,  # C type: __int64 or long-long  Python type: int
		'unsigneduint64': ctypes.c_ulonglong,  # C type: unsigned __int64 or unsigned long-long  Python type: int
		'unsignedlonglong': ctypes.c_ulonglong,  # C type: unsigned __int64 or unsigned long-long  Python type: int
		'size_t': ctypes.c_size_t,  # C type: unsigned size_t  Python type: int
		'ssize_t': ctypes.c_ssize_t,  # C type: ssize_t or Py_ssize_t  Python type: int
		'float': ctypes.c_float,  # C type: float  Python type: float
		'double': ctypes.c_double,  # C type: double  Python type: float
		'longdouble': ctypes.c_longdouble,  # C type: long double  Python type: float
		'char*': ctypes.c_char_p,  # C type: char* (NUL terminated)  Python type: bytes object or None
		'wchar_t*': ctypes.c_wchar_p,  # C type: wchar_t* (NUL terminated)  Python type: string object or None
		'void*': ctypes.c_void_p,  # C type: wchar_t* (NUL terminated)  Python type: int or None
		'void': None,  # C type: void  Python type: None
	}

	c_type_string = c_type_string.replace(' ', '').replace('const', '')  # remove spaces, and "const" because there isn't really a const type in python...
	is_array = ']' in c_type_string
	pointer_level = c_type_string.count("*")

	if c_type_string == "...":
		return None

	if is_array and pointer_level > 0:  # array of pointers to structures
		type_of_array_string = c_type_string.split('[')[0]
		array_size = int(c_type_string.split('[')[1][:-1])
		type_of_array_without_pointers_string = type_of_array_string.replace('*', '')

		if type_of_array_string in c_string_to_ctypes_string:  # basic type pointer (int*, char*, float*, ...)
			return c_string_to_ctypes_string[type_of_array_string] * array_size

		if type_of_array_without_pointers_string in c_string_to_ctypes_string:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
			type_of_array_end = c_string_to_ctypes_string[type_of_array_without_pointers_string]
			for i in range(pointer_level):
				type_of_array_end = ctypes.POINTER(type_of_array_end)
			return type_of_array_end * array_size

		if type_of_array_without_pointers_string in raypyc.structures.__structs:  # a struct array pointer level 1+ or just a pointer level 1
			type_of_array_end = raypyc.structures.__structs[type_of_array_without_pointers_string]
			for i in range(pointer_level):
				type_of_array_end = ctypes.POINTER(type_of_array_end)
			return type_of_array_end * array_size

		raise TypeError(f"can wrapped this string, the string: {c_type_string}")

	elif is_array:
		type_of_array_string = c_type_string.split('[')[0]
		array_size = int(c_type_string.split('[')[1][:-1])

		if type_of_array_string in c_string_to_ctypes_string:  # basic type array (int, char, float, ...)
			return c_string_to_ctypes_string[type_of_array_string] * array_size

		if type_of_array_string in raypyc.structures.__structs:  # a struct array
			return raypyc.structures.__structs[type_of_array_string] * array_size

		raise TypeError(f"can wrapped this string, the string: {c_type_string}")

	elif pointer_level > 0:
		if c_type_string in c_string_to_ctypes_string:  # basic type pointer (int**, char*, float*, ...)
			return c_string_to_ctypes_string[c_type_string]

		type_without_pointers_string = c_type_string.replace('*', '')

		if type_without_pointers_string in c_string_to_ctypes_string:  # basic type pointer(probably double+ pointer level) (int**, char**, float**, ...)
			type_of_pointer_end = c_string_to_ctypes_string[type_without_pointers_string]
			for i in range(pointer_level):
				type_of_pointer_end = ctypes.POINTER(type_of_pointer_end)
			return type_of_pointer_end

		if type_without_pointers_string in raypyc.structures.__structs:  # a struct pointer level 1+ or just a pointer level 1
			type_of_pointer_end = raypyc.structures.__structs[type_without_pointers_string]
			for i in range(pointer_level):
				type_of_pointer_end = ctypes.POINTER(type_of_pointer_end)
			return type_of_pointer_end

		raise TypeError(f"can wrapped this string, the string: {c_type_string}")

	if c_type_string in c_string_to_ctypes_string:  # "regular" value not a pointer or an array
		return c_string_to_ctypes_string[c_type_string]

	if c_type_string in raypyc.structures.__structs:  # a struct
		return raypyc.structures.__structs[c_type_string]

	raise TypeError(f"can wrapped this string, the string: {c_type_string}")


def is_string_contained_in_list(_string: str, _list: list[str]) -> bool:
	for _item in _list:
		if _item in _string:
			return True
	return False


# get numbers from string
def get_numbers_from_string(string):
	ints = []
	for s in string.split(' '):
		if s.isdigit():
			ints.append(int(s))
	return ints


def underscore(_string):
	_string = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', _string)
	_string = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', _string)
	_string = _string.replace("-", "_")
	return _string.lower()


def wrap_function(funcname, _argtypes, _restype):
	func = _raylib_dynamic_library.__getattr__(funcname)
	func.argtypes = _argtypes
	func.restype = _restype
	return func


# add function to module
def add_function_to_module(_current_module, name_of_function, function):
	setattr(_current_module, name_of_function, function)


# return a set (from a functions set) of functions that can be wrap
def check_for_functions_that_can_wrap(functions_set):
	functions_that_can_be_wrap = []
	functions_that_cant_be_wrap = []
	# check if function can wrap
	for function in functions_set:
		do_wrapper_this_function = True
		if 'params' in function.keys():
			for function_param in function['params']:
				function_param_processed = function_param["type"].replace('const', '').replace(" ", "").replace("*", "")
				if function_param_processed.count("[") > 0:
					function_param_processed = function_param_processed.split('[')[0]

				try:
					evaluate_c_type_string_to_python_type(function_param["type"])
				except:
					do_wrapper_this_function = False

				if is_string_contained_in_list(function_param_processed, ['Sound', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']):
					do_wrapper_this_function = False
					break

		if do_wrapper_this_function:
			function_returnType_processed = function["returnType"].replace('const', '').replace(" ", "").replace("*", "")
			if function_returnType_processed.count("[") > 0:
				function_returnType_processed = function_returnType_processed.split('[')[0]

			try:
				evaluate_c_type_string_to_python_type(function["returnType"])
			except:
				do_wrapper_this_function = False

			if is_string_contained_in_list(function_returnType_processed, ['AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback', 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']):
				do_wrapper_this_function = False

		if do_wrapper_this_function:
			functions_that_can_be_wrap.append(function)
		else:
			functions_that_cant_be_wrap.append(function)

	return functions_that_can_be_wrap


# wrap functions to ctypes functions => to _raylib_dynamic_library ctypes functions
def wrap_functions_to_ctypes_functions_add_function_to_this_module(functions_to_wrap, _current_module):
	for function_to_wrap in functions_to_wrap:
		if function_to_wrap['name'] not in wrapped_functions_names:
			wrapped_functions_names.append(function_to_wrap['name'])
			name_of_function = underscore(function_to_wrap['name']).replace('3_d', '_3d').replace('2_d', '_2d')
			function_to_wrap_ctype = {'name': function_to_wrap['name'], 'parametersTypes': [], 'returnType': None}

			if 'params' in function_to_wrap.keys():
				for function_param in function_to_wrap['params']:
					if function_param['type'] != "...":
						function_to_wrap_ctype['parametersTypes'].append(evaluate_c_type_string_to_python_type(function_param['type']))
			function_to_wrap_ctype['returnType'] = evaluate_c_type_string_to_python_type(function_to_wrap['returnType'])

			f = wrap_function(function_to_wrap_ctype['name'], function_to_wrap_ctype['parametersTypes'], function_to_wrap_ctype['returnType'])
			add_function_to_module(current_module, name_of_function, f)


# load rlgl data
with open(pathlib.Path(pathlib.Path(__file__).parent / 'rlgl_api.json')) as reader:
	rlgl_api = json.load(reader)

rlgl_api_functions = rlgl_api['functions']

# load raylib data
with open(pathlib.Path(pathlib.Path(__file__).parent / 'raylib_api.json')) as reader:
	raylib_api = json.load(reader)

raylib_api_functions = raylib_api['functions']

# load raymath data
with open(pathlib.Path(pathlib.Path(__file__).parent / 'raymath_api.json')) as reader:
	raymath_api = json.load(reader)

raymath_api_functions = raymath_api['functions']

# load raygui data
with open(pathlib.Path(pathlib.Path(__file__).parent / 'raygui_api.json')) as reader:
	raygui_api = json.load(reader)

raygui_api_functions = raygui_api['functions']

rlgl_functions_to_wrapped = check_for_functions_that_can_wrap(rlgl_api_functions)
raylib_functions_to_wrapped = check_for_functions_that_can_wrap(raylib_api_functions)
raymath_functions_to_wrapped = check_for_functions_that_can_wrap(raymath_api_functions)
if sys.platform != 'emscripten':
	raygui_functions_to_wrapped = check_for_functions_that_can_wrap(raygui_api_functions)

wrap_functions_to_ctypes_functions_add_function_to_this_module(rlgl_functions_to_wrapped, current_module)
wrap_functions_to_ctypes_functions_add_function_to_this_module(raylib_functions_to_wrapped, current_module)
wrap_functions_to_ctypes_functions_add_function_to_this_module(raymath_functions_to_wrapped, current_module)
if sys.platform != 'emscripten':
	wrap_functions_to_ctypes_functions_add_function_to_this_module(raygui_functions_to_wrapped, current_module)
