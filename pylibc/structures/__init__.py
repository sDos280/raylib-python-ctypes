from multipledispatch import dispatch

from typing import (
    Any,
    List,
    Optional,
    Sequence,
    Type
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

Bool = c_bool
VoidPtr = c_void_p
CharPtr = c_char_p
CharPtrPtr = POINTER(c_char_p)
UCharPtr = POINTER(c_ubyte)
IntPtr = POINTER(c_int)
UIntPtr = POINTER(c_uint)
FloatPtr = POINTER(c_float)
UShortPtr = POINTER(c_ushort)
Char = c_char
UChar = c_ubyte
Byte = c_byte
Short = c_short
Int = c_int
Float = c_float
UInt = c_uint
Double = c_double
Struct = Structure


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
class Vector2(Struct):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
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
        self.x = i

    @property
    def y(self) -> float:
        return self.y.value

    @y.setter
    def y(self, i: float) -> None:
        self.y = i

    def __set(self, x: float = 0, y: float = 0) -> None:
        super(Vector2, self).__init__(x, y)


# Vector3, 3 components
class Vector3(Struct):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
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

    def __set(self, x: float = 0, y: float = 0, z: float = 0):
        super(Vector3, self).__init__(x, y, z)


# Vector4, 4 components
class Vector4(Struct):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
        ('w', Float),  # Vector w component
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
        self.w = _to_float(i)

    def __set(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0):
        super(Vector4, self).__init__(_to_float(x), _to_float(y), _to_float(z), _to_float(w))


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4


# Matrix, 4x4 components, column major, OpenGL style, right-handed
class Matrix(Struct):
    _fields_ = [
        ('m0', Float), ('m4', Float), ('m8', Float), ('m12', Float),  # Matrix first row (4 components)
        ('m1', Float), ('m5', Float), ('m9', Float), ('m13', Float),  # Matrix second row (4 components)
        ('m2', Float), ('m6', Float), ('m10', Float), ('m14', Float),  # Matrix third row (4 components)
        ('m3', Float), ('m7', Float), ('m11', Float), ('m15', Float),  # Matrix fourth row (4 components)
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
        return self.m6.value

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

    def __set(self, m0: float = 0, m1: float = 0, m2: float = 0, m3: float = 0,
              m4: float = 0, m5: float = 0, m6: float = 0, m7: float = 0,
              m8: float = 0, m9: float = 0, m10: float = 0, m11: float = 0,
              m12: float = 0, m13: float = 0, m14: float = 0, m15: float = 0, ) -> None:
        super(Matrix, self).__init__(m0, m1, m2, m3,
                                     m4, m5, m6, m7,
                                     m8, m9, m10, m11,
                                     m12, m13, m14, m15)


# Color, 4 components, R8G8B8A8 (32bit)
class Color(Struct):
    _fields_ = [
        ('r', UChar),  # Color red value
        ('g', UChar),  # Color green value
        ('b', UChar),  # Color blue value
        ('a', UChar),  # Color alpha value
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
        self.r = i

    @property
    def g(self) -> int:
        return self.g.value

    @g.setter
    def g(self, i: int) -> None:
        self.g = i

    @property
    def b(self) -> int:
        return self.b.value

    @b.setter
    def b(self, i: int) -> None:
        self.b = i

    @property
    def a(self) -> int:
        return self.a.value

    @a.setter
    def a(self, i: int) -> None:
        self.a = i

    def __set(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255) -> None:
        super(Color, self).__init__(r, g, b, a)


# Rectangle, 4 components
class Rectangle(Struct):
    _fields_ = [
        ('x', Float),  # Color red value
        ('y', Float),  # Color green value
        ('width', Float),  # Color blue value
        ('height', Float),  # Color alpha value
    ]

    @dispatch((int, float), (int, float), (int, float), (int, float))
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0) -> None:
        self.__set(x, y, width, height)

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
    def width(self) -> float:
        return self.width.value

    @width.setter
    def width(self, i: float) -> None:
        self.width = i

    @property
    def height(self) -> float:
        return self.height.value

    @height.setter
    def height(self, i: float) -> None:
        self.height = i

    def __set(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        super(Rectangle, self).__init__(x, y, width, height)


# Image, pixel data stored in CPU memory (RAM)
class Image(Struct):
    _fields_ = [
        ('data', VoidPtr),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    def __init__(self, image: 'Image') -> None:
        if isinstance(image, Image):
            self.__set(image)
        else:
            raise ValueError('Invalid argument')

    @property
    def data(self) -> VoidPtr:
        return self.data.value

    @data.setter
    def data(self, i: VoidPtr) -> None:
        self.data = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = i

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = i

    def __set(self, image) -> None:
        super(Image, self).__init__(image.data, image.width, image.height, image.mipmaps, image.format)


# Texture, tex data stored in GPU memory (VRAM)
class Texture(Struct):
    _fields_ = [
        ('id', UInt),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    def __init__(self, texture: 'Texture') -> None:
        if isinstance(texture, Texture):
            self.__set(texture)
        else:
            raise ValueError('Invalid argument')

    @property
    def id(self) -> UInt:
        return self.id.value

    @id.setter
    def id(self, i: UInt) -> None:
        self.id = i

    @property
    def width(self) -> int:
        return self.width.value

    @width.setter
    def width(self, i: int) -> None:
        self.width = i

    @property
    def height(self) -> int:
        return self.height.value

    @height.setter
    def height(self, i: int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> int:
        return self.mipmaps.value

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> int:
        return self.format.value

    @format.setter
    def format(self, i: int) -> None:
        self.format = i

    def __set(self, texture: 'Texture'):
        super(Texture, self).__init__(texture.id, texture.width, texture.height, texture.mipmaps, texture.format)


# Texture2D, same as Texture
Texture2D = Texture

# TextureCubemap, same as Texture
TextureCubemap = Texture


# RenderTexture, fbo for texture rendering
class RenderTexture(Struct):
    _fields_ = [
        ('id', UInt),  # OpenGL framebuffer object id
        ('texture', Texture),  # Image base width
        ('depth', Texture)  # Image base width
    ]

    def __init__(self, renderTexture: 'RenderTexture') -> None:
        if isinstance(renderTexture, RenderTexture):
            self.__set(renderTexture)
        else:
            raise ValueError('Invalid argument')

    @property
    def id(self) -> UInt:
        return self.id.value

    @id.setter
    def id(self, i: UInt) -> None:
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
class NPatchInfo(Struct):
    _fields_ = [
        ('source', Rectangle),  # Texture source rectangle
        ('left', Int),  # Left border offset
        ('top', Int),  # Top border offset
        ('right', Int),  # Right border offset
        ('bottom', Int),  # Bottom border offset
        ('layout', Int)  # Layout of the n-patch: 3x3, 1x3 or 3x1
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
        self.source = i

    @property
    def left(self) -> int:
        return self.left.value

    @left.setter
    def left(self, i: int) -> None:
        self.left = i

    @property
    def top(self) -> int:
        return self.top.value

    @top.setter
    def top(self, i: int) -> None:
        self.top = i

    @property
    def right(self) -> int:
        return self.right.value

    @right.setter
    def right(self, i: int) -> None:
        self.right = i

    @property
    def bottom(self) -> int:
        return self.bottom.value

    @bottom.setter
    def bottom(self, i: int) -> None:
        self.bottom = i

    @property
    def layout(self) -> int:
        return self.layout.value

    @layout.setter
    def layout(self, i: int) -> None:
        self.layout = i

    def __set(self, nPatchInfo: 'NPatchInfo'):
        super.__init__(self, nPatchInfo.source, nPatchInfo.left, nPatchInfo.top, nPatchInfo.right, nPatchInfo.bottom,
                       nPatchInfo.layout)

# GlyphInfo, font characters glyphs info
class GlyphInfo(Struct):
    _fields_ = [
        ('value', Int),  # Character value (Unicode)
        ('offsetX', Int),  # Character offset X when drawing
        ('offsetY', Int),  # Character offset Y when drawing
        ('advanceX', Int),  # Character advance position X
        ('image', Image)  # Character image data
    ]

    def __init__(self, glyphInfo: 'GlyphInfo') -> None:
        if isinstance(glyphInfo, NPatchInfo):
            self.__set(glyphInfo)
        else:
            raise ValueError('Invalid argument')

    @property
    def value(self) -> int:
        return self.value.value

    @value.setter
    def value(self, i: int) -> None:
        self.value = i

    @property
    def offsetX(self) -> int:
        return self.offsetX.value

    @offsetX.setter
    def offsetX(self, i: int) -> None:
        self.offsetX = i

    @property
    def offsetY(self) -> int:
        return self.offsetY.value

    @offsetY.setter
    def offsetY(self, i: int) -> None:
        self.offsetY = i

    @property
    def advanceX(self) -> int:
        return self.advanceX.value

    @advanceX.setter
    def advanceX(self, i: int) -> None:
        self.advanceX = i

    @property
    def image(self) -> Image:
        return self.image.value

    @image.setter
    def image(self, i: Image) -> None:
        self.image = i

    def __set(self, glyphInfo: 'GlyphInfo'):
        super.__init__(self, glyphInfo.value, glyphInfo.offsetX, glyphInfo.offsetY, glyphInfo.advanceX, glyphInfo.image)

# Font, font texture and GlyphInfo array data
class Font(Struct):
    _fields_ = [
        ('baseSize', Int),  # Character value (Unicode)
        ('glyphCount', Int),  # Character offset X when drawing
        ('glyphPadding', Int),  # Character offset Y when drawing
        ('texture', Texture2D),  # Character advance position X
        ('recs', POINTER(Rectangle)),  # Character image data
        ('glyphs', POINTER(GlyphInfo))  # Character image data
    ]

    def __init__(self, font: 'Font') -> None:
        if isinstance(font, NPatchInfo):
            self.__set(font)
        else:
            raise ValueError('Invalid argument')

    @property
    def baseSize(self) -> int:
        return self.baseSize.value

    @baseSize.setter
    def baseSize(self, i: int) -> None:
        self.baseSize = i

    @property
    def glyphCount(self) -> int:
        return self.glyphCount.value

    @glyphCount.setter
    def glyphCount(self, i: int) -> None:
        self.glyphCount = i

    @property
    def glyphPadding(self) -> int:
        return self.glyphPadding.value

    @glyphPadding.setter
    def glyphPadding(self, i: int) -> None:
        self.glyphPadding = i

    @property
    def texture(self) -> Texture2D:
        return self.texture.value

    @texture.setter
    def texture(self, i: Texture2D) -> None:
        self.texture = i

    @property
    def recs(self) -> POINTER(Rectangle):
        return self.recs

    @recs.setter
    def recs(self, i: POINTER(Rectangle)) -> None:
        self.recs = i

    @property
    def glyphs(self) -> POINTER(GlyphInfo):
        return self.glyphs

    @glyphs.setter
    def glyphs(self, i: POINTER(GlyphInfo)) -> None:
        self.glyphs = i

    def __set(self, font: 'Font'):
        super.__init__(self, font.baseSize, font.glyphCount, font.glyphPadding, font.texture, font.recs, font.glyphs)
