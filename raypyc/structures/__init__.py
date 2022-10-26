from ctypes import *
from raypyc.defines import *


class rlVertexBuffer(Structure):
	"""Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""
	_fields_ = [
		('elementCount', c_int),  # Number of elements in the buffer (QUADS)
		('vertices', POINTER(c_float)),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
		('texcoords', POINTER(c_float)),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
		('colors', POINTER(c_ubyte)),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
		('indices', POINTER(c_uint)),  # Vertex indices (in case vertex data comes indexed) (6 indices per quad)
		('vaoId', c_uint),  # OpenGL Vertex Array Object id
		('vboId', c_uint * 4)  # OpenGL Vertex Buffer Objects id (4 types of vertex data)
	]

	@property
	def elementCount(self) -> c_int:
		return self.elementCount

	@elementCount.setter
	def elementCount(self, i: c_int) -> None:
		self.elementCount = i

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
	def colors(self) -> POINTER(c_ubyte):
		return self.colors

	@colors.setter
	def colors(self, i: POINTER(c_ubyte)) -> None:
		self.colors = i

	@property
	def indices(self) -> POINTER(c_uint):
		return self.indices

	@indices.setter
	def indices(self, i: POINTER(c_uint)) -> None:
		self.indices = i

	@property
	def vaoId(self) -> c_uint:
		return self.vaoId

	@vaoId.setter
	def vaoId(self, i: c_uint) -> None:
		self.vaoId = i

	@property
	def vboId(self) -> c_uint * 4:
		return self.vboId

	@vboId.setter
	def vboId(self, i: c_uint * 4) -> None:
		self.vboId = i


class rlDrawCall(Structure):
	"""of those state-change happens (this is done in core module)"""
	_fields_ = [
		('mode', c_int),  # Drawing mode: LINES, TRIANGLES, QUADS
		('vertexCount', c_int),  # Number of vertex of the draw
		('vertexAlignment', c_int),  # Number of vertex required for index alignment (LINES, TRIANGLES)
		('textureId', c_uint)  # Texture id to be used on the draw -> Use to create new draw call if changes
	]

	@property
	def mode(self) -> c_int:
		return self.mode

	@mode.setter
	def mode(self, i: c_int) -> None:
		self.mode = i

	@property
	def vertexCount(self) -> c_int:
		return self.vertexCount

	@vertexCount.setter
	def vertexCount(self, i: c_int) -> None:
		self.vertexCount = i

	@property
	def vertexAlignment(self) -> c_int:
		return self.vertexAlignment

	@vertexAlignment.setter
	def vertexAlignment(self, i: c_int) -> None:
		self.vertexAlignment = i

	@property
	def textureId(self) -> c_uint:
		return self.textureId

	@textureId.setter
	def textureId(self, i: c_uint) -> None:
		self.textureId = i


class rlRenderBatch(Structure):
	"""rlRenderBatch type"""
	_fields_ = [
		('bufferCount', c_int),  # Number of vertex buffers (multi-buffering support)
		('currentBuffer', c_int),  # Current buffer tracking in case of multi-buffering
		('vertexBuffer', POINTER(rlVertexBuffer)),  # Dynamic buffer(s) for vertex data
		('draws', POINTER(rlDrawCall)),  # Draw calls array, depends on textureId
		('drawCounter', c_int),  # Draw calls counter
		('currentDepth', c_float)  # Current depth value for next draw
	]

	@property
	def bufferCount(self) -> c_int:
		return self.bufferCount

	@bufferCount.setter
	def bufferCount(self, i: c_int) -> None:
		self.bufferCount = i

	@property
	def currentBuffer(self) -> c_int:
		return self.currentBuffer

	@currentBuffer.setter
	def currentBuffer(self, i: c_int) -> None:
		self.currentBuffer = i

	@property
	def vertexBuffer(self) -> POINTER(rlVertexBuffer):
		return self.vertexBuffer

	@vertexBuffer.setter
	def vertexBuffer(self, i: POINTER(rlVertexBuffer)) -> None:
		self.vertexBuffer = i

	@property
	def draws(self) -> POINTER(rlDrawCall):
		return self.draws

	@draws.setter
	def draws(self, i: POINTER(rlDrawCall)) -> None:
		self.draws = i

	@property
	def drawCounter(self) -> c_int:
		return self.drawCounter

	@drawCounter.setter
	def drawCounter(self, i: c_int) -> None:
		self.drawCounter = i

	@property
	def currentDepth(self) -> c_float:
		return self.currentDepth

	@currentDepth.setter
	def currentDepth(self, i: c_float) -> None:
		self.currentDepth = i


class Matrix(Structure):
	"""Matrix, 4x4 components, column major, OpenGL style, right handed"""
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
	def m0(self) -> c_float:
		return self.m0

	@m0.setter
	def m0(self, i: c_float) -> None:
		self.m0 = i

	@property
	def m4(self) -> c_float:
		return self.m4

	@m4.setter
	def m4(self, i: c_float) -> None:
		self.m4 = i

	@property
	def m8(self) -> c_float:
		return self.m8

	@m8.setter
	def m8(self, i: c_float) -> None:
		self.m8 = i

	@property
	def m12(self) -> c_float:
		return self.m12

	@m12.setter
	def m12(self, i: c_float) -> None:
		self.m12 = i

	@property
	def m1(self) -> c_float:
		return self.m1

	@m1.setter
	def m1(self, i: c_float) -> None:
		self.m1 = i

	@property
	def m5(self) -> c_float:
		return self.m5

	@m5.setter
	def m5(self, i: c_float) -> None:
		self.m5 = i

	@property
	def m9(self) -> c_float:
		return self.m9

	@m9.setter
	def m9(self, i: c_float) -> None:
		self.m9 = i

	@property
	def m13(self) -> c_float:
		return self.m13

	@m13.setter
	def m13(self, i: c_float) -> None:
		self.m13 = i

	@property
	def m2(self) -> c_float:
		return self.m2

	@m2.setter
	def m2(self, i: c_float) -> None:
		self.m2 = i

	@property
	def m6(self) -> c_float:
		return self.m6

	@m6.setter
	def m6(self, i: c_float) -> None:
		self.m6 = i

	@property
	def m10(self) -> c_float:
		return self.m10

	@m10.setter
	def m10(self, i: c_float) -> None:
		self.m10 = i

	@property
	def m14(self) -> c_float:
		return self.m14

	@m14.setter
	def m14(self, i: c_float) -> None:
		self.m14 = i

	@property
	def m3(self) -> c_float:
		return self.m3

	@m3.setter
	def m3(self, i: c_float) -> None:
		self.m3 = i

	@property
	def m7(self) -> c_float:
		return self.m7

	@m7.setter
	def m7(self, i: c_float) -> None:
		self.m7 = i

	@property
	def m11(self) -> c_float:
		return self.m11

	@m11.setter
	def m11(self, i: c_float) -> None:
		self.m11 = i

	@property
	def m15(self) -> c_float:
		return self.m15

	@m15.setter
	def m15(self, i: c_float) -> None:
		self.m15 = i


class rlglData(Structure):
	""""""
	_fields_ = [
		('currentBatch', POINTER(rlRenderBatch)),  # Current render batch
		('defaultBatch', rlRenderBatch),  # Default internal render batch
		('vertexCounter', c_int),  # Current active render batch vertex counter (generic, used for all batches)
		('texcoordx', c_float),  # Current active texture coordinate (added on glVertex*())
		('texcoordy', c_float),  # Current active texture coordinate (added on glVertex*())
		('normalx', c_float),  # Current active normal (added on glVertex*())
		('normaly', c_float),  # Current active normal (added on glVertex*())
		('normalz', c_float),  # Current active normal (added on glVertex*())
		('colorr', c_ubyte),  # Current active color (added on glVertex*())
		('colorg', c_ubyte),  # Current active color (added on glVertex*())
		('colorb', c_ubyte),  # Current active color (added on glVertex*())
		('colora', c_ubyte),  # Current active color (added on glVertex*())
		('currentMatrixMode', c_int),  # Current matrix mode
		('currentMatrix', POINTER(Matrix)),  # Current matrix pointer
		('modelview', Matrix),  # Default modelview matrix
		('projection', Matrix),  # Default projection matrix
		('transform', Matrix),  # Transform matrix to be used with rlTranslate, rlRotate, rlScale
		('transformRequired', c_bool),  # Require transform matrix application to current draw-call vertex (if required)
		('stack', Matrix * RL_MAX_MATRIX_STACK_SIZE),  # Matrix stack for push/pop
		('stackCounter', c_int),  # Matrix stack counter
		('defaultTextureId', c_uint),  # Default texture used on shapes/poly drawing (required by shader)
		('activeTextureId', c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS),  # Active texture ids to be enabled on batch drawing (0 active by default)
		('defaultVShaderId', c_uint),  # Default vertex shader id (used by default shader program)
		('defaultFShaderId', c_uint),  # Default fragment shader id (used by default shader program)
		('defaultShaderId', c_uint),  # Default shader program id, supports vertex color and diffuse texture
		('defaultShaderLocs', POINTER(c_int)),  # Default shader locations pointer to be used on rendering
		('currentShaderId', c_uint),  # Current shader id to be used on rendering (by default, defaultShaderId)
		('currentShaderLocs', POINTER(c_int)),  # Current shader locations pointer to be used on rendering (by default, defaultShaderLocs)
		('stereoRender', c_bool),  # Stereo rendering flag
		('projectionStereo', Matrix * 2),  # VR stereo rendering eyes projection matrices
		('viewOffsetStereo', Matrix * 2),  # VR stereo rendering eyes view offset matrices
		('currentBlendMode', c_int),  # Blending mode active
		('glBlendSrcFactor', c_int),  # Blending source factor
		('glBlendDstFactor', c_int),  # Blending destination factor
		('glBlendEquation', c_int),  # Blending equation
		('framebufferWidth', c_int),  # Current framebuffer width
		('framebufferHeight', c_int)  # Current framebuffer height
	]

	@property
	def currentBatch(self) -> POINTER(rlRenderBatch):
		return self.currentBatch

	@currentBatch.setter
	def currentBatch(self, i: POINTER(rlRenderBatch)) -> None:
		self.currentBatch = i

	@property
	def defaultBatch(self) -> rlRenderBatch:
		return self.defaultBatch

	@defaultBatch.setter
	def defaultBatch(self, i: rlRenderBatch) -> None:
		self.defaultBatch = i

	@property
	def vertexCounter(self) -> c_int:
		return self.vertexCounter

	@vertexCounter.setter
	def vertexCounter(self, i: c_int) -> None:
		self.vertexCounter = i

	@property
	def texcoordx(self) -> c_float:
		return self.texcoordx

	@texcoordx.setter
	def texcoordx(self, i: c_float) -> None:
		self.texcoordx = i

	@property
	def texcoordy(self) -> c_float:
		return self.texcoordy

	@texcoordy.setter
	def texcoordy(self, i: c_float) -> None:
		self.texcoordy = i

	@property
	def normalx(self) -> c_float:
		return self.normalx

	@normalx.setter
	def normalx(self, i: c_float) -> None:
		self.normalx = i

	@property
	def normaly(self) -> c_float:
		return self.normaly

	@normaly.setter
	def normaly(self, i: c_float) -> None:
		self.normaly = i

	@property
	def normalz(self) -> c_float:
		return self.normalz

	@normalz.setter
	def normalz(self, i: c_float) -> None:
		self.normalz = i

	@property
	def colorr(self) -> c_ubyte:
		return self.colorr

	@colorr.setter
	def colorr(self, i: c_ubyte) -> None:
		self.colorr = i

	@property
	def colorg(self) -> c_ubyte:
		return self.colorg

	@colorg.setter
	def colorg(self, i: c_ubyte) -> None:
		self.colorg = i

	@property
	def colorb(self) -> c_ubyte:
		return self.colorb

	@colorb.setter
	def colorb(self, i: c_ubyte) -> None:
		self.colorb = i

	@property
	def colora(self) -> c_ubyte:
		return self.colora

	@colora.setter
	def colora(self, i: c_ubyte) -> None:
		self.colora = i

	@property
	def currentMatrixMode(self) -> c_int:
		return self.currentMatrixMode

	@currentMatrixMode.setter
	def currentMatrixMode(self, i: c_int) -> None:
		self.currentMatrixMode = i

	@property
	def currentMatrix(self) -> POINTER(Matrix):
		return self.currentMatrix

	@currentMatrix.setter
	def currentMatrix(self, i: POINTER(Matrix)) -> None:
		self.currentMatrix = i

	@property
	def modelview(self) -> Matrix:
		return self.modelview

	@modelview.setter
	def modelview(self, i: Matrix) -> None:
		self.modelview = i

	@property
	def projection(self) -> Matrix:
		return self.projection

	@projection.setter
	def projection(self, i: Matrix) -> None:
		self.projection = i

	@property
	def transform(self) -> Matrix:
		return self.transform

	@transform.setter
	def transform(self, i: Matrix) -> None:
		self.transform = i

	@property
	def transformRequired(self) -> c_bool:
		return self.transformRequired

	@transformRequired.setter
	def transformRequired(self, i: c_bool) -> None:
		self.transformRequired = i

	@property
	def stack(self) -> Matrix * RL_MAX_MATRIX_STACK_SIZE:
		return self.stack

	@stack.setter
	def stack(self, i: Matrix * RL_MAX_MATRIX_STACK_SIZE) -> None:
		self.stack = i

	@property
	def stackCounter(self) -> c_int:
		return self.stackCounter

	@stackCounter.setter
	def stackCounter(self, i: c_int) -> None:
		self.stackCounter = i

	@property
	def defaultTextureId(self) -> c_uint:
		return self.defaultTextureId

	@defaultTextureId.setter
	def defaultTextureId(self, i: c_uint) -> None:
		self.defaultTextureId = i

	@property
	def activeTextureId(self) -> c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS:
		return self.activeTextureId

	@activeTextureId.setter
	def activeTextureId(self, i: c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS) -> None:
		self.activeTextureId = i

	@property
	def defaultVShaderId(self) -> c_uint:
		return self.defaultVShaderId

	@defaultVShaderId.setter
	def defaultVShaderId(self, i: c_uint) -> None:
		self.defaultVShaderId = i

	@property
	def defaultFShaderId(self) -> c_uint:
		return self.defaultFShaderId

	@defaultFShaderId.setter
	def defaultFShaderId(self, i: c_uint) -> None:
		self.defaultFShaderId = i

	@property
	def defaultShaderId(self) -> c_uint:
		return self.defaultShaderId

	@defaultShaderId.setter
	def defaultShaderId(self, i: c_uint) -> None:
		self.defaultShaderId = i

	@property
	def defaultShaderLocs(self) -> POINTER(c_int):
		return self.defaultShaderLocs

	@defaultShaderLocs.setter
	def defaultShaderLocs(self, i: POINTER(c_int)) -> None:
		self.defaultShaderLocs = i

	@property
	def currentShaderId(self) -> c_uint:
		return self.currentShaderId

	@currentShaderId.setter
	def currentShaderId(self, i: c_uint) -> None:
		self.currentShaderId = i

	@property
	def currentShaderLocs(self) -> POINTER(c_int):
		return self.currentShaderLocs

	@currentShaderLocs.setter
	def currentShaderLocs(self, i: POINTER(c_int)) -> None:
		self.currentShaderLocs = i

	@property
	def stereoRender(self) -> c_bool:
		return self.stereoRender

	@stereoRender.setter
	def stereoRender(self, i: c_bool) -> None:
		self.stereoRender = i

	@property
	def projectionStereo(self) -> Matrix * 2:
		return self.projectionStereo

	@projectionStereo.setter
	def projectionStereo(self, i: Matrix * 2) -> None:
		self.projectionStereo = i

	@property
	def viewOffsetStereo(self) -> Matrix * 2:
		return self.viewOffsetStereo

	@viewOffsetStereo.setter
	def viewOffsetStereo(self, i: Matrix * 2) -> None:
		self.viewOffsetStereo = i

	@property
	def currentBlendMode(self) -> c_int:
		return self.currentBlendMode

	@currentBlendMode.setter
	def currentBlendMode(self, i: c_int) -> None:
		self.currentBlendMode = i

	@property
	def glBlendSrcFactor(self) -> c_int:
		return self.glBlendSrcFactor

	@glBlendSrcFactor.setter
	def glBlendSrcFactor(self, i: c_int) -> None:
		self.glBlendSrcFactor = i

	@property
	def glBlendDstFactor(self) -> c_int:
		return self.glBlendDstFactor

	@glBlendDstFactor.setter
	def glBlendDstFactor(self, i: c_int) -> None:
		self.glBlendDstFactor = i

	@property
	def glBlendEquation(self) -> c_int:
		return self.glBlendEquation

	@glBlendEquation.setter
	def glBlendEquation(self, i: c_int) -> None:
		self.glBlendEquation = i

	@property
	def framebufferWidth(self) -> c_int:
		return self.framebufferWidth

	@framebufferWidth.setter
	def framebufferWidth(self, i: c_int) -> None:
		self.framebufferWidth = i

	@property
	def framebufferHeight(self) -> c_int:
		return self.framebufferHeight

	@framebufferHeight.setter
	def framebufferHeight(self, i: c_int) -> None:
		self.framebufferHeight = i


class Vector2(Structure):
	"""Vector2, 2 components"""
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float)  # Vector y component
	]

	@property
	def x(self) -> c_float:
		return self.x

	@x.setter
	def x(self, i: c_float) -> None:
		self.x = i

	@property
	def y(self) -> c_float:
		return self.y

	@y.setter
	def y(self, i: c_float) -> None:
		self.y = i


class Vector3(Structure):
	"""Vector3, 3 components"""
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float)  # Vector z component
	]

	@property
	def x(self) -> c_float:
		return self.x

	@x.setter
	def x(self, i: c_float) -> None:
		self.x = i

	@property
	def y(self) -> c_float:
		return self.y

	@y.setter
	def y(self, i: c_float) -> None:
		self.y = i

	@property
	def z(self) -> c_float:
		return self.z

	@z.setter
	def z(self, i: c_float) -> None:
		self.z = i


class Vector4(Structure):
	"""Vector4, 4 components"""
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float),  # Vector z component
		('w', c_float)  # Vector w component
	]

	@property
	def x(self) -> c_float:
		return self.x

	@x.setter
	def x(self, i: c_float) -> None:
		self.x = i

	@property
	def y(self) -> c_float:
		return self.y

	@y.setter
	def y(self, i: c_float) -> None:
		self.y = i

	@property
	def z(self) -> c_float:
		return self.z

	@z.setter
	def z(self, i: c_float) -> None:
		self.z = i

	@property
	def w(self) -> c_float:
		return self.w

	@w.setter
	def w(self, i: c_float) -> None:
		self.w = i


class Quaternion(Structure):
	"""Quaternion, 4 components (Vector4 alias)"""
	_fields_ = [
		('x', c_float),  # Vector x component
		('y', c_float),  # Vector y component
		('z', c_float),  # Vector z component
		('w', c_float)  # Vector w component
	]

	@property
	def x(self) -> c_float:
		return self.x

	@x.setter
	def x(self, i: c_float) -> None:
		self.x = i

	@property
	def y(self) -> c_float:
		return self.y

	@y.setter
	def y(self, i: c_float) -> None:
		self.y = i

	@property
	def z(self) -> c_float:
		return self.z

	@z.setter
	def z(self, i: c_float) -> None:
		self.z = i

	@property
	def w(self) -> c_float:
		return self.w

	@w.setter
	def w(self, i: c_float) -> None:
		self.w = i


class Color(Structure):
	"""Color, 4 components, R8G8B8A8 (32bit)"""
	_fields_ = [
		('r', c_ubyte),  # Color red value
		('g', c_ubyte),  # Color green value
		('b', c_ubyte),  # Color blue value
		('a', c_ubyte)  # Color alpha value
	]

	@property
	def r(self) -> c_ubyte:
		return self.r

	@r.setter
	def r(self, i: c_ubyte) -> None:
		self.r = i

	@property
	def g(self) -> c_ubyte:
		return self.g

	@g.setter
	def g(self, i: c_ubyte) -> None:
		self.g = i

	@property
	def b(self) -> c_ubyte:
		return self.b

	@b.setter
	def b(self, i: c_ubyte) -> None:
		self.b = i

	@property
	def a(self) -> c_ubyte:
		return self.a

	@a.setter
	def a(self, i: c_ubyte) -> None:
		self.a = i


class Rectangle(Structure):
	"""Rectangle, 4 components"""
	_fields_ = [
		('x', c_float),  # Rectangle top-left corner position x
		('y', c_float),  # Rectangle top-left corner position y
		('width', c_float),  # Rectangle width
		('height', c_float)  # Rectangle height
	]

	@property
	def x(self) -> c_float:
		return self.x

	@x.setter
	def x(self, i: c_float) -> None:
		self.x = i

	@property
	def y(self) -> c_float:
		return self.y

	@y.setter
	def y(self, i: c_float) -> None:
		self.y = i

	@property
	def width(self) -> c_float:
		return self.width

	@width.setter
	def width(self, i: c_float) -> None:
		self.width = i

	@property
	def height(self) -> c_float:
		return self.height

	@height.setter
	def height(self, i: c_float) -> None:
		self.height = i


class Image(Structure):
	"""Image, pixel data stored in CPU memory (RAM)"""
	_fields_ = [
		('data', c_void_p),  # Image raw data
		('width', c_int),  # Image base width
		('height', c_int),  # Image base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def data(self) -> c_void_p:
		return self.data

	@data.setter
	def data(self, i: c_void_p) -> None:
		self.data = i

	@property
	def width(self) -> c_int:
		return self.width

	@width.setter
	def width(self, i: c_int) -> None:
		self.width = i

	@property
	def height(self) -> c_int:
		return self.height

	@height.setter
	def height(self, i: c_int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> c_int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> c_int:
		return self.format

	@format.setter
	def format(self, i: c_int) -> None:
		self.format = i


class Texture(Structure):
	"""Texture, tex data stored in GPU memory (VRAM)"""
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
		self.id = i

	@property
	def width(self) -> c_int:
		return self.width

	@width.setter
	def width(self, i: c_int) -> None:
		self.width = i

	@property
	def height(self) -> c_int:
		return self.height

	@height.setter
	def height(self, i: c_int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> c_int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> c_int:
		return self.format

	@format.setter
	def format(self, i: c_int) -> None:
		self.format = i


class Texture2D(Structure):
	"""Texture2D, same as Texture"""
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
		self.id = i

	@property
	def width(self) -> c_int:
		return self.width

	@width.setter
	def width(self, i: c_int) -> None:
		self.width = i

	@property
	def height(self) -> c_int:
		return self.height

	@height.setter
	def height(self, i: c_int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> c_int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> c_int:
		return self.format

	@format.setter
	def format(self, i: c_int) -> None:
		self.format = i


class TextureCubemap(Structure):
	"""TextureCubemap, same as Texture"""
	_fields_ = [
		('id', c_uint),  # OpenGL texture id
		('width', c_int),  # Texture base width
		('height', c_int),  # Texture base height
		('mipmaps', c_int),  # Mipmap levels, 1 by default
		('format', c_int)  # Data format (PixelFormat type)
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
		self.id = i

	@property
	def width(self) -> c_int:
		return self.width

	@width.setter
	def width(self, i: c_int) -> None:
		self.width = i

	@property
	def height(self) -> c_int:
		return self.height

	@height.setter
	def height(self, i: c_int) -> None:
		self.height = i

	@property
	def mipmaps(self) -> c_int:
		return self.mipmaps

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		self.mipmaps = i

	@property
	def format(self) -> c_int:
		return self.format

	@format.setter
	def format(self, i: c_int) -> None:
		self.format = i


class RenderTexture(Structure):
	"""RenderTexture, fbo for texture rendering"""
	_fields_ = [
		('id', c_uint),  # OpenGL framebuffer object id
		('texture', Texture),  # Color buffer attachment texture
		('depth', Texture)  # Depth buffer attachment texture
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
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


class RenderTexture2D(Structure):
	"""RenderTexture2D, same as RenderTexture"""
	_fields_ = [
		('id', c_uint),  # OpenGL framebuffer object id
		('texture', Texture),  # Color buffer attachment texture
		('depth', Texture)  # Depth buffer attachment texture
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
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


class NPatchInfo(Structure):
	"""NPatchInfo, n-patch layout info"""
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
	def left(self) -> c_int:
		return self.left

	@left.setter
	def left(self, i: c_int) -> None:
		self.left = i

	@property
	def top(self) -> c_int:
		return self.top

	@top.setter
	def top(self, i: c_int) -> None:
		self.top = i

	@property
	def right(self) -> c_int:
		return self.right

	@right.setter
	def right(self, i: c_int) -> None:
		self.right = i

	@property
	def bottom(self) -> c_int:
		return self.bottom

	@bottom.setter
	def bottom(self, i: c_int) -> None:
		self.bottom = i

	@property
	def layout(self) -> c_int:
		return self.layout

	@layout.setter
	def layout(self, i: c_int) -> None:
		self.layout = i


class GlyphInfo(Structure):
	"""GlyphInfo, font characters glyphs info"""
	_fields_ = [
		('value', c_int),  # Character value (Unicode)
		('offsetX', c_int),  # Character offset X when drawing
		('offsetY', c_int),  # Character offset Y when drawing
		('advanceX', c_int),  # Character advance position X
		('image', Image)  # Character image data
	]

	@property
	def value(self) -> c_int:
		return self.value

	@value.setter
	def value(self, i: c_int) -> None:
		self.value = i

	@property
	def offsetX(self) -> c_int:
		return self.offsetX

	@offsetX.setter
	def offsetX(self, i: c_int) -> None:
		self.offsetX = i

	@property
	def offsetY(self) -> c_int:
		return self.offsetY

	@offsetY.setter
	def offsetY(self, i: c_int) -> None:
		self.offsetY = i

	@property
	def advanceX(self) -> c_int:
		return self.advanceX

	@advanceX.setter
	def advanceX(self, i: c_int) -> None:
		self.advanceX = i

	@property
	def image(self) -> Image:
		return self.image

	@image.setter
	def image(self, i: Image) -> None:
		self.image = i


class Font(Structure):
	"""Font, font texture and GlyphInfo array data"""
	_fields_ = [
		('baseSize', c_int),  # Base size (default chars height)
		('glyphCount', c_int),  # Number of glyph characters
		('glyphPadding', c_int),  # Padding around the glyph characters
		('texture', Texture2D),  # Texture atlas containing the glyphs
		('recs', POINTER(Rectangle)),  # Rectangles in texture for the glyphs
		('glyphs', POINTER(GlyphInfo))  # Glyphs info data
	]

	@property
	def baseSize(self) -> c_int:
		return self.baseSize

	@baseSize.setter
	def baseSize(self, i: c_int) -> None:
		self.baseSize = i

	@property
	def glyphCount(self) -> c_int:
		return self.glyphCount

	@glyphCount.setter
	def glyphCount(self, i: c_int) -> None:
		self.glyphCount = i

	@property
	def glyphPadding(self) -> c_int:
		return self.glyphPadding

	@glyphPadding.setter
	def glyphPadding(self, i: c_int) -> None:
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


class Camera3D(Structure):
	"""Camera, defines position/orientation in 3d space"""
	_fields_ = [
		('position', Vector3),  # Camera position
		('target', Vector3),  # Camera target it looks-at
		('up', Vector3),  # Camera up vector (rotation over its axis)
		('fovy', c_float),  # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
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
	def fovy(self) -> c_float:
		return self.fovy

	@fovy.setter
	def fovy(self, i: c_float) -> None:
		self.fovy = i

	@property
	def projection(self) -> c_int:
		return self.projection

	@projection.setter
	def projection(self, i: c_int) -> None:
		self.projection = i


class Camera(Structure):
	"""Camera type fallback, defaults to Camera3D"""
	_fields_ = [
		('position', Vector3),  # Camera position
		('target', Vector3),  # Camera target it looks-at
		('up', Vector3),  # Camera up vector (rotation over its axis)
		('fovy', c_float),  # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
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
	def fovy(self) -> c_float:
		return self.fovy

	@fovy.setter
	def fovy(self, i: c_float) -> None:
		self.fovy = i

	@property
	def projection(self) -> c_int:
		return self.projection

	@projection.setter
	def projection(self, i: c_int) -> None:
		self.projection = i


class Camera2D(Structure):
	"""Camera2D, defines position/orientation in 2d space"""
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
	def rotation(self) -> c_float:
		return self.rotation

	@rotation.setter
	def rotation(self, i: c_float) -> None:
		self.rotation = i

	@property
	def zoom(self) -> c_float:
		return self.zoom

	@zoom.setter
	def zoom(self, i: c_float) -> None:
		self.zoom = i


class Mesh(Structure):
	"""Mesh, vertex data and vao/vbo"""
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
	def vertexCount(self) -> c_int:
		return self.vertexCount

	@vertexCount.setter
	def vertexCount(self, i: c_int) -> None:
		self.vertexCount = i

	@property
	def triangleCount(self) -> c_int:
		return self.triangleCount

	@triangleCount.setter
	def triangleCount(self, i: c_int) -> None:
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
	def vaoId(self) -> c_uint:
		return self.vaoId

	@vaoId.setter
	def vaoId(self, i: c_uint) -> None:
		self.vaoId = i

	@property
	def vboId(self) -> POINTER(c_uint):
		return self.vboId

	@vboId.setter
	def vboId(self, i: POINTER(c_uint)) -> None:
		self.vboId = i


class Shader(Structure):
	"""Shader"""
	_fields_ = [
		('id', c_uint),  # Shader program id
		('locs', POINTER(c_int))  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
	]

	@property
	def id(self) -> c_uint:
		return self.id

	@id.setter
	def id(self, i: c_uint) -> None:
		self.id = i

	@property
	def locs(self) -> POINTER(c_int):
		return self.locs

	@locs.setter
	def locs(self, i: POINTER(c_int)) -> None:
		self.locs = i


class MaterialMap(Structure):
	"""MaterialMap"""
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
	def value(self) -> c_float:
		return self.value

	@value.setter
	def value(self, i: c_float) -> None:
		self.value = i


class Material(Structure):
	"""Material, includes shader and maps"""
	_fields_ = [
		('shader', Shader),  # Material shader
		('maps', POINTER(MaterialMap)),  # Material maps array (MAX_MATERIAL_MAPS)
		('params', c_float * 4)  # Material generic parameters (if required)
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


class Transform(Structure):
	"""Transform, vectex transformation data"""
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


class BoneInfo(Structure):
	"""Bone, skeletal animation bone"""
	_fields_ = [
		('name', c_char * 32),  # Bone name
		('parent', c_int)  # Bone parent
	]

	@property
	def name(self) -> c_char * 32:
		return self.name

	@name.setter
	def name(self, i: c_char * 32) -> None:
		self.name = i

	@property
	def parent(self) -> c_int:
		return self.parent

	@parent.setter
	def parent(self, i: c_int) -> None:
		self.parent = i


class Model(Structure):
	"""Model, meshes, materials and animation data"""
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
	def meshCount(self) -> c_int:
		return self.meshCount

	@meshCount.setter
	def meshCount(self, i: c_int) -> None:
		self.meshCount = i

	@property
	def materialCount(self) -> c_int:
		return self.materialCount

	@materialCount.setter
	def materialCount(self, i: c_int) -> None:
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
	def boneCount(self) -> c_int:
		return self.boneCount

	@boneCount.setter
	def boneCount(self, i: c_int) -> None:
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


class ModelAnimation(Structure):
	"""ModelAnimation"""
	_fields_ = [
		('boneCount', c_int),  # Number of bones
		('frameCount', c_int),  # Number of animation frames
		('bones', POINTER(BoneInfo)),  # Bones information (skeleton)
		('framePoses', POINTER(POINTER(Transform)))  # Poses array by frame
	]

	@property
	def boneCount(self) -> c_int:
		return self.boneCount

	@boneCount.setter
	def boneCount(self, i: c_int) -> None:
		self.boneCount = i

	@property
	def frameCount(self) -> c_int:
		return self.frameCount

	@frameCount.setter
	def frameCount(self, i: c_int) -> None:
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


class Ray(Structure):
	"""Ray, ray for raycasting"""
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


class RayCollision(Structure):
	"""RayCollision, ray hit information"""
	_fields_ = [
		('hit', c_bool),  # Did the ray hit something?
		('distance', c_float),  # Distance to nearest hit
		('point', Vector3),  # Point of nearest hit
		('normal', Vector3)  # Surface normal of hit
	]

	@property
	def hit(self) -> c_bool:
		return self.hit

	@hit.setter
	def hit(self, i: c_bool) -> None:
		self.hit = i

	@property
	def distance(self) -> c_float:
		return self.distance

	@distance.setter
	def distance(self, i: c_float) -> None:
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


class BoundingBox(Structure):
	"""BoundingBox"""
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


class VrDeviceInfo(Structure):
	"""VrDeviceInfo, Head-Mounted-Display device parameters"""
	_fields_ = [
		('hResolution', c_int),  # Horizontal resolution in pixels
		('vResolution', c_int),  # Vertical resolution in pixels
		('hScreenSize', c_float),  # Horizontal size in meters
		('vScreenSize', c_float),  # Vertical size in meters
		('vScreenCenter', c_float),  # Screen center in meters
		('eyeToScreenDistance', c_float),  # Distance between eye and display in meters
		('lensSeparationDistance', c_float),  # Lens separation distance in meters
		('interpupillaryDistance', c_float),  # IPD (distance between pupils) in meters
		('lensDistortionValues', c_float * 4),  # Lens distortion constant parameters
		('chromaAbCorrection', c_float * 4)  # Chromatic aberration correction parameters
	]

	@property
	def hResolution(self) -> c_int:
		return self.hResolution

	@hResolution.setter
	def hResolution(self, i: c_int) -> None:
		self.hResolution = i

	@property
	def vResolution(self) -> c_int:
		return self.vResolution

	@vResolution.setter
	def vResolution(self, i: c_int) -> None:
		self.vResolution = i

	@property
	def hScreenSize(self) -> c_float:
		return self.hScreenSize

	@hScreenSize.setter
	def hScreenSize(self, i: c_float) -> None:
		self.hScreenSize = i

	@property
	def vScreenSize(self) -> c_float:
		return self.vScreenSize

	@vScreenSize.setter
	def vScreenSize(self, i: c_float) -> None:
		self.vScreenSize = i

	@property
	def vScreenCenter(self) -> c_float:
		return self.vScreenCenter

	@vScreenCenter.setter
	def vScreenCenter(self, i: c_float) -> None:
		self.vScreenCenter = i

	@property
	def eyeToScreenDistance(self) -> c_float:
		return self.eyeToScreenDistance

	@eyeToScreenDistance.setter
	def eyeToScreenDistance(self, i: c_float) -> None:
		self.eyeToScreenDistance = i

	@property
	def lensSeparationDistance(self) -> c_float:
		return self.lensSeparationDistance

	@lensSeparationDistance.setter
	def lensSeparationDistance(self, i: c_float) -> None:
		self.lensSeparationDistance = i

	@property
	def interpupillaryDistance(self) -> c_float:
		return self.interpupillaryDistance

	@interpupillaryDistance.setter
	def interpupillaryDistance(self, i: c_float) -> None:
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


class VrStereoConfig(Structure):
	"""VrStereoConfig, VR stereo rendering configuration for simulator"""
	_fields_ = [
		('projection', Matrix * 2),  # VR projection matrices (per eye)
		('viewOffset', Matrix * 2),  # VR view offset matrices (per eye)
		('leftLensCenter', c_float * 2),  # VR left lens center
		('rightLensCenter', c_float * 2),  # VR right lens center
		('leftScreenCenter', c_float * 2),  # VR left screen center
		('rightScreenCenter', c_float * 2),  # VR right screen center
		('scale', c_float * 2),  # VR distortion scale
		('scaleIn', c_float * 2)  # VR distortion scale in
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


class FilePathList(Structure):
	"""File path list"""
	_fields_ = [
		('capacity', c_uint),  # Filepaths max entries
		('count', c_uint),  # Filepaths entries count
		('paths', POINTER(POINTER(c_char)))  # Filepaths entries
	]

	@property
	def capacity(self) -> c_uint:
		return self.capacity

	@capacity.setter
	def capacity(self, i: c_uint) -> None:
		self.capacity = i

	@property
	def count(self) -> c_uint:
		return self.count

	@count.setter
	def count(self, i: c_uint) -> None:
		self.count = i

	@property
	def paths(self) -> POINTER(POINTER(c_char)):
		return self.paths

	@paths.setter
	def paths(self, i: POINTER(POINTER(c_char))) -> None:
		self.paths = i


class float3(Structure):
	"""NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
	_fields_ = [
		('v', c_float * 3)  # 
	]

	@property
	def v(self) -> c_float * 3:
		return self.v

	@v.setter
	def v(self, i: c_float * 3) -> None:
		self.v = i


class float16(Structure):
	""""""
	_fields_ = [
		('v', c_float * 16)  # 
	]

	@property
	def v(self) -> c_float * 16:
		return self.v

	@v.setter
	def v(self, i: c_float * 16) -> None:
		self.v = i


class GuiStyleProp(Structure):
	"""Style property"""
	_fields_ = [
		('controlId', c_ushort),  # 
		('propertyId', c_ushort),  # 
		('propertyValue', c_uint)  # 
	]

	@property
	def controlId(self) -> c_ushort:
		return self.controlId

	@controlId.setter
	def controlId(self, i: c_ushort) -> None:
		self.controlId = i

	@property
	def propertyId(self) -> c_ushort:
		return self.propertyId

	@propertyId.setter
	def propertyId(self, i: c_ushort) -> None:
		self.propertyId = i

	@property
	def propertyValue(self) -> c_uint:
		return self.propertyValue

	@propertyValue.setter
	def propertyValue(self, i: c_uint) -> None:
		self.propertyValue = i


__structs = {
	"rlVertexBuffer": rlVertexBuffer,
	"rlDrawCall": rlDrawCall,
	"rlRenderBatch": rlRenderBatch,
	"Matrix": Matrix,
	"rlglData": rlglData,
	"Vector2": Vector2,
	"Vector3": Vector3,
	"Vector4": Vector4,
	"Quaternion": Quaternion,
	"Color": Color,
	"Rectangle": Rectangle,
	"Image": Image,
	"Texture": Texture,
	"Texture2D": Texture2D,
	"TextureCubemap": TextureCubemap,
	"RenderTexture": RenderTexture,
	"RenderTexture2D": RenderTexture2D,
	"NPatchInfo": NPatchInfo,
	"GlyphInfo": GlyphInfo,
	"Font": Font,
	"Camera3D": Camera3D,
	"Camera": Camera,
	"Camera2D": Camera2D,
	"Mesh": Mesh,
	"Shader": Shader,
	"MaterialMap": MaterialMap,
	"Material": Material,
	"Transform": Transform,
	"BoneInfo": BoneInfo,
	"Model": Model,
	"ModelAnimation": ModelAnimation,
	"Ray": Ray,
	"RayCollision": RayCollision,
	"BoundingBox": BoundingBox,
	"VrDeviceInfo": VrDeviceInfo,
	"VrStereoConfig": VrStereoConfig,
	"FilePathList": FilePathList,
	"float3": float3,
	"float16": float16,
	"GuiStyleProp": GuiStyleProp
}