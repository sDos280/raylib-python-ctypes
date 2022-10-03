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
UCharPtr = POINTER(c_ubyte)  # C type: unsigned char *  Python type: int
Short = c_short  # C type: short  Python type: int
UShort = c_ushort  # C type: unsigned short  Python type: int
UShortPtr = POINTER(c_ushort)  # C type: unsigned short *  Python type: int
Int = c_int  # C type: int  Python type: int
IntPtr = POINTER(c_int)  # C type: int *  Python type: int
UInt = c_uint  # C type: unsigned int  Python type: int
UIntPtr = POINTER(c_uint)  # C type: unsigned int * Python type: int
Long = c_long  # C type: long  Python type: int
ULong = c_ulong  # C type: unsigned long  Python type: int
ULLong = c_longlong  # C type: __int64 or long-long  Python type: int
ULLong = c_ulonglong  # C type: unsigned __int64 or unsigned long-long  Python type: int
Float = c_float  # C type: float  Python type: float
FloatPtr = POINTER(c_float)  # C type: float*  Python type: iny
Double = c_double  # C type: double  Python type: float
LDouble = c_longdouble  # C type: long double  Python type: float
CharPtr = c_char_p  # C type: char* (NUL terminated)  Python type: bytes object or None
VoidPtr = c_void_p  # C type: wchar_t* (NUL terminated)  Python type: int or None
Void = c_void_p  # C type: void  Python type: None


def _to_byte_str(value: str):
    pass


def _to_str(value: bytes):
    pass


def copyDataTo(src, dest):
    pass


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


# Camera, defines position/orientation in 3d space
class Camera3D(Structure):
    _fields_ = [
        ('position', Vector3),  # Camera position
        ('target', Vector3),  # Camera target it looks-at
        ('up', Vector3),  # Camera up vector (rotation over its axis)
        ('fovy', Float),
        # Camera field-of-view aperture in Y (degrees) in perspective, used as near plane width in orthographic
        ('projection', Int)  # CCamera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
    ]

    @property
    def position(self) -> Vector3:
        pass

    @position.setter
    def position(self, i: Vector3) -> None:
        pass

    @property
    def target(self) -> Vector3:
        pass

    @target.setter
    def target(self, i: Vector3) -> None:
        pass

    @property
    def up(self) -> Vector3:
        pass

    @up.setter
    def up(self, i: Vector3) -> None:
        pass

    @property
    def fovy(self) -> float:
        pass

    @fovy.setter
    def fovy(self, i: float) -> None:
        pass

    @property
    def projection(self) -> int:
        pass

    @projection.setter
    def projection(self, i: int) -> None:
        pass


# Camera type fallback, defaults to Camera3D
Camera = Camera3D


# Camera2D, defines position/orientation in 2d space
class Camera2D(Structure):
    _fields_ = [
        ('offset', Vector2),  # Camera offset (displacement from target)
        ('target', Vector2),  # Camera target (rotation and zoom origin)
        ('rotation', Float),  # Camera rotation in degrees
        ('zoom', Float)  # Camera zoom (scaling), should be 1.0f by default
    ]

    @property
    def offset(self) -> Vector2:
        pass

    @offset.setter
    def offset(self, i: Vector2) -> None:
        pass

    @property
    def target(self) -> Vector2:
        pass

    @target.setter
    def target(self, i: Vector2) -> None:
        pass

    @property
    def rotation(self) -> float:
        pass

    @rotation.setter
    def rotation(self, i: float) -> None:
        pass

    @property
    def zoom(self) -> float:
        pass

    @zoom.setter
    def zoom(self, i: float) -> None:
        pass


# Mesh, vertex data and vao/vbo
class Mesh(Structure):
    _fields_ = [
        ('vertexCount', Int),  # Number of vertices stored in arrays
        ('triangleCount', Int),  # Number of triangles stored (indexed or not)

        # Vertex attributes data
        ('vertices', FloatPtr),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
        ('texcoords', FloatPtr),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
        ('texcoords2', FloatPtr),
        # Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
        ('normals', FloatPtr),  # Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
        ('tangents', FloatPtr),  # Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
        ('colors', UCharPtr),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
        ('indices', UShortPtr),  # Vertex indices (in case vertex data comes indexed)

        # Animation vertex data
        ('animVertices', FloatPtr),  # Camera zoom (scaling), should be 1.0f by default
        ('animNormals', FloatPtr),  # Camera zoom (scaling), should be 1.0f by default
        ('boneIds', Float),  # Camera zoom (scaling), should be 1.0f by default
        ('boneWeights', FloatPtr),  # Camera zoom (scaling), should be 1.0f by default

        # OpenGL identifiers
        ('vaoId', UInt),  # OpenGL Vertex Array Object id
        ('vboId', UIntPtr)  # OpenGL Vertex Buffer Objects id (default vertex data)
    ]

    @property
    def vertexCount(self) -> int:
        pass

    @vertexCount.setter
    def vertexCount(self, i: int) -> None:
        pass

    @property
    def triangleCount(self) -> int:
        pass

    @triangleCount.setter
    def triangleCount(self, i: int) -> None:
        pass

    @property
    def vertices(self) -> FloatPtr:
        pass

    @vertices.setter
    def vertices(self, i: FloatPtr) -> None:
        pass

    @property
    def texcoords(self) -> FloatPtr:
        pass

    @texcoords.setter
    def texcoords(self, i: FloatPtr) -> None:
        pass

    @property
    def texcoords2(self) -> FloatPtr:
        pass

    @texcoords2.setter
    def texcoords2(self, i: FloatPtr) -> None:
        pass

    @property
    def normals(self) -> FloatPtr:
        pass

    @normals.setter
    def normals(self, i: FloatPtr) -> None:
        pass

    @property
    def tangents(self) -> FloatPtr:
        pass

    @tangents.setter
    def tangents(self, i: FloatPtr) -> None:
        pass

    @property
    def colors(self) -> UCharPtr:
        pass

    @colors.setter
    def colors(self, i: UCharPtr) -> None:
        pass

    @property
    def indices(self) -> UShortPtr:
        pass

    @indices.setter
    def indices(self, i: UShortPtr) -> None:
        pass

    @property
    def animVertices(self) -> FloatPtr:
        pass

    @animVertices.setter
    def animVertices(self, i: FloatPtr) -> None:
        pass

    @property
    def animNormals(self) -> FloatPtr:
        pass

    @animNormals.setter
    def animNormals(self, i: FloatPtr) -> None:
        pass

    @property
    def boneIds(self) -> UCharPtr:
        pass

    @boneIds.setter
    def boneIds(self, i: UCharPtr) -> None:
        pass

    @property
    def boneWeights(self) -> FloatPtr:
        pass

    @boneWeights.setter
    def boneWeights(self, i: FloatPtr) -> None:
        pass

    @property
    def vaoId(self) -> int:
        pass

    @vaoId.setter
    def vaoId(self, i: int) -> None:
        pass

    @property
    def vboId(self) -> UIntPtr:
        pass

    @vboId.setter
    def vboId(self, i: UIntPtr) -> None:
        pass


# Shader
class Shader(Structure):
    _fields_ = [
        ('id', UInt),  # Shader program id
        ('locs', IntPtr)  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
    ]

    @property
    def id(self) -> int:
        pass

    @id.setter
    def id(self, i: int) -> None:
        pass

    @property
    def locs(self) -> IntPtr:
        pass

    @locs.setter
    def locs(self, i: IntPtr) -> None:
        pass


# MaterialMap
class MaterialMap(Structure):
    _fields_ = [
        ('texture', Texture2D),  # Material map texture
        ('color', Color),  # Material map color
        ('value', Float)  # Material map value
    ]

    @property
    def texture(self) -> Texture2D:
        pass

    @texture.setter
    def texture(self, i: Texture2D) -> None:
        pass

    @property
    def color(self) -> Color:
        pass

    @color.setter
    def color(self, i: Color) -> None:
        pass

    @property
    def value(self) -> float:
        pass

    @value.setter
    def value(self, i: float) -> None:
        pass


# Material, includes shader and maps
class Material(Structure):
    _fields_ = [
        ('shader', Shader),  # Material map texture
        ('maps', POINTER(MaterialMap)),  # Material map color
        ('params', Float * 4)  # Material map value
    ]

    @property
    def shader(self) -> Shader:
        pass

    @shader.setter
    def shader(self, i: Shader) -> None:
        pass

    @property
    def maps(self) -> POINTER(MaterialMap):
        pass

    @maps.setter
    def maps(self, i: POINTER(MaterialMap)) -> None:
        pass

    @property
    def params(self) -> Float * 4:
        pass

    @params.setter
    def params(self, i: Float * 4) -> None:
        pass


# Transform, vertex transformation data
class Transform(Structure):
    _fields_ = [
        ('translation', Vector3),  # Translation
        ('rotation', Quaternion),  # Rotation
        ('scale', Vector3)  # Scale
    ]

    @property
    def translation(self) -> Vector3:
        pass

    @translation.setter
    def translation(self, i: Vector3) -> None:
        pass

    @property
    def rotation(self) -> Quaternion:
        pass

    @rotation.setter
    def rotation(self, i: Quaternion) -> None:
        pass

    @property
    def scale(self) -> Vector3:
        pass

    @scale.setter
    def scale(self, i: Vector3) -> None:
        pass


# Bone, skeletal animation bone
class BoneInfo(Structure):
    _fields_ = [
        ('name', Char * 32),  # Bone name
        ('parent', Int),  # Bone parent
    ]

    @property
    def name(self) -> Char * 32:
        pass

    @name.setter
    def name(self, i: Char * 32) -> None:
        pass

    @property
    def parent(self) -> int:
        pass

    @parent.setter
    def parent(self, i: int) -> None:
        pass


# Model, meshes, materials and animation data
class Model(Structure):
    _fields_ = [
        ('transform', Matrix),  # Local transform matrix

        ('meshCount', Int),  # Number of meshes
        ('materialCount', Int),  # Number of materials
        ('meshes', POINTER(Mesh)),  # Meshes array
        ('materials', POINTER(Material)),  # Materials array
        ('meshMaterial', IntPtr),  # Mesh material number

        # Animation data
        ('boneCount', Int),  # Number of bones
        ('bones', POINTER(BoneInfo)),  # Bones information (skeleton)
        ('bindPose', POINTER(Transform))  # Bones base transformation (pose)
    ]

    @property
    def transform(self) -> Matrix:
        pass

    @transform.setter
    def transform(self, i: Matrix) -> None:
        pass

    @property
    def meshCount(self) -> int:
        pass

    @meshCount.setter
    def meshCount(self, i: int) -> None:
        pass

    @property
    def materialCount(self) -> int:
        pass

    @materialCount.setter
    def materialCount(self, i: int) -> None:
        pass

    @property
    def meshes(self) -> POINTER(Mesh):
        pass

    @meshes.setter
    def meshes(self, i: POINTER(Mesh)) -> None:
        pass

    @property
    def materials(self) -> POINTER(Material):
        pass

    @materials.setter
    def materials(self, i: POINTER(Material)) -> None:
        pass

    @property
    def meshMaterial(self) -> IntPtr:
        pass

    @meshMaterial.setter
    def meshMaterial(self, i: IntPtr) -> None:
        pass

    @property
    def boneCount(self) -> int:
        pass

    @boneCount.setter
    def boneCount(self, i: int) -> None:
        pass

    @property
    def bones(self) -> POINTER(BoneInfo):
        pass

    @bones.setter
    def bones(self, i: POINTER(BoneInfo)) -> None:
        pass

    @property
    def bindPose(self) -> POINTER(Transform):
        pass

    @bindPose.setter
    def bindPose(self, i: POINTER(Transform)) -> None:
        pass


# ModelAnimation
class Model(Structure):
    _fields_ = [
        ('boneCount', Int),  # Number of bones
        ('frameCount', Int),  # Number of animation frames
        ('bones', POINTER(BoneInfo)),  # Bones information (skeleton)
        ('framePoses', POINTER(POINTER(Transform)))  # Poses array by frame
    ]

    @property
    def boneCount(self) -> int:
        pass

    @boneCount.setter
    def boneCount(self, i: int) -> None:
        pass

    @property
    def frameCount(self) -> int:
        pass

    @frameCount.setter
    def frameCount(self, i: int) -> None:
        pass

    @property
    def bones(self) -> POINTER(BoneInfo):
        pass

    @bones.setter
    def bones(self, i: POINTER(BoneInfo)) -> None:
        pass

    @property
    def framePoses(self) -> POINTER(POINTER(Transform)):
        pass

    @framePoses.setter
    def framePoses(self, i: POINTER(POINTER(Transform))) -> None:
        pass


# Ray, ray for raycasting
class Ray(Structure):
    _fields_ = [
        ('position', Vector3),  # Ray position (origin)
        ('direction', Vector3)  # Ray direction
    ]

    @property
    def position(self) -> Vector3:
        pass

    @position.setter
    def position(self, i: Vector3) -> None:
        pass

    @property
    def direction(self) -> Vector3:
        pass

    @direction.setter
    def direction(self, i: Vector3) -> None:
        pass


# RayCollision, ray hit information
class RayCollision(Structure):
    _fields_ = [
        ('hit', Bool),  # Did the ray hit something?
        ('distance', Float),  # Distance to the nearest hit
        ('point', Vector3),  # Point of the nearest hit
        ('normal', Vector3)  # Surface normal of hit
    ]

    @property
    def hit(self) -> bool:
        pass

    @hit.setter
    def hit(self, i: bool) -> None:
        pass

    @property
    def distance(self) -> float:
        pass

    @distance.setter
    def distance(self, i: float) -> None:
        pass

    @property
    def point(self) -> Vector3:
        pass

    @point.setter
    def point(self, i: Vector3) -> None:
        pass

    @property
    def normal(self) -> Vector3:
        pass

    @normal.setter
    def normal(self, i: Vector3) -> None:
        pass


# BoundingBox
class BoundingBox(Structure):
    _fields_ = [
        ('min', Vector3),  # Minimum vertex box-corner
        ('max', Vector3)  # Maximum vertex box-corner
    ]

    @property
    def min(self) -> Vector3:
        pass

    @min.setter
    def min(self, i: Vector3) -> None:
        pass

    @property
    def max(self) -> Vector3:
        pass

    @max.setter
    def max(self, i: Vector3) -> None:
        pass


# File path list
class FilePathList(Structure):
    _fields_ = [
        ('capacity', UInt),  # Filepaths max entries
        ('count', UInt),  # Filepaths entries count
        ('paths', POINTER(CharPtr))  # Filepaths entries
    ]

    @property
    def capacity(self) -> int:
        pass

    @capacity.setter
    def capacity(self, i: int) -> None:
        pass

    @property
    def count(self) -> int:
        pass

    @count.setter
    def count(self, i: int) -> None:
        pass

    @property
    def paths(self) -> POINTER(CharPtr):
        pass

    @paths.setter
    def paths(self, i: POINTER(CharPtr)) -> None:
        pass
