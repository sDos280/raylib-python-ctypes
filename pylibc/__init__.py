import os
from pathlib import Path
import json
import inflection

from pylibc.structures import (
    Image
)

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

typesDictionary = {
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
    'void *': c_void_p,  # C type: wchar_t* (NUL terminated)  Python type: string object or None
    'void': c_void_p,  # C type: void  Python type: None

    # Structures
    'Image': Image
}

current_module = __import__(__name__)

_rl = cdll.LoadLibrary(str(Path(__file__).parent / 'lib/raylib.dll'))

functions_data = {}

# Opening JSON file
with open(Path(__file__).parent / 'functions.json') as json_file:
    functions_data = json.load(json_file)

rcore_functions_data = functions_data['rcore_functions']


def wrap_function(funcname, argtypes=None, restype=None):
    func = _rl.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func


# wrapper for core functions
for core_function in rcore_functions_data:
    for index, parametersType in enumerate(core_function['parametersTypes']):
        try:
            core_function['parametersTypes'][index] = typesDictionary[parametersType]
        except:
            print(core_function)

    core_function['parametersTypes'] = core_function['parametersTypes'] if len(core_function['parametersTypes']) != 1 and core_function['parametersTypes'] != 'void' else None
    core_function['parametersName'] = core_function['parametersName'] if len(core_function['parametersName']) != 1 and core_function['parametersName'] != 'void' else None
    core_function['returnType'] = typesDictionary[core_function['returnType'][0]]

# wrapper for core functions
for core_function in rcore_functions_data:
    try:
        name_of_function = inflection.underscore(core_function['name']).replace('3_d', '_3d').replace('2_d', '_2d')
        f = wrap_function(core_function['name'], core_function['parametersTypes'], core_function['returnType'])
        setattr(current_module, name_of_function, f)
    except:
        print(core_function['name'], core_function['parametersTypes'], core_function['returnType'])
