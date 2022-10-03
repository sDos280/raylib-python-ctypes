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
    c_long,
    c_ulong,
    c_longlong,
    c_ulonglong,
    c_longdouble
)

Bool = c_bool  # C type: _Bool  Python type: bool (1)
Char = c_char  # C type: char  Python type: 1-character bytes object
UChar = c_ubyte  # C type: unsigned char  Python type: int
Short = c_short  # C type: short  Python type: int
UShort = c_ushort  # C type: unsigned short  Python type: int
Int = c_int  # C type: int  Python type: int
UInt = c_uint  # C type: unsigned int  Python type: int
Long = c_long  # C type: long  Python type: int
ULong = c_ulong  # C type: unsigned long  Python type: int
ULLong = c_longlong  # C type: __int64 or long-long  Python type: int
ULLong = c_ulonglong  # C type: unsigned __int64 or unsigned long-long  Python type: int
Float = c_float  # C type: float  Python type: float
Double = c_double  # C type: double  Python type: float
LDouble = c_longdouble  # C type: long double  Python type: float
CharPnt = c_char_p  # C type: char* (NUL terminated)  Python type: bytes object or None
VoidPtr = c_void_p  # C type: wchar_t* (NUL terminated)  Python type: int or None
Void = c_void_p  # C type: void  Python type: None


# ----------------------------------------------------------------------------------
# Structures Definition
# ----------------------------------------------------------------------------------

# Vector2, 2 components
class Vector2(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
    ]

    @property
    def x(self) -> float:
        pass

    @x.setter
    def x(self, i: float) -> None:
        pass

    @property
    def y(self) -> float:
        pass

    @y.setter
    def y(self, i: float) -> None:
        pass


# Vector3, 3 components
class Vector3(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
    ]

    @property
    def x(self) -> float:
        pass

    @x.setter
    def x(self, i: float) -> None:
        pass

    @property
    def y(self) -> float:
        pass

    @y.setter
    def y(self, i: float) -> None:
        pass

    @property
    def z(self) -> float:
        pass

    @z.setter
    def z(self, i: float) -> None:
        pass


# Vector4, 4 components
class Vector4(Structure):
    _fields_ = [
        ('x', Float),  # Vector x component
        ('y', Float),  # Vector y component
        ('z', Float),  # Vector z component
        ('w', Float),  # Vector w component
    ]

    @property
    def x(self) -> float:
        pass

    @x.setter
    def x(self, i: float) -> None:
        pass

    @property
    def y(self) -> float:
        pass

    @y.setter
    def y(self, i: float) -> None:
        pass

    @property
    def z(self) -> float:
        pass

    @z.setter
    def z(self, i: float) -> None:
        pass

    @property
    def w(self) -> float:
        pass

    @w.setter
    def w(self, i: float) -> None:
        pass


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4


# Matrix, 4x4 components, column major, OpenGL style, right-handed
class Matrix(Structure):
    _fields_ = [
        ('m0', Float), ('m4', Float), ('m8', Float), ('m12', Float),  # Matrix first row (4 components)
        ('m1', Float), ('m5', Float), ('m9', Float), ('m13', Float),  # Matrix second row (4 components)
        ('m2', Float), ('m6', Float), ('m10', Float), ('m14', Float),  # Matrix third row (4 components)
        ('m3', Float), ('m7', Float), ('m11', Float), ('m15', Float),  # Matrix fourth row (4 components)
    ]

    @property
    def m0(self) -> float:
        pass

    @m0.setter
    def m0(self, i: float) -> None:
        pass

    @property
    def m1(self) -> float:
        pass

    @m1.setter
    def m1(self, i: float) -> None:
        pass

    @property
    def m2(self) -> float:
        pass

    @m2.setter
    def m2(self, i: float) -> None:
        pass

    @property
    def m3(self) -> float:
        pass

    @m3.setter
    def m3(self, i: float) -> None:
        pass

    @property
    def m4(self) -> float:
        pass

    @m4.setter
    def m4(self, i: float) -> None:
        pass

    @property
    def m5(self) -> float:
        pass

    @m5.setter
    def m5(self, i: float) -> None:
        pass

    @property
    def m6(self) -> float:
        pass

    @m6.setter
    def m6(self, i: float) -> None:
        pass

    @property
    def m7(self) -> float:
        pass

    @m7.setter
    def m7(self, i: float) -> None:
        pass

    @property
    def m8(self) -> float:
        pass

    @m8.setter
    def m8(self, i: float) -> None:
        pass

    @property
    def m9(self) -> float:
        pass

    @m9.setter
    def m9(self, i: float) -> None:
        pass

    @property
    def m10(self) -> float:
        pass

    @m10.setter
    def m10(self, i: float) -> None:
        pass

    @property
    def m11(self) -> float:
        pass

    @m11.setter
    def m11(self, i: float) -> None:
        pass

    @property
    def m12(self) -> float:
        pass

    @m12.setter
    def m12(self, i: float) -> None:
        pass

    @property
    def m13(self) -> float:
        pass

    @m13.setter
    def m13(self, i: float) -> None:
        pass

    @property
    def m14(self) -> float:
        pass

    @m14.setter
    def m14(self, i: float) -> None:
        pass

    @property
    def m15(self) -> float:
        pass

    @m15.setter
    def m15(self, i: float) -> None:
        pass


# Color, 4 components, R8G8B8A8 (32bit)
class Color(Structure):
    _fields_ = [
        ('r', UChar),  # Color red value
        ('g', UChar),  # Color green value
        ('b', UChar),  # Color blue value
        ('a', UChar),  # Color alpha value
    ]

    @property
    def r(self) -> int:
        pass

    @r.setter
    def r(self, i: int) -> None:
        pass

    @property
    def g(self) -> int:
        pass

    @g.setter
    def g(self, i: int) -> None:
        pass

    @property
    def b(self) -> int:
        pass

    @b.setter
    def b(self, i: int) -> None:
        pass

    @property
    def a(self) -> int:
        pass

    @a.setter
    def a(self, i: int) -> None:
        pass


# Rectangle, 4 components
class Rectangle(Structure):
    _fields_ = [
        ('x', Float),  # Color red value
        ('y', Float),  # Color green value
        ('width', Float),  # Color blue value
        ('height', Float),  # Color alpha value
    ]

    @property
    def x(self) -> float:
        pass

    @x.setter
    def x(self, i: float) -> None:
        pass

    @property
    def y(self) -> float:
        pass

    @y.setter
    def y(self, i: float) -> None:
        pass

    @property
    def width(self) -> float:
        pass

    @width.setter
    def width(self, i: float) -> None:
        pass

    @property
    def height(self) -> float:
        pass

    @height.setter
    def height(self, i: float) -> None:
        pass


# Image, pixel data stored in CPU memory (RAM)
class Image(Structure):
    _fields_ = [
        ('data', VoidPtr),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    @property
    def data(self) -> VoidPtr:
        pass

    @data.setter
    def data(self, i: VoidPtr) -> None:
        pass

    @property
    def width(self) -> int:
        pass

    @width.setter
    def width(self, i: int) -> None:
        pass

    @property
    def height(self) -> int:
        pass

    @height.setter
    def height(self, i: int) -> None:
        pass

    @property
    def mipmaps(self) -> int:
        pass

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        pass

    @property
    def format(self) -> int:
        pass

    @format.setter
    def format(self, i: int) -> None:
        pass


# Texture, tex data stored in GPU memory (VRAM)
class Texture(Structure):
    _fields_ = [
        ('id', UInt),  # Image raw data
        ('width', Int),  # Image base width
        ('height', Int),  # Image base height
        ('mipmaps', Int),  # Mipmap levels, 1 by default
        ('format', Int)  # Data format (PixelFormat type)
    ]

    @property
    def id(self) -> UInt:
        pass

    @id.setter
    def id(self, i: UInt) -> None:
        pass

    @property
    def width(self) -> int:
        pass

    @width.setter
    def width(self, i: int) -> None:
        pass

    @property
    def height(self) -> int:
        pass

    @height.setter
    def height(self, i: int) -> None:
        pass

    @property
    def mipmaps(self) -> int:
        pass

    @mipmaps.setter
    def mipmaps(self, i: int) -> None:
        pass

    @property
    def format(self) -> int:
        pass

    @format.setter
    def format(self, i: int) -> None:
        pass


# Texture2D, same as Texture
Texture2D = Texture

# TextureCubemap, same as Texture
TextureCubemap = Texture


# RenderTexture, fbo for texture rendering
class RenderTexture(Structure):
    _fields_ = [
        ('id', UInt),  # OpenGL framebuffer object id
        ('texture', Texture),  # Image base width
        ('depth', Texture)  # Image base width
    ]

    @property
    def id(self) -> int:
        pass

    @id.setter
    def id(self, i: int) -> None:
        pass

    @property
    def texture(self) -> Texture:
        pass

    @texture.setter
    def texture(self, i: Texture) -> None:
        pass

    @property
    def depth(self) -> Texture:
        pass

    @depth.setter
    def depth(self, i: Texture) -> None:
        pass


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture


# NPatchInfo, n-patch layout infoStructureers
class NPatchInfo(Structure):
    _fields_ = [
        ('source', Rectangle),  # Texture source rectangle
        ('left', Int),  # Left border offset
        ('top', Int),  # Top border offset
        ('right', Int),  # Right border offset
        ('bottom', Int),  # Bottom border offset
        ('layout', Int)  # Layout of the n-patch: 3x3, 1x3 or 3x1
    ]

    @property
    def source(self) -> Rectangle:
        pass

    @source.setter
    def source(self, i: Rectangle) -> None:
        pass

    @property
    def left(self) -> int:
        pass

    @left.setter
    def left(self, i: int) -> None:
        pass

    @property
    def top(self) -> int:
        pass

    @top.setter
    def top(self, i: int) -> None:
        pass

    @property
    def right(self) -> int:
        pass

    @right.setter
    def right(self, i: int) -> None:
        pass

    @property
    def bottom(self) -> int:
        pass

    @bottom.setter
    def bottom(self, i: int) -> None:
        pass

    @property
    def layout(self) -> int:
        pass

    @layout.setter
    def layout(self, i: int) -> None:
        pass


# GlyphInfo, font characters glyphs info
class GlyphInfo(Structure):
    _fields_ = [
        ('value', Int),  # Character value (Unicode)
        ('offsetX', Int),  # Character offset X when drawing
        ('offsetY', Int),  # Character offset Y when drawing
        ('advanceX', Int),  # Character advance position X
        ('image', Image)  # Character image data
    ]

    @property
    def value(self) -> int:
        pass

    @value.setter
    def value(self, i: int) -> None:
        pass

    @property
    def offsetX(self) -> int:
        pass

    @offsetX.setter
    def offsetX(self, i: int) -> None:
        pass

    @property
    def offsetY(self) -> int:
        pass

    @offsetY.setter
    def offsetY(self, i: int) -> None:
        pass

    @property
    def advanceX(self) -> int:
        pass

    @advanceX.setter
    def advanceX(self, i: int) -> None:
        pass

    @property
    def image(self) -> Image:
        pass

    @image.setter
    def image(self, i: Image) -> None:
        pass


# Font, font texture and GlyphInfo array data
class Font(Structure):
    _fields_ = [
        ('baseSize', Int),  # Character value (Unicode)
        ('glyphCount', Int),  # Character offset X when drawing
        ('glyphPadding', Int),  # Character offset Y when drawing
        ('texture', Texture2D),  # Character advance position X
        ('recs', POINTER(Rectangle)),  # Character image data
        ('glyphs', POINTER(GlyphInfo))  # Character image data
    ]

    @property
    def baseSize(self) -> int:
        pass

    @baseSize.setter
    def baseSize(self, i: int) -> None:
        pass

    @property
    def glyphCount(self) -> int:
        pass

    @glyphCount.setter
    def glyphCount(self, i: int) -> None:
        pass

    @property
    def glyphPadding(self) -> int:
        pass

    @glyphPadding.setter
    def glyphPadding(self, i: int) -> None:
        pass

    @property
    def texture(self) -> Texture2D:
        pass

    @texture.setter
    def texture(self, i: Texture2D) -> None:
        pass

    @property
    def recs(self) -> POINTER(Rectangle):
        pass

    @recs.setter
    def recs(self, i: POINTER(Rectangle)) -> None:
        pass

    @property
    def glyphs(self) -> POINTER(GlyphInfo):
        pass

    @glyphs.setter
    def glyphs(self, i: POINTER(GlyphInfo)) -> None:
        pass
