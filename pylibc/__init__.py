from pathlib import Path
import json
import inflection

from ctypes import (
    POINTER,
    Structure,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_short,
    c_ubyte,
    c_float,
    c_ushort,
    c_void_p,
    c_int,
    c_uint,
    cdll
)

typesDictionary = {
    'Bool': c_bool,
    'VoidPtr': c_void_p,
    'CharPtr': c_char_p,
    'CharPtrPtr': POINTER(c_char_p),
    'UCharPtr': POINTER(c_ubyte),
    'IntPtr': POINTER(c_int),
    'UIntPtr': POINTER(c_uint),
    'FloatPtr': POINTER(c_float),
    'UShortPtr': POINTER(c_ushort),
    'Char': c_char,
    'UChar': c_ubyte,
    'Byte': c_byte,
    'Short': c_short,
    'Int': c_int,
    'Float': c_float,
    'UInt': c_uint,
    'Double': c_double,
    'Struct': Structure,
    'None': None
}


current_module = __import__(__name__)

_rl = cdll.LoadLibrary(str(Path(__file__).parent / 'lib/raylib.dll'))

functions_data = {}
# Opening JSON file
with open('C:/Raylib Python Bindings/raylib-python-ctypes/pylibc/functions.json') as json_file:
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
        core_function['parametersTypes'][index] = typesDictionary[parametersType]

    core_function['parametersTypes'] = core_function['parametersTypes'] if len(core_function['parametersTypes']) != 1 and core_function['parametersTypes'] else None
    core_function['parameters'] = core_function['parameters'] if len(core_function['parameters']) != 1 and core_function['parameters'] else None
    core_function['returnType'] = typesDictionary[core_function['returnType'][0]]

# wrapper for core functions
for core_function in rcore_functions_data:
    name_of_function = inflection.underscore(core_function['name']).replace('3_d', '_3d').replace('2_d', '_2d')
    f = wrap_function(core_function['name'], core_function['parametersTypes'], core_function['returnType'])
    setattr(current_module, name_of_function, f)
