import ctypes
from raypyc.defines import *


class rAudioBuffer(ctypes.Structure):
	"""dummy structure"""
	_fields_ = [
		("buffer", ctypes.c_byte * 392)
	]


class rAudioProcessor(ctypes.Structure):
	"""dummy structure"""
	_fields_ = [
		("buffer", ctypes.c_byte * 24)
	]


class rlVertexBuffer(ctypes.Structure):
	"""Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""
	_fields_ = [
		('elementCount', ctypes.c_int),  # Number of elements in the buffer (QUADS)
		('vertices', ctypes.POINTER(ctypes.c_float)),  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
		('texcoords', ctypes.POINTER(ctypes.c_float)),  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
		('colors', ctypes.POINTER(ctypes.c_ubyte)),  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
		('vaoId', ctypes.c_uint),  # OpenGL Vertex Array Object id
		('vboId', ctypes.c_uint * 4)  # OpenGL Vertex Buffer Objects id (4 types of vertex data)
	]


class rlDrawCall(ctypes.Structure):
	"""of those state-change happens (this is done in core module)"""
	_fields_ = [
		('mode', ctypes.c_int),  # Drawing mode: LINES, TRIANGLES, QUADS
		('vertexCount', ctypes.c_int),  # Number of vertex of the draw
		('vertexAlignment', ctypes.c_int),  # Number of vertex required for index alignment (LINES, TRIANGLES)
		('textureId', ctypes.c_uint)  # Texture id to be used on the draw -> Use to create new draw call if changes
	]


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


class Vector2(ctypes.Structure):
	"""Vector2, 2 components"""
	_fields_ = [
		('x', ctypes.c_float),  # Vector x component
		('y', ctypes.c_float)  # Vector y component
	]


class Vector3(ctypes.Structure):
	"""Vector3, 3 components"""
	_fields_ = [
		('x', ctypes.c_float),  # Vector x component
		('y', ctypes.c_float),  # Vector y component
		('z', ctypes.c_float)  # Vector z component
	]


class Vector4(ctypes.Structure):
	"""Vector4, 4 components"""
	_fields_ = [
		('x', ctypes.c_float),  # Vector x component
		('y', ctypes.c_float),  # Vector y component
		('z', ctypes.c_float),  # Vector z component
		('w', ctypes.c_float)  # Vector w component
	]


Quaternion = Vector4


class Matrix(ctypes.Structure):
	"""Matrix, 4x4 components, column major, OpenGL style, right-handed"""
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


class Color(ctypes.Structure):
	"""Color, 4 components, R8G8B8A8 (32bit)"""
	_fields_ = [
		('r', ctypes.c_ubyte),  # Color red value
		('g', ctypes.c_ubyte),  # Color green value
		('b', ctypes.c_ubyte),  # Color blue value
		('a', ctypes.c_ubyte)  # Color alpha value
	]


class Rectangle(ctypes.Structure):
	"""Rectangle, 4 components"""
	_fields_ = [
		('x', ctypes.c_float),  # Rectangle top-left corner position x
		('y', ctypes.c_float),  # Rectangle top-left corner position y
		('width', ctypes.c_float),  # Rectangle width
		('height', ctypes.c_float)  # Rectangle height
	]


class Image(ctypes.Structure):
	"""Image, pixel data stored in CPU memory (RAM)"""
	_fields_ = [
		('data', ctypes.c_void_p),  # Image raw data
		('width', ctypes.c_int),  # Image base width
		('height', ctypes.c_int),  # Image base height
		('mipmaps', ctypes.c_int),  # Mipmap levels, 1 by default
		('format', ctypes.c_int)  # Data format (PixelFormat type)
	]


class Texture(ctypes.Structure):
	"""Texture, tex data stored in GPU memory (VRAM)"""
	_fields_ = [
		('id', ctypes.c_uint),  # OpenGL texture id
		('width', ctypes.c_int),  # Texture base width
		('height', ctypes.c_int),  # Texture base height
		('mipmaps', ctypes.c_int),  # Mipmap levels, 1 by default
		('format', ctypes.c_int)  # Data format (PixelFormat type)
	]


Texture2D = Texture


TextureCubemap = Texture


class RenderTexture(ctypes.Structure):
	"""RenderTexture, fbo for texture rendering"""
	_fields_ = [
		('id', ctypes.c_uint),  # OpenGL framebuffer object id
		('texture', Texture),  # Color buffer attachment texture
		('depth', Texture)  # Depth buffer attachment texture
	]


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


class GlyphInfo(ctypes.Structure):
	"""GlyphInfo, font characters glyphs info"""
	_fields_ = [
		('value', ctypes.c_int),  # Character value (Unicode)
		('offsetX', ctypes.c_int),  # Character offset X when drawing
		('offsetY', ctypes.c_int),  # Character offset Y when drawing
		('advanceX', ctypes.c_int),  # Character advance position X
		('image', Image)  # Character image data
	]


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


class Camera3D(ctypes.Structure):
	"""Camera, defines position/orientation in 3d space"""
	_fields_ = [
		('position', Vector3),  # Camera position
		('target', Vector3),  # Camera target it looks-at
		('up', Vector3),  # Camera up vector (rotation over its axis)
		('fovy', ctypes.c_float),  # Camera field-of-view aperture in Y (degrees) in perspective, used as near plane width in orthographic
		('projection', ctypes.c_int)  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
	]


Camera = Camera3D


class Camera2D(ctypes.Structure):
	"""Camera2D, defines position/orientation in 2d space"""
	_fields_ = [
		('offset', Vector2),  # Camera offset (displacement from target)
		('target', Vector2),  # Camera target (rotation and zoom origin)
		('rotation', ctypes.c_float),  # Camera rotation in degrees
		('zoom', ctypes.c_float),  # Camera zoom (scaling) should be 1.0f by default
	]


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


class Shader(ctypes.Structure):
	"""Shader"""
	_fields_ = [
		('id', ctypes.c_uint),  # Shader program id
		('locs', ctypes.POINTER(ctypes.c_int))  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
	]


class MaterialMap(ctypes.Structure):
	"""MaterialMap"""
	_fields_ = [
		('texture', Texture2D),  # Material map texture
		('color', Color),  # Material map color
		('value', ctypes.c_float)  # Material map value
	]


class Material(ctypes.Structure):
	"""Material, includes shader and maps"""
	_fields_ = [
		('shader', Shader),  # Material shader
		('maps', ctypes.POINTER(MaterialMap)),  # Material maps array (MAX_MATERIAL_MAPS)
		('params', ctypes.c_float * 4)  # Material generic parameters (if required)
	]


class Transform(ctypes.Structure):
	"""Transform, vertex transformation data"""
	_fields_ = [
		('translation', Vector3),  # Translation
		('rotation', Quaternion),  # Rotation
		('scale', Vector3)  # Scale
	]


class BoneInfo(ctypes.Structure):
	"""Bone, skeletal animation bone"""
	_fields_ = [
		('name', ctypes.c_char * 32),  # Bone name
		('parent', ctypes.c_int)  # Bone parent
	]


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


class ModelAnimation(ctypes.Structure):
	"""ModelAnimation"""
	_fields_ = [
		('boneCount', ctypes.c_int),  # Number of bones
		('frameCount', ctypes.c_int),  # Number of animation frames
		('bones', ctypes.POINTER(BoneInfo)),  # Bones information (skeleton)
		('framePoses', ctypes.POINTER(ctypes.POINTER(Transform)))  # Poses array by frame
	]


class Ray(ctypes.Structure):
	"""Ray, ray for raycasting"""
	_fields_ = [
		('position', Vector3),  # Ray position (origin)
		('direction', Vector3)  # Ray direction
	]


class RayCollision(ctypes.Structure):
	"""RayCollision, ray hit information"""
	_fields_ = [
		('hit', ctypes.c_bool),  # Did the ray hit something?
		('distance', ctypes.c_float),  # Distance to the nearest hit
		('point', Vector3),  # Point of the nearest hit
		('normal', Vector3)  # Surface normal of hit
	]


class BoundingBox(ctypes.Structure):
	"""BoundingBox"""
	_fields_ = [
		('min', Vector3),  # Minimum vertex box-corner
		('max', Vector3)  # Maximum vertex box-corner
	]


class Wave(ctypes.Structure):
	"""Wave, audio wave data"""
	_fields_ = [
		('frameCount', ctypes.c_uint),  # Total number of frames (considering channels)
		('sampleRate', ctypes.c_uint),  # Frequency (samples per second)
		('sampleSize', ctypes.c_uint),  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
		('channels', ctypes.c_uint),  # Number of channels (1-mono, 2-stereo, ...)
		('data', ctypes.c_void_p)  # Buffer data pointer
	]


class AudioStream(ctypes.Structure):
	"""AudioStream, custom audio stream"""
	_fields_ = [
		('buffer', ctypes.POINTER(rAudioBuffer)),  # Pointer to internal data used by the audio system
		('processor', ctypes.POINTER(rAudioProcessor)),  # Pointer to internal data processor, useful for audio effects
		('sampleRate', ctypes.c_uint),  # Frequency (samples per second)
		('sampleSize', ctypes.c_uint),  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
		('channels', ctypes.c_uint),  # Number of channels (1-mono, 2-stereo ...)
	]


class Sound(ctypes.Structure):
	"""Sound"""
	_fields_ = [
		('stream', AudioStream),  # Audio stream
		('frameCount', ctypes.c_uint)  # Total number of frames (considering channels)
	]


class Music(ctypes.Structure):
	"""Music, audio stream, anything longer than ~10 seconds should be streamed"""
	_fields_ = [
		('stream', AudioStream),  # Audio stream
		('frameCount', ctypes.c_uint),  # Total number of frames (considering channels)
		('looping', ctypes.c_bool),  # Music looping enable
		('ctxType', ctypes.c_int),  # Type of music context (audio filetype)
		('ctxData', ctypes.c_void_p),  # Audio context data depends on type
	]


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


class FilePathList(ctypes.Structure):
	"""File path list"""
	_fields_ = [
		('capacity', ctypes.c_uint),  # Filepaths max entries
		('count', ctypes.c_uint),  # Filepaths entries count
		('paths', ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))  # Filepaths entries
	]


class float3(ctypes.Structure):
	"""NOTE: Helper types to be used instead of array return types for *ToFloat functions"""
	_fields_ = [
		('v', ctypes.c_float * 3)
	]


class float16(ctypes.Structure):
	""""""
	_fields_ = [
		('v', ctypes.c_float * 16)
	]


class GuiStyleProp(ctypes.Structure):
	"""Style property"""
	_fields_ = [
		('controlId', ctypes.c_ushort),
		('propertyId', ctypes.c_ushort),
		('propertyValue', ctypes.c_uint)
	]


__structs = {
	"rlVertexBuffer": rlVertexBuffer,
	"rlDrawCall": rlDrawCall,
	"rlRenderBatch": rlRenderBatch,
	"Vector2": Vector2,
	"Vector3": Vector3,
	"Vector4": Vector4,
	"Quaternion": Quaternion,
	"Matrix": Matrix,
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
