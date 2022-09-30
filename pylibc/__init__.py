from pathlib import Path

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

_Bool = c_bool
_VoidPtr = c_void_p
_CharPtr = c_char_p
_CharPtrPtr = POINTER(c_char_p)
_UCharPtr = POINTER(c_ubyte)
_IntPtr = POINTER(c_int)
_UIntPtr = POINTER(c_uint)
_FloatPtr = POINTER(c_float)
_UShortPtr = POINTER(c_ushort)
_Char = c_char
_UChar = c_ubyte
_Byte = c_byte
_Short = c_short
_Int = c_int
_Float = c_float
_UInt = c_uint
_Double = c_double
_Struct = Structure

current_module = __import__(__name__)

_rl = cdll.LoadLibrary(str(Path(__file__).parent / 'lib/raylib.dll'))
