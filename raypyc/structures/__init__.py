import ctypes

from raypyc.defines import *


class rAudioBuffer(ctypes.Structure):
    """dummy structure"""
    _fields_ = [
        ("data", ctypes.c_byte * 24)
    ]


class rAudioProcessor(ctypes.Structure):
    """dummy structure"""
    _fields_ = [
        ("data", ctypes.c_byte * 24)
    ]


class rlVertexBuffer(ctypes.Structure):
    """Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""
    _fields_ = [
        ('elementCount', ctypes.c_int),  # Number of elements in the buffer (QUADS)
        ('vertices', ctypes.POINTER(ctypes.c_float)),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
        ('texcoords', ctypes.POINTER(ctypes.c_float)),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
        ('colors', ctypes.POINTER(ctypes.c_ubyte)),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
        ('indices', ctypes.POINTER(ctypes.c_uint)),  # Vertex indices (in case vertex data comes indexed) (6 indices per quad)
        ('vaoId', ctypes.c_uint),  # OpenGL Vertex Array Object id
        ('vboId', ctypes.c_uint * 4)  # OpenGL Vertex Buffer Objects id (4 types of vertex data)
    ]

    @property
    def elementCount(self) -> ctypes.c_int:
        return self.elementCount

    @elementCount.setter
    def elementCount(self, i: ctypes.c_int) -> None:
        self.elementCount = i

    @property
    def vertices(self) -> ctypes.POINTER(ctypes.c_float):
        return self.vertices

    @vertices.setter
    def vertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.vertices = i

    @property
    def texcoords(self) -> ctypes.POINTER(ctypes.c_float):
        return self.texcoords

    @texcoords.setter
    def texcoords(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.texcoords = i

    @property
    def colors(self) -> ctypes.POINTER(ctypes.c_ubyte):
        return self.colors

    @colors.setter
    def colors(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
        self.colors = i

    @property
    def indices(self) -> ctypes.POINTER(ctypes.c_uint):
        return self.indices

    @indices.setter
    def indices(self, i: ctypes.POINTER(ctypes.c_uint)) -> None:
        self.indices = i

    @property
    def vaoId(self) -> ctypes.c_uint:
        return self.vaoId

    @vaoId.setter
    def vaoId(self, i: ctypes.c_uint) -> None:
        self.vaoId = i

    @property
    def vboId(self) -> ctypes.c_uint * 4:
        return self.vboId

    @vboId.setter
    def vboId(self, i: ctypes.c_uint * 4) -> None:
        self.vboId = i


class rlDrawCall(ctypes.Structure):
    """of those state-change happens (this is done in core module)"""
    _fields_ = [
        ('mode', ctypes.c_int),  # Drawing mode: LINES, TRIANGLES, QUADS
        ('vertexCount', ctypes.c_int),  # Number of vertex of the draw
        ('vertexAlignment', ctypes.c_int),  # Number of vertex required for index alignment (LINES, TRIANGLES)
        ('textureId', ctypes.c_uint)  # Texture id to be used on the draw -> Use to create new draw call if changes
    ]

    @property
    def mode(self) -> ctypes.c_int:
        return self.mode

    @mode.setter
    def mode(self, i: ctypes.c_int) -> None:
        self.mode = i

    @property
    def vertexCount(self) -> ctypes.c_int:
        return self.vertexCount

    @vertexCount.setter
    def vertexCount(self, i: ctypes.c_int) -> None:
        self.vertexCount = i

    @property
    def vertexAlignment(self) -> ctypes.c_int:
        return self.vertexAlignment

    @vertexAlignment.setter
    def vertexAlignment(self, i: ctypes.c_int) -> None:
        self.vertexAlignment = i

    @property
    def textureId(self) -> ctypes.c_uint:
        return self.textureId

    @textureId.setter
    def textureId(self, i: ctypes.c_uint) -> None:
        self.textureId = i


class rlRenderBatch(ctypes.Structure):
    """rlRenderBatch type"""
    _fields_ = [
        ('bufferCount', ctypes.c_int),  # Number of vertex buffers (multi-buffering support)
        ('currentBuffer', ctypes.c_int),  # Current buffer tracking in case of multi-buffering
        ('vertexBuffer', ctypes.POINTER(rlVertexBuffer)),  # Dynamic buffer(s) for vertex data
        ('draws', ctypes.POINTER(rlDrawCall)),  # Draw calls array, depends on textureId
        ('drawCounter', ctypes.c_int),  # Draw calls counter
        ('currentDepth', ctypes.c_float)  # Current depth value for next draw
    ]

    @property
    def bufferCount(self) -> ctypes.c_int:
        return self.bufferCount

    @bufferCount.setter
    def bufferCount(self, i: ctypes.c_int) -> None:
        self.bufferCount = i

    @property
    def currentBuffer(self) -> ctypes.c_int:
        return self.currentBuffer

    @currentBuffer.setter
    def currentBuffer(self, i: ctypes.c_int) -> None:
        self.currentBuffer = i

    @property
    def vertexBuffer(self) -> ctypes.POINTER(rlVertexBuffer):
        return self.vertexBuffer

    @vertexBuffer.setter
    def vertexBuffer(self, i: ctypes.POINTER(rlVertexBuffer)) -> None:
        self.vertexBuffer = i

    @property
    def draws(self) -> ctypes.POINTER(rlDrawCall):
        return self.draws

    @draws.setter
    def draws(self, i: ctypes.POINTER(rlDrawCall)) -> None:
        self.draws = i

    @property
    def drawCounter(self) -> ctypes.c_int:
        return self.drawCounter

    @drawCounter.setter
    def drawCounter(self, i: ctypes.c_int) -> None:
        self.drawCounter = i

    @property
    def currentDepth(self) -> ctypes.c_float:
        return self.currentDepth

    @currentDepth.setter
    def currentDepth(self, i: ctypes.c_float) -> None:
        self.currentDepth = i


class Matrix(ctypes.Structure):
    """Matrix, 4x4 components, column major, OpenGL style, right handed"""
    _fields_ = [
        ('m0', ctypes.c_float),  # Matrix first row (4 components)
        ('m4', ctypes.c_float),  # Matrix first row (4 components)
        ('m8', ctypes.c_float),  # Matrix first row (4 components)
        ('m12', ctypes.c_float),  # Matrix first row (4 components)
        ('m1', ctypes.c_float),  # Matrix second row (4 components)
        ('m5', ctypes.c_float),  # Matrix second row (4 components)
        ('m9', ctypes.c_float),  # Matrix second row (4 components)
        ('m13', ctypes.c_float),  # Matrix second row (4 components)
        ('m2', ctypes.c_float),  # Matrix third row (4 components)
        ('m6', ctypes.c_float),  # Matrix third row (4 components)
        ('m10', ctypes.c_float),  # Matrix third row (4 components)
        ('m14', ctypes.c_float),  # Matrix third row (4 components)
        ('m3', ctypes.c_float),  # Matrix fourth row (4 components)
        ('m7', ctypes.c_float),  # Matrix fourth row (4 components)
        ('m11', ctypes.c_float),  # Matrix fourth row (4 components)
        ('m15', ctypes.c_float)  # Matrix fourth row (4 components)
    ]

    @property
    def m0(self) -> ctypes.c_float:
        return self.m0

    @m0.setter
    def m0(self, i: ctypes.c_float) -> None:
        self.m0 = i

    @property
    def m4(self) -> ctypes.c_float:
        return self.m4

    @m4.setter
    def m4(self, i: ctypes.c_float) -> None:
        self.m4 = i

    @property
    def m8(self) -> ctypes.c_float:
        return self.m8

    @m8.setter
    def m8(self, i: ctypes.c_float) -> None:
        self.m8 = i

    @property
    def m12(self) -> ctypes.c_float:
        return self.m12

    @m12.setter
    def m12(self, i: ctypes.c_float) -> None:
        self.m12 = i

    @property
    def m1(self) -> ctypes.c_float:
        return self.m1

    @m1.setter
    def m1(self, i: ctypes.c_float) -> None:
        self.m1 = i

    @property
    def m5(self) -> ctypes.c_float:
        return self.m5

    @m5.setter
    def m5(self, i: ctypes.c_float) -> None:
        self.m5 = i

    @property
    def m9(self) -> ctypes.c_float:
        return self.m9

    @m9.setter
    def m9(self, i: ctypes.c_float) -> None:
        self.m9 = i

    @property
    def m13(self) -> ctypes.c_float:
        return self.m13

    @m13.setter
    def m13(self, i: ctypes.c_float) -> None:
        self.m13 = i

    @property
    def m2(self) -> ctypes.c_float:
        return self.m2

    @m2.setter
    def m2(self, i: ctypes.c_float) -> None:
        self.m2 = i

    @property
    def m6(self) -> ctypes.c_float:
        return self.m6

    @m6.setter
    def m6(self, i: ctypes.c_float) -> None:
        self.m6 = i

    @property
    def m10(self) -> ctypes.c_float:
        return self.m10

    @m10.setter
    def m10(self, i: ctypes.c_float) -> None:
        self.m10 = i

    @property
    def m14(self) -> ctypes.c_float:
        return self.m14

    @m14.setter
    def m14(self, i: ctypes.c_float) -> None:
        self.m14 = i

    @property
    def m3(self) -> ctypes.c_float:
        return self.m3

    @m3.setter
    def m3(self, i: ctypes.c_float) -> None:
        self.m3 = i

    @property
    def m7(self) -> ctypes.c_float:
        return self.m7

    @m7.setter
    def m7(self, i: ctypes.c_float) -> None:
        self.m7 = i

    @property
    def m11(self) -> ctypes.c_float:
        return self.m11

    @m11.setter
    def m11(self, i: ctypes.c_float) -> None:
        self.m11 = i

    @property
    def m15(self) -> ctypes.c_float:
        return self.m15

    @m15.setter
    def m15(self, i: ctypes.c_float) -> None:
        self.m15 = i


class rlglData(ctypes.Structure):
    """"""
    _fields_ = [
        ('currentBatch', ctypes.POINTER(rlRenderBatch)),  # Current render batch
        ('defaultBatch', rlRenderBatch),  # Default internal render batch
        ('vertexCounter', ctypes.c_int),  # Current active render batch vertex counter (generic, used for all batches)
        ('texcoordx', ctypes.c_float),  # Current active texture coordinate (added on glVertex*())
        ('texcoordy', ctypes.c_float),  # Current active texture coordinate (added on glVertex*())
        ('normalx', ctypes.c_float),  # Current active normal (added on glVertex*())
        ('normaly', ctypes.c_float),  # Current active normal (added on glVertex*())
        ('normalz', ctypes.c_float),  # Current active normal (added on glVertex*())
        ('colorr', ctypes.c_ubyte),  # Current active color (added on glVertex*())
        ('colorg', ctypes.c_ubyte),  # Current active color (added on glVertex*())
        ('colorb', ctypes.c_ubyte),  # Current active color (added on glVertex*())
        ('colora', ctypes.c_ubyte),  # Current active color (added on glVertex*())
        ('currentMatrixMode', ctypes.c_int),  # Current matrix mode
        ('currentMatrix', ctypes.POINTER(Matrix)),  # Current matrix pointer
        ('modelview', Matrix),  # Default modelview matrix
        ('projection', Matrix),  # Default projection matrix
        ('transform', Matrix),  # Transform matrix to be used with rlTranslate, rlRotate, rlScale
        ('transformRequired', ctypes.c_bool),  # Require transform matrix application to current draw-call vertex (if required)
        ('stack', Matrix * RL_MAX_MATRIX_STACK_SIZE),  # Matrix stack for push/pop
        ('stackCounter', ctypes.c_int),  # Matrix stack counter
        ('defaultTextureId', ctypes.c_uint),  # Default texture used on shapes/poly drawing (required by shader)
        ('activeTextureId', ctypes.c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS),  # Active texture ids to be enabled on batch drawing (0 active by default)
        ('defaultVShaderId', ctypes.c_uint),  # Default vertex shader id (used by default shader program)
        ('defaultFShaderId', ctypes.c_uint),  # Default fragment shader id (used by default shader program)
        ('defaultShaderId', ctypes.c_uint),  # Default shader program id, supports vertex color and diffuse texture
        ('defaultShaderLocs', ctypes.POINTER(ctypes.c_int)),  # Default shader locations pointer to be used on rendering
        ('currentShaderId', ctypes.c_uint),  # Current shader id to be used on rendering (by default, defaultShaderId)
        ('currentShaderLocs', ctypes.POINTER(ctypes.c_int)),  # Current shader locations pointer to be used on rendering (by default, defaultShaderLocs)
        ('stereoRender', ctypes.c_bool),  # Stereo rendering flag
        ('projectionStereo', Matrix * 2),  # VR stereo rendering eyes projection matrices
        ('viewOffsetStereo', Matrix * 2),  # VR stereo rendering eyes view offset matrices
        ('currentBlendMode', ctypes.c_int),  # Blending mode active
        ('glBlendSrcFactor', ctypes.c_int),  # Blending source factor
        ('glBlendDstFactor', ctypes.c_int),  # Blending destination factor
        ('glBlendEquation', ctypes.c_int),  # Blending equation
        ('framebufferWidth', ctypes.c_int),  # Current framebuffer width
        ('framebufferHeight', ctypes.c_int)  # Current framebuffer height
    ]

    @property
    def currentBatch(self) -> ctypes.POINTER(rlRenderBatch):
        return self.currentBatch

    @currentBatch.setter
    def currentBatch(self, i: ctypes.POINTER(rlRenderBatch)) -> None:
        self.currentBatch = i

    @property
    def defaultBatch(self) -> rlRenderBatch:
        return self.defaultBatch

    @defaultBatch.setter
    def defaultBatch(self, i: rlRenderBatch) -> None:
        self.defaultBatch = i

    @property
    def vertexCounter(self) -> ctypes.c_int:
        return self.vertexCounter

    @vertexCounter.setter
    def vertexCounter(self, i: ctypes.c_int) -> None:
        self.vertexCounter = i

    @property
    def texcoordx(self) -> ctypes.c_float:
        return self.texcoordx

    @texcoordx.setter
    def texcoordx(self, i: ctypes.c_float) -> None:
        self.texcoordx = i

    @property
    def texcoordy(self) -> ctypes.c_float:
        return self.texcoordy

    @texcoordy.setter
    def texcoordy(self, i: ctypes.c_float) -> None:
        self.texcoordy = i

    @property
    def normalx(self) -> ctypes.c_float:
        return self.normalx

    @normalx.setter
    def normalx(self, i: ctypes.c_float) -> None:
        self.normalx = i

    @property
    def normaly(self) -> ctypes.c_float:
        return self.normaly

    @normaly.setter
    def normaly(self, i: ctypes.c_float) -> None:
        self.normaly = i

    @property
    def normalz(self) -> ctypes.c_float:
        return self.normalz

    @normalz.setter
    def normalz(self, i: ctypes.c_float) -> None:
        self.normalz = i

    @property
    def colorr(self) -> ctypes.c_ubyte:
        return self.colorr

    @colorr.setter
    def colorr(self, i: ctypes.c_ubyte) -> None:
        self.colorr = i

    @property
    def colorg(self) -> ctypes.c_ubyte:
        return self.colorg

    @colorg.setter
    def colorg(self, i: ctypes.c_ubyte) -> None:
        self.colorg = i

    @property
    def colorb(self) -> ctypes.c_ubyte:
        return self.colorb

    @colorb.setter
    def colorb(self, i: ctypes.c_ubyte) -> None:
        self.colorb = i

    @property
    def colora(self) -> ctypes.c_ubyte:
        return self.colora

    @colora.setter
    def colora(self, i: ctypes.c_ubyte) -> None:
        self.colora = i

    @property
    def currentMatrixMode(self) -> ctypes.c_int:
        return self.currentMatrixMode

    @currentMatrixMode.setter
    def currentMatrixMode(self, i: ctypes.c_int) -> None:
        self.currentMatrixMode = i

    @property
    def currentMatrix(self) -> ctypes.POINTER(Matrix):
        return self.currentMatrix

    @currentMatrix.setter
    def currentMatrix(self, i: ctypes.POINTER(Matrix)) -> None:
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
    def transformRequired(self) -> ctypes.c_bool:
        return self.transformRequired

    @transformRequired.setter
    def transformRequired(self, i: ctypes.c_bool) -> None:
        self.transformRequired = i

    @property
    def stack(self) -> Matrix * RL_MAX_MATRIX_STACK_SIZE:
        return self.stack

    @stack.setter
    def stack(self, i: Matrix * RL_MAX_MATRIX_STACK_SIZE) -> None:
        self.stack = i

    @property
    def stackCounter(self) -> ctypes.c_int:
        return self.stackCounter

    @stackCounter.setter
    def stackCounter(self, i: ctypes.c_int) -> None:
        self.stackCounter = i

    @property
    def defaultTextureId(self) -> ctypes.c_uint:
        return self.defaultTextureId

    @defaultTextureId.setter
    def defaultTextureId(self, i: ctypes.c_uint) -> None:
        self.defaultTextureId = i

    @property
    def activeTextureId(self) -> ctypes.c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS:
        return self.activeTextureId

    @activeTextureId.setter
    def activeTextureId(self, i: ctypes.c_uint * RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS) -> None:
        self.activeTextureId = i

    @property
    def defaultVShaderId(self) -> ctypes.c_uint:
        return self.defaultVShaderId

    @defaultVShaderId.setter
    def defaultVShaderId(self, i: ctypes.c_uint) -> None:
        self.defaultVShaderId = i

    @property
    def defaultFShaderId(self) -> ctypes.c_uint:
        return self.defaultFShaderId

    @defaultFShaderId.setter
    def defaultFShaderId(self, i: ctypes.c_uint) -> None:
        self.defaultFShaderId = i

    @property
    def defaultShaderId(self) -> ctypes.c_uint:
        return self.defaultShaderId

    @defaultShaderId.setter
    def defaultShaderId(self, i: ctypes.c_uint) -> None:
        self.defaultShaderId = i

    @property
    def defaultShaderLocs(self) -> ctypes.POINTER(ctypes.c_int):
        return self.defaultShaderLocs

    @defaultShaderLocs.setter
    def defaultShaderLocs(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
        self.defaultShaderLocs = i

    @property
    def currentShaderId(self) -> ctypes.c_uint:
        return self.currentShaderId

    @currentShaderId.setter
    def currentShaderId(self, i: ctypes.c_uint) -> None:
        self.currentShaderId = i

    @property
    def currentShaderLocs(self) -> ctypes.POINTER(ctypes.c_int):
        return self.currentShaderLocs

    @currentShaderLocs.setter
    def currentShaderLocs(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
        self.currentShaderLocs = i

    @property
    def stereoRender(self) -> ctypes.c_bool:
        return self.stereoRender

    @stereoRender.setter
    def stereoRender(self, i: ctypes.c_bool) -> None:
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
    def currentBlendMode(self) -> ctypes.c_int:
        return self.currentBlendMode

    @currentBlendMode.setter
    def currentBlendMode(self, i: ctypes.c_int) -> None:
        self.currentBlendMode = i

    @property
    def glBlendSrcFactor(self) -> ctypes.c_int:
        return self.glBlendSrcFactor

    @glBlendSrcFactor.setter
    def glBlendSrcFactor(self, i: ctypes.c_int) -> None:
        self.glBlendSrcFactor = i

    @property
    def glBlendDstFactor(self) -> ctypes.c_int:
        return self.glBlendDstFactor

    @glBlendDstFactor.setter
    def glBlendDstFactor(self, i: ctypes.c_int) -> None:
        self.glBlendDstFactor = i

    @property
    def glBlendEquation(self) -> ctypes.c_int:
        return self.glBlendEquation

    @glBlendEquation.setter
    def glBlendEquation(self, i: ctypes.c_int) -> None:
        self.glBlendEquation = i

    @property
    def framebufferWidth(self) -> ctypes.c_int:
        return self.framebufferWidth

    @framebufferWidth.setter
    def framebufferWidth(self, i: ctypes.c_int) -> None:
        self.framebufferWidth = i

    @property
    def framebufferHeight(self) -> ctypes.c_int:
        return self.framebufferHeight

    @framebufferHeight.setter
    def framebufferHeight(self, i: ctypes.c_int) -> None:
        self.framebufferHeight = i


class Vector2(ctypes.Structure):
    """Vector2, 2 components"""
    _fields_ = [
        ('x', ctypes.c_float),  # Vector x component
        ('y', ctypes.c_float)  # Vector y component
    ]

    @property
    def x(self) -> ctypes.c_float:
        return self.x

    @x.setter
    def x(self, i: ctypes.c_float) -> None:
        self.x = i

    @property
    def y(self) -> ctypes.c_float:
        return self.y

    @y.setter
    def y(self, i: ctypes.c_float) -> None:
        self.y = i


class Vector3(ctypes.Structure):
    """Vector3, 3 components"""
    _fields_ = [
        ('x', ctypes.c_float),  # Vector x component
        ('y', ctypes.c_float),  # Vector y component
        ('z', ctypes.c_float)  # Vector z component
    ]

    @property
    def x(self) -> ctypes.c_float:
        return self.x

    @x.setter
    def x(self, i: ctypes.c_float) -> None:
        self.x = i

    @property
    def y(self) -> ctypes.c_float:
        return self.y

    @y.setter
    def y(self, i: ctypes.c_float) -> None:
        self.y = i

    @property
    def z(self) -> ctypes.c_float:
        return self.z

    @z.setter
    def z(self, i: ctypes.c_float) -> None:
        self.z = i


class Vector4(ctypes.Structure):
    """Vector4, 4 components"""
    _fields_ = [
        ('x', ctypes.c_float),  # Vector x component
        ('y', ctypes.c_float),  # Vector y component
        ('z', ctypes.c_float),  # Vector z component
        ('w', ctypes.c_float)  # Vector w component
    ]

    @property
    def x(self) -> ctypes.c_float:
        return self.x

    @x.setter
    def x(self, i: ctypes.c_float) -> None:
        self.x = i

    @property
    def y(self) -> ctypes.c_float:
        return self.y

    @y.setter
    def y(self, i: ctypes.c_float) -> None:
        self.y = i

    @property
    def z(self) -> ctypes.c_float:
        return self.z

    @z.setter
    def z(self, i: ctypes.c_float) -> None:
        self.z = i

    @property
    def w(self) -> ctypes.c_float:
        return self.w

    @w.setter
    def w(self, i: ctypes.c_float) -> None:
        self.w = i


Quaternion = Vector4


class Color(ctypes.Structure):
    """Color, 4 components, R8G8B8A8 (32bit)"""
    _fields_ = [
        ('r', ctypes.c_ubyte),  # Color red value
        ('g', ctypes.c_ubyte),  # Color green value
        ('b', ctypes.c_ubyte),  # Color blue value
        ('a', ctypes.c_ubyte)  # Color alpha value
    ]

    @property
    def r(self) -> ctypes.c_ubyte:
        return self.r

    @r.setter
    def r(self, i: ctypes.c_ubyte) -> None:
        self.r = i

    @property
    def g(self) -> ctypes.c_ubyte:
        return self.g

    @g.setter
    def g(self, i: ctypes.c_ubyte) -> None:
        self.g = i

    @property
    def b(self) -> ctypes.c_ubyte:
        return self.b

    @b.setter
    def b(self, i: ctypes.c_ubyte) -> None:
        self.b = i

    @property
    def a(self) -> ctypes.c_ubyte:
        return self.a

    @a.setter
    def a(self, i: ctypes.c_ubyte) -> None:
        self.a = i


class Rectangle(ctypes.Structure):
    """Rectangle, 4 components"""
    _fields_ = [
        ('x', ctypes.c_float),  # Rectangle top-left corner position x
        ('y', ctypes.c_float),  # Rectangle top-left corner position y
        ('width', ctypes.c_float),  # Rectangle width
        ('height', ctypes.c_float)  # Rectangle height
    ]

    @property
    def x(self) -> ctypes.c_float:
        return self.x

    @x.setter
    def x(self, i: ctypes.c_float) -> None:
        self.x = i

    @property
    def y(self) -> ctypes.c_float:
        return self.y

    @y.setter
    def y(self, i: ctypes.c_float) -> None:
        self.y = i

    @property
    def width(self) -> ctypes.c_float:
        return self.width

    @width.setter
    def width(self, i: ctypes.c_float) -> None:
        self.width = i

    @property
    def height(self) -> ctypes.c_float:
        return self.height

    @height.setter
    def height(self, i: ctypes.c_float) -> None:
        self.height = i


class Image(ctypes.Structure):
    """Image, pixel data stored in CPU memory (RAM)"""
    _fields_ = [
        ('data', ctypes.c_void_p),  # Image raw data
        ('width', ctypes.c_int),  # Image base width
        ('height', ctypes.c_int),  # Image base height
        ('mipmaps', ctypes.c_int),  # Mipmap levels, 1 by default
        ('format', ctypes.c_int)  # Data format (PixelFormat type)
    ]

    @property
    def data(self) -> ctypes.c_void_p:
        return self.data

    @data.setter
    def data(self, i: ctypes.c_void_p) -> None:
        self.data = i

    @property
    def width(self) -> ctypes.c_int:
        return self.width

    @width.setter
    def width(self, i: ctypes.c_int) -> None:
        self.width = i

    @property
    def height(self) -> ctypes.c_int:
        return self.height

    @height.setter
    def height(self, i: ctypes.c_int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> ctypes.c_int:
        return self.mipmaps

    @mipmaps.setter
    def mipmaps(self, i: ctypes.c_int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> ctypes.c_int:
        return self.format

    @format.setter
    def format(self, i: ctypes.c_int) -> None:
        self.format = i


class Texture(ctypes.Structure):
    """Texture, tex data stored in GPU memory (VRAM)"""
    _fields_ = [
        ('id', ctypes.c_uint),  # OpenGL texture id
        ('width', ctypes.c_int),  # Texture base width
        ('height', ctypes.c_int),  # Texture base height
        ('mipmaps', ctypes.c_int),  # Mipmap levels, 1 by default
        ('format', ctypes.c_int)  # Data format (PixelFormat type)
    ]

    @property
    def id(self) -> ctypes.c_uint:
        return self.id

    @id.setter
    def id(self, i: ctypes.c_uint) -> None:
        self.id = i

    @property
    def width(self) -> ctypes.c_int:
        return self.width

    @width.setter
    def width(self, i: ctypes.c_int) -> None:
        self.width = i

    @property
    def height(self) -> ctypes.c_int:
        return self.height

    @height.setter
    def height(self, i: ctypes.c_int) -> None:
        self.height = i

    @property
    def mipmaps(self) -> ctypes.c_int:
        return self.mipmaps

    @mipmaps.setter
    def mipmaps(self, i: ctypes.c_int) -> None:
        self.mipmaps = i

    @property
    def format(self) -> ctypes.c_int:
        return self.format

    @format.setter
    def format(self, i: ctypes.c_int) -> None:
        self.format = i


Texture2D = Texture

TextureCubemap = Texture


class RenderTexture(ctypes.Structure):
    """RenderTexture, fbo for texture rendering"""
    _fields_ = [
        ('id', ctypes.c_uint),  # OpenGL framebuffer object id
        ('texture', Texture),  # Color buffer attachment texture
        ('depth', Texture)  # Depth buffer attachment texture
    ]

    @property
    def id(self) -> ctypes.c_uint:
        return self.id

    @id.setter
    def id(self, i: ctypes.c_uint) -> None:
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


RenderTexture2D = RenderTexture


class NPatchInfo(ctypes.Structure):
    """NPatchInfo, n-patch layout info"""
    _fields_ = [
        ('source', Rectangle),  # Texture source rectangle
        ('left', ctypes.c_int),  # Left border offset
        ('top', ctypes.c_int),  # Top border offset
        ('right', ctypes.c_int),  # Right border offset
        ('bottom', ctypes.c_int),  # Bottom border offset
        ('layout', ctypes.c_int),  # Layout of the n-patch: 3x3 1x3 or 3x1
    ]

    @property
    def source(self) -> Rectangle:
        return self.source

    @source.setter
    def source(self, i: Rectangle) -> None:
        self.source = i

    @property
    def left(self) -> ctypes.c_int:
        return self.left

    @left.setter
    def left(self, i: ctypes.c_int) -> None:
        self.left = i

    @property
    def top(self) -> ctypes.c_int:
        return self.top

    @top.setter
    def top(self, i: ctypes.c_int) -> None:
        self.top = i

    @property
    def right(self) -> ctypes.c_int:
        return self.right

    @right.setter
    def right(self, i: ctypes.c_int) -> None:
        self.right = i

    @property
    def bottom(self) -> ctypes.c_int:
        return self.bottom

    @bottom.setter
    def bottom(self, i: ctypes.c_int) -> None:
        self.bottom = i

    @property
    def layout(self) -> ctypes.c_int:
        return self.layout

    @layout.setter
    def layout(self, i: ctypes.c_int) -> None:
        self.layout = i


class GlyphInfo(ctypes.Structure):
    """GlyphInfo, font characters glyphs info"""
    _fields_ = [
        ('value', ctypes.c_int),  # Character value (Unicode)
        ('offsetX', ctypes.c_int),  # Character offset X when drawing
        ('offsetY', ctypes.c_int),  # Character offset Y when drawing
        ('advanceX', ctypes.c_int),  # Character advance position X
        ('image', Image)  # Character image data
    ]

    @property
    def value(self) -> ctypes.c_int:
        return self.value

    @value.setter
    def value(self, i: ctypes.c_int) -> None:
        self.value = i

    @property
    def offsetX(self) -> ctypes.c_int:
        return self.offsetX

    @offsetX.setter
    def offsetX(self, i: ctypes.c_int) -> None:
        self.offsetX = i

    @property
    def offsetY(self) -> ctypes.c_int:
        return self.offsetY

    @offsetY.setter
    def offsetY(self, i: ctypes.c_int) -> None:
        self.offsetY = i

    @property
    def advanceX(self) -> ctypes.c_int:
        return self.advanceX

    @advanceX.setter
    def advanceX(self, i: ctypes.c_int) -> None:
        self.advanceX = i

    @property
    def image(self) -> Image:
        return self.image

    @image.setter
    def image(self, i: Image) -> None:
        self.image = i


class Font(ctypes.Structure):
    """Font, font texture and GlyphInfo array data"""
    _fields_ = [
        ('baseSize', ctypes.c_int),  # Base size (default chars height)
        ('glyphCount', ctypes.c_int),  # Number of glyph characters
        ('glyphPadding', ctypes.c_int),  # Padding around the glyph characters
        ('texture', Texture2D),  # Texture atlas containing the glyphs
        ('recs', ctypes.POINTER(Rectangle)),  # Rectangles in texture for the glyphs
        ('glyphs', ctypes.POINTER(GlyphInfo))  # Glyphs info data
    ]

    @property
    def baseSize(self) -> ctypes.c_int:
        return self.baseSize

    @baseSize.setter
    def baseSize(self, i: ctypes.c_int) -> None:
        self.baseSize = i

    @property
    def glyphCount(self) -> ctypes.c_int:
        return self.glyphCount

    @glyphCount.setter
    def glyphCount(self, i: ctypes.c_int) -> None:
        self.glyphCount = i

    @property
    def glyphPadding(self) -> ctypes.c_int:
        return self.glyphPadding

    @glyphPadding.setter
    def glyphPadding(self, i: ctypes.c_int) -> None:
        self.glyphPadding = i

    @property
    def texture(self) -> Texture2D:
        return self.texture

    @texture.setter
    def texture(self, i: Texture2D) -> None:
        self.texture = i

    @property
    def recs(self) -> ctypes.POINTER(Rectangle):
        return self.recs

    @recs.setter
    def recs(self, i: ctypes.POINTER(Rectangle)) -> None:
        self.recs = i

    @property
    def glyphs(self) -> ctypes.POINTER(GlyphInfo):
        return self.glyphs

    @glyphs.setter
    def glyphs(self, i: ctypes.POINTER(GlyphInfo)) -> None:
        self.glyphs = i


class Camera3D(ctypes.Structure):
    """Camera, defines position/orientation in 3d space"""
    _fields_ = [
        ('position', Vector3),  # Camera position
        ('target', Vector3),  # Camera target it looks-at
        ('up', Vector3),  # Camera up vector (rotation over its axis)
        ('fovy', ctypes.c_float),  # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
        ('projection', ctypes.c_int)  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
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
    def fovy(self) -> ctypes.c_float:
        return self.fovy

    @fovy.setter
    def fovy(self, i: ctypes.c_float) -> None:
        self.fovy = i

    @property
    def projection(self) -> ctypes.c_int:
        return self.projection

    @projection.setter
    def projection(self, i: ctypes.c_int) -> None:
        self.projection = i


Camera = Camera3D


class Camera2D(ctypes.Structure):
    """Camera2D, defines position/orientation in 2d space"""
    _fields_ = [
        ('offset', Vector2),  # Camera offset (displacement from target)
        ('target', Vector2),  # Camera target (rotation and zoom origin)
        ('rotation', ctypes.c_float),  # Camera rotation in degrees
        ('zoom', ctypes.c_float),  # Camera zoom (scaling) should be 1.0f by default
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
    def rotation(self) -> ctypes.c_float:
        return self.rotation

    @rotation.setter
    def rotation(self, i: ctypes.c_float) -> None:
        self.rotation = i

    @property
    def zoom(self) -> ctypes.c_float:
        return self.zoom

    @zoom.setter
    def zoom(self, i: ctypes.c_float) -> None:
        self.zoom = i


class Mesh(ctypes.Structure):
    """Mesh, vertex data and vao/vbo"""
    _fields_ = [
        ('vertexCount', ctypes.c_int),  # Number of vertices stored in arrays
        ('triangleCount', ctypes.c_int),  # Number of triangles stored (indexed or not)
        ('vertices', ctypes.POINTER(ctypes.c_float)),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
        ('texcoords', ctypes.POINTER(ctypes.c_float)),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
        ('texcoords2', ctypes.POINTER(ctypes.c_float)),  # Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
        ('normals', ctypes.POINTER(ctypes.c_float)),  # Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
        ('tangents', ctypes.POINTER(ctypes.c_float)),  # Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
        ('colors', ctypes.POINTER(ctypes.c_ubyte)),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
        ('indices', ctypes.POINTER(ctypes.c_ushort)),  # Vertex indices (in case vertex data comes indexed)
        ('animVertices', ctypes.POINTER(ctypes.c_float)),  # Animated vertex positions (after bones transformations)
        ('animNormals', ctypes.POINTER(ctypes.c_float)),  # Animated normals (after bones transformations)
        ('boneIds', ctypes.POINTER(ctypes.c_ubyte)),  # Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
        ('boneWeights', ctypes.POINTER(ctypes.c_float)),  # Vertex bone weight, up to 4 bones influence by vertex (skinning)
        ('vaoId', ctypes.c_uint),  # OpenGL Vertex Array Object id
        ('vboId', ctypes.POINTER(ctypes.c_uint))  # OpenGL Vertex Buffer Objects id (default vertex data)
    ]

    @property
    def vertexCount(self) -> ctypes.c_int:
        return self.vertexCount

    @vertexCount.setter
    def vertexCount(self, i: ctypes.c_int) -> None:
        self.vertexCount = i

    @property
    def triangleCount(self) -> ctypes.c_int:
        return self.triangleCount

    @triangleCount.setter
    def triangleCount(self, i: ctypes.c_int) -> None:
        self.triangleCount = i

    @property
    def vertices(self) -> ctypes.POINTER(ctypes.c_float):
        return self.vertices

    @vertices.setter
    def vertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.vertices = i

    @property
    def texcoords(self) -> ctypes.POINTER(ctypes.c_float):
        return self.texcoords

    @texcoords.setter
    def texcoords(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.texcoords = i

    @property
    def texcoords2(self) -> ctypes.POINTER(ctypes.c_float):
        return self.texcoords2

    @texcoords2.setter
    def texcoords2(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.texcoords2 = i

    @property
    def normals(self) -> ctypes.POINTER(ctypes.c_float):
        return self.normals

    @normals.setter
    def normals(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.normals = i

    @property
    def tangents(self) -> ctypes.POINTER(ctypes.c_float):
        return self.tangents

    @tangents.setter
    def tangents(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.tangents = i

    @property
    def colors(self) -> ctypes.POINTER(ctypes.c_ubyte):
        return self.colors

    @colors.setter
    def colors(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
        self.colors = i

    @property
    def indices(self) -> ctypes.POINTER(ctypes.c_ushort):
        return self.indices

    @indices.setter
    def indices(self, i: ctypes.POINTER(ctypes.c_ushort)) -> None:
        self.indices = i

    @property
    def animVertices(self) -> ctypes.POINTER(ctypes.c_float):
        return self.animVertices

    @animVertices.setter
    def animVertices(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.animVertices = i

    @property
    def animNormals(self) -> ctypes.POINTER(ctypes.c_float):
        return self.animNormals

    @animNormals.setter
    def animNormals(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.animNormals = i

    @property
    def boneIds(self) -> ctypes.POINTER(ctypes.c_ubyte):
        return self.boneIds

    @boneIds.setter
    def boneIds(self, i: ctypes.POINTER(ctypes.c_ubyte)) -> None:
        self.boneIds = i

    @property
    def boneWeights(self) -> ctypes.POINTER(ctypes.c_float):
        return self.boneWeights

    @boneWeights.setter
    def boneWeights(self, i: ctypes.POINTER(ctypes.c_float)) -> None:
        self.boneWeights = i

    @property
    def vaoId(self) -> ctypes.c_uint:
        return self.vaoId

    @vaoId.setter
    def vaoId(self, i: ctypes.c_uint) -> None:
        self.vaoId = i

    @property
    def vboId(self) -> ctypes.POINTER(ctypes.c_uint):
        return self.vboId

    @vboId.setter
    def vboId(self, i: ctypes.POINTER(ctypes.c_uint)) -> None:
        self.vboId = i


class Shader(ctypes.Structure):
    """Shader"""
    _fields_ = [
        ('id', ctypes.c_uint),  # Shader program id
        ('locs', ctypes.POINTER(ctypes.c_int))  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
    ]

    @property
    def id(self) -> ctypes.c_uint:
        return self.id

    @id.setter
    def id(self, i: ctypes.c_uint) -> None:
        self.id = i

    @property
    def locs(self) -> ctypes.POINTER(ctypes.c_int):
        return self.locs

    @locs.setter
    def locs(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
        self.locs = i


class MaterialMap(ctypes.Structure):
    """MaterialMap"""
    _fields_ = [
        ('texture', Texture2D),  # Material map texture
        ('color', Color),  # Material map color
        ('value', ctypes.c_float)  # Material map value
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
    def value(self) -> ctypes.c_float:
        return self.value

    @value.setter
    def value(self, i: ctypes.c_float) -> None:
        self.value = i


class Material(ctypes.Structure):
    """Material, includes shader and maps"""
    _fields_ = [
        ('shader', Shader),  # Material shader
        ('maps', ctypes.POINTER(MaterialMap)),  # Material maps array (MAX_MATERIAL_MAPS)
        ('params', ctypes.c_float * 4)  # Material generic parameters (if required)
    ]

    @property
    def shader(self) -> Shader:
        return self.shader

    @shader.setter
    def shader(self, i: Shader) -> None:
        self.shader = i

    @property
    def maps(self) -> ctypes.POINTER(MaterialMap):
        return self.maps

    @maps.setter
    def maps(self, i: ctypes.POINTER(MaterialMap)) -> None:
        self.maps = i

    @property
    def params(self) -> ctypes.c_float * 4:
        return self.params

    @params.setter
    def params(self, i: ctypes.c_float * 4) -> None:
        self.params = i


class Transform(ctypes.Structure):
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


class BoneInfo(ctypes.Structure):
    """Bone, skeletal animation bone"""
    _fields_ = [
        ('name', ctypes.c_char * 32),  # Bone name
        ('parent', ctypes.c_int)  # Bone parent
    ]

    @property
    def name(self) -> ctypes.c_char * 32:
        return self.name

    @name.setter
    def name(self, i: ctypes.c_char * 32) -> None:
        self.name = i

    @property
    def parent(self) -> ctypes.c_int:
        return self.parent

    @parent.setter
    def parent(self, i: ctypes.c_int) -> None:
        self.parent = i


class Model(ctypes.Structure):
    """Model, meshes, materials and animation data"""
    _fields_ = [
        ('transform', Matrix),  # Local transform matrix
        ('meshCount', ctypes.c_int),  # Number of meshes
        ('materialCount', ctypes.c_int),  # Number of materials
        ('meshes', ctypes.POINTER(Mesh)),  # Meshes array
        ('materials', ctypes.POINTER(Material)),  # Materials array
        ('meshMaterial', ctypes.POINTER(ctypes.c_int)),  # Mesh material number
        ('boneCount', ctypes.c_int),  # Number of bones
        ('bones', ctypes.POINTER(BoneInfo)),  # Bones information (skeleton)
        ('bindPose', ctypes.POINTER(Transform))  # Bones base transformation (pose)
    ]

    @property
    def transform(self) -> Matrix:
        return self.transform

    @transform.setter
    def transform(self, i: Matrix) -> None:
        self.transform = i

    @property
    def meshCount(self) -> ctypes.c_int:
        return self.meshCount

    @meshCount.setter
    def meshCount(self, i: ctypes.c_int) -> None:
        self.meshCount = i

    @property
    def materialCount(self) -> ctypes.c_int:
        return self.materialCount

    @materialCount.setter
    def materialCount(self, i: ctypes.c_int) -> None:
        self.materialCount = i

    @property
    def meshes(self) -> ctypes.POINTER(Mesh):
        return self.meshes

    @meshes.setter
    def meshes(self, i: ctypes.POINTER(Mesh)) -> None:
        self.meshes = i

    @property
    def materials(self) -> ctypes.POINTER(Material):
        return self.materials

    @materials.setter
    def materials(self, i: ctypes.POINTER(Material)) -> None:
        self.materials = i

    @property
    def meshMaterial(self) -> ctypes.POINTER(ctypes.c_int):
        return self.meshMaterial

    @meshMaterial.setter
    def meshMaterial(self, i: ctypes.POINTER(ctypes.c_int)) -> None:
        self.meshMaterial = i

    @property
    def boneCount(self) -> ctypes.c_int:
        return self.boneCount

    @boneCount.setter
    def boneCount(self, i: ctypes.c_int) -> None:
        self.boneCount = i

    @property
    def bones(self) -> ctypes.POINTER(BoneInfo):
        return self.bones

    @bones.setter
    def bones(self, i: ctypes.POINTER(BoneInfo)) -> None:
        self.bones = i

    @property
    def bindPose(self) -> ctypes.POINTER(Transform):
        return self.bindPose

    @bindPose.setter
    def bindPose(self, i: ctypes.POINTER(Transform)) -> None:
        self.bindPose = i


class ModelAnimation(ctypes.Structure):
    """ModelAnimation"""
    _fields_ = [
        ('boneCount', ctypes.c_int),  # Number of bones
        ('frameCount', ctypes.c_int),  # Number of animation frames
        ('bones', ctypes.POINTER(BoneInfo)),  # Bones information (skeleton)
        ('framePoses', ctypes.POINTER(ctypes.POINTER(Transform)))  # Poses array by frame
    ]

    @property
    def boneCount(self) -> ctypes.c_int:
        return self.boneCount

    @boneCount.setter
    def boneCount(self, i: ctypes.c_int) -> None:
        self.boneCount = i

    @property
    def frameCount(self) -> ctypes.c_int:
        return self.frameCount

    @frameCount.setter
    def frameCount(self, i: ctypes.c_int) -> None:
        self.frameCount = i

    @property
    def bones(self) -> ctypes.POINTER(BoneInfo):
        return self.bones

    @bones.setter
    def bones(self, i: ctypes.POINTER(BoneInfo)) -> None:
        self.bones = i

    @property
    def framePoses(self) -> ctypes.POINTER(ctypes.POINTER(Transform)):
        return self.framePoses

    @framePoses.setter
    def framePoses(self, i: ctypes.POINTER(ctypes.POINTER(Transform))) -> None:
        self.framePoses = i


class Ray(ctypes.Structure):
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


class RayCollision(ctypes.Structure):
    """RayCollision, ray hit information"""
    _fields_ = [
        ('hit', ctypes.c_bool),  # Did the ray hit something?
        ('distance', ctypes.c_float),  # Distance to nearest hit
        ('point', Vector3),  # Point of nearest hit
        ('normal', Vector3)  # Surface normal of hit
    ]

    @property
    def hit(self) -> ctypes.c_bool:
        return self.hit

    @hit.setter
    def hit(self, i: ctypes.c_bool) -> None:
        self.hit = i

    @property
    def distance(self) -> ctypes.c_float:
        return self.distance

    @distance.setter
    def distance(self, i: ctypes.c_float) -> None:
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


class BoundingBox(ctypes.Structure):
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


class Wave(ctypes.Structure):
    """Wave, audio wave data"""
    _fields_ = [
        ('frameCount', ctypes.c_uint),  # Total number of frames (considering channels)
        ('sampleRate', ctypes.c_uint),  # Frequency (samples per second)
        ('sampleSize', ctypes.c_uint),  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
        ('channels', ctypes.c_uint),  # Number of channels (1-mono, 2-stereo, ...)
        ('data', ctypes.c_void_p)  # Buffer data pointer
    ]

    @property
    def frameCount(self) -> ctypes.c_uint:
        return self.frameCount

    @frameCount.setter
    def frameCount(self, i: ctypes.c_uint) -> None:
        self.frameCount = i

    @property
    def sampleRate(self) -> ctypes.c_uint:
        return self.sampleRate

    @sampleRate.setter
    def sampleRate(self, i: ctypes.c_uint) -> None:
        self.sampleRate = i

    @property
    def sampleSize(self) -> ctypes.c_uint:
        return self.sampleSize

    @sampleSize.setter
    def sampleSize(self, i: ctypes.c_uint) -> None:
        self.sampleSize = i

    @property
    def channels(self) -> ctypes.c_uint:
        return self.channels

    @channels.setter
    def channels(self, i: ctypes.c_uint) -> None:
        self.channels = i

    @property
    def data(self) -> ctypes.c_void_p:
        return self.data

    @data.setter
    def data(self, i: ctypes.c_void_p) -> None:
        self.data = i


class AudioStream(ctypes.Structure):
    """AudioStream, custom audio stream"""
    _fields_ = [
        ('buffer', ctypes.POINTER(rAudioBuffer)),  # Pointer to internal data used by the audio system
        ('processor', ctypes.POINTER(rAudioProcessor)),  # Pointer to internal data processor, useful for audio effects
        ('sampleRate', ctypes.c_uint),  # Frequency (samples per second)
        ('sampleSize', ctypes.c_uint),  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
        ('channels', ctypes.c_uint),  # Number of channels (1-mono, 2-stereo ...)
    ]

    @property
    def buffer(self) -> ctypes.POINTER(rAudioBuffer):
        return self.buffer

    @buffer.setter
    def buffer(self, i: ctypes.POINTER(rAudioBuffer)) -> None:
        self.buffer = i

    @property
    def processor(self) -> ctypes.POINTER(rAudioProcessor):
        return self.processor

    @processor.setter
    def processor(self, i: ctypes.POINTER(rAudioProcessor)) -> None:
        self.processor = i

    @property
    def sampleRate(self) -> ctypes.c_uint:
        return self.sampleRate

    @sampleRate.setter
    def sampleRate(self, i: ctypes.c_uint) -> None:
        self.sampleRate = i

    @property
    def sampleSize(self) -> ctypes.c_uint:
        return self.sampleSize

    @sampleSize.setter
    def sampleSize(self, i: ctypes.c_uint) -> None:
        self.sampleSize = i

    @property
    def channels(self) -> ctypes.c_uint:
        return self.channels

    @channels.setter
    def channels(self, i: ctypes.c_uint) -> None:
        self.channels = i


class Sound(ctypes.Structure):
    """Sound"""
    _fields_ = [
        ('stream', AudioStream),  # Audio stream
        ('frameCount', ctypes.c_uint)  # Total number of frames (considering channels)
    ]

    @property
    def stream(self) -> AudioStream:
        return self.stream

    @stream.setter
    def stream(self, i: AudioStream) -> None:
        self.stream = i

    @property
    def frameCount(self) -> ctypes.c_uint:
        return self.frameCount

    @frameCount.setter
    def frameCount(self, i: ctypes.c_uint) -> None:
        self.frameCount = i


class Music(ctypes.Structure):
    """Music, audio stream, anything longer than ~10 seconds should be streamed"""
    _fields_ = [
        ('stream', AudioStream),  # Audio stream
        ('frameCount', ctypes.c_uint),  # Total number of frames (considering channels)
        ('looping', ctypes.c_bool),  # Music looping enable
        ('ctxType', ctypes.c_int),  # Type of music context (audio filetype)
        ('ctxData', ctypes.c_void_p),  # Audio context data depends on type
    ]

    @property
    def stream(self) -> AudioStream:
        return self.stream

    @stream.setter
    def stream(self, i: AudioStream) -> None:
        self.stream = i

    @property
    def frameCount(self) -> ctypes.c_uint:
        return self.frameCount

    @frameCount.setter
    def frameCount(self, i: ctypes.c_uint) -> None:
        self.frameCount = i

    @property
    def looping(self) -> ctypes.c_bool:
        return self.looping

    @looping.setter
    def looping(self, i: ctypes.c_bool) -> None:
        self.looping = i

    @property
    def ctxType(self) -> ctypes.c_int:
        return self.ctxType

    @ctxType.setter
    def ctxType(self, i: ctypes.c_int) -> None:
        self.ctxType = i

    @property
    def ctxData(self) -> ctypes.c_void_p:
        return self.ctxData

    @ctxData.setter
    def ctxData(self, i: ctypes.c_void_p) -> None:
        self.ctxData = i


class VrDeviceInfo(ctypes.Structure):
    """VrDeviceInfo, Head-Mounted-Display device parameters"""
    _fields_ = [
        ('hResolution', ctypes.c_int),  # Horizontal resolution in pixels
        ('vResolution', ctypes.c_int),  # Vertical resolution in pixels
        ('hScreenSize', ctypes.c_float),  # Horizontal size in meters
        ('vScreenSize', ctypes.c_float),  # Vertical size in meters
        ('vScreenCenter', ctypes.c_float),  # Screen center in meters
        ('eyeToScreenDistance', ctypes.c_float),  # Distance between eye and display in meters
        ('lensSeparationDistance', ctypes.c_float),  # Lens separation distance in meters
        ('interpupillaryDistance', ctypes.c_float),  # IPD (distance between pupils) in meters
        ('lensDistortionValues', ctypes.c_float * 4),  # Lens distortion constant parameters
        ('chromaAbCorrection', ctypes.c_float * 4)  # Chromatic aberration correction parameters
    ]

    @property
    def hResolution(self) -> ctypes.c_int:
        return self.hResolution

    @hResolution.setter
    def hResolution(self, i: ctypes.c_int) -> None:
        self.hResolution = i

    @property
    def vResolution(self) -> ctypes.c_int:
        return self.vResolution

    @vResolution.setter
    def vResolution(self, i: ctypes.c_int) -> None:
        self.vResolution = i

    @property
    def hScreenSize(self) -> ctypes.c_float:
        return self.hScreenSize

    @hScreenSize.setter
    def hScreenSize(self, i: ctypes.c_float) -> None:
        self.hScreenSize = i

    @property
    def vScreenSize(self) -> ctypes.c_float:
        return self.vScreenSize

    @vScreenSize.setter
    def vScreenSize(self, i: ctypes.c_float) -> None:
        self.vScreenSize = i

    @property
    def vScreenCenter(self) -> ctypes.c_float:
        return self.vScreenCenter

    @vScreenCenter.setter
    def vScreenCenter(self, i: ctypes.c_float) -> None:
        self.vScreenCenter = i

    @property
    def eyeToScreenDistance(self) -> ctypes.c_float:
        return self.eyeToScreenDistance

    @eyeToScreenDistance.setter
    def eyeToScreenDistance(self, i: ctypes.c_float) -> None:
        self.eyeToScreenDistance = i

    @property
    def lensSeparationDistance(self) -> ctypes.c_float:
        return self.lensSeparationDistance

    @lensSeparationDistance.setter
    def lensSeparationDistance(self, i: ctypes.c_float) -> None:
        self.lensSeparationDistance = i

    @property
    def interpupillaryDistance(self) -> ctypes.c_float:
        return self.interpupillaryDistance

    @interpupillaryDistance.setter
    def interpupillaryDistance(self, i: ctypes.c_float) -> None:
        self.interpupillaryDistance = i

    @property
    def lensDistortionValues(self) -> ctypes.c_float * 4:
        return self.lensDistortionValues

    @lensDistortionValues.setter
    def lensDistortionValues(self, i: ctypes.c_float * 4) -> None:
        self.lensDistortionValues = i

    @property
    def chromaAbCorrection(self) -> ctypes.c_float * 4:
        return self.chromaAbCorrection

    @chromaAbCorrection.setter
    def chromaAbCorrection(self, i: ctypes.c_float * 4) -> None:
        self.chromaAbCorrection = i


class VrStereoConfig(ctypes.Structure):
    """VrStereoConfig, VR stereo rendering configuration for simulator"""
    _fields_ = [
        ('projection', Matrix * 2),  # VR projection matrices (per eye)
        ('viewOffset', Matrix * 2),  # VR view offset matrices (per eye)
        ('leftLensCenter', ctypes.c_float * 2),  # VR left lens center
        ('rightLensCenter', ctypes.c_float * 2),  # VR right lens center
        ('leftScreenCenter', ctypes.c_float * 2),  # VR left screen center
        ('rightScreenCenter', ctypes.c_float * 2),  # VR right screen center
        ('scale', ctypes.c_float * 2),  # VR distortion scale
        ('scaleIn', ctypes.c_float * 2)  # VR distortion scale in
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
    def leftLensCenter(self) -> ctypes.c_float * 2:
        return self.leftLensCenter

    @leftLensCenter.setter
    def leftLensCenter(self, i: ctypes.c_float * 2) -> None:
        self.leftLensCenter = i

    @property
    def rightLensCenter(self) -> ctypes.c_float * 2:
        return self.rightLensCenter

    @rightLensCenter.setter
    def rightLensCenter(self, i: ctypes.c_float * 2) -> None:
        self.rightLensCenter = i

    @property
    def leftScreenCenter(self) -> ctypes.c_float * 2:
        return self.leftScreenCenter

    @leftScreenCenter.setter
    def leftScreenCenter(self, i: ctypes.c_float * 2) -> None:
        self.leftScreenCenter = i

    @property
    def rightScreenCenter(self) -> ctypes.c_float * 2:
        return self.rightScreenCenter

    @rightScreenCenter.setter
    def rightScreenCenter(self, i: ctypes.c_float * 2) -> None:
        self.rightScreenCenter = i

    @property
    def scale(self) -> ctypes.c_float * 2:
        return self.scale

    @scale.setter
    def scale(self, i: ctypes.c_float * 2) -> None:
        self.scale = i

    @property
    def scaleIn(self) -> ctypes.c_float * 2:
        return self.scaleIn

    @scaleIn.setter
    def scaleIn(self, i: ctypes.c_float * 2) -> None:
        self.scaleIn = i


class FilePathList(ctypes.Structure):
    """File path list"""
    _fields_ = [
        ('capacity', ctypes.c_uint),  # Filepaths max entries
        ('count', ctypes.c_uint),  # Filepaths entries count
        ('paths', ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))  # Filepaths entries
    ]

    @property
    def capacity(self) -> ctypes.c_uint:
        return self.capacity

    @capacity.setter
    def capacity(self, i: ctypes.c_uint) -> None:
        self.capacity = i

    @property
    def count(self) -> ctypes.c_uint:
        return self.count

    @count.setter
    def count(self, i: ctypes.c_uint) -> None:
        self.count = i

    @property
    def paths(self) -> ctypes.POINTER(ctypes.POINTER(ctypes.c_char)):
        return self.paths

    @paths.setter
    def paths(self, i: ctypes.POINTER(ctypes.POINTER(ctypes.c_char))) -> None:
        self.paths = i


class float3(ctypes.Structure):
    """NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
    _fields_ = [
        ('v', ctypes.c_float * 3)  # 
    ]

    @property
    def v(self) -> ctypes.c_float * 3:
        return self.v

    @v.setter
    def v(self, i: ctypes.c_float * 3) -> None:
        self.v = i


class float16(ctypes.Structure):
    """"""
    _fields_ = [
        ('v', ctypes.c_float * 16)  # 
    ]

    @property
    def v(self) -> ctypes.c_float * 16:
        return self.v

    @v.setter
    def v(self, i: ctypes.c_float * 16) -> None:
        self.v = i


class GuiStyleProp(ctypes.Structure):
    """Style property"""
    _fields_ = [
        ('controlId', ctypes.c_ushort),  # 
        ('propertyId', ctypes.c_ushort),  # 
        ('propertyValue', ctypes.c_uint)  # 
    ]

    @property
    def controlId(self) -> ctypes.c_ushort:
        return self.controlId

    @controlId.setter
    def controlId(self, i: ctypes.c_ushort) -> None:
        self.controlId = i

    @property
    def propertyId(self) -> ctypes.c_ushort:
        return self.propertyId

    @propertyId.setter
    def propertyId(self, i: ctypes.c_ushort) -> None:
        self.propertyId = i

    @property
    def propertyValue(self) -> ctypes.c_uint:
        return self.propertyValue

    @propertyValue.setter
    def propertyValue(self, i: ctypes.c_uint) -> None:
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
    "Wave": Wave,
    "AudioStream": AudioStream,
    "Sound": Sound,
    "Music": Music,
    "VrDeviceInfo": VrDeviceInfo,
    "VrStereoConfig": VrStereoConfig,
    "FilePathList": FilePathList,
    "float3": float3,
    "float16": float16,
    "GuiStyleProp": GuiStyleProp
}
