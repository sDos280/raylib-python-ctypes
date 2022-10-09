from pathlib import Path
import json
import inflection
import os
import sys
from pylibc.structures import *

from ctypes import (
    POINTER,
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

# we don't use spaces...
typesDictionaryCstringToCtypes = {
    'bool': c_bool,  # C type: _Bool  Python type: bool (1)
    'char': c_char,  # C type: char  Python type: 1-character bytes object
    'wchar_t': c_wchar,  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': c_ubyte,  # C type: unsigned char  Python type: int
    'short': c_short,  # C type: short  Python type: int
    'unsignedshort': c_ushort,  # C type: unsigned short  Python type: int
    'int': c_int,  # C type: int  Python type: int
    'unsignedint': c_uint,  # C type: unsigned int  Python type: int
    'long': c_long,  # C type: long  Python type: int
    'unsignedlong': c_ulong,  # C type: unsigned long  Python type: int
    'uint64': c_longlong,  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': c_ulonglong,  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': c_size_t,  # C type: unsigned size_t  Python type: int
    'ssize_t': c_ssize_t,  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': c_float,  # C type: float  Python type: float
    'double': c_double,  # C type: double  Python type: float
    'longdouble': c_longdouble,  # C type: long double  Python type: float
    'char*': c_char_p,  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t*': c_wchar_p,  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void*': c_void_p,  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': None,  # C type: void  Python type: None

    'Vector2': Vector2,
    'Vector3': Vector3,
    'Vector4': Vector4,
    'Quaternion': Quaternion,
    'Matrix': Matrix,
    'Color': Color,
    'Rectangle': Rectangle,
    'Image': Image,
    'Texture': Texture,
    'Texture2D': Texture2D,
    'TextureCubemap': TextureCubemap,
    'RenderTexture': RenderTexture,
    'RenderTexture2D': RenderTexture2D,
    'NPatchInfo': NPatchInfo,
    'GlyphInfo': GlyphInfo,
    'Font': Font,
    'Camera3D': Camera3D,
    'Camera': Camera,
    'Camera2D': Camera2D,
    'Mesh': Mesh,
    'Shader': Shader,
    'MaterialMap': MaterialMap,
    'Material': Material,
    'Transform': Transform,
    'BoneInfo': BoneInfo,
    'Model': Model,
    'ModelAnimation': ModelAnimation,
    'Ray': Ray,
    'RayCollision': RayCollision,
    'BoundingBox': BoundingBox,
    'VrDeviceInfo': VrDeviceInfo,
    'VrStereoConfig': VrStereoConfig,
    'FilePathList': FilePathList
}

typesDictionaryCstringToCtypesString = {
    'bool': 'c_bool',  # C type: _Bool  Python type: bool (1)
    'char': 'c_char',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'c_wchar',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': 'c_ubyte',  # C type: unsigned char  Python type: int
    'short': 'c_short',  # C type: short  Python type: int
    'unsignedshort': 'c_ushort',  # C type: unsigned short  Python type: int
    'int': 'c_int',  # C type: int  Python type: int
    'unsignedint': 'c_uint',  # C type: unsigned int  Python type: int
    'long': 'c_long',  # C type: long  Python type: int
    'unsignedlong': 'c_ulong',  # C type: unsigned long  Python type: int
    'uint64': 'c_longlong',  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': 'c_ulonglong',  # C type: unsigned __int64 or unsigned long-long  Python type: int
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

typesDictionaryCtypestoCstring = {
    c_bool: 'bool',  # C type: _Bool  Python type: bool (1)
    c_char: 'char',  # C type: char  Python type: 1-character bytes object
    c_wchar: 'wchar_t',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    c_ubyte: 'unsignedchar',  # C type: unsigned char  Python type: int
    c_short: 'short',  # C type: short  Python type: int
    c_ushort: 'unsignedshort',  # C type: unsigned short  Python type: int
    c_int: 'int',  # C type: int  Python type: int
    c_uint: 'unsignedint',  # C type: unsigned int  Python type: int
    c_long: 'long',  # C type: long  Python type: int
    c_ulong: 'unsignedlong',  # C type: unsigned long  Python type: int
    c_longlong: 'uint64',  # C type: __int64 or long-long  Python type: int
    c_ulonglong: 'unsigneduint64',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    c_size_t: 'size_t',  # C type: unsigned size_t  Python type: int
    c_ssize_t: 'ssize_t',  # C type: ssize_t or Py_ssize_t  Python type: int
    c_float: 'float',  # C type: float  Python type: float
    c_double: 'double',  # C type: double  Python type: float
    c_longdouble: 'long double',  # C type: long double  Python type: float
    c_char_p: 'char*',  # C type: char* (NUL terminated)  Python type: bytes object or None
    c_wchar_p: 'wchar_t*',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    c_void_p: 'void*',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    None: 'void',  # C type: void  Python type: None
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
}

typesDictionaryCstringToPythonTypesString = {
    'bool': 'bool',  # C type: _Bool  Python type: bool (1)
    'char': 'bytes',  # C type: char  Python type: 1-character bytes object
    'wchar_t': 'str',  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': 'int',  # C type: unsigned char  Python type: int
    'short': 'int',  # C type: short  Python type: int
    'unsignedshort': 'int',  # C type: unsigned short  Python type: int
    'int': 'int',  # C type: int  Python type: int
    'unsignedint': 'int',  # C type: unsigned int  Python type: int
    'long': 'int',  # C type: long  Python type: int
    'unsignedlong': 'int',  # C type: unsigned long  Python type: int
    'uint64': 'int',  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': 'int',  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': 'int',  # C type: unsigned size_t  Python type: int
    'ssize_t': 'int',  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': 'float',  # C type: float  Python type: float
    'double': 'float',  # C type: double  Python type: float
    'longdouble': 'float',  # C type: long double  Python type: float
    'char*': 'bytes',  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t*': 'string',  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void*': 'int',  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': 'None',  # C type: void  Python type: None
}

typesDictionaryCstringToPythonTypes = {
    'bool': bool,  # C type: _Bool  Python type: bool (1)
    'char': bytes,  # C type: char  Python type: 1-character bytes object
    'wchar_t': str,  # C type: wchar_t  Python type: 1-character string
    # 'char': c_byte,  # C type: char  Python type: int
    'unsignedchar': int,  # C type: unsigned char  Python type: int
    'short': 'int',  # C type: short  Python type: int
    'unsignedshort': int,  # C type: unsigned short  Python type: int
    'int': 'int',  # C type: int  Python type: int
    'unsignedint': int,  # C type: unsigned int  Python type: int
    'long': 'int',  # C type: long  Python type: int
    'unsignedlong': int,  # C type: unsigned long  Python type: int
    'uint64': int,  # C type: __int64 or long-long  Python type: int
    'unsigneduint64': int,  # C type: unsigned __int64 or unsigned long-long  Python type: int
    'size_t': int,  # C type: unsigned size_t  Python type: int
    'ssize_t': int,  # C type: ssize_t or Py_ssize_t  Python type: int
    'float': float,  # C type: float  Python type: float
    'double': float,  # C type: double  Python type: float
    'longdouble': float,  # C type: long double  Python type: float
    'char*': bytes,  # C type: char* (NUL terminated)  Python type: bytes object or None
    'wchar_t*': str,  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void*': int,  # C type: wchar_t* (NUL terminated)  Python type: int or None
    'void': None,  # C type: void  Python type: None

    'Vector2': Vector2,
    'Vector3': Vector3,
    'Vector4': Vector4,
    'Quaternion': Quaternion,
    'Matrix': Matrix,
    'Color': Color,
    'Rectangle': Rectangle,
    'Image': Image,
    'Texture': Texture,
    'Texture2D': Texture2D,
    'TextureCubemap': TextureCubemap,
    'RenderTexture': RenderTexture,
    'RenderTexture2D': RenderTexture2D,
    'NPatchInfo': NPatchInfo,
    'GlyphInfo': GlyphInfo,
    'Font': Font,
    'Camera3D': Camera3D,
    'Camera': Camera,
    'Camera2D': Camera2D,
    'Mesh': Mesh,
    'Shader': Shader,
    'MaterialMap': MaterialMap,
    'Material': Material,
    'Transform': Transform,
    'BoneInfo': BoneInfo,
    'Model': Model,
    'ModelAnimation': ModelAnimation,
    'Ray': Ray,
    'RayCollision': RayCollision,
    'BoundingBox': BoundingBox,
    'VrDeviceInfo': VrDeviceInfo,
    'VrStereoConfig': VrStereoConfig,
    'FilePathList': FilePathList
}

current_module = __import__(__name__)

_rl = cdll.LoadLibrary(str(Path(__file__).parent / 'lib/raylib.dll'))


def wrap_function(funcname, _argtypes, _restype):
    func = _rl.__getattr__(funcname)
    func.argtypes = None if _argtypes == [None] else _argtypes

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
                function_param_type = function_param['type']
                function_param_pointer_level = function_param_type.count("*")
                sfunction_param_is_array = function_param_type.count("]")
                if sfunction_param_is_array == 0:
                    if function_param_pointer_level == 0 or (
                            function_param_type.replace(" ", "") in typesDictionaryCstringToPythonTypesString or function_param_type.replace(" ", "").replace('const',
                                                                                                                                                              '') in typesDictionaryCstringToPythonTypesString):  # if value isn't a pointer value
                        if function_param_type.replace(" ", "") in typesDictionaryCstringToPythonTypesString:  # that why in the typesDictionary we don't use spaces for the key
                            do_wrapper_this_function = True
                        elif function_param_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToPythonTypesString:  # there isn't really a const type in python
                            do_wrapper_this_function = True
                        else:  # probably type is struct
                            do_wrapper_this_function = True  # probably type is struct
                    else:
                        if function_param_type.replace('const', '').replace(" ", "") in typesDictionaryCstringToCtypesString:
                            do_wrapper_this_function = True
                        else:
                            if function_param_type.replace('const', '').replace(" ", "").replace("*", "") in typesDictionaryCstringToCtypesString:
                                do_wrapper_this_function = True
                            else:
                                do_wrapper_this_function = True  # probably type is struct
                else:
                    if function_param_type.replace('const', '').replace(" ", "").replace("*", "").replace('[', '').replace(']', '').replace(
                            f'{str(get_numbers_from_string(function_param_type.replace("const", "").replace(" ", "").replace("*", "").replace("[", " ").replace("]", " "))[0])}',
                            '') in typesDictionaryCstringToCtypesString:  # that why in the typesDictionary we don't use spaces for the key
                        do_wrapper_this_function = True
                    else:
                        do_wrapper_this_function = True  # probably type is struct

                if function_param_type.replace('const', '').replace(" ", "").replace("*", "").replace('[', '').replace(']', '') in ['AudioStream', 'Wave', 'Sound', 'Music', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback',
                                                                                                                                    'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']:
                    do_wrapper_this_function = False
                    break

        if do_wrapper_this_function:
            function_return_type = function['returnType']
            function_param_pointer_level = function_return_type.count("*")
            sfunction_param_is_array = function_return_type.count("]")
            if sfunction_param_is_array == 0:
                if function_param_pointer_level == 0 or (
                        function_return_type.replace(" ", "") in typesDictionaryCstringToCtypesString or function_return_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypesString):  # if value isn't a pointer value
                    if function_return_type.replace(" ", "") in typesDictionaryCstringToCtypesString:  # that why in the typesDictionary we don't use spaces for the key
                        do_wrapper_this_function = True
                    elif function_return_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypesString:  # there isn't really a const type in python
                        do_wrapper_this_function = True
                    else:  # probably type is struct
                        do_wrapper_this_function = True  # probably type is struct
                else:
                    if function_return_type.replace('const', '').replace(" ", "") in typesDictionaryCstringToCtypesString:
                        do_wrapper_this_function = True
                    else:
                        if function_return_type.replace('const', '').replace(" ", "").replace("*", "") in typesDictionaryCstringToCtypesString:
                            do_wrapper_this_function = True
                        else:
                            do_wrapper_this_function = True  # probably type is struct
            else:
                if function_return_type.replace('const', '').replace(" ", "").replace("*", "").replace('[', '').replace(']', '').replace(
                        f'{str(get_numbers_from_string(function_return_type.replace("const", "").replace(" ", "").replace("*", "").replace("[", " ").replace("]", " "))[0])}',
                        '') in typesDictionaryCstringToCtypesString:  # that why in the typesDictionary we don't use spaces for the key
                    do_wrapper_this_function = True
                else:
                    do_wrapper_this_function = True  # probably type is struct

            if function_return_type.replace('const', '').replace(" ", "").replace("*", "").replace('[', '').replace(']', '') in ['AudioStream', 'Wave', 'Sound', 'Music', 'AudioCallback', 'SaveFileTextCallback', 'LoadFileTextCallback',
                                                                                                                                 'TraceLogCallback', 'LoadFileDataCallback', 'SaveFileDataCallback']:
                do_wrapper_this_function = False

        if do_wrapper_this_function:
            functions_that_can_be_wrap.append(function)
        else:
            functions_that_cant_be_wrap.append(function)

    return functions_that_can_be_wrap


# wrap functions to ctypes functions => to _rl ctypes functions
def wrap_functions_to_ctypes_functions_add_function_to_this_module(functions_to_wrap, _current_module):
    for function_to_wrap in functions_to_wrap:
        name_of_function = inflection.underscore(function_to_wrap['name']).replace('3_d', '_3d').replace('2_d', '_2d')
        function_to_wrap_ctype = {'name': function_to_wrap['name'], 'parametersTypes': [], 'returnType': None}

        if 'params' in function_to_wrap.keys():
            for function_param in function_to_wrap['params']:
                function_param_type = function_param['type']
                function_param_pointer_level = function_param_type.count("*")
                # function_param_is_array = function_param_type.count("]") raylib functions shouldn't really return arrays...
                if function_param_pointer_level == 0 or (
                        function_param_type.replace(" ", "") in typesDictionaryCstringToCtypes or function_param_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypes):  # if value isn't a pointer value
                    if function_param_type.replace(" ", "") in typesDictionaryCstringToCtypes:  # that why in the typesDictionary we don't use spaces for the key
                        function_to_wrap_ctype['parametersTypes'].append(typesDictionaryCstringToCtypes[function_param_type.replace(" ", "")])
                    elif function_param_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypes:  # there isn't really a const type in python
                        function_to_wrap_ctype['parametersTypes'].append(typesDictionaryCstringToCtypes[function_param_type.replace(" ", "").replace('const', '')])
                else:
                    function_param_processed = function_param_type.replace('const', '').replace(' ', '').replace('*', '')
                    function_param_processed_ctype = None
                    if function_param_processed in typesDictionaryCstringToCtypes:
                        function_param_processed_ctype = typesDictionaryCstringToCtypes[function_param_processed]
                    for i in range(function_param_pointer_level):
                        function_param_processed_ctype = POINTER(function_param_processed_ctype)
                    function_to_wrap_ctype['parametersTypes'].append(function_param_processed_ctype)

        function_return_type = function_to_wrap['returnType']
        function_return_type_pointer_level = function_return_type.count("*")
        # function_param_is_array = function_param_type.count("]") raylib functions shouldn't really return arrays...
        if function_return_type_pointer_level == 0 or (
                function_return_type.replace(" ", "") in typesDictionaryCstringToCtypes or function_return_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypes):  # if value isn't a pointer value
            if function_return_type.replace(" ", "") in typesDictionaryCstringToCtypes:  # that why in the typesDictionary we don't use spaces for the key
                function_to_wrap_ctype['returnType'] = typesDictionaryCstringToCtypes[function_return_type.replace(" ", "")]
            elif function_return_type.replace(" ", "").replace('const', '') in typesDictionaryCstringToCtypes:  # there isn't really a const type in python
                function_to_wrap_ctype['returnType'] = typesDictionaryCstringToCtypes[function_return_type.replace(" ", "").replace('const', '')]
        else:
            function_return_type_processed = function_return_type.replace('const', '').replace(' ', '').replace('*', '')
            function_return_type_processed_ctype = None
            if function_return_type.replace('const', '').replace(' ', '') in typesDictionaryCstringToCtypes:
                function_return_type_processed_ctype = typesDictionaryCstringToCtypes[function_return_type_processed]
            for i in range(function_return_type_pointer_level):
                function_return_type_processed_ctype = POINTER(function_return_type_processed_ctype)
            function_to_wrap_ctype['parametersTypes'].append(function_return_type_processed_ctype)
        f = wrap_function(function_to_wrap_ctype['name'], function_to_wrap_ctype['parametersTypes'], function_to_wrap_ctype['returnType'])
        add_function_to_module(current_module, name_of_function, f)

# remove the current functions_code.pyi file and generated new one
def generate_functions_code_pyi_file():
    if Path(Path(__file__).parent / '__init__.pyi').exists():
        os.remove(Path(Path(__file__).parent / '__init__.pyi'))
        with open(Path(Path(__file__).parent / '__init__.pyi'), "x"):  # generate __init__.pyi file => function signature
            pass
        with open(Path(Path(__file__).parent / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from structures import *\n\n')
    else:
        print(f"there isn\'t a __init__.pyi in {Path(Path(__file__).parent / '__init__.pyi')}, regenerating a new one here")
        with open(Path(Path(__file__).parent / '__init__.pyi'), "x"):  # generate __init__.pyi file => function signature
            pass
        with open(Path(Path(__file__).parent / '__init__.pyi'), "w") as structs_code_file_write:  # add import stuff
            structs_code_file_write.write('from structures import *\n\n')


def generate_functions_code_in_code_pyi_file(functions_set):
    with open(Path(Path(__file__).parent / '__init__.pyi'), "a") as functions_code_file_w:
        for function in functions_set:
            name_of_function = inflection.underscore(function['name']).replace('3_d', '_3d').replace('2_d', '_2d')
            function_copy = dict(function)
            function_copy['name'] = str(name_of_function)
            function_string = generate_function_signature_code(function_copy)
            functions_code_file_w.write(function_string)


def generate_function_signature_code(function_data):
    function_return_type_sting = function_data['returnType']
    function_return_type_pointer_level = function_data['returnType'].count("*")
    # function_return_type_is_array = function_data['returnType'].count("]") c functions shouldn't return an array

    function_string = f"# {function_data['description']}\ndef {function_data['name']}("
    if 'params' in function_data.keys():  # only return stuff
        for param in function_data['params']:
            function_param_type_sting = param['type']
            function_param_name_sting = param['name']
            function_param_name_pointer_level = param['type'].count("*")
            if function_param_name_pointer_level == 0 or (function_param_type_sting.replace(" ", "") in typesDictionaryCstringToPythonTypesString or function_param_type_sting.replace(" ", "").replace('const',
                                                                                                                                                                                                        '') in typesDictionaryCstringToPythonTypesString):  # if value isn't a pointer value or in typesDictionaryCstringToCtypesString:
                if function_param_type_sting.replace(" ", "") in typesDictionaryCstringToPythonTypesString:
                    function_string += f"{function_param_name_sting}: {typesDictionaryCstringToPythonTypesString[function_param_type_sting.replace(' ', '')]}, "
                elif function_param_type_sting.replace(' ', '').replace('const', '') in typesDictionaryCstringToPythonTypesString:
                    function_string += f"{function_param_name_sting}: {typesDictionaryCstringToPythonTypesString[function_param_type_sting.replace(' ', '').replace('const', '')]}, "
                else:  # probably type is struct
                    function_string += f"{function_param_name_sting}: {function_param_type_sting.replace(' ', '').replace('const', '')}, "
            else:  # ctyps function wrapper

                function_param_processed_with_pointer_end = ""
                function_return_type_processed_with_pointer = function_param_type_sting.replace('const', '').replace(" ", "")
                if function_return_type_processed_with_pointer in typesDictionaryCstringToCtypesString:
                    function_string += f"{function_param_name_sting}: {typesDictionaryCstringToCtypesString[function_return_type_processed_with_pointer]}, "
                else:
                    function_return_type_processed = function_param_type_sting.replace('const', '').replace(" ", "").replace("*", "")
                    function_param_processed_ctype = ""
                    if function_return_type_processed in typesDictionaryCstringToCtypesString:
                        function_param_processed_ctype = typesDictionaryCstringToCtypesString[f"{function_return_type_processed}"]
                    else:
                        function_param_processed_ctype = function_return_type_processed
                    for i in range(function_param_name_pointer_level):
                        function_param_processed_ctype = f"POINTER({function_param_processed_ctype})"

                    function_param_processed_with_pointer_end = function_param_processed_ctype
                function_string += f"{function_param_name_sting}: {function_param_processed_with_pointer_end}, "
        function_string = function_string[:-2]

    function_string += ") -> "
    if function_return_type_pointer_level == 0 or (function_return_type_sting.replace(" ", "") in typesDictionaryCstringToPythonTypesString or function_return_type_sting.replace(" ", "").replace('const',
                                                                                                                                                                                                   '') in typesDictionaryCstringToPythonTypesString):  # if value isn't a pointer value or in typesDictionaryCstringToCtypesString:
        if function_return_type_sting.replace(" ", "") in typesDictionaryCstringToPythonTypesString:
            function_string += f"{typesDictionaryCstringToPythonTypesString[function_return_type_sting.replace(' ', '')]}:\n\tpass\n\n"
        elif function_return_type_sting.replace(' ', '').replace('const', '') in typesDictionaryCstringToPythonTypesString:
            function_string += f"{typesDictionaryCstringToPythonTypesString[function_return_type_sting.replace(' ', '').replace('const', '')]}:\n\tpass\n\n"
        else:  # probably type is struct
            function_string += f"{function_return_type_sting.replace(' ', '').replace('const', '')}:\n\tpass\n\n"
    else:  # ctyps function wrapper
        function_return_type_processed_with_pointer_end = ""
        function_return_type_processed_with_pointer = function_return_type_sting.replace('const', '').replace(" ", "")
        if function_return_type_processed_with_pointer in typesDictionaryCstringToCtypesString:
            function_string += f"{typesDictionaryCstringToCtypesString[function_return_type_processed_with_pointer]}:\n\tpass\n\n"
        else:
            function_return_type_processed = function_return_type_sting.replace('const', '').replace(" ", "").replace("*", "")
            function_return_type_processed_ctype = ""
            if function_return_type_processed in typesDictionaryCstringToCtypesString:
                function_return_type_processed_ctype = typesDictionaryCstringToCtypesString[f"{function_return_type_processed}"]
            else:
                function_return_type_processed_ctype = function_return_type_processed
            for i in range(function_return_type_pointer_level):
                function_return_type_processed_ctype = f"POINTER({function_return_type_processed_ctype})"

            function_return_type_processed_with_pointer_end = function_return_type_processed_ctype
        function_string += f"{function_return_type_processed_with_pointer_end}:  # {function_data['description']}\n\tpass\n\n"

    return function_string


# load raylib data
with open(Path(Path(__file__).parent / 'raylib_api.json')) as reader:
    raylib_api = json.load(reader)

raylib_api_functions = raylib_api['functions']

functions_to_wrapped = check_for_functions_that_can_wrap(raylib_api_functions)

wrap_functions_to_ctypes_functions_add_function_to_this_module(functions_to_wrapped, current_module)