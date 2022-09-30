from multipledispatch import dispatch

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

from typing import (
    Any,
    List,
    Optional,
    Sequence,
    Type,
    Union
)

from ctypes import (
    pointer,
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


def _to_int(value: float):
    return int(value) if isinstance(value, float) else value


def _to_float(value: int):
    return float(value) if isinstance(value, int) else value


def _to_byte_str(value: str):
    if not isinstance(value, (str, bytes)):
        value = str(value)
    return value.encode('utf-8', 'ignore')


def _to_str(value: bytes):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def copyDataTo(src, dest):
    pointer(dest)[0] = pointer(src)[0]


def _flatten(filter_types: Sequence[Type], *args: Any, map_to: Optional[Type] = None) -> List[Any]:
    flatten_list = []
    for value in args:
        if isinstance(value, filter_types):
            flatten_list.append(map_to(value) if map_to else value)
        else:
            flatten_list.extend(_flatten(filter_types, *value, map_to=map_to))

    return flatten_list


# ----------------------------------------------------------------------------------
# Structures Definition
# ----------------------------------------------------------------------------------

# Vector2, 2 components
class Vector2(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
    ]

    @dispatch()
    def __init__(self) -> None:
        self.__set()

    @dispatch((float, int), (float, int))
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__set(x, y)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = _to_float(i)

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = _to_float(i)

    def __set(self, x: float = 0, y: float = 0) -> None:
        super(Vector2, self).__init__(_to_float(x), _to_float(y))


# Vector3, 3 components
class Vector3(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
        ('z', _Float),  # Vector z component
    ]

    @dispatch()
    def __init__(self) -> None:
        self.__set()

    @dispatch((float, int), (float, int), (float, int))
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.__set(x, y, z)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = _to_float(i)

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = _to_float(i)

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = _to_float(i)

    def __set(self, x: float = 0, y: float = 0, z: float = 0):
        super(Vector3, self).__init__(_to_float(x), _to_float(y), _to_float(z))


# Vector4, 4 components
class Vector4(_Struct):
    _fields_ = [
        ('x', _Float),  # Vector x component
        ('y', _Float),  # Vector y component
        ('z', _Float),  # Vector z component
        ('w', _Float),  # Vector w component
    ]

    @dispatch()
    def __init__(self) -> None:
        self.__set()

    @dispatch((float, int), (float, int), (float, int), (float, int))
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        self.__set(x, y, z, w)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = _to_float(i)

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = _to_float(i)

    @property
    def z(self) -> float:
        return self.z.value

    @z.setter
    def z(self, i: float) -> None:
        self.z = _to_float(i)

    @property
    def w(self) -> float:
        return self.w.value

    @w.setter
    def w(self, i: float) -> None:
        self.w = _to_float(i)

    def __set(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0):
        super(Vector4, self).__init__(_to_float(x), _to_float(y), _to_float(z), _to_float(w))


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4


# Matrix, 4x4 components, column major, OpenGL style, right-handed
class Matrix(_Struct):
    _fields_ = [
        ('m0', _Float), ('m4', _Float), ('m8', _Float), ('m12', _Float),  # Matrix first row (4 components)
        ('m1', _Float), ('m5', _Float), ('m9', _Float), ('m13', _Float),  # Matrix second row (4 components)
        ('m2', _Float), ('m6', _Float), ('m10', _Float), ('m14', _Float),  # Matrix third row (4 components)
        ('m3', _Float), ('m7', _Float), ('m11', _Float), ('m15', _Float),  # Matrix fourth row (4 components)
    ]

    @dispatch()
    def __init__(self) -> None:
        self.__set()

    @dispatch((float, int), (float, int), (float, int), (float, int),
              (float, int), (float, int), (float, int), (float, int),
              (float, int), (float, int), (float, int), (float, int),
              (float, int), (float, int), (float, int), (float, int))
    def __init__(self, m0: float = 0, m1: float = 0, m2: float = 0, m3: float = 0,
                 m4: float = 0, m5: float = 0, m6: float = 0, m7: float = 0,
                 m8: float = 0, m9: float = 0, m10: float = 0, m11: float = 0,
                 m12: float = 0, m13: float = 0, m14: float = 0, m15: float = 0, ) -> None:
        self.__set(m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15)

    @property
    def m0(self) -> float:
        return self.m0.value

    @m0.setter
    def m0(self, i: float) -> None:
        self.m0 = _to_float(i)

    @property
    def m1(self) -> float:
        return self.m1.value

    @m1.setter
    def m1(self, i: float) -> None:
        self.m1 = _to_float(i)

    @property
    def m2(self) -> float:
        return self.m2.value

    @m2.setter
    def m2(self, i: float) -> None:
        self.m2 = _to_float(i)

    @property
    def m3(self) -> float:
        return self.m3.value

    @m3.setter
    def m3(self, i: float) -> None:
        self.m3 = _to_float(i)

    @property
    def m4(self) -> float:
        return self.m4.value

    @m4.setter
    def m4(self, i: float) -> None:
        self.m4 = _to_float(i)

    @property
    def m5(self) -> float:
        return self.m5.value

    @m5.setter
    def m5(self, i: float) -> None:
        self.m5 = _to_float(i)

    @property
    def m6(self) -> float:
        return self.m6.value

    @m6.setter
    def m6(self, i: float) -> None:
        self.m6 = _to_float(i)

    @property
    def m7(self) -> float:
        return self.m7.value

    @m7.setter
    def m7(self, i: float) -> None:
        self.m7 = _to_float(i)

    @property
    def m8(self) -> float:
        return self.m8.value

    @m8.setter
    def m8(self, i: float) -> None:
        self.m8 = _to_float(i)

    @property
    def m9(self) -> float:
        return self.m9.value

    @m9.setter
    def m9(self, i: float) -> None:
        self.m9 = _to_float(i)

    @property
    def m10(self) -> float:
        return self.m10.value

    @m10.setter
    def m10(self, i: float) -> None:
        self.m10 = _to_float(i)

    @property
    def m11(self) -> float:
        return self.m11.value

    @m11.setter
    def m11(self, i: float) -> None:
        self.m11 = _to_float(i)

    @property
    def m12(self) -> float:
        return self.m12.value

    @m12.setter
    def m12(self, i: float) -> None:
        self.m12 = _to_float(i)

    @property
    def m13(self) -> float:
        return self.m13.value

    @m13.setter
    def m13(self, i: float) -> None:
        self.m13 = _to_float(i)

    @property
    def m14(self) -> float:
        return self.m14.value

    @m14.setter
    def m14(self, i: float) -> None:
        self.m14 = _to_float(i)

    @property
    def m15(self) -> float:
        return self.m15.value

    @m15.setter
    def m15(self, i: float) -> None:
        self.m15 = _to_float(i)

    def __set(self, m0: float = 0, m1: float = 0, m2: float = 0, m3: float = 0,
              m4: float = 0, m5: float = 0, m6: float = 0, m7: float = 0,
              m8: float = 0, m9: float = 0, m10: float = 0, m11: float = 0,
              m12: float = 0, m13: float = 0, m14: float = 0, m15: float = 0, ) -> None:
        super(Matrix, self).__init__(_to_float(m0), _to_float(m1), _to_float(m2), _to_float(m3),
                                     _to_float(m4), _to_float(m5), _to_float(m6), _to_float(m7),
                                     _to_float(m8), _to_float(m9), _to_float(m10), _to_float(m11),
                                     _to_float(m12), _to_float(m13), _to_float(m14), _to_float(m15))


# Color, 4 components, R8G8B8A8 (32bit)
class Color(_Struct):
    _fields_ = [
        ('r', _UChar),  # Color red value
        ('g', _UChar),  # Color green value
        ('b', _UChar),  # Color blue value
        ('a', _UChar),  # Color alpha value
    ]

    @dispatch()
    def __init__(self) -> None:
        self.__set()

    @dispatch(int, int, int, int)
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 0) -> None:
        self.__set(r, g, b, a)

    @property
    def r(self) -> int:
        return self.r.value

    @r.setter
    def r(self, i: int) -> None:
        self.r = _UChar(i)

    @property
    def g(self) -> int:
        return self.g.value

    @g.setter
    def g(self, i: int) -> None:
        self.g = _UChar(i)

    @property
    def b(self) -> int:
        return self.b.value

    @b.setter
    def b(self, i: int) -> None:
        self.b = _UChar(i)

    @property
    def a(self) -> int:
        return self.a.value

    @a.setter
    def a(self, i: int) -> None:
        self.a = _UChar(i)

    def __set(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255) -> None:
        super(Color, self).__init__(_UChar(r), _UChar(g), _UChar(b), _UChar(a))


# Rectangle, 4 components
class Rectangle(_Struct):
    _fields_ = [
        ('x', _Float),  # Color red value
        ('y', _Float),  # Color green value
        ('width', _Float),  # Color blue value
        ('height', _Float),  # Color alpha value
    ]

    @dispatch((int, float), (int, float), (int, float), (int, float))
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0) -> None:
        self.__set(x, y, width, height)

    @property
    def x(self) -> float:
        return self.x.value

    @x.setter
    def x(self, i: float) -> None:
        self.x = _to_float(i)

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = _to_float(i)

    @property
    def width(self) -> float:
        return self.width.value

    @width.setter
    def width(self, i: float) -> None:
        self.width = _to_float(i)

    @property
    def height(self) -> float:
        return self.height.value

    @height.setter
    def height(self, i: float) -> None:
        self.height = _to_float(i)

    def __set(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        super(Rectangle, self).__init__(_to_float(x), _to_float(y), _to_float(width), _to_float(height))


# Image, pixel data stored in CPU memory (RAM)
class Image(_Struct):
    _fields_ = [
        ('data', _VoidPtr),  # Image raw data
        ('width', _Int),  # Image base width
        ('height', _Int),  # Image base height
        ('mipmaps', _Int),  # Mipmap levels, 1 by default
        ('format', _Int)  # Data format (PixelFormat type)
    ]

    def __init__(self, image: 'Image') -> None:
        if isinstance(image, Image):
            self.__set(image)
        else:
            raise ValueError('Invalid argument')

    @property
    def data(self) -> _VoidPtr:
        return self.data.value

    @data.setter
    def data(self, i: _VoidPtr) -> None:
        self.data = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = _to_int(i)

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = _to_int(i)

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = _to_int(i)

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = _to_int(i)

    def __set(self, image) -> None:
        super(Image, self).__init__(image.data, image.width, image.height, image.mipmaps, image.format)


# Texture, tex data stored in GPU memory (VRAM)
class Texture(_Struct):
    _fields_ = [
        ('id', _UInt),  # Image raw data
        ('width', _Int),  # Image base width
        ('height', _Int),  # Image base height
        ('mipmaps', _Int),  # Mipmap levels, 1 by default
        ('format', _Int)  # Data format (PixelFormat type)
    ]

    def __init__(self, texture: 'Texture') -> None:
        if isinstance(texture, Texture):
            self.__set(texture)
        else:
            raise ValueError('Invalid argument')

    @property
    def id(self) -> _UInt:
        return self.id.value

    @id.setter
    def id(self, i: _UInt) -> None:
        self.id = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = _to_int(i)

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = _to_int(i)

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = _to_int(i)

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = _to_int(i)

    def __set(self, texture: 'Texture'):
        super(Texture, self).__init__(texture.id, texture.width, texture.height, texture.mipmaps, texture.format)


# Texture2D, same as Texture
Texture2D = Texture

# TextureCubemap, same as Texture
TextureCubemap = Texture


# RenderTexture, fbo for texture rendering
class RenderTexture(_Struct):
    _fields_ = [
        ('id', _UInt),  # OpenGL framebuffer object id
        ('texture', Texture),  # Image base width
        ('depth', Texture),  # Image base width
    ]

    def __init__(self, renderTexture: 'RenderTexture') -> None:
        if isinstance(renderTexture, RenderTexture):
            self.__set(renderTexture)
        else:
            raise ValueError('Invalid argument')

    @property
    def id(self) -> _UInt:
        return self.id.value

    @id.setter
    def id(self, i: _UInt) -> None:
        self.id = i

    @property
    def texture(self) -> Texture:
        return self.texture

    @texture.setter
    def texture(self, i: Texture) -> None:
        self.texture = i

    @property
    def depth(self) -> Texture:
        return self.depth

    @depth.setter
    def depth(self, i: Texture) -> None:
        self.depth = i

    def __set(self, renderTexture: 'RenderTexture'):
        super(RenderTexture, self).__init__(renderTexture.id, renderTexture.texture, renderTexture.depth)


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture


# NPatchInfo, n-patch layout infostructers
class NPatchInfo(_Struct):
    _fields_ = [
        ('source', Rectangle),  # Texture source rectangle
        ('left', _Int),  # Left border offset
        ('top', _Int),  # Top border offset
        ('right', _Int),  # Right border offset
        ('bottom', _Int),  # Bottom border offset
        ('layout', _Int),  # Layout of the n-patch: 3x3, 1x3 or 3x1
    ]

    def __init__(self, nPatchInfo: 'NPatchInfo') -> None:
        if isinstance(nPatchInfo, NPatchInfo):
            self.__set(nPatchInfo)
        else:
            raise ValueError('Invalid argument')

    @property
    def source(self) -> Rectangle:
        return self.source.value

    @source.setter
    def source(self, i: Rectangle) -> None:
        self.source = _to_int(i)

    @property
    def left(self) -> int:
        return self.left.value

    @left.setter
    def left(self, i: int) -> None:
        self.left = _to_int(i)

    @property
    def top(self) -> int:
        return self.top.value

    @top.setter
    def top(self, i: int) -> None:
        self.top = _to_int(i)

    @property
    def right(self) -> int:
        return self.right.value

    @right.setter
    def right(self, i: int) -> None:
        self.right = _to_int(i)

    @property
    def bottom(self) -> int:
        return self.bottom.value

    @bottom.setter
    def bottom(self, i: int) -> None:
        self.bottom = _to_int(i)

    @property
    def layout(self) -> int:
        return self.layout.value

    @layout.setter
    def layout(self, i: int) -> None:
        self.layout = _to_int(i)

    def __set(self, nPatchInfo: 'NPatchInfo'):
        super.__init__(self, Rectangle(nPatchInfo.source), _to_int(nPatchInfo.left), _to_int(nPatchInfo.top), _to_int(nPatchInfo.right), _to_int(nPatchInfo.bottom), _to_int(nPatchInfo.layout))