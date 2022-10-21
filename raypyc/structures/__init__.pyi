from ctypes import *


class Matrix(Structure):
	"""Matrix, 4x4 components, column major, OpenGL style, right handed"""
	@property
	def m0(self) -> c_float:
		...

	@m0.setter
	def m0(self, i: c_float) -> None:
		...

	@property
	def m4(self) -> c_float:
		...

	@m4.setter
	def m4(self, i: c_float) -> None:
		...

	@property
	def m8(self) -> c_float:
		...

	@m8.setter
	def m8(self, i: c_float) -> None:
		...

	@property
	def m12(self) -> c_float:
		...

	@m12.setter
	def m12(self, i: c_float) -> None:
		...

	@property
	def m1(self) -> c_float:
		...

	@m1.setter
	def m1(self, i: c_float) -> None:
		...

	@property
	def m5(self) -> c_float:
		...

	@m5.setter
	def m5(self, i: c_float) -> None:
		...

	@property
	def m9(self) -> c_float:
		...

	@m9.setter
	def m9(self, i: c_float) -> None:
		...

	@property
	def m13(self) -> c_float:
		...

	@m13.setter
	def m13(self, i: c_float) -> None:
		...

	@property
	def m2(self) -> c_float:
		...

	@m2.setter
	def m2(self, i: c_float) -> None:
		...

	@property
	def m6(self) -> c_float:
		...

	@m6.setter
	def m6(self, i: c_float) -> None:
		...

	@property
	def m10(self) -> c_float:
		...

	@m10.setter
	def m10(self, i: c_float) -> None:
		...

	@property
	def m14(self) -> c_float:
		...

	@m14.setter
	def m14(self, i: c_float) -> None:
		...

	@property
	def m3(self) -> c_float:
		...

	@m3.setter
	def m3(self, i: c_float) -> None:
		...

	@property
	def m7(self) -> c_float:
		...

	@m7.setter
	def m7(self, i: c_float) -> None:
		...

	@property
	def m11(self) -> c_float:
		...

	@m11.setter
	def m11(self, i: c_float) -> None:
		...

	@property
	def m15(self) -> c_float:
		...

	@m15.setter
	def m15(self, i: c_float) -> None:
		...


class rlVertexBuffer(Structure):
	"""Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""
	@property
	def elementCount(self) -> c_int:
		...

	@elementCount.setter
	def elementCount(self, i: c_int) -> None:
		...

	@property
	def vertices(self) -> POINTER(c_float):
		...

	@vertices.setter
	def vertices(self, i: POINTER(c_float)) -> None:
		...

	@property
	def texcoords(self) -> POINTER(c_float):
		...

	@texcoords.setter
	def texcoords(self, i: POINTER(c_float)) -> None:
		...

	@property
	def colors(self) -> POINTER(c_ubyte):
		...

	@colors.setter
	def colors(self, i: POINTER(c_ubyte)) -> None:
		...

	@property
	def indices(self) -> POINTER(c_uint):
		...

	@indices.setter
	def indices(self, i: POINTER(c_uint)) -> None:
		...

	@property
	def vaoId(self) -> c_uint:
		...

	@vaoId.setter
	def vaoId(self, i: c_uint) -> None:
		...

	@property
	def vboId(self) -> c_uint * 4:
		...

	@vboId.setter
	def vboId(self, i: c_uint * 4) -> None:
		...


class rlDrawCall(Structure):
	"""of those state-change happens (this is done in core module)"""
	@property
	def mode(self) -> c_int:
		...

	@mode.setter
	def mode(self, i: c_int) -> None:
		...

	@property
	def vertexCount(self) -> c_int:
		...

	@vertexCount.setter
	def vertexCount(self, i: c_int) -> None:
		...

	@property
	def vertexAlignment(self) -> c_int:
		...

	@vertexAlignment.setter
	def vertexAlignment(self, i: c_int) -> None:
		...

	@property
	def textureId(self) -> c_uint:
		...

	@textureId.setter
	def textureId(self, i: c_uint) -> None:
		...


class rlRenderBatch(Structure):
	"""rlRenderBatch type"""
	@property
	def bufferCount(self) -> c_int:
		...

	@bufferCount.setter
	def bufferCount(self, i: c_int) -> None:
		...

	@property
	def currentBuffer(self) -> c_int:
		...

	@currentBuffer.setter
	def currentBuffer(self, i: c_int) -> None:
		...

	@property
	def vertexBuffer(self) -> POINTER(rlVertexBuffer):
		...

	@vertexBuffer.setter
	def vertexBuffer(self, i: POINTER(rlVertexBuffer)) -> None:
		...

	@property
	def draws(self) -> POINTER(rlDrawCall):
		...

	@draws.setter
	def draws(self, i: POINTER(rlDrawCall)) -> None:
		...

	@property
	def drawCounter(self) -> c_int:
		...

	@drawCounter.setter
	def drawCounter(self, i: c_int) -> None:
		...

	@property
	def currentDepth(self) -> c_float:
		...

	@currentDepth.setter
	def currentDepth(self, i: c_float) -> None:
		...


class rlglData(Structure):
	""""""
	@property
	def currentBatch(self) -> POINTER(rlRenderBatch):
		...

	@currentBatch.setter
	def currentBatch(self, i: POINTER(rlRenderBatch)) -> None:
		...

	@property
	def defaultBatch(self) -> rlRenderBatch:
		...

	@defaultBatch.setter
	def defaultBatch(self, i: rlRenderBatch) -> None:
		...

	@property
	def vertexCounter(self) -> c_int:
		...

	@vertexCounter.setter
	def vertexCounter(self, i: c_int) -> None:
		...

	@property
	def texcoordx(self) -> c_float:
		...

	@texcoordx.setter
	def texcoordx(self, i: c_float) -> None:
		...

	@property
	def texcoordy(self) -> c_float:
		...

	@texcoordy.setter
	def texcoordy(self, i: c_float) -> None:
		...

	@property
	def normalx(self) -> c_float:
		...

	@normalx.setter
	def normalx(self, i: c_float) -> None:
		...

	@property
	def normaly(self) -> c_float:
		...

	@normaly.setter
	def normaly(self, i: c_float) -> None:
		...

	@property
	def normalz(self) -> c_float:
		...

	@normalz.setter
	def normalz(self, i: c_float) -> None:
		...

	@property
	def colorr(self) -> c_ubyte:
		...

	@colorr.setter
	def colorr(self, i: c_ubyte) -> None:
		...

	@property
	def colorg(self) -> c_ubyte:
		...

	@colorg.setter
	def colorg(self, i: c_ubyte) -> None:
		...

	@property
	def colorb(self) -> c_ubyte:
		...

	@colorb.setter
	def colorb(self, i: c_ubyte) -> None:
		...

	@property
	def colora(self) -> c_ubyte:
		...

	@colora.setter
	def colora(self, i: c_ubyte) -> None:
		...

	@property
	def currentMatrixMode(self) -> c_int:
		...

	@currentMatrixMode.setter
	def currentMatrixMode(self, i: c_int) -> None:
		...

	@property
	def currentMatrix(self) -> POINTER(Matrix):
		...

	@currentMatrix.setter
	def currentMatrix(self, i: POINTER(Matrix)) -> None:
		...

	@property
	def modelview(self) -> Matrix:
		...

	@modelview.setter
	def modelview(self, i: Matrix) -> None:
		...

	@property
	def projection(self) -> Matrix:
		...

	@projection.setter
	def projection(self, i: Matrix) -> None:
		...

	@property
	def transform(self) -> Matrix:
		...

	@transform.setter
	def transform(self, i: Matrix) -> None:
		...

	@property
	def transformRequired(self) -> c_bool:
		...

	@transformRequired.setter
	def transformRequired(self, i: c_bool) -> None:
		...

	@property
	def stack(self) -> Matrix * RL_MAX_MATRIX_STACK_SIZE:
		...

	@stack.setter
	def stack(self, i: Matrix * RL_MAX_MATRIX_STACK_SIZE) -> None:
		...

	@property
	def stackCounter(self) -> c_int:
		...

	@stackCounter.setter
	def stackCounter(self, i: c_int) -> None:
		...

	@property
	def defaultTextureId(self) -> c_uint:
		...

	@defaultTextureId.setter
	def defaultTextureId(self, i: c_uint) -> None:
		...

	@property
	def activeTextureId(self) -> c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS:
		...

	@activeTextureId.setter
	def activeTextureId(self, i: c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS) -> None:
		...

	@property
	def defaultVShaderId(self) -> c_uint:
		...

	@defaultVShaderId.setter
	def defaultVShaderId(self, i: c_uint) -> None:
		...

	@property
	def defaultFShaderId(self) -> c_uint:
		...

	@defaultFShaderId.setter
	def defaultFShaderId(self, i: c_uint) -> None:
		...

	@property
	def defaultShaderId(self) -> c_uint:
		...

	@defaultShaderId.setter
	def defaultShaderId(self, i: c_uint) -> None:
		...

	@property
	def defaultShaderLocs(self) -> POINTER(c_int):
		...

	@defaultShaderLocs.setter
	def defaultShaderLocs(self, i: POINTER(c_int)) -> None:
		...

	@property
	def currentShaderId(self) -> c_uint:
		...

	@currentShaderId.setter
	def currentShaderId(self, i: c_uint) -> None:
		...

	@property
	def currentShaderLocs(self) -> POINTER(c_int):
		...

	@currentShaderLocs.setter
	def currentShaderLocs(self, i: POINTER(c_int)) -> None:
		...

	@property
	def stereoRender(self) -> c_bool:
		...

	@stereoRender.setter
	def stereoRender(self, i: c_bool) -> None:
		...

	@property
	def projectionStereo(self) -> Matrix * 2:
		...

	@projectionStereo.setter
	def projectionStereo(self, i: Matrix * 2) -> None:
		...

	@property
	def viewOffsetStereo(self) -> Matrix * 2:
		...

	@viewOffsetStereo.setter
	def viewOffsetStereo(self, i: Matrix * 2) -> None:
		...

	@property
	def currentBlendMode(self) -> c_int:
		...

	@currentBlendMode.setter
	def currentBlendMode(self, i: c_int) -> None:
		...

	@property
	def glBlendSrcFactor(self) -> c_int:
		...

	@glBlendSrcFactor.setter
	def glBlendSrcFactor(self, i: c_int) -> None:
		...

	@property
	def glBlendDstFactor(self) -> c_int:
		...

	@glBlendDstFactor.setter
	def glBlendDstFactor(self, i: c_int) -> None:
		...

	@property
	def glBlendEquation(self) -> c_int:
		...

	@glBlendEquation.setter
	def glBlendEquation(self, i: c_int) -> None:
		...

	@property
	def glBlendSrcFactorRGB(self) -> c_int:
		...

	@glBlendSrcFactorRGB.setter
	def glBlendSrcFactorRGB(self, i: c_int) -> None:
		...

	@property
	def glBlendDestFactorRGB(self) -> c_int:
		...

	@glBlendDestFactorRGB.setter
	def glBlendDestFactorRGB(self, i: c_int) -> None:
		...

	@property
	def glBlendSrcFactorAlpha(self) -> c_int:
		...

	@glBlendSrcFactorAlpha.setter
	def glBlendSrcFactorAlpha(self, i: c_int) -> None:
		...

	@property
	def glBlendDestFactorAlpha(self) -> c_int:
		...

	@glBlendDestFactorAlpha.setter
	def glBlendDestFactorAlpha(self, i: c_int) -> None:
		...

	@property
	def glBlendEquationRGB(self) -> c_int:
		...

	@glBlendEquationRGB.setter
	def glBlendEquationRGB(self, i: c_int) -> None:
		...

	@property
	def glBlendEquationAlpha(self) -> c_int:
		...

	@glBlendEquationAlpha.setter
	def glBlendEquationAlpha(self, i: c_int) -> None:
		...

	@property
	def glCustomBlendModeModified(self) -> c_bool:
		...

	@glCustomBlendModeModified.setter
	def glCustomBlendModeModified(self, i: c_bool) -> None:
		...

	@property
	def framebufferWidth(self) -> c_int:
		...

	@framebufferWidth.setter
	def framebufferWidth(self, i: c_int) -> None:
		...

	@property
	def framebufferHeight(self) -> c_int:
		...

	@framebufferHeight.setter
	def framebufferHeight(self, i: c_int) -> None:
		...


class Vector2(Structure):
	"""Vector2, 2 components"""
	@property
	def x(self) -> c_float:
		...

	@x.setter
	def x(self, i: c_float) -> None:
		...

	@property
	def y(self) -> c_float:
		...

	@y.setter
	def y(self, i: c_float) -> None:
		...


class Vector3(Structure):
	"""Vector3, 3 components"""
	@property
	def x(self) -> c_float:
		...

	@x.setter
	def x(self, i: c_float) -> None:
		...

	@property
	def y(self) -> c_float:
		...

	@y.setter
	def y(self, i: c_float) -> None:
		...

	@property
	def z(self) -> c_float:
		...

	@z.setter
	def z(self, i: c_float) -> None:
		...


class Vector4(Structure):
	"""Vector4, 4 components"""
	@property
	def x(self) -> c_float:
		...

	@x.setter
	def x(self, i: c_float) -> None:
		...

	@property
	def y(self) -> c_float:
		...

	@y.setter
	def y(self, i: c_float) -> None:
		...

	@property
	def z(self) -> c_float:
		...

	@z.setter
	def z(self, i: c_float) -> None:
		...

	@property
	def w(self) -> c_float:
		...

	@w.setter
	def w(self, i: c_float) -> None:
		...


class Quaternion(Structure):
	"""Quaternion, 4 components (Vector4 alias)"""
	@property
	def x(self) -> c_float:
		...

	@x.setter
	def x(self, i: c_float) -> None:
		...

	@property
	def y(self) -> c_float:
		...

	@y.setter
	def y(self, i: c_float) -> None:
		...

	@property
	def z(self) -> c_float:
		...

	@z.setter
	def z(self, i: c_float) -> None:
		...

	@property
	def w(self) -> c_float:
		...

	@w.setter
	def w(self, i: c_float) -> None:
		...


class Color(Structure):
	"""Color, 4 components, R8G8B8A8 (32bit)"""
	@property
	def r(self) -> c_ubyte:
		...

	@r.setter
	def r(self, i: c_ubyte) -> None:
		...

	@property
	def g(self) -> c_ubyte:
		...

	@g.setter
	def g(self, i: c_ubyte) -> None:
		...

	@property
	def b(self) -> c_ubyte:
		...

	@b.setter
	def b(self, i: c_ubyte) -> None:
		...

	@property
	def a(self) -> c_ubyte:
		...

	@a.setter
	def a(self, i: c_ubyte) -> None:
		...


class Rectangle(Structure):
	"""Rectangle, 4 components"""
	@property
	def x(self) -> c_float:
		...

	@x.setter
	def x(self, i: c_float) -> None:
		...

	@property
	def y(self) -> c_float:
		...

	@y.setter
	def y(self, i: c_float) -> None:
		...

	@property
	def width(self) -> c_float:
		...

	@width.setter
	def width(self, i: c_float) -> None:
		...

	@property
	def height(self) -> c_float:
		...

	@height.setter
	def height(self, i: c_float) -> None:
		...


class Image(Structure):
	"""Image, pixel data stored in CPU memory (RAM)"""
	@property
	def data(self) -> c_void_p:
		...

	@data.setter
	def data(self, i: c_void_p) -> None:
		...

	@property
	def width(self) -> c_int:
		...

	@width.setter
	def width(self, i: c_int) -> None:
		...

	@property
	def height(self) -> c_int:
		...

	@height.setter
	def height(self, i: c_int) -> None:
		...

	@property
	def mipmaps(self) -> c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		...

	@property
	def format(self) -> c_int:
		...

	@format.setter
	def format(self, i: c_int) -> None:
		...


class Texture(Structure):
	"""Texture, tex data stored in GPU memory (VRAM)"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def width(self) -> c_int:
		...

	@width.setter
	def width(self, i: c_int) -> None:
		...

	@property
	def height(self) -> c_int:
		...

	@height.setter
	def height(self, i: c_int) -> None:
		...

	@property
	def mipmaps(self) -> c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		...

	@property
	def format(self) -> c_int:
		...

	@format.setter
	def format(self, i: c_int) -> None:
		...


class Texture2D(Structure):
	"""Texture2D, same as Texture"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def width(self) -> c_int:
		...

	@width.setter
	def width(self, i: c_int) -> None:
		...

	@property
	def height(self) -> c_int:
		...

	@height.setter
	def height(self, i: c_int) -> None:
		...

	@property
	def mipmaps(self) -> c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		...

	@property
	def format(self) -> c_int:
		...

	@format.setter
	def format(self, i: c_int) -> None:
		...


class TextureCubemap(Structure):
	"""TextureCubemap, same as Texture"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def width(self) -> c_int:
		...

	@width.setter
	def width(self, i: c_int) -> None:
		...

	@property
	def height(self) -> c_int:
		...

	@height.setter
	def height(self, i: c_int) -> None:
		...

	@property
	def mipmaps(self) -> c_int:
		...

	@mipmaps.setter
	def mipmaps(self, i: c_int) -> None:
		...

	@property
	def format(self) -> c_int:
		...

	@format.setter
	def format(self, i: c_int) -> None:
		...


class RenderTexture(Structure):
	"""RenderTexture, fbo for texture rendering"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def texture(self) -> Texture:
		...

	@texture.setter
	def texture(self, i: Texture) -> None:
		...

	@property
	def depth(self) -> Texture:
		...

	@depth.setter
	def depth(self, i: Texture) -> None:
		...


class RenderTexture2D(Structure):
	"""RenderTexture2D, same as RenderTexture"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def texture(self) -> Texture:
		...

	@texture.setter
	def texture(self, i: Texture) -> None:
		...

	@property
	def depth(self) -> Texture:
		...

	@depth.setter
	def depth(self, i: Texture) -> None:
		...


class NPatchInfo(Structure):
	"""NPatchInfo, n-patch layout info"""
	@property
	def source(self) -> Rectangle:
		...

	@source.setter
	def source(self, i: Rectangle) -> None:
		...

	@property
	def left(self) -> c_int:
		...

	@left.setter
	def left(self, i: c_int) -> None:
		...

	@property
	def top(self) -> c_int:
		...

	@top.setter
	def top(self, i: c_int) -> None:
		...

	@property
	def right(self) -> c_int:
		...

	@right.setter
	def right(self, i: c_int) -> None:
		...

	@property
	def bottom(self) -> c_int:
		...

	@bottom.setter
	def bottom(self, i: c_int) -> None:
		...

	@property
	def layout(self) -> c_int:
		...

	@layout.setter
	def layout(self, i: c_int) -> None:
		...


class GlyphInfo(Structure):
	"""GlyphInfo, font characters glyphs info"""
	@property
	def value(self) -> c_int:
		...

	@value.setter
	def value(self, i: c_int) -> None:
		...

	@property
	def offsetX(self) -> c_int:
		...

	@offsetX.setter
	def offsetX(self, i: c_int) -> None:
		...

	@property
	def offsetY(self) -> c_int:
		...

	@offsetY.setter
	def offsetY(self, i: c_int) -> None:
		...

	@property
	def advanceX(self) -> c_int:
		...

	@advanceX.setter
	def advanceX(self, i: c_int) -> None:
		...

	@property
	def image(self) -> Image:
		...

	@image.setter
	def image(self, i: Image) -> None:
		...


class Font(Structure):
	"""Font, font texture and GlyphInfo array data"""
	@property
	def baseSize(self) -> c_int:
		...

	@baseSize.setter
	def baseSize(self, i: c_int) -> None:
		...

	@property
	def glyphCount(self) -> c_int:
		...

	@glyphCount.setter
	def glyphCount(self, i: c_int) -> None:
		...

	@property
	def glyphPadding(self) -> c_int:
		...

	@glyphPadding.setter
	def glyphPadding(self, i: c_int) -> None:
		...

	@property
	def texture(self) -> Texture2D:
		...

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		...

	@property
	def recs(self) -> POINTER(Rectangle):
		...

	@recs.setter
	def recs(self, i: POINTER(Rectangle)) -> None:
		...

	@property
	def glyphs(self) -> POINTER(GlyphInfo):
		...

	@glyphs.setter
	def glyphs(self, i: POINTER(GlyphInfo)) -> None:
		...


class Camera3D(Structure):
	"""Camera, defines position/orientation in 3d space"""
	@property
	def position(self) -> Vector3:
		...

	@position.setter
	def position(self, i: Vector3) -> None:
		...

	@property
	def target(self) -> Vector3:
		...

	@target.setter
	def target(self, i: Vector3) -> None:
		...

	@property
	def up(self) -> Vector3:
		...

	@up.setter
	def up(self, i: Vector3) -> None:
		...

	@property
	def fovy(self) -> c_float:
		...

	@fovy.setter
	def fovy(self, i: c_float) -> None:
		...

	@property
	def projection(self) -> c_int:
		...

	@projection.setter
	def projection(self, i: c_int) -> None:
		...


class Camera(Structure):
	"""Camera type fallback, defaults to Camera3D"""
	@property
	def position(self) -> Vector3:
		...

	@position.setter
	def position(self, i: Vector3) -> None:
		...

	@property
	def target(self) -> Vector3:
		...

	@target.setter
	def target(self, i: Vector3) -> None:
		...

	@property
	def up(self) -> Vector3:
		...

	@up.setter
	def up(self, i: Vector3) -> None:
		...

	@property
	def fovy(self) -> c_float:
		...

	@fovy.setter
	def fovy(self, i: c_float) -> None:
		...

	@property
	def projection(self) -> c_int:
		...

	@projection.setter
	def projection(self, i: c_int) -> None:
		...


class Camera2D(Structure):
	"""Camera2D, defines position/orientation in 2d space"""
	@property
	def offset(self) -> Vector2:
		...

	@offset.setter
	def offset(self, i: Vector2) -> None:
		...

	@property
	def target(self) -> Vector2:
		...

	@target.setter
	def target(self, i: Vector2) -> None:
		...

	@property
	def rotation(self) -> c_float:
		...

	@rotation.setter
	def rotation(self, i: c_float) -> None:
		...

	@property
	def zoom(self) -> c_float:
		...

	@zoom.setter
	def zoom(self, i: c_float) -> None:
		...


class Mesh(Structure):
	"""Mesh, vertex data and vao/vbo"""
	@property
	def vertexCount(self) -> c_int:
		...

	@vertexCount.setter
	def vertexCount(self, i: c_int) -> None:
		...

	@property
	def triangleCount(self) -> c_int:
		...

	@triangleCount.setter
	def triangleCount(self, i: c_int) -> None:
		...

	@property
	def vertices(self) -> POINTER(c_float):
		...

	@vertices.setter
	def vertices(self, i: POINTER(c_float)) -> None:
		...

	@property
	def texcoords(self) -> POINTER(c_float):
		...

	@texcoords.setter
	def texcoords(self, i: POINTER(c_float)) -> None:
		...

	@property
	def texcoords2(self) -> POINTER(c_float):
		...

	@texcoords2.setter
	def texcoords2(self, i: POINTER(c_float)) -> None:
		...

	@property
	def normals(self) -> POINTER(c_float):
		...

	@normals.setter
	def normals(self, i: POINTER(c_float)) -> None:
		...

	@property
	def tangents(self) -> POINTER(c_float):
		...

	@tangents.setter
	def tangents(self, i: POINTER(c_float)) -> None:
		...

	@property
	def colors(self) -> POINTER(c_ubyte):
		...

	@colors.setter
	def colors(self, i: POINTER(c_ubyte)) -> None:
		...

	@property
	def indices(self) -> POINTER(c_ushort):
		...

	@indices.setter
	def indices(self, i: POINTER(c_ushort)) -> None:
		...

	@property
	def animVertices(self) -> POINTER(c_float):
		...

	@animVertices.setter
	def animVertices(self, i: POINTER(c_float)) -> None:
		...

	@property
	def animNormals(self) -> POINTER(c_float):
		...

	@animNormals.setter
	def animNormals(self, i: POINTER(c_float)) -> None:
		...

	@property
	def boneIds(self) -> POINTER(c_ubyte):
		...

	@boneIds.setter
	def boneIds(self, i: POINTER(c_ubyte)) -> None:
		...

	@property
	def boneWeights(self) -> POINTER(c_float):
		...

	@boneWeights.setter
	def boneWeights(self, i: POINTER(c_float)) -> None:
		...

	@property
	def vaoId(self) -> c_uint:
		...

	@vaoId.setter
	def vaoId(self, i: c_uint) -> None:
		...

	@property
	def vboId(self) -> POINTER(c_uint):
		...

	@vboId.setter
	def vboId(self, i: POINTER(c_uint)) -> None:
		...


class Shader(Structure):
	"""Shader"""
	@property
	def id(self) -> c_uint:
		...

	@id.setter
	def id(self, i: c_uint) -> None:
		...

	@property
	def locs(self) -> POINTER(c_int):
		...

	@locs.setter
	def locs(self, i: POINTER(c_int)) -> None:
		...


class MaterialMap(Structure):
	"""MaterialMap"""
	@property
	def texture(self) -> Texture2D:
		...

	@texture.setter
	def texture(self, i: Texture2D) -> None:
		...

	@property
	def color(self) -> Color:
		...

	@color.setter
	def color(self, i: Color) -> None:
		...

	@property
	def value(self) -> c_float:
		...

	@value.setter
	def value(self, i: c_float) -> None:
		...


class Material(Structure):
	"""Material, includes shader and maps"""
	@property
	def shader(self) -> Shader:
		...

	@shader.setter
	def shader(self, i: Shader) -> None:
		...

	@property
	def maps(self) -> POINTER(MaterialMap):
		...

	@maps.setter
	def maps(self, i: POINTER(MaterialMap)) -> None:
		...

	@property
	def params(self) -> c_float * 4:
		...

	@params.setter
	def params(self, i: c_float * 4) -> None:
		...


class Transform(Structure):
	"""Transform, vectex transformation data"""
	@property
	def translation(self) -> Vector3:
		...

	@translation.setter
	def translation(self, i: Vector3) -> None:
		...

	@property
	def rotation(self) -> Quaternion:
		...

	@rotation.setter
	def rotation(self, i: Quaternion) -> None:
		...

	@property
	def scale(self) -> Vector3:
		...

	@scale.setter
	def scale(self, i: Vector3) -> None:
		...


class BoneInfo(Structure):
	"""Bone, skeletal animation bone"""
	@property
	def name(self) -> c_char * 32:
		...

	@name.setter
	def name(self, i: c_char * 32) -> None:
		...

	@property
	def parent(self) -> c_int:
		...

	@parent.setter
	def parent(self, i: c_int) -> None:
		...


class Model(Structure):
	"""Model, meshes, materials and animation data"""
	@property
	def transform(self) -> Matrix:
		...

	@transform.setter
	def transform(self, i: Matrix) -> None:
		...

	@property
	def meshCount(self) -> c_int:
		...

	@meshCount.setter
	def meshCount(self, i: c_int) -> None:
		...

	@property
	def materialCount(self) -> c_int:
		...

	@materialCount.setter
	def materialCount(self, i: c_int) -> None:
		...

	@property
	def meshes(self) -> POINTER(Mesh):
		...

	@meshes.setter
	def meshes(self, i: POINTER(Mesh)) -> None:
		...

	@property
	def materials(self) -> POINTER(Material):
		...

	@materials.setter
	def materials(self, i: POINTER(Material)) -> None:
		...

	@property
	def meshMaterial(self) -> POINTER(c_int):
		...

	@meshMaterial.setter
	def meshMaterial(self, i: POINTER(c_int)) -> None:
		...

	@property
	def boneCount(self) -> c_int:
		...

	@boneCount.setter
	def boneCount(self, i: c_int) -> None:
		...

	@property
	def bones(self) -> POINTER(BoneInfo):
		...

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		...

	@property
	def bindPose(self) -> POINTER(Transform):
		...

	@bindPose.setter
	def bindPose(self, i: POINTER(Transform)) -> None:
		...


class ModelAnimation(Structure):
	"""ModelAnimation"""
	@property
	def boneCount(self) -> c_int:
		...

	@boneCount.setter
	def boneCount(self, i: c_int) -> None:
		...

	@property
	def frameCount(self) -> c_int:
		...

	@frameCount.setter
	def frameCount(self, i: c_int) -> None:
		...

	@property
	def bones(self) -> POINTER(BoneInfo):
		...

	@bones.setter
	def bones(self, i: POINTER(BoneInfo)) -> None:
		...

	@property
	def framePoses(self) -> POINTER(POINTER(Transform)):
		...

	@framePoses.setter
	def framePoses(self, i: POINTER(POINTER(Transform))) -> None:
		...


class Ray(Structure):
	"""Ray, ray for raycasting"""
	@property
	def position(self) -> Vector3:
		...

	@position.setter
	def position(self, i: Vector3) -> None:
		...

	@property
	def direction(self) -> Vector3:
		...

	@direction.setter
	def direction(self, i: Vector3) -> None:
		...


class RayCollision(Structure):
	"""RayCollision, ray hit information"""
	@property
	def hit(self) -> c_bool:
		...

	@hit.setter
	def hit(self, i: c_bool) -> None:
		...

	@property
	def distance(self) -> c_float:
		...

	@distance.setter
	def distance(self, i: c_float) -> None:
		...

	@property
	def point(self) -> Vector3:
		...

	@point.setter
	def point(self, i: Vector3) -> None:
		...

	@property
	def normal(self) -> Vector3:
		...

	@normal.setter
	def normal(self, i: Vector3) -> None:
		...


class BoundingBox(Structure):
	"""BoundingBox"""
	@property
	def min(self) -> Vector3:
		...

	@min.setter
	def min(self, i: Vector3) -> None:
		...

	@property
	def max(self) -> Vector3:
		...

	@max.setter
	def max(self, i: Vector3) -> None:
		...


class VrDeviceInfo(Structure):
	"""VrDeviceInfo, Head-Mounted-Display device parameters"""
	@property
	def hResolution(self) -> c_int:
		...

	@hResolution.setter
	def hResolution(self, i: c_int) -> None:
		...

	@property
	def vResolution(self) -> c_int:
		...

	@vResolution.setter
	def vResolution(self, i: c_int) -> None:
		...

	@property
	def hScreenSize(self) -> c_float:
		...

	@hScreenSize.setter
	def hScreenSize(self, i: c_float) -> None:
		...

	@property
	def vScreenSize(self) -> c_float:
		...

	@vScreenSize.setter
	def vScreenSize(self, i: c_float) -> None:
		...

	@property
	def vScreenCenter(self) -> c_float:
		...

	@vScreenCenter.setter
	def vScreenCenter(self, i: c_float) -> None:
		...

	@property
	def eyeToScreenDistance(self) -> c_float:
		...

	@eyeToScreenDistance.setter
	def eyeToScreenDistance(self, i: c_float) -> None:
		...

	@property
	def lensSeparationDistance(self) -> c_float:
		...

	@lensSeparationDistance.setter
	def lensSeparationDistance(self, i: c_float) -> None:
		...

	@property
	def interpupillaryDistance(self) -> c_float:
		...

	@interpupillaryDistance.setter
	def interpupillaryDistance(self, i: c_float) -> None:
		...

	@property
	def lensDistortionValues(self) -> c_float * 4:
		...

	@lensDistortionValues.setter
	def lensDistortionValues(self, i: c_float * 4) -> None:
		...

	@property
	def chromaAbCorrection(self) -> c_float * 4:
		...

	@chromaAbCorrection.setter
	def chromaAbCorrection(self, i: c_float * 4) -> None:
		...


class VrStereoConfig(Structure):
	"""VrStereoConfig, VR stereo rendering configuration for simulator"""
	@property
	def projection(self) -> Matrix * 2:
		...

	@projection.setter
	def projection(self, i: Matrix * 2) -> None:
		...

	@property
	def viewOffset(self) -> Matrix * 2:
		...

	@viewOffset.setter
	def viewOffset(self, i: Matrix * 2) -> None:
		...

	@property
	def leftLensCenter(self) -> c_float * 2:
		...

	@leftLensCenter.setter
	def leftLensCenter(self, i: c_float * 2) -> None:
		...

	@property
	def rightLensCenter(self) -> c_float * 2:
		...

	@rightLensCenter.setter
	def rightLensCenter(self, i: c_float * 2) -> None:
		...

	@property
	def leftScreenCenter(self) -> c_float * 2:
		...

	@leftScreenCenter.setter
	def leftScreenCenter(self, i: c_float * 2) -> None:
		...

	@property
	def rightScreenCenter(self) -> c_float * 2:
		...

	@rightScreenCenter.setter
	def rightScreenCenter(self, i: c_float * 2) -> None:
		...

	@property
	def scale(self) -> c_float * 2:
		...

	@scale.setter
	def scale(self, i: c_float * 2) -> None:
		...

	@property
	def scaleIn(self) -> c_float * 2:
		...

	@scaleIn.setter
	def scaleIn(self, i: c_float * 2) -> None:
		...


class FilePathList(Structure):
	"""File path list"""
	@property
	def capacity(self) -> c_uint:
		...

	@capacity.setter
	def capacity(self, i: c_uint) -> None:
		...

	@property
	def count(self) -> c_uint:
		...

	@count.setter
	def count(self, i: c_uint) -> None:
		...

	@property
	def paths(self) -> POINTER(POINTER(c_char)):
		...

	@paths.setter
	def paths(self, i: POINTER(POINTER(c_char))) -> None:
		...


class float3(Structure):
	"""NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
	@property
	def v(self) -> c_float * 3:
		...

	@v.setter
	def v(self, i: c_float * 3) -> None:
		...


class float16(Structure):
	""""""
	@property
	def v(self) -> c_float * 16:
		...

	@v.setter
	def v(self, i: c_float * 16) -> None:
		...


class GuiStyleProp(Structure):
	"""Style property"""
	@property
	def controlId(self) -> c_ushort:
		...

	@controlId.setter
	def controlId(self, i: c_ushort) -> None:
		...

	@property
	def propertyId(self) -> c_ushort:
		...

	@propertyId.setter
	def propertyId(self, i: c_ushort) -> None:
		...

	@property
	def propertyValue(self) -> c_uint:
		...

	@propertyValue.setter
	def propertyValue(self, i: c_uint) -> None:
		...


