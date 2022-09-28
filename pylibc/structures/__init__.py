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


# Quaternion, 4 components (Vector4 alias)
class Quaternion(Vector4):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        super(Vector4, self).__init__(x, y, z, w)


class Matrix(_Struct):
    _fields_ = [
        ('m0', _Float), ('m4', _Float), ('m8', _Float), ('m12', _Float),  # Matrix first row (4 components)
        ('m1', _Float), ('m5', _Float), ('m9', _Float), ('m13', _Float),  # Matrix second row (4 components)
        ('m2', _Float), ('m6', _Float), ('m10', _Float), ('m14', _Float),  # Matrix third row (4 components)
        ('m3', _Float), ('m7', _Float), ('m11', _Float), ('m15', _Float),  # Matrix fourth row (4 components)

    ]

    def __init__(self, m0: float = 0, m1: float = 0, m2: float = 0, m3: float = 0,
                 m4: float = 0, m5: float = 0, m6: float = 0, m7: float = 0,
                 m8: float = 0, m9: float = 0, m10: float = 0, m11: float = 0,
                 m12: float = 0, m13: float = 0, m14: float = 0, m15: float = 0, ) -> None:
        super(Matrix, self).__init__(m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15)

    @property
    def m0(self) -> float:
        return self.m0.value

    @m0.setter
    def m0(self, i: float) -> None:
        self.m0 = i

    @property
    def m1(self) -> float:
        return self.m1.value

    @m1.setter
    def m1(self, i: float) -> None:
        self.m1 = i

    @property
    def m2(self) -> float:
        return self.m2.value

    @m2.setter
    def m2(self, i: float) -> None:
        self.m2 = i

    @property
    def m3(self) -> float:
        return self.m3.value

    @m3.setter
    def m3(self, i: float) -> None:
        self.m3 = i

    @property
    def m4(self) -> float:
        return self.m4.value

    @m4.setter
    def m4(self, i: float) -> None:
        self.m4 = i

    @property
    def m5(self) -> float:
        return self.m5.value

    @m5.setter
    def m5(self, i: float) -> None:
        self.m5 = i

    @property
    def m6(self) -> float:
        return self.x.value

    @m6.setter
    def m6(self, i: float) -> None:
        self.m6 = i

    @property
    def m7(self) -> float:
        return self.m7.value

    @m7.setter
    def m7(self, i: float) -> None:
        self.m7 = i

    @property
    def m8(self) -> float:
        return self.m8.value

    @m8.setter
    def m8(self, i: float) -> None:
        self.m8 = i

    @property
    def m9(self) -> float:
        return self.m9.value

    @m9.setter
    def m9(self, i: float) -> None:
        self.m9 = i

    @property
    def m10(self) -> float:
        return self.m10.value

    @m10.setter
    def m10(self, i: float) -> None:
        self.m10 = i

    @property
    def m11(self) -> float:
        return self.m11.value

    @m11.setter
    def m11(self, i: float) -> None:
        self.m11 = i

    @property
    def m12(self) -> float:
        return self.m12.value

    @m12.setter
    def m12(self, i: float) -> None:
        self.m12 = i

    @property
    def m13(self) -> float:
        return self.m13.value

    @m13.setter
    def m13(self, i: float) -> None:
        self.m13 = i

    @property
    def m14(self) -> float:
        return self.m14.value

    @m14.setter
    def m14(self, i: float) -> None:
        self.m14 = i

    @property
    def m15(self) -> float:
        return self.m15.value

    @m15.setter
    def m15(self, i: float) -> None:
        self.m15 = i
