from pathlib import Path
import json
import inflection
import os

from pylibc.structures import *

from ctypes import (
    POINTER,
    Structure,
    c_bool,
    c_char,
    c_char_p,
    c_double,
    c_short,
    c_ubyte,
    c_float,
    c_void_p,
    c_int,
    c_uint,
    c_wchar,
    c_ushort,
    c_long,
    c_ulong,
    c_longlong,
    c_ulonglong,
    c_size_t,
    c_ssize_t,
    c_longdouble,
    c_wchar_p,
    cdll
)

typesDictionaryCstringToCtypes = {
    'bool': c_bool,  # C type: _Bool  Python type: bool (1)
    'char': c_char,  # C type: char  Python type: 1-character bytes object
    'wchar_t': c_wchar,  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsigned char': c_ubyte,  # C type: unsigned char  Python type: int
    'short': c_short,  # C type: short  Python type: int
    'unsigned short': c_ushort,  # C type: unsigned short  Python type: int
    'int': c_int,  # C type: int  Python type: int
    'unsigned int': c_uint,  # C type: unsigned int  Python type: int
    'long': c_long,  # C type: long  Python type: int
    'unsigned long': c_ulong,  # C type: unsigned long  Python type: int
    'uint64': c_longlong,  # C type: __int64 or long-long  Python type: int
    'unsigned uint64': c_ulonglong,  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': c_size_t,  # C type: unsigned size_t  Python type: int
    'ssize_t': c_ssize_t,  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': c_float,  # C type: float  Python type: float
    'double': c_double,  # C type: double  Python type: float
    'long double': c_longdouble,  # C type: long double  Python type: float
    'char *': c_char_p,  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t *': c_wchar_p,  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void *': c_void_p,  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': None,  # C type: void  Python type: None

    # Structures
    'Image': Image,  # C type: struct Image
    'Vector2': Vector2,  # C type: struct Vector2
    'Color': Color,  # C type: struct Color
    'Camera3D': Camera3D,  # C type: struct Camera3D
    'Camera': Camera,  # C type: struct Camera
    'Camera2D': Camera2D,  # C type: struct Camera2D
    'Shader': Shader,  # C type: struct Shader
    'Matrix': Matrix,  # C type: struct Matrix
    'Texture2D': Texture2D,  # C type: struct Texture2D
    'RenderTexture2D': RenderTexture2D,  # C type: struct RenderTexture2D
    'Ray': Ray,  # C type: struct Ray
    'Vector3': Vector3,  # C type: struct Vector3
}

typesDictionaryCstringToCtypesString = {
    'bool': 'c_bool',  # C type: _Bool  Python type: bool (1)
    'char': 'c_char',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'c_wchar',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsigned char': 'c_ubyte',  # C type: unsigned char  Python type: int
    'short': 'c_short',  # C type: short  Python type: int
    'unsigned short': 'c_ushort',  # C type: unsigned short  Python type: int
    'int': 'c_int',  # C type: int  Python type: int
    'unsigned int': 'c_uint',  # C type: unsigned int  Python type: int
    'long': 'c_long',  # C type: long  Python type: int
    'unsigned long': 'c_ulong',  # C type: unsigned long  Python type: int
    'uint64': 'c_longlong',  # C type: __int64 or long-long  Python type: int
    'unsigned uint64': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': 'c_size_t',  # C type: unsigned size_t  Python type: int
    'ssize_t': 'c_ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': 'c_float',  # C type: float  Python type: float
    'double': 'c_double',  # C type: double  Python type: float
    'long double': 'c_longdouble',  # C type: long double  Python type: float
    'char *': 'c_char_p',  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t *': 'c_wchar_p',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void *': 'c_void_p',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': 'None',  # C type: void  Python type: None

    # Structures
    'Image': 'Image',  # C type: struct Image
    'Vector2': 'Vector2',  # C type: struct Vector2
    'Color': 'Color',  # C type: struct Color
    'Camera3D': 'Camera3D',  # C type: struct Camera3D
    'Camera': 'Camera',  # C type: struct Camera
    'Camera2D': 'Camera2D',  # C type: struct Camera2D
    'Shader': 'Shader',  # C type: struct Shader
    'Matrix': 'Matrix',  # C type: struct Matrix
    'Texture2D': 'Texture2D',  # C type: struct Texture2D
    'RenderTexture2D': 'RenderTexture2D',  # C type: struct RenderTexture2D
    'Ray': 'Ray',  # C type: struct Ray
    'Vector3': 'Vector3',  # C type: struct Vector3
}

typesDictionaryCtypestoCstring = {
    c_bool: 'bool',  # C type: _Bool  Python type: bool (1)
    c_char: 'char',  # C type: char  Python type: 1-character bytes object
    c_wchar: 'wchar_t',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    c_ubyte: 'unsigned char',  # C type: unsigned char  Python type: int
    c_short: 'short',  # C type: short  Python type: int
    c_ushort: 'unsigned short',  # C type: unsigned short  Python type: int
    c_int: 'int',  # C type: int  Python type: int
    c_uint: 'unsigned int',  # C type: unsigned int  Python type: int
    c_long: 'long',  # C type: long  Python type: int
    c_ulong: 'unsigned long',  # C type: unsigned long  Python type: int
    c_longlong: 'uint64',  # C type: __int64 or long-long  Python type: int
    c_ulonglong: 'unsigned uint64',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    c_size_t: 'size_t',  # C type: unsigned size_t  Python type: int
    c_ssize_t: 'ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
    c_float: 'float',  # C type: float  Python type: float
    c_double: 'double',  # C type: double  Python type: float
    c_longdouble: 'long double',  # C type: long double  Python type: float
    c_char_p: 'char *',  # C type: char* (NUL terminated)  Python type: bytes object or None
    c_wchar_p: 'wchar_t *',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    c_void_p: 'void *',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    None: 'void',  # C type: void  Python type: None

    # Structures
    Image: 'Image',  # C type: struct Image
    Vector2: 'Vector2',  # C type: struct Vector2
    Color: 'Color',  # C type: struct Color
    Camera3D: 'Camera3D',  # C type: struct Camera3D
    Camera: 'Camera',  # C type: struct Camera
    Camera2D: 'Camera2D',  # C type: struct Camera2D
    Shader: 'Shader',  # C type: struct Shader
    Matrix: 'Matrix',  # C type: struct Matrix
    Texture2D: 'Texture2D',  # C type: struct Texture2D
    RenderTexture2D: 'RenderTexture2D',  # C type: struct RenderTexture2D
    Ray: 'Ray',  # C type: struct Ray
    Vector3: 'Vector3',  # C type: struct Vector3
}

typesDictionaryCtypestoPythonTypesString = {
    c_bool: 'bool',  # C type: _Bool  Python type: bool (1)
    c_char: 'bytes',  # C type: char  Python type: 1-character bytes object
    c_wchar: 'str',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    c_ubyte: 'int',  # C type: unsigned char  Python type: int
    c_short: 'int',  # C type: short  Python type: int
    c_ushort: 'int',  # C type: unsigned short  Python type: int
    c_int: 'int',  # C type: int  Python type: int
    c_uint: 'int',  # C type: unsigned int  Python type: int
    c_long: 'int',  # C type: long  Python type: int
    c_ulong: 'int',  # C type: unsigned long  Python type: int
    c_longlong: 'int',  # C type: __int64 or long-long  Python type: int
    c_ulonglong: 'int',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    c_size_t: 'int',  # C type: unsigned size_t  Python type: int
    c_ssize_t: 'int',  # C type: ssize_t or Py_ssize_t  Python type: int
    c_float: 'float',  # C type: float  Python type: float
    c_double: 'float',  # C type: double  Python type: float
    c_longdouble: 'float',  # C type: long double  Python type: float
    c_char_p: 'Union[bytes, None]',  # C type: char* (NUL terminated)  Python type: bytes object or None
    c_wchar_p: 'Union[str, None]',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    c_void_p: 'Union[int, None]',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    None: 'None',

    # Structures
    Image: 'Image',  # C type: struct Image
    Vector2: 'Vector2',  # C type: struct Vector2
    Color: 'Color',  # C type: struct Color
    Camera3D: 'Camera3D',  # C type: struct Camera3D
    Camera: 'Camera',  # C type: struct Camera
    Camera2D: 'Camera2D',  # C type: struct Camera2D
    Shader: 'Shader',  # C type: struct Shader
    Matrix: 'Matrix',  # C type: struct Matrix
    Texture2D: 'Texture2D',  # C type: struct Texture2D
    RenderTexture2D: 'RenderTexture2D',  # C type: struct RenderTexture2D
    Ray: 'Ray',  # C type: struct Ray
    Vector3: 'Vector3',  # C type: struct Vector3
}

typesDictionaryCstringToPythonTypesString = {
    'bool': 'bool',  # C type: _Bool  Python type: bool (1)
    'char': 'bytes',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'str',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsigned char': 'int',  # C type: unsigned char  Python type: int
    'short': 'int',  # C type: short  Python type: int
    'unsigned short': 'int',  # C type: unsigned short  Python type: int
    'int': 'int',  # C type: int  Python type: int
    'unsigned int': 'int',  # C type: unsigned int  Python type: int
    'long': 'int',  # C type: long  Python type: int
    'unsigned long': 'int',  # C type: unsigned long  Python type: int
    'uint64': 'int',  # C type: __int64 or long-long  Python type: int
    'unsigned uint64': 'int',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': 'int',  # C type: unsigned size_t  Python type: int
    'ssize_t': 'int',  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': 'float',  # C type: float  Python type: float
    'double': 'float',  # C type: double  Python type: float
    'long double': 'float',  # C type: long double  Python type: float
    'char *': 'Union[bytes, None]',  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t *': 'Union[string, None]',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void *': 'Union[int, None]',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': 'None',  # C type: void  Python type: None

    # Structures
    'Image': 'Image',  # C type: struct Image
    'Vector2': 'Vector2',  # C type: struct Vector2
    'Color': 'Color',  # C type: struct Color
    'Camera3D': 'Camera3D',  # C type: struct Camera3D
    'Camera': 'Camera',  # C type: struct Camera
    'Camera2D': 'Camera2D',  # C type: struct Camera2D
    'Shader': 'Shader',  # C type: struct Shader
    'Matrix': 'Matrix',  # C type: struct Matrix
    'Texture2D': 'Texture2D',  # C type: struct Texture2D
    'RenderTexture2D': 'RenderTexture2D',  # C type: struct RenderTexture2D
    'Ray': 'Ray',  # C type: struct Ray
    'Vector3': 'Vector3',  # C type: struct Vector3
}

current_module = __import__(__name__)

_rl = cdll.LoadLibrary(str(Path(__file__).parent / 'lib/raylib.dll'))

functions_data = {}

# Opening JSON file
with open(Path(__file__).parent / 'functions.json') as json_file:
    functions_data = json.load(json_file)

rcore_functions_data = functions_data['rcore_functions']


def wrap_function(funcname, _argtypes, _restype):
    func = _rl.__getattr__(funcname)
    func.argtypes = None if _argtypes == [None] else _argtypes

    func.restype = None if _restype == [None] else _restype[0]

    return func


# add function to module
def add_function_to_module(_current_module, name_of_function, function):
    setattr(_current_module, name_of_function, function)


# return a set (from a functions set) of functions that can be wrap
def check_if_functions_can_wrap(functions_set):
    functions_that_can_be_wrap = []
    # check if function can wrap
    for core_function in functions_set:
        do_wrapper_this_function = True

        for parametersType in core_function['parametersTypes']:
            if not (parametersType in typesDictionaryCstringToCtypes):
                do_wrapper_this_function = False

        if not (core_function['returnType'][0] in typesDictionaryCstringToCtypes and len(core_function['returnType']) == 1):
            do_wrapper_this_function = False

        if do_wrapper_this_function:
            functions_that_can_be_wrap.append(core_function)

    return functions_that_can_be_wrap


# wrap functions to ctypes functions => to _rl ctypes functions
def wrap_functions_to_ctypes_functions_and_add_function_to_this_module(functions_to_wrap, current_module):
    for function_to_wrap in functions_to_wrap:
        function_to_wrap_ctype = {'name': function_to_wrap['name'], 'parametersTypes': [], 'returnType': []}

        for parameterTypes in function_to_wrap['parametersTypes']:
            function_to_wrap_ctype['parametersTypes'].append(typesDictionaryCstringToCtypes[parameterTypes])

        for parameterTypes in function_to_wrap['returnType']:
            function_to_wrap_ctype['returnType'].append(typesDictionaryCstringToCtypes[parameterTypes])

        function_ctype = wrap_function(function_to_wrap_ctype['name'], function_to_wrap_ctype['parametersTypes'], function_to_wrap_ctype['returnType'])
        name_of_function = inflection.underscore(function_to_wrap_ctype['name']).replace('3_d', '_3d').replace('2_d', '_2d')
        add_function_to_module(current_module, name_of_function, function_ctype)


# remove the current functions_code.pyi file and generated new one
def generate_functions_code_pyi_file():
    if Path(Path(__file__).parent / '__init__.pyi').exists():
        os.remove(Path(Path(__file__).parent / '__init__.pyi'))
        with open(Path(Path(__file__).parent / '__init__.pyi'), "x") as functions_code_file_c:  # generate functions_code.py file => functions signature
            pass


def generate_functions_code_in_code_pyi_file(functions_that_can_be_wrap_ctype_set):
    # [print(function_that_can_be_wrap_ctype_set) for function_that_can_be_wrap_ctype_set in functions_that_can_be_wrap_ctype_set]
    with open(Path(Path(__file__).parent / '__init__.pyi'), "w") as functions_code_file_w:
        functions_code_file_w.write(f"from structures import *\n")
        functions_code_file_w.write(f"from typing import (Union)\n\n")
        for function_that_can_be_wrap_ctype in functions_that_can_be_wrap_ctype_set:
            name_of_function = inflection.underscore(function_that_can_be_wrap_ctype['name']).replace('3_d', '_3d').replace('2_d', '_2d')
            function_that_can_be_wrap_python_arguments_string = ""
            for function_that_can_be_wrap_ctype_data in zip(function_that_can_be_wrap_ctype['parametersNames'], function_that_can_be_wrap_ctype['parametersTypes']):
                if typesDictionaryCstringToPythonTypesString[function_that_can_be_wrap_ctype_data[1]] != 'None':
                    function_that_can_be_wrap_python_arguments_string += f"{function_that_can_be_wrap_ctype_data[0]}: {typesDictionaryCstringToPythonTypesString[function_that_can_be_wrap_ctype_data[1]]}, "
            function_that_can_be_wrap_python_arguments_string = function_that_can_be_wrap_python_arguments_string[:-2]
            functions_code = f"def {name_of_function}({function_that_can_be_wrap_python_arguments_string}) -> {typesDictionaryCstringToPythonTypesString[function_that_can_be_wrap_ctype['returnType'][0]]}:\n\tpass\n\n"
            functions_code_file_w.write(functions_code)


core_functions_that_can_be_wrap_ctype = check_if_functions_can_wrap(rcore_functions_data)

wrap_functions_to_ctypes_functions_and_add_function_to_this_module(core_functions_that_can_be_wrap_ctype, current_module)

generate_functions_code_pyi_file()

generate_functions_code_in_code_pyi_file(core_functions_that_can_be_wrap_ctype)
