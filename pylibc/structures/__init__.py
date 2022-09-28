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

# ----------------------------------------------------------------------------------
# Structures Definition
# ----------------------------------------------------------------------------------

# Vector2, 2 components
class Vector2(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
    ]

    def __init__(self, x: float = 0, y: float = 0) -> None:
        super(Vector2, self).__init__(x, y)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

# Vector3, 3 components
class Vector3(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
        ('z', _Float),  # Vector z component
    ]

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        super(Vector3, self).__init__(x, y, z)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = i

# Vector4, 4 components
class Vector4(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
        ('z', _Float),  # Vector z component
        ('w', _Float),  # Vector w component
    ]

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        super(Vector4, self).__init__(x, y, z, w)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = i

    @property
    def w(self) -> float:
        return self.w.value

    @w.setter
    def w(self, i: float) -> None:
        self.w = i
