from ctypes import *


#  Vector2, 2 components
class Vector2(Structure):
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float)  # Vector y component
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i


#  Vector3, 3 components
class Vector3(Structure):
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float)  # Vector z component
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i

	@property
	def z(self) -> float:
		return self.z

	@z.setter
	def z(self, i: float) -> None:
		self.z = i


#  Vector4, 4 components
class Vector4(Structure):
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float),  # Vector z component
		('w', c_float)  # Vector w component
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i

	@property
	def z(self) -> float:
		return self.z

	@z.setter
	def z(self, i: float) -> None:
		self.z = i

	@property
	def w(self) -> float:
		return self.w

	@w.setter
	def w(self, i: float) -> None:
		self.w = i


#  Quaternion, 4 components (Vector4 alias)
class Quaternion(Structure):
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float),  # Vector z component
		('w', c_float)  # Vector w component
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i

	@property
	def z(self) -> float:
		return self.z

	@z.setter
	def z(self, i: float) -> None:
		self.z = i

	@property
	def w(self) -> float:
		return self.w

	@w.setter
	def w(self, i: float) -> None:
		self.w = i


#  Matrix, 4x4 components, column major, OpenGL style, right handed
class Matrix(Structure):
	_fields_ = [
		('m0', c_float),  # Matrix first row (4 components)
		('m4', c_float),  # Matrix first row (4 components)
		('m8', c_float),  # Matrix first row (4 components)
		('m12', c_float),  # Matrix first row (4 components)
		('m1', c_float),  # Matrix second row (4 components)
		('m5', c_float),  # Matrix second row (4 components)
		('m9', c_float),  # Matrix second row (4 components)
		('m13', c_float),  # Matrix second row (4 components)
		('m2', c_float),  # Matrix third row (4 components)
		('m6', c_float),  # Matrix third row (4 components)
		('m10', c_float),  # Matrix third row (4 components)
		('m14', c_float),  # Matrix third row (4 components)
		('m3', c_float),  # Matrix fourth row (4 components)
		('m7', c_float),  # Matrix fourth row (4 components)
		('m11', c_float),  # Matrix fourth row (4 components)
		('m15', c_float)  # Matrix fourth row (4 components)
	]

	@property
	def m0(self) -> float:
		return self.m0

	@m0.setter
	def m0(self, i: float) -> None:
		self.m0 = i

	@property
	def m4(self) -> float:
		return self.m4

	@m4.setter
	def m4(self, i: float) -> None:
		self.m4 = i

	@property
	def m8(self) -> float:
		return self.m8

	@m8.setter
	def m8(self, i: float) -> None:
		self.m8 = i

	@property
	def m12(self) -> float:
		return self.m12

	@m12.setter
	def m12(self, i: float) -> None:
		self.m12 = i

	@property
	def m1(self) -> float:
		return self.m1

	@m1.setter
	def m1(self, i: float) -> None:
		self.m1 = i

	@property
	def m5(self) -> float:
		return self.m5

	@m5.setter
	def m5(self, i: float) -> None:
		self.m5 = i

	@property
	def m9(self) -> float:
		return self.m9

	@m9.setter
	def m9(self, i: float) -> None:
		self.m9 = i

	@property
	def m13(self) -> float:
		return self.m13

	@m13.setter
	def m13(self, i: float) -> None:
		self.m13 = i

	@property
	def m2(self) -> float:
		return self.m2

	@m2.setter
	def m2(self, i: float) -> None:
		self.m2 = i

	@property
	def m6(self) -> float:
		return self.m6

	@m6.setter
	def m6(self, i: float) -> None:
		self.m6 = i

	@property
	def m10(self) -> float:
		return self.m10

	@m10.setter
	def m10(self, i: float) -> None:
		self.m10 = i

	@property
	def m14(self) -> float:
		return self.m14

	@m14.setter
	def m14(self, i: float) -> None:
		self.m14 = i

	@property
	def m3(self) -> float:
		return self.m3

	@m3.setter
	def m3(self, i: float) -> None:
		self.m3 = i

	@property
	def m7(self) -> float:
		return self.m7

	@m7.setter
	def m7(self, i: float) -> None:
		self.m7 = i

	@property
	def m11(self) -> float:
		return self.m11

	@m11.setter
	def m11(self, i: float) -> None:
		self.m11 = i

	@property
	def m15(self) -> float:
		return self.m15

	@m15.setter
	def m15(self, i: float) -> None:
		self.m15 = i


#  Color, 4 components, R8G8B8A8 (32bit)
class Color(Structure):
	_fields_ = [
		('r', c_ubyte),  # Color red value
		('g', c_ubyte),  # Color green value
		('b', c_ubyte),  # Color blue value
		('a', c_ubyte)  # Color alpha value
	]

	@property
	def r(self) -> int:
		return self.r

	@r.setter
	def r(self, i: int) -> None:
		self.r = i

	@property
	def g(self) -> int:
		return self.g

	@g.setter
	def g(self, i: int) -> None:
		self.g = i

	@property
	def b(self) -> int:
		return self.b

	@b.setter
	def b(self, i: int) -> None:
		self.b = i

	@property
	def a(self) -> int:
		return self.a

	@a.setter
	def a(self, i: int) -> None:
		self.a = i


#  Rectangle, 4 components
class Rectangle(Structure):
	_fields_ = [
		('x', c_float),  # Rectangle top-left corner position x
		('y', c_float),  # Rectangle top-left corner position y
		('width', c_float),  # Rectangle width
		('height', c_float)  # Rectangle height
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i

	@property
	def width(self) -> float:
		return self.width

	@width.setter
	def width(self, i: float) -> None:
		self.width = i

	@property
	def height(self) -> float:
		return self.height

	@height.setter
	def height(self, i: float) -> None:
		self.height = i


#  Image, pixel data stored in CPU memory (RAM)
class Image(Structure):
	_fields_ = [
		('data', c_void_p),  # Image raw data
		('width', c_int),  # Image base width
		('height', c_int),  # Image base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def data(self) -> int:
		return self.data

	@data.setter
	def data(self, i: int) -> None:
		self.data = i

	@property
	def width(self) -> int:
		return self.width

	@width.setter
	def width(self, i: int) -> None:
		self.width = i

	@property
	def height(self) -> int:
		return self.height

	@height.setter
	def height(self, i: int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> int:
		return self.format

	@format.setter
	def format(self, i: int) -> None:
		self.format = i


#  Texture, tex data stored in GPU memory (VRAM)
class Texture(Structure):
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
		self.id = i

	@property
	def width(self) -> int:
		return self.width

	@width.setter
	def width(self, i: int) -> None:
		self.width = i

	@property
	def height(self) -> int:
		return self.height

	@height.setter
	def height(self, i: int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> int:
		return self.format

	@format.setter
	def format(self, i: int) -> None:
		self.format = i


#  Texture2D, same as Texture
class Texture2D(Structure):
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
		self.id = i

	@property
	def width(self) -> int:
		return self.width

	@width.setter
	def width(self, i: int) -> None:
		self.width = i

	@property
	def height(self) -> int:
		return self.height

	@height.setter
	def height(self, i: int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> int:
		return self.format

	@format.setter
	def format(self, i: int) -> None:
		self.format = i


#  TextureCubemap, same as Texture
class TextureCubemap(Structure):
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
		self.id = i

	@property
	def width(self) -> int:
		return self.width

	@width.setter
	def width(self, i: int) -> None:
		self.width = i

	@property
	def height(self) -> int:
		return self.height

	@height.setter
	def height(self, i: int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> int:
		return self.format

	@format.setter
	def format(self, i: int) -> None:
		self.format = i


#  RenderTexture, fbo for texture rendering
class RenderTexture(Structure):
	_fields_ = [
		('id', c_uint),  # OpenGL framebuffer object id
		('texture', Texture),  # Color buffer attachment texture
		('depth', Texture)  # Depth buffer attachment texture
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
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


#  RenderTexture2D, same as RenderTexture
class RenderTexture2D(Structure):
	_fields_ = [
		('id', c_uint),  # OpenGL framebuffer object id
		('texture', Texture),  # Color buffer attachment texture
		('depth', Texture)  # Depth buffer attachment texture
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
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


#  NPatchInfo, n-patch layout info
class NPatchInfo(Structure):
	_fields_ = [
		('source', Rectangle),  # Texture source rectangle
		('left', c_int),  # Left border offset
		('top', c_int),  # Top border offset
		('right', c_int),  # Right border offset
		('bottom', c_int),  # Bottom border offset
		('layout', c_int),  # Layout of the n-patch: 3x3 1x3 or 3x1
	]

	@property
	def source(self) -> Rectangle:
		return self.source

	@source.setter
	def source(self, i: Rectangle) -> None:
		self.source = i

	@property
	def left(self) -> int:
		return self.left

	@left.setter
	def left(self, i: int) -> None:
		self.left = i

	@property
	def top(self) -> int:
		return self.top

	@top.setter
	def top(self, i: int) -> None:
		self.top = i

	@property
	def right(self) -> int:
		return self.right

	@right.setter
	def right(self, i: int) -> None:
		self.right = i

	@property
	def bottom(self) -> int:
		return self.bottom

	@bottom.setter
	def bottom(self, i: int) -> None:
		self.bottom = i

	@property
	def layout(self) -> int:
		return self.layout

	@layout.setter
	def layout(self, i: int) -> None:
		self.layout = i


#  GlyphInfo, font characters glyphs info
class GlyphInfo(Structure):
	_fields_ = [
		('value', c_int),  # Character value (Unicode)
		('offsetX', c_int),  # Character offset X when drawing
		('offsetY', c_int),  # Character offset Y when drawing
		('advanceX', c_int),  # Character advance position X
		('image', Image)  # Character image data
	]

	@property
	def value(self) -> int:
		return self.value

	@value.setter
	def value(self, i: int) -> None:
		self.value = i

	@property
	def offsetX(self) -> int:
		return self.offsetX

	@offsetX.setter
	def offsetX(self, i: int) -> None:
		self.offsetX = i

	@property
	def offsetY(self) -> int:
		return self.offsetY

	@offsetY.setter
	def offsetY(self, i: int) -> None:
		self.offsetY = i

	@property
	def advanceX(self) -> int:
		return self.advanceX

	@advanceX.setter
	def advanceX(self, i: int) -> None:
		self.advanceX = i

	@property
	def image(self) -> Image:
		return self.image

	@image.setter
	def image(self, i: Image) -> None:
		self.image = i


#  Font, font texture and GlyphInfo array data
class Font(Structure):
	_fields_ = [
		('baseSize', c_int),  # Base size (default chars height)
		('glyphCount', c_int),  # Number of glyph characters
		('glyphPadding', c_int),  # Padding around the glyph characters
		('texture', Texture2D),  # Texture atlas containing the glyphs
		('recs', POINTER(Rectangle)),  # Rectangles in texture for the glyphs
		('glyphs', POINTER(GlyphInfo))  # Glyphs info data
	]

	@property
	def baseSize(self) -> int:
		return self.baseSize

	@baseSize.setter
	def baseSize(self, i: int) -> None:
		self.baseSize = i

	@property
	def glyphCount(self) -> int:
		return self.glyphCount

	@glyphCount.setter
	def glyphCount(self, i: int) -> None:
		self.glyphCount = i

	@property
	def glyphPadding(self) -> int:
		return self.glyphPadding

	@glyphPadding.setter
	def glyphPadding(self, i: int) -> None:
		self.glyphPadding = i

	@property
	def texture(self) -> Texture2D:
		return self.texture

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


#  Camera, defines position/orientation in 3d space
class Camera3D(Structure):
	_fields_ = [
		('position', Vector3),  # Camera position
		('target', Vector3),  # Camera target it looks-at
		('up', Vector3),  # Camera up vector (rotation over its axis)
		('fovy', c_float),  # Camera field-of-view aperture in Y (degrees) in perspective, used as near plane width in orthographic
		('projection', c_int)  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
	]

	@property
	def position(self) -> Vector3:
		return self.position

	@position.setter
	def position(self, i: Vector3) -> None:
		self.position = i

	@property
	def target(self) -> Vector3:
		return self.target

	@target.setter
	def target(self, i: Vector3) -> None:
		self.target = i

	@property
	def up(self) -> Vector3:
		return self.up

	@up.setter
	def up(self, i: Vector3) -> None:
		self.up = i

	@property
	def fovy(self) -> float:
		return self.fovy

	@fovy.setter
	def fovy(self, i: float) -> None:
		self.fovy = i

	@property
	def projection(self) -> int:
		return self.projection

	@projection.setter
	def projection(self, i: int) -> None:
		self.projection = i


#  Camera type fallback, defaults to Camera3D
class Camera(Structure):
	_fields_ = [
		('position', Vector3),  # Camera position
		('target', Vector3),  # Camera target it looks-at
		('up', Vector3),  # Camera up vector (rotation over its axis)
		('fovy', c_float),  # Camera field-of-view aperture in Y (degrees) in perspective, used as near plane width in orthographic
		('projection', c_int)  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
	]

	@property
	def position(self) -> Vector3:
		return self.position

	@position.setter
	def position(self, i: Vector3) -> None:
		self.position = i

	@property
	def target(self) -> Vector3:
		return self.target

	@target.setter
	def target(self, i: Vector3) -> None:
		self.target = i

	@property
	def up(self) -> Vector3:
		return self.up

	@up.setter
	def up(self, i: Vector3) -> None:
		self.up = i

	@property
	def fovy(self) -> float:
		return self.fovy

	@fovy.setter
	def fovy(self, i: float) -> None:
		self.fovy = i

	@property
	def projection(self) -> int:
		return self.projection

	@projection.setter
	def projection(self, i: int) -> None:
		self.projection = i


#  Camera2D, defines position/orientation in 2d space
class Camera2D(Structure):
	_fields_ = [
		('offset', Vector2),  # Camera offset (displacement from target)
		('target', Vector2),  # Camera target (rotation and zoom origin)
		('rotation', c_float),  # Camera rotation in degrees
		('zoom', c_float),  # Camera zoom (scaling) should be 1.0f by default
	]

	@property
	def offset(self) -> Vector2:
		return self.offset

	@offset.setter
	def offset(self, i: Vector2) -> None:
		self.offset = i

	@property
	def target(self) -> Vector2:
		return self.target

	@target.setter
	def target(self, i: Vector2) -> None:
		self.target = i

	@property
	def rotation(self) -> float:
		return self.rotation

	@rotation.setter
	def rotation(self, i: float) -> None:
		self.rotation = i

	@property
	def zoom(self) -> float:
		return self.zoom

	@zoom.setter
	def zoom(self, i: float) -> None:
		self.zoom = i


#  Mesh, vertex data and vao/vbo
class Mesh(Structure):
	_fields_ = [
		('vertexCount', c_int),  # Number of vertices stored in arrays
		('triangleCount', c_int),  # Number of triangles stored (indexed or not)
		('vertices', POINTER(c_float)),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
		('texcoords', POINTER(c_float)),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
		('texcoords2', POINTER(c_float)),  # Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
		('normals', POINTER(c_float)),  # Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
		('tangents', POINTER(c_float)),  # Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
		('colors', POINTER(c_ubyte)),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
		('indices', POINTER(c_ushort)),  # Vertex indices (in case vertex data comes indexed)
		('animVertices', POINTER(c_float)),  # Animated vertex positions (after bones transformations)
		('animNormals', POINTER(c_float)),  # Animated normals (after bones transformations)
		('boneIds', POINTER(c_ubyte)),  # Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
		('boneWeights', POINTER(c_float)),  # Vertex bone weight, up to 4 bones influence by vertex (skinning)
		('vaoId', c_uint),  # OpenGL Vertex Array Object id
		('vboId', POINTER(c_uint))  # OpenGL Vertex Buffer Objects id (default vertex data)
	]

	@property
	def vertexCount(self) -> int:
		return self.vertexCount

	@vertexCount.setter
	def vertexCount(self, i: int) -> None:
		self.vertexCount = i

	@property
	def triangleCount(self) -> int:
		return self.triangleCount

	@triangleCount.setter
	def triangleCount(self, i: int) -> None:
		self.triangleCount = i

	@property
	def vertices(self) -> POINTER(c_float):
		return self.vertices

	@vertices.setter
	def vertices(self, i: POINTER(c_float)) -> None:
		self.vertices = i

	@property
	def texcoords(self) -> POINTER(c_float):
		return self.texcoords

	@texcoords.setter
	def texcoords(self, i: POINTER(c_float)) -> None:
		self.texcoords = i

	@property
	def texcoords2(self) -> POINTER(c_float):
		return self.texcoords2

	@texcoords2.setter
	def texcoords2(self, i: POINTER(c_float)) -> None:
		self.texcoords2 = i

	@property
	def normals(self) -> POINTER(c_float):
		return self.normals

	@normals.setter
	def normals(self, i: POINTER(c_float)) -> None:
		self.normals = i

	@property
	def tangents(self) -> POINTER(c_float):
		return self.tangents

	@tangents.setter
	def tangents(self, i: POINTER(c_float)) -> None:
		self.tangents = i

	@property
	def colors(self) -> POINTER(c_ubyte):
		return self.colors

	@colors.setter
	def colors(self, i: POINTER(c_ubyte)) -> None:
		self.colors = i

	@property
	def indices(self) -> POINTER(c_ushort):
		return self.indices

	@indices.setter
	def indices(self, i: POINTER(c_ushort)) -> None:
		self.indices = i

	@property
	def animVertices(self) -> POINTER(c_float):
		return self.animVertices

	@animVertices.setter
	def animVertices(self, i: POINTER(c_float)) -> None:
		self.animVertices = i

	@property
	def animNormals(self) -> POINTER(c_float):
		return self.animNormals

	@animNormals.setter
	def animNormals(self, i: POINTER(c_float)) -> None:
		self.animNormals = i

	@property
	def boneIds(self) -> POINTER(c_ubyte):
		return self.boneIds

	@boneIds.setter
	def boneIds(self, i: POINTER(c_ubyte)) -> None:
		self.boneIds = i

	@property
	def boneWeights(self) -> POINTER(c_float):
		return self.boneWeights

	@boneWeights.setter
	def boneWeights(self, i: POINTER(c_float)) -> None:
		self.boneWeights = i

	@property
	def vaoId(self) -> int:
		return self.vaoId

	@vaoId.setter
	def vaoId(self, i: int) -> None:
		self.vaoId = i

	@property
	def vboId(self) -> POINTER(c_uint):
		return self.vboId

	@vboId.setter
	def vboId(self, i: POINTER(c_uint)) -> None:
		self.vboId = i


#  Shader
class Shader(Structure):
	_fields_ = [
		('id', c_uint),  # Shader program id
		('locs', POINTER(c_int))  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
	]

	@property
	def id(self) -> int:
		return self.id

	@id.setter
	def id(self, i: int) -> None:
		self.id = i

	@property
	def locs(self) -> POINTER(c_int):
		return self.locs

	@locs.setter
	def locs(self, i: POINTER(c_int)) -> None:
		self.locs = i


#  MaterialMap
class MaterialMap(Structure):
	_fields_ = [
		('texture', Texture2D),  # Material map texture
		('color', Color),  # Material map color
		('value', c_float)  # Material map value
	]

	@property
	def texture(self) -> Texture2D:
		return self.texture

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		self.texture = i

	@property
	def color(self) -> Color:
		return self.color

	@color.setter
	def color(self, i: Color) -> None:
		self.color = i

	@property
	def value(self) -> float:
		return self.value

	@value.setter
	def value(self, i: float) -> None:
		self.value = i


#  Material, includes shader and maps
class Material(Structure):
	_fields_ = [
		('shader', Shader),  # Material shader
		('maps', POINTER(MaterialMap)),  # Material maps array (MAX_MATERIAL_MAPS)
		('params', c_float*4)  # Material generic parameters (if required)
	]

	@property
	def shader(self) -> Shader:
		return self.shader

	@shader.setter
	def shader(self, i: Shader) -> None:
		self.shader = i

	@property
	def maps(self) -> POINTER(MaterialMap):
		return self.maps

	@maps.setter
	def maps(self, i: POINTER(MaterialMap)) -> None:
		self.maps = i

	@property
	def params(self) -> c_float * 4:
		return self.params

	@params.setter
	def params(self, i: c_float * 4) -> None:
		self.params = i


#  Transform, vertex transformation data
class Transform(Structure):
	_fields_ = [
		('translation', Vector3),  # Translation
		('rotation', Quaternion),  # Rotation
		('scale', Vector3)  # Scale
	]

	@property
	def translation(self) -> Vector3:
		return self.translation

	@translation.setter
	def translation(self, i: Vector3) -> None:
		self.translation = i

	@property
	def rotation(self) -> Quaternion:
		return self.rotation

	@rotation.setter
	def rotation(self, i: Quaternion) -> None:
		self.rotation = i

	@property
	def scale(self) -> Vector3:
		return self.scale

	@scale.setter
	def scale(self, i: Vector3) -> None:
		self.scale = i


#  Bone, skeletal animation bone
class BoneInfo(Structure):
	_fields_ = [
		('name', c_char*32),  # Bone name
		('parent', c_int)  # Bone parent
	]

	@property
	def name(self) -> c_char * 32:
		return self.name

	@name.setter
	def name(self, i: c_char * 32) -> None:
		self.name = i

	@property
	def parent(self) -> int:
		return self.parent

	@parent.setter
	def parent(self, i: int) -> None:
		self.parent = i


#  Model, meshes, materials and animation data
class Model(Structure):
	_fields_ = [
		('transform', Matrix),  # Local transform matrix
		('meshCount', c_int),  # Number of meshes
		('materialCount', c_int),  # Number of materials
		('meshes', POINTER(Mesh)),  # Meshes array
		('materials', POINTER(Material)),  # Materials array
		('meshMaterial', POINTER(c_int)),  # Mesh material number
		('boneCount', c_int),  # Number of bones
		('bones', POINTER(BoneInfo)),  # Bones information (skeleton)
		('bindPose', POINTER(Transform))  # Bones base transformation (pose)
	]

	@property
	def transform(self) -> Matrix:
		return self.transform

	@transform.setter
	def transform(self, i: Matrix) -> None:
		self.transform = i

	@property
	def meshCount(self) -> int:
		return self.meshCount

	@meshCount.setter
	def meshCount(self, i: int) -> None:
		self.meshCount = i

	@property
	def materialCount(self) -> int:
		return self.materialCount

	@materialCount.setter
	def materialCount(self, i: int) -> None:
		self.materialCount = i

	@property
	def meshes(self) -> POINTER(Mesh):
		return self.meshes

	@meshes.setter
	def meshes(self, i: POINTER(Mesh)) -> None:
		self.meshes = i

	@property
	def materials(self) -> POINTER(Material):
		return self.materials

	@materials.setter
	def materials(self, i: POINTER(Material)) -> None:
		self.materials = i

	@property
	def meshMaterial(self) -> POINTER(c_int):
		return self.meshMaterial

	@meshMaterial.setter
	def meshMaterial(self, i: POINTER(c_int)) -> None:
		self.meshMaterial = i

	@property
	def boneCount(self) -> int:
		return self.boneCount

	@boneCount.setter
	def boneCount(self, i: int) -> None:
		self.boneCount = i

	@property
	def bones(self) -> POINTER(BoneInfo):
		return self.bones

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		self.bones = i

	@property
	def bindPose(self) -> POINTER(Transform):
		return self.bindPose

	@bindPose.setter
	def bindPose(self, i: POINTER(Transform)) -> None:
		self.bindPose = i


#  ModelAnimation
class ModelAnimation(Structure):
	_fields_ = [
		('boneCount', c_int),  # Number of bones
		('frameCount', c_int),  # Number of animation frames
		('bones', POINTER(BoneInfo)),  # Bones information (skeleton)
		('framePoses', POINTER(POINTER(Transform)))  # Poses array by frame
	]

	@property
	def boneCount(self) -> int:
		return self.boneCount

	@boneCount.setter
	def boneCount(self, i: int) -> None:
		self.boneCount = i

	@property
	def frameCount(self) -> int:
		return self.frameCount

	@frameCount.setter
	def frameCount(self, i: int) -> None:
		self.frameCount = i

	@property
	def bones(self) -> POINTER(BoneInfo):
		return self.bones

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		self.bones = i

	@property
	def framePoses(self) -> POINTER(POINTER(Transform)):
		return self.framePoses

	@framePoses.setter
	def framePoses(self, i: POINTER(POINTER(Transform))) -> None:
		self.framePoses = i


#  Ray, ray for raycasting
class Ray(Structure):
	_fields_ = [
		('position', Vector3),  # Ray position (origin)
		('direction', Vector3)  # Ray direction
	]

	@property
	def position(self) -> Vector3:
		return self.position

	@position.setter
	def position(self, i: Vector3) -> None:
		self.position = i

	@property
	def direction(self) -> Vector3:
		return self.direction

	@direction.setter
	def direction(self, i: Vector3) -> None:
		self.direction = i


#  RayCollision, ray hit information
class RayCollision(Structure):
	_fields_ = [
		('hit', c_bool),  # Did the ray hit something?
		('distance', c_float),  # Distance to nearest hit
		('point', Vector3),  # Point of nearest hit
		('normal', Vector3)  # Surface normal of hit
	]

	@property
	def hit(self) -> bool:
		return self.hit

	@hit.setter
	def hit(self, i: bool) -> None:
		self.hit = i

	@property
	def distance(self) -> float:
		return self.distance

	@distance.setter
	def distance(self, i: float) -> None:
		self.distance = i

	@property
	def point(self) -> Vector3:
		return self.point

	@point.setter
	def point(self, i: Vector3) -> None:
		self.point = i

	@property
	def normal(self) -> Vector3:
		return self.normal

	@normal.setter
	def normal(self, i: Vector3) -> None:
		self.normal = i


#  BoundingBox
class BoundingBox(Structure):
	_fields_ = [
		('min', Vector3),  # Minimum vertex box-corner
		('max', Vector3)  # Maximum vertex box-corner
	]

	@property
	def min(self) -> Vector3:
		return self.min

	@min.setter
	def min(self, i: Vector3) -> None:
		self.min = i

	@property
	def max(self) -> Vector3:
		return self.max

	@max.setter
	def max(self, i: Vector3) -> None:
		self.max = i


#  VrDeviceInfo, Head-Mounted-Display device parameters
class VrDeviceInfo(Structure):
	_fields_ = [
		('hResolution', c_int),  # Horizontal resolution in pixels
		('vResolution', c_int),  # Vertical resolution in pixels
		('hScreenSize', c_float),  # Horizontal size in meters
		('vScreenSize', c_float),  # Vertical size in meters
		('vScreenCenter', c_float),  # Screen center in meters
		('eyeToScreenDistance', c_float),  # Distance between eye and display in meters
		('lensSeparationDistance', c_float),  # Lens separation distance in meters
		('interpupillaryDistance', c_float),  # IPD (distance between pupils) in meters
		('lensDistortionValues', c_float*4),  # Lens distortion constant parameters
		('chromaAbCorrection', c_float*4)  # Chromatic aberration correction parameters
	]

	@property
	def hResolution(self) -> int:
		return self.hResolution

	@hResolution.setter
	def hResolution(self, i: int) -> None:
		self.hResolution = i

	@property
	def vResolution(self) -> int:
		return self.vResolution

	@vResolution.setter
	def vResolution(self, i: int) -> None:
		self.vResolution = i

	@property
	def hScreenSize(self) -> float:
		return self.hScreenSize

	@hScreenSize.setter
	def hScreenSize(self, i: float) -> None:
		self.hScreenSize = i

	@property
	def vScreenSize(self) -> float:
		return self.vScreenSize

	@vScreenSize.setter
	def vScreenSize(self, i: float) -> None:
		self.vScreenSize = i

	@property
	def vScreenCenter(self) -> float:
		return self.vScreenCenter

	@vScreenCenter.setter
	def vScreenCenter(self, i: float) -> None:
		self.vScreenCenter = i

	@property
	def eyeToScreenDistance(self) -> float:
		return self.eyeToScreenDistance

	@eyeToScreenDistance.setter
	def eyeToScreenDistance(self, i: float) -> None:
		self.eyeToScreenDistance = i

	@property
	def lensSeparationDistance(self) -> float:
		return self.lensSeparationDistance

	@lensSeparationDistance.setter
	def lensSeparationDistance(self, i: float) -> None:
		self.lensSeparationDistance = i

	@property
	def interpupillaryDistance(self) -> float:
		return self.interpupillaryDistance

	@interpupillaryDistance.setter
	def interpupillaryDistance(self, i: float) -> None:
		self.interpupillaryDistance = i

	@property
	def lensDistortionValues(self) -> c_float * 4:
		return self.lensDistortionValues

	@lensDistortionValues.setter
	def lensDistortionValues(self, i: c_float * 4) -> None:
		self.lensDistortionValues = i

	@property
	def chromaAbCorrection(self) -> c_float * 4:
		return self.chromaAbCorrection

	@chromaAbCorrection.setter
	def chromaAbCorrection(self, i: c_float * 4) -> None:
		self.chromaAbCorrection = i


#  VrStereoConfig, VR stereo rendering configuration for simulator
class VrStereoConfig(Structure):
	_fields_ = [
		('projection', Matrix*2),  # VR projection matrices (per eye)
		('viewOffset', Matrix*2),  # VR view offset matrices (per eye)
		('leftLensCenter', c_float*2),  # VR left lens center
		('rightLensCenter', c_float*2),  # VR right lens center
		('leftScreenCenter', c_float*2),  # VR left screen center
		('rightScreenCenter', c_float*2),  # VR right screen center
		('scale', c_float*2),  # VR distortion scale
		('scaleIn', c_float*2)  # VR distortion scale in
	]

	@property
	def projection(self) -> Matrix * 2:
		return self.projection

	@projection.setter
	def projection(self, i: Matrix * 2) -> None:
		self.projection = i

	@property
	def viewOffset(self) -> Matrix * 2:
		return self.viewOffset

	@viewOffset.setter
	def viewOffset(self, i: Matrix * 2) -> None:
		self.viewOffset = i

	@property
	def leftLensCenter(self) -> c_float * 2:
		return self.leftLensCenter

	@leftLensCenter.setter
	def leftLensCenter(self, i: c_float * 2) -> None:
		self.leftLensCenter = i

	@property
	def rightLensCenter(self) -> c_float * 2:
		return self.rightLensCenter

	@rightLensCenter.setter
	def rightLensCenter(self, i: c_float * 2) -> None:
		self.rightLensCenter = i

	@property
	def leftScreenCenter(self) -> c_float * 2:
		return self.leftScreenCenter

	@leftScreenCenter.setter
	def leftScreenCenter(self, i: c_float * 2) -> None:
		self.leftScreenCenter = i

	@property
	def rightScreenCenter(self) -> c_float * 2:
		return self.rightScreenCenter

	@rightScreenCenter.setter
	def rightScreenCenter(self, i: c_float * 2) -> None:
		self.rightScreenCenter = i

	@property
	def scale(self) -> c_float * 2:
		return self.scale

	@scale.setter
	def scale(self, i: c_float * 2) -> None:
		self.scale = i

	@property
	def scaleIn(self) -> c_float * 2:
		return self.scaleIn

	@scaleIn.setter
	def scaleIn(self, i: c_float * 2) -> None:
		self.scaleIn = i


#  File path list
class FilePathList(Structure):
	_fields_ = [
		('capacity', c_uint),  # Filepaths max entries
		('count', c_uint),  # Filepaths entries count
		('paths', POINTER(POINTER(c_char)))  # Filepaths entries
	]

	@property
	def capacity(self) -> int:
		return self.capacity

	@capacity.setter
	def capacity(self, i: int) -> None:
		self.capacity = i

	@property
	def count(self) -> int:
		return self.count

	@count.setter
	def count(self, i: int) -> None:
		self.count = i

	@property
	def paths(self) -> POINTER(POINTER(c_char)):
		return self.paths

	@paths.setter
	def paths(self, i: POINTER(POINTER(c_char))) -> None:
		self.paths = i


