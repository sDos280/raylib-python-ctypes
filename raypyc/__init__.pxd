cdef extern from "config.h":
	DEF SUPPORT_MODULE_RSHAPES = 1
	DEF SUPPORT_MODULE_RTEXTURES = 1
	DEF SUPPORT_MODULE_RTEXT = 1  # WARNING: It requires SUPPORT_MODULE_RTEXTURES to load sprite font textures
	DEF SUPPORT_MODULE_RMODELS = 1
	DEF SUPPORT_MODULE_RAUDIO = 1
	DEF SUPPORT_CAMERA_SYSTEM = 1
	DEF SUPPORT_GESTURES_SYSTEM = 1
	DEF SUPPORT_MOUSE_GESTURES = 1
	DEF SUPPORT_SSH_KEYBOARD_RPI = 1
	DEF SUPPORT_WINMM_HIGHRES_TIMER = 1
	DEF SUPPORT_SCREEN_CAPTURE = 1
	DEF SUPPORT_GIF_RECORDING = 1
	DEF SUPPORT_COMPRESSION_API = 1
	DEF MAX_FILEPATH_CAPACITY = 8192  # Maximum file paths capacity
	DEF MAX_FILEPATH_LENGTH = 4096  # Maximum length for filepaths (Linux PATH_MAX default value)
	DEF MAX_KEYBOARD_KEYS = 512  # Maximum number of keyboard keys supported
	DEF MAX_MOUSE_BUTTONS = 8  # Maximum number of mouse buttons supported
	DEF MAX_GAMEPADS = 4  # Maximum number of gamepads supported
	DEF MAX_GAMEPAD_AXIS = 8  # Maximum number of axis supported (per gamepad)
	DEF MAX_GAMEPAD_BUTTONS = 32  # Maximum number of buttons supported (per gamepad)
	DEF MAX_TOUCH_POINTS = 8  # Maximum number of touch points supported
	DEF MAX_KEY_PRESSED_QUEUE = 16  # Maximum number of keys in the key input queue
	DEF MAX_CHAR_PRESSED_QUEUE = 16  # Maximum number of characters in the char input queue
	DEF MAX_DECOMPRESSION_SIZE = 64  # Max size allocated for decompression in MB
	DEF RL_DEFAULT_BATCH_BUFFERS = 1  # Default number of batch buffers (multi-buffering)
	DEF RL_DEFAULT_BATCH_DRAWCALLS = 256  # Default number of batch draw calls (by state changes: mode, texture)
	DEF RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS = 4  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
	DEF RL_MAX_MATRIX_STACK_SIZE = 32  # Maximum size of internal Matrix stack
	DEF RL_MAX_SHADER_LOCATIONS = 32  # Maximum number of shader locations supported
	DEF RL_CULL_DISTANCE_NEAR = 0.01  # Default projection matrix near cull distance
	DEF RL_CULL_DISTANCE_FAR = 1000.0  # Default projection matrix far cull distance
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION = "vertexPosition"  # Binded by default to shader location: 0
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD = "vertexTexCoord"  # Binded by default to shader location: 1
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL = "vertexNormal"  # Binded by default to shader location: 2
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR = "vertexColor"  # Binded by default to shader location: 3
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT = "vertexTangent"  # Binded by default to shader location: 4
	DEF RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2 = "vertexTexCoord2"  # Binded by default to shader location: 5
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_MVP = "mvp"  # model-view-projection matrix
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW = "matView"  # view matrix
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION = "matProjection"  # projection matrix
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL = "matModel"  # model matrix
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL = "matNormal"  # normal matrix (transpose(inverse(matModelView))
	DEF RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR = "colDiffuse"  # color diffuse (base tint color, multiplied by texture color)
	DEF RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0 = "texture0"  # texture0 (texture slot active 0)
	DEF RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1 = "texture1"  # texture1 (texture slot active 1)
	DEF RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2 = "texture2"  # texture2 (texture slot active 2)
	DEF SUPPORT_QUADS_DRAW_MODE = 1
	DEF SUPPORT_FILEFORMAT_PNG = 1
	DEF SUPPORT_FILEFORMAT_GIF = 1
	DEF SUPPORT_FILEFORMAT_QOI = 1
	DEF SUPPORT_FILEFORMAT_DDS = 1
	DEF SUPPORT_FILEFORMAT_HDR = 1
	DEF SUPPORT_IMAGE_EXPORT = 1
	DEF SUPPORT_IMAGE_GENERATION = 1
	DEF SUPPORT_IMAGE_MANIPULATION = 1
	DEF SUPPORT_DEFAULT_FONT = 1
	DEF SUPPORT_FILEFORMAT_FNT = 1
	DEF SUPPORT_FILEFORMAT_TTF = 1
	DEF SUPPORT_TEXT_MANIPULATION = 1
	DEF MAX_TEXT_BUFFER_LENGTH = 1024  # Size of internal static buffers used on some functions:
	DEF MAX_TEXTSPLIT_COUNT = 128  # Maximum number of substrings to split: TextSplit()
	DEF SUPPORT_FILEFORMAT_OBJ = 1
	DEF SUPPORT_FILEFORMAT_MTL = 1
	DEF SUPPORT_FILEFORMAT_IQM = 1
	DEF SUPPORT_FILEFORMAT_GLTF = 1
	DEF SUPPORT_FILEFORMAT_VOX = 1
	DEF SUPPORT_MESH_GENERATION = 1
	DEF MAX_MATERIAL_MAPS = 12  # Maximum number of shader maps supported
	DEF MAX_MESH_VERTEX_BUFFERS = 7  # Maximum vertex buffers (VBO) per mesh
	DEF SUPPORT_FILEFORMAT_WAV = 1
	DEF SUPPORT_FILEFORMAT_OGG = 1
	DEF SUPPORT_FILEFORMAT_XM = 1
	DEF SUPPORT_FILEFORMAT_MOD = 1
	DEF SUPPORT_FILEFORMAT_MP3 = 1
	DEF AUDIO_DEVICE_CHANNELS = 2  # Device output channels: stereo
	DEF AUDIO_DEVICE_SAMPLE_RATE = 0  # Device sample rate (device default)
	DEF MAX_AUDIO_BUFFER_POOL_CHANNELS = 16  # Maximum number of audio pool channels
	DEF SUPPORT_TRACELOG = 1
	DEF MAX_TRACELOG_MSG_LENGTH = 128  # Max length of one trace-log message
	
	
	#  dummy structure
	ctypedef struct rAudioBuffer:
		signed char[392] data;
	
	
	#  dummy structure
	ctypedef struct rAudioProcessor:
		signed char[24] data;
	
	
	
	
	
cdef extern from "rlgl.h":
	DEF RLGL_VERSION = "4.0"
	DEF RL_DEFAULT_BATCH_BUFFER_ELEMENTS = 8192
	DEF RL_TEXTURE_WRAP_S = 10242  # GL_TEXTURE_WRAP_S
	DEF RL_TEXTURE_WRAP_T = 10243  # GL_TEXTURE_WRAP_T
	DEF RL_TEXTURE_MAG_FILTER = 10240  # GL_TEXTURE_MAG_FILTER
	DEF RL_TEXTURE_MIN_FILTER = 10241  # GL_TEXTURE_MIN_FILTER
	DEF RL_TEXTURE_FILTER_NEAREST = 9728  # GL_NEAREST
	DEF RL_TEXTURE_FILTER_LINEAR = 9729  # GL_LINEAR
	DEF RL_TEXTURE_FILTER_MIP_NEAREST = 9984  # GL_NEAREST_MIPMAP_NEAREST
	DEF RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR = 9986  # GL_NEAREST_MIPMAP_LINEAR
	DEF RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST = 9985  # GL_LINEAR_MIPMAP_NEAREST
	DEF RL_TEXTURE_FILTER_MIP_LINEAR = 9987  # GL_LINEAR_MIPMAP_LINEAR
	DEF RL_TEXTURE_FILTER_ANISOTROPIC = 12288  # Anisotropic filter (custom identifier)
	DEF RL_TEXTURE_WRAP_REPEAT = 10497  # GL_REPEAT
	DEF RL_TEXTURE_WRAP_CLAMP = 33071  # GL_CLAMP_TO_EDGE
	DEF RL_TEXTURE_WRAP_MIRROR_REPEAT = 33648  # GL_MIRRORED_REPEAT
	DEF RL_TEXTURE_WRAP_MIRROR_CLAMP = 34626  # GL_MIRROR_CLAMP_EXT
	DEF RL_MODELVIEW = 5888  # GL_MODELVIEW
	DEF RL_PROJECTION = 5889  # GL_PROJECTION
	DEF RL_TEXTURE = 5890  # GL_TEXTURE
	DEF RL_LINES = 1  # GL_LINES
	DEF RL_TRIANGLES = 4  # GL_TRIANGLES
	DEF RL_QUADS = 7  # GL_QUADS
	DEF RL_UNSIGNED_BYTE = 5121  # GL_UNSIGNED_BYTE
	DEF RL_FLOAT = 5126  # GL_FLOAT
	DEF RL_STREAM_DRAW = 35040  # GL_STREAM_DRAW
	DEF RL_STREAM_READ = 35041  # GL_STREAM_READ
	DEF RL_STREAM_COPY = 35042  # GL_STREAM_COPY
	DEF RL_STATIC_DRAW = 35044  # GL_STATIC_DRAW
	DEF RL_STATIC_READ = 35045  # GL_STATIC_READ
	DEF RL_STATIC_COPY = 35046  # GL_STATIC_COPY
	DEF RL_DYNAMIC_DRAW = 35048  # GL_DYNAMIC_DRAW
	DEF RL_DYNAMIC_READ = 35049  # GL_DYNAMIC_READ
	DEF RL_DYNAMIC_COPY = 35050  # GL_DYNAMIC_COPY
	DEF RL_FRAGMENT_SHADER = 35632  # GL_FRAGMENT_SHADER
	DEF RL_VERTEX_SHADER = 35633  # GL_VERTEX_SHADER
	DEF RL_COMPUTE_SHADER = 37305  # GL_COMPUTE_SHADER
	DEF PI = 3.141592653589793
	DEF DEG2RAD = (PI/180.0)
	DEF RAD2DEG = (180.0/PI)
	DEF GL_SHADING_LANGUAGE_VERSION = 35724
	DEF GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 33776
	DEF GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777
	DEF GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778
	DEF GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779
	DEF GL_ETC1_RGB8_OES = 36196
	DEF GL_COMPRESSED_RGB8_ETC2 = 37492
	DEF GL_COMPRESSED_RGBA8_ETC2_EAC = 37496
	DEF GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 35840
	DEF GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 35842
	DEF GL_COMPRESSED_RGBA_ASTC_4x4_KHR = 37808
	DEF GL_COMPRESSED_RGBA_ASTC_8x8_KHR = 37815
	DEF GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047
	DEF GL_TEXTURE_MAX_ANISOTROPY_EXT = 34046
	DEF GL_UNSIGNED_SHORT_5_6_5 = 33635
	DEF GL_UNSIGNED_SHORT_5_5_5_1 = 32820
	DEF GL_UNSIGNED_SHORT_4_4_4_4 = 32819
	DEF GL_LUMINANCE = 6409
	DEF GL_LUMINANCE_ALPHA = 6410
	
	ctypedef enum rlGlVersion:
		OPENGL_11 = 1,
		OPENGL_21 = 2,
		OPENGL_33 = 3,
		OPENGL_43 = 4,
		OPENGL_ES_20 = 5
	
	
	ctypedef enum rlFramebufferAttachType:
		RL_ATTACHMENT_COLOR_CHANNEL0 = 0,
		RL_ATTACHMENT_COLOR_CHANNEL1 = 1,
		RL_ATTACHMENT_COLOR_CHANNEL2 = 2,
		RL_ATTACHMENT_COLOR_CHANNEL3 = 3,
		RL_ATTACHMENT_COLOR_CHANNEL4 = 4,
		RL_ATTACHMENT_COLOR_CHANNEL5 = 5,
		RL_ATTACHMENT_COLOR_CHANNEL6 = 6,
		RL_ATTACHMENT_COLOR_CHANNEL7 = 7,
		RL_ATTACHMENT_DEPTH = 100,
		RL_ATTACHMENT_STENCIL = 200
	
	
	ctypedef enum rlFramebufferAttachTextureType:
		RL_ATTACHMENT_CUBEMAP_POSITIVE_X = 0,
		RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = 1,
		RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = 2,
		RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = 3,
		RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = 4,
		RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = 5,
		RL_ATTACHMENT_TEXTURE2D = 100,
		RL_ATTACHMENT_RENDERBUFFER = 200
	
	
	#  Trace log level
	ctypedef enum rlTraceLogLevel:
		RL_LOG_ALL = 0,  #  Display all logs
		RL_LOG_TRACE = 1,  #  Trace logging, intended for internal use only
		RL_LOG_DEBUG = 2,  #  Debug logging, used for internal debugging, it should be disabled on release builds
		RL_LOG_INFO = 3,  #  Info logging, used for program execution info
		RL_LOG_WARNING = 4,  #  Warning logging, used on recoverable failures
		RL_LOG_ERROR = 5,  #  Error logging, used on unrecoverable failures
		RL_LOG_FATAL = 6,  #  Fatal logging, used to abort program: exit(EXIT_FAILURE)
		RL_LOG_NONE = 7  #  Disable logging
	
	
	#  Texture formats (support depends on OpenGL version)
	ctypedef enum rlPixelFormat:
		RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1,  #  8 bit per pixel (no alpha)
		RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2,  #  8*2 bpp (2 channels)
		RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3,  #  16 bpp
		RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4,  #  24 bpp
		RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5,  #  16 bpp (1 bit alpha)
		RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6,  #  16 bpp (4 bit alpha)
		RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7,  #  32 bpp
		RL_PIXELFORMAT_UNCOMPRESSED_R32 = 8,  #  32 bpp (1 channel - float)
		RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9,  #  32*3 bpp (3 channels - float)
		RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10,  #  32*4 bpp (4 channels - float)
		RL_PIXELFORMAT_COMPRESSED_DXT1_RGB = 11,  #  4 bpp (no alpha)
		RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12,  #  4 bpp (1 bit alpha)
		RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13,  #  8 bpp
		RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14,  #  8 bpp
		RL_PIXELFORMAT_COMPRESSED_ETC1_RGB = 15,  #  4 bpp
		RL_PIXELFORMAT_COMPRESSED_ETC2_RGB = 16,  #  4 bpp
		RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17,  #  8 bpp
		RL_PIXELFORMAT_COMPRESSED_PVRT_RGB = 18,  #  4 bpp
		RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19,  #  4 bpp
		RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20,  #  8 bpp
		RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21  #  2 bpp
	
	
	#  Texture parameters: filter mode
	ctypedef enum rlTextureFilter:
		RL_TEXTURE_FILTER_POINT = 0,  #  No filter, just pixel approximation
		RL_TEXTURE_FILTER_BILINEAR = 1,  #  Linear filtering
		RL_TEXTURE_FILTER_TRILINEAR = 2,  #  Trilinear filtering (linear with mipmaps)
		RL_TEXTURE_FILTER_ANISOTROPIC_4X = 3,  #  Anisotropic filtering 4x
		RL_TEXTURE_FILTER_ANISOTROPIC_8X = 4,  #  Anisotropic filtering 8x
		RL_TEXTURE_FILTER_ANISOTROPIC_16X = 5  #  Anisotropic filtering 16x
	
	
	#  Color blending modes (pre-defined)
	ctypedef enum rlBlendMode:
		RL_BLEND_ALPHA = 0,  #  Blend textures considering alpha (default)
		RL_BLEND_ADDITIVE = 1,  #  Blend textures adding colors
		RL_BLEND_MULTIPLIED = 2,  #  Blend textures multiplying colors
		RL_BLEND_ADD_COLORS = 3,  #  Blend textures adding colors (alternative)
		RL_BLEND_SUBTRACT_COLORS = 4,  #  Blend textures subtracting colors (alternative)
		RL_BLEND_ALPHA_PREMULTIPLY = 5,  #  Blend premultiplied textures considering alpha
		RL_BLEND_CUSTOM = 6  #  Blend textures using custom src/dst factors (use rlSetBlendFactors())
	
	
	#  Shader location point type
	ctypedef enum rlShaderLocationIndex:
		RL_SHADER_LOC_VERTEX_POSITION = 0,  #  Shader location: vertex attribute: position
		RL_SHADER_LOC_VERTEX_TEXCOORD01 = 1,  #  Shader location: vertex attribute: texcoord01
		RL_SHADER_LOC_VERTEX_TEXCOORD02 = 2,  #  Shader location: vertex attribute: texcoord02
		RL_SHADER_LOC_VERTEX_NORMAL = 3,  #  Shader location: vertex attribute: normal
		RL_SHADER_LOC_VERTEX_TANGENT = 4,  #  Shader location: vertex attribute: tangent
		RL_SHADER_LOC_VERTEX_COLOR = 5,  #  Shader location: vertex attribute: color
		RL_SHADER_LOC_MATRIX_MVP = 6,  #  Shader location: matrix uniform: model-view-projection
		RL_SHADER_LOC_MATRIX_VIEW = 7,  #  Shader location: matrix uniform: view (camera transform)
		RL_SHADER_LOC_MATRIX_PROJECTION = 8,  #  Shader location: matrix uniform: projection
		RL_SHADER_LOC_MATRIX_MODEL = 9,  #  Shader location: matrix uniform: model (transform)
		RL_SHADER_LOC_MATRIX_NORMAL = 10,  #  Shader location: matrix uniform: normal
		RL_SHADER_LOC_VECTOR_VIEW = 11,  #  Shader location: vector uniform: view
		RL_SHADER_LOC_COLOR_DIFFUSE = 12,  #  Shader location: vector uniform: diffuse color
		RL_SHADER_LOC_COLOR_SPECULAR = 13,  #  Shader location: vector uniform: specular color
		RL_SHADER_LOC_COLOR_AMBIENT = 14,  #  Shader location: vector uniform: ambient color
		RL_SHADER_LOC_MAP_ALBEDO = 15,  #  Shader location: sampler2d texture: albedo (same as: RL_SHADER_LOC_MAP_DIFFUSE)
		RL_SHADER_LOC_MAP_METALNESS = 16,  #  Shader location: sampler2d texture: metalness (same as: RL_SHADER_LOC_MAP_SPECULAR)
		RL_SHADER_LOC_MAP_NORMAL = 17,  #  Shader location: sampler2d texture: normal
		RL_SHADER_LOC_MAP_ROUGHNESS = 18,  #  Shader location: sampler2d texture: roughness
		RL_SHADER_LOC_MAP_OCCLUSION = 19,  #  Shader location: sampler2d texture: occlusion
		RL_SHADER_LOC_MAP_EMISSION = 20,  #  Shader location: sampler2d texture: emission
		RL_SHADER_LOC_MAP_HEIGHT = 21,  #  Shader location: sampler2d texture: height
		RL_SHADER_LOC_MAP_CUBEMAP = 22,  #  Shader location: samplerCube texture: cubemap
		RL_SHADER_LOC_MAP_IRRADIANCE = 23,  #  Shader location: samplerCube texture: irradiance
		RL_SHADER_LOC_MAP_PREFILTER = 24,  #  Shader location: samplerCube texture: prefilter
		RL_SHADER_LOC_MAP_BRDF = 25  #  Shader location: sampler2d texture: brdf
	
	
	#  Shader uniform data type
	ctypedef enum rlShaderUniformDataType:
		RL_SHADER_UNIFORM_FLOAT = 0,  #  Shader uniform type: float
		RL_SHADER_UNIFORM_VEC2 = 1,  #  Shader uniform type: vec2 (2 float)
		RL_SHADER_UNIFORM_VEC3 = 2,  #  Shader uniform type: vec3 (3 float)
		RL_SHADER_UNIFORM_VEC4 = 3,  #  Shader uniform type: vec4 (4 float)
		RL_SHADER_UNIFORM_INT = 4,  #  Shader uniform type: int
		RL_SHADER_UNIFORM_IVEC2 = 5,  #  Shader uniform type: ivec2 (2 int)
		RL_SHADER_UNIFORM_IVEC3 = 6,  #  Shader uniform type: ivec3 (3 int)
		RL_SHADER_UNIFORM_IVEC4 = 7,  #  Shader uniform type: ivec4 (4 int)
		RL_SHADER_UNIFORM_SAMPLER2D = 8  #  Shader uniform type: sampler2d
	
	
	#  Shader attribute data types
	ctypedef enum rlShaderAttributeDataType:
		RL_SHADER_ATTRIB_FLOAT = 0,  #  Shader attribute type: float
		RL_SHADER_ATTRIB_VEC2 = 1,  #  Shader attribute type: vec2 (2 float)
		RL_SHADER_ATTRIB_VEC3 = 2,  #  Shader attribute type: vec3 (3 float)
		RL_SHADER_ATTRIB_VEC4 = 3  #  Shader attribute type: vec4 (4 float)
	
	
	
	#  Dynamic vertex buffers (position + texcoords + colors + indices arrays)
	ctypedef struct rlVertexBuffer:
		int elementCount;  # Number of elements in the buffer (QUADS)
		float * vertices;  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
		float * texcoords;  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
		unsigned char * colors;  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
		unsigned int * indices;  # Vertex indices (in case vertex data comes indexed) (6 indices per quad)
		unsigned int vaoId;  # OpenGL Vertex Array Object id
		unsigned int[4] vboId;  # OpenGL Vertex Buffer Objects id (4 types of vertex data)
	
	#  of those state-change happens (this is done in core module)
	ctypedef struct rlDrawCall:
		int mode;  # Drawing mode: LINES, TRIANGLES, QUADS
		int vertexCount;  # Number of vertex of the draw
		int vertexAlignment;  # Number of vertex required for index alignment (LINES, TRIANGLES)
		unsigned int textureId;  # Texture id to be used on the draw -> Use to create new draw call if changes
	
	#  rlRenderBatch type
	ctypedef struct rlRenderBatch:
		int bufferCount;  # Number of vertex buffers (multi-buffering support)
		int currentBuffer;  # Current buffer tracking in case of multi-buffering
		rlVertexBuffer * vertexBuffer;  # Dynamic buffer(s) for vertex data
		rlDrawCall * draws;  # Draw calls array, depends on textureId
		int drawCounter;  # Draw calls counter
		float currentDepth;  # Current depth value for next draw
	
	#  Matrix, 4x4 components, column major, OpenGL style, right handed
	ctypedef struct Matrix:
		float m0;  # Matrix first row (4 components)
		float m4;  # Matrix first row (4 components)
		float m8;  # Matrix first row (4 components)
		float m12;  # Matrix first row (4 components)
		float m1;  # Matrix second row (4 components)
		float m5;  # Matrix second row (4 components)
		float m9;  # Matrix second row (4 components)
		float m13;  # Matrix second row (4 components)
		float m2;  # Matrix third row (4 components)
		float m6;  # Matrix third row (4 components)
		float m10;  # Matrix third row (4 components)
		float m14;  # Matrix third row (4 components)
		float m3;  # Matrix fourth row (4 components)
		float m7;  # Matrix fourth row (4 components)
		float m11;  # Matrix fourth row (4 components)
		float m15;  # Matrix fourth row (4 components)
	
	#  
	ctypedef struct rlglData:
		rlRenderBatch * currentBatch;  # Current render batch
		rlRenderBatch defaultBatch;  # Default internal render batch
		int vertexCounter;  # Current active render batch vertex counter (generic, used for all batches)
		float texcoordx;  # Current active texture coordinate (added on glVertex*())
		float texcoordy;  # Current active texture coordinate (added on glVertex*())
		float normalx;  # Current active normal (added on glVertex*())
		float normaly;  # Current active normal (added on glVertex*())
		float normalz;  # Current active normal (added on glVertex*())
		unsigned char colorr;  # Current active color (added on glVertex*())
		unsigned char colorg;  # Current active color (added on glVertex*())
		unsigned char colorb;  # Current active color (added on glVertex*())
		unsigned char colora;  # Current active color (added on glVertex*())
		int currentMatrixMode;  # Current matrix mode
		Matrix * currentMatrix;  # Current matrix pointer
		Matrix modelview;  # Default modelview matrix
		Matrix projection;  # Default projection matrix
		Matrix transform;  # Transform matrix to be used with rlTranslate, rlRotate, rlScale
		bint transformRequired;  # Require transform matrix application to current draw-call vertex (if required)
		Matrix[RL_MAX_MATRIX_STACK_SIZE] stack;  # Matrix stack for push/pop
		int stackCounter;  # Matrix stack counter
		unsigned int defaultTextureId;  # Default texture used on shapes/poly drawing (required by shader)
		unsigned int[RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS] activeTextureId;  # Active texture ids to be enabled on batch drawing (0 active by default)
		unsigned int defaultVShaderId;  # Default vertex shader id (used by default shader program)
		unsigned int defaultFShaderId;  # Default fragment shader id (used by default shader program)
		unsigned int defaultShaderId;  # Default shader program id, supports vertex color and diffuse texture
		int * defaultShaderLocs;  # Default shader locations pointer to be used on rendering
		unsigned int currentShaderId;  # Current shader id to be used on rendering (by default, defaultShaderId)
		int * currentShaderLocs;  # Current shader locations pointer to be used on rendering (by default, defaultShaderLocs)
		bint stereoRender;  # Stereo rendering flag
		Matrix[2] projectionStereo;  # VR stereo rendering eyes projection matrices
		Matrix[2] viewOffsetStereo;  # VR stereo rendering eyes view offset matrices
		int currentBlendMode;  # Blending mode active
		int glBlendSrcFactor;  # Blending source factor
		int glBlendDstFactor;  # Blending destination factor
		int glBlendEquation;  # Blending equation
		int framebufferWidth;  # Current framebuffer width
		int framebufferHeight;  # Current framebuffer height
	
	
	void rlMatrixMode(int mode);  # Choose the current matrix to be transformed
	void rlPushMatrix();  # Push the current matrix to stack
	void rlPopMatrix();  # Pop lattest inserted matrix from stack
	void rlLoadIdentity();  # Reset current matrix to identity matrix
	void rlTranslatef(float x, float y, float z);  # Multiply the current matrix by a translation matrix
	void rlRotatef(float angle, float x, float y, float z);  # Multiply the current matrix by a rotation matrix
	void rlScalef(float x, float y, float z);  # Multiply the current matrix by a scaling matrix
	void rlMultMatrixf(float * matf);  # Multiply the current matrix by another matrix
	void rlFrustum(double left, double right, double bottom, double top, double znear, double zfar);
	void rlOrtho(double left, double right, double bottom, double top, double znear, double zfar);
	void rlViewport(int x, int y, int width, int height);  # Set the viewport area
	void rlBegin(int mode);  # Initialize drawing mode (how to organize vertex)
	void rlEnd();  # Finish vertex providing
	void rlVertex2i(int x, int y);  # Define one vertex (position) - 2 int
	void rlVertex2f(float x, float y);  # Define one vertex (position) - 2 float
	void rlVertex3f(float x, float y, float z);  # Define one vertex (position) - 3 float
	void rlTexCoord2f(float x, float y);  # Define one vertex (texture coordinate) - 2 float
	void rlNormal3f(float x, float y, float z);  # Define one vertex (normal) - 3 float
	void rlColor4ub(unsigned char r, unsigned char g, unsigned char b, unsigned char a);  # Define one vertex (color) - 4 byte
	void rlColor3f(float x, float y, float z);  # Define one vertex (color) - 3 float
	void rlColor4f(float x, float y, float z, float w);  # Define one vertex (color) - 4 float
	bint rlEnableVertexArray(unsigned int vaoId);  # Enable vertex array (VAO, if supported)
	void rlDisableVertexArray();  # Disable vertex array (VAO, if supported)
	void rlEnableVertexBuffer(unsigned int id);  # Enable vertex buffer (VBO)
	void rlDisableVertexBuffer();  # Disable vertex buffer (VBO)
	void rlEnableVertexBufferElement(unsigned int id);  # Enable vertex buffer element (VBO element)
	void rlDisableVertexBufferElement();  # Disable vertex buffer element (VBO element)
	void rlEnableVertexAttribute(unsigned int index);  # Enable vertex attribute index
	void rlDisableVertexAttribute(unsigned int index);  # Disable vertex attribute index
	void rlActiveTextureSlot(int slot);  # Select and active a texture slot
	void rlEnableTexture(unsigned int id);  # Enable texture
	void rlDisableTexture();  # Disable texture
	void rlEnableTextureCubemap(unsigned int id);  # Enable texture cubemap
	void rlDisableTextureCubemap();  # Disable texture cubemap
	void rlTextureParameters(unsigned int id, int param, int value);  # Set texture parameters (filter, wrap)
	void rlEnableShader(unsigned int id);  # Enable shader program
	void rlDisableShader();  # Disable shader program
	void rlEnableFramebuffer(unsigned int id);  # Enable render texture (fbo)
	void rlDisableFramebuffer();  # Disable render texture (fbo), return to default framebuffer
	void rlActiveDrawBuffers(int count);  # Activate multiple draw color buffers
	void rlEnableColorBlend();  # Enable color blending
	void rlDisableColorBlend();  # Disable color blending
	void rlEnableDepthTest();  # Enable depth test
	void rlDisableDepthTest();  # Disable depth test
	void rlEnableDepthMask();  # Enable depth write
	void rlDisableDepthMask();  # Disable depth write
	void rlEnableBackfaceCulling();  # Enable backface culling
	void rlDisableBackfaceCulling();  # Disable backface culling
	void rlEnableScissorTest();  # Enable scissor test
	void rlDisableScissorTest();  # Disable scissor test
	void rlScissor(int x, int y, int width, int height);  # Scissor test
	void rlEnableWireMode();  # Enable wire mode
	void rlDisableWireMode();  # Disable wire mode
	void rlSetLineWidth(float width);  # Set the line drawing width
	float rlGetLineWidth();  # Get the line drawing width
	void rlEnableSmoothLines();  # Enable line aliasing
	void rlDisableSmoothLines();  # Disable line aliasing
	void rlEnableStereoRender();  # Enable stereo rendering
	void rlDisableStereoRender();  # Disable stereo rendering
	bint rlIsStereoRenderEnabled();  # Check if stereo render is enabled
	void rlClearColor(unsigned char r, unsigned char g, unsigned char b, unsigned char a);  # Clear color buffer with color
	void rlClearScreenBuffers();  # Clear used screen buffers (color and depth)
	void rlCheckErrors();  # Check and log OpenGL error codes
	void rlSetBlendMode(int mode);  # Set blending mode
	void rlSetBlendFactors(int glSrcFactor, int glDstFactor, int glEquation);  # Set blending mode factor and equation (using OpenGL factors)
	void rlglInit(int width, int height);  # Initialize rlgl (buffers, shaders, textures, states)
	void rlglClose();  # De-inititialize rlgl (buffers, shaders, textures)
	void rlLoadExtensions(void * loader);  # Load OpenGL extensions (loader function required)
	int rlGetVersion();  # Get current OpenGL version
	void rlSetFramebufferWidth(int width);  # Set current framebuffer width
	int rlGetFramebufferWidth();  # Get default framebuffer width
	void rlSetFramebufferHeight(int height);  # Set current framebuffer height
	int rlGetFramebufferHeight();  # Get default framebuffer height
	unsigned int rlGetTextureIdDefault();  # Get default texture id
	unsigned int rlGetShaderIdDefault();  # Get default shader id
	int * rlGetShaderLocsDefault();  # Get default shader locations
	rlRenderBatch rlLoadRenderBatch(int numBuffers, int bufferElements);  # Load a render batch system
	void rlUnloadRenderBatch(rlRenderBatch batch);  # Unload render batch system
	void rlDrawRenderBatch(rlRenderBatch * batch);  # Draw render batch data (Update->Draw->Reset)
	void rlSetRenderBatchActive(rlRenderBatch * batch);  # Set the active render batch for rlgl (NULL for default internal)
	void rlDrawRenderBatchActive();  # Update and draw internal render batch
	bint rlCheckRenderBatchLimit(int vCount);  # Check internal buffer overflow for a given number of vertex
	void rlSetTexture(unsigned int id);  # Set current texture for render batch and check buffers limits
	unsigned int rlLoadVertexArray();  # Load vertex array (vao) if supported
	unsigned int rlLoadVertexBuffer(const void * buffer, int size, bint dynamic);  # Load a vertex buffer attribute
	unsigned int rlLoadVertexBufferElement(const void * buffer, int size, bint dynamic);  # Load a new attributes element buffer
	void rlUpdateVertexBuffer(unsigned int bufferId, const void * data, int dataSize, int offset);  # Update GPU buffer with new data
	void rlUpdateVertexBufferElements(unsigned int id, const void * data, int dataSize, int offset);  # Update vertex buffer elements with new data
	void rlUnloadVertexArray(unsigned int vaoId);
	void rlUnloadVertexBuffer(unsigned int vboId);
	void rlSetVertexAttribute(unsigned int index, int compSize, int type, bint normalized, int stride, const void * pointer);
	void rlSetVertexAttributeDivisor(unsigned int index, int divisor);
	void rlSetVertexAttributeDefault(int locIndex, const void * value, int attribType, int count);  # Set vertex attribute default value
	void rlDrawVertexArray(int offset, int count);
	void rlDrawVertexArrayElements(int offset, int count, const void * buffer);
	void rlDrawVertexArrayInstanced(int offset, int count, int instances);
	void rlDrawVertexArrayElementsInstanced(int offset, int count, const void * buffer, int instances);
	unsigned int rlLoadTexture(const void * data, int width, int height, int format, int mipmapCount);  # Load texture in GPU
	unsigned int rlLoadTextureDepth(int width, int height, bint useRenderBuffer);  # Load depth texture/renderbuffer (to be attached to fbo)
	unsigned int rlLoadTextureCubemap(const void * data, int size, int format);  # Load texture cubemap
	void rlUpdateTexture(unsigned int id, int offsetX, int offsetY, int width, int height, int format, const void * data);  # Update GPU texture with new data
	void rlGetGlTextureFormats(int format, unsigned int * glInternalFormat, unsigned int * glFormat, unsigned int * glType);  # Get OpenGL internal formats
	const char * rlGetPixelFormatName(unsigned int format);  # Get name string for pixel format
	void rlUnloadTexture(unsigned int id);  # Unload texture from GPU memory
	void rlGenTextureMipmaps(unsigned int id, int width, int height, int format, int * mipmaps);  # Generate mipmap data for selected texture
	void * rlReadTexturePixels(unsigned int id, int width, int height, int format);  # Read texture pixel data
	unsigned char * rlReadScreenPixels(int width, int height);  # Read screen pixel data (color buffer)
	unsigned int rlLoadFramebuffer(int width, int height);  # Load an empty framebuffer
	void rlFramebufferAttach(unsigned int fboId, unsigned int texId, int attachType, int texType, int mipLevel);  # Attach texture/renderbuffer to a framebuffer
	bint rlFramebufferComplete(unsigned int id);  # Verify framebuffer is complete
	void rlUnloadFramebuffer(unsigned int id);  # Delete framebuffer from GPU
	unsigned int rlLoadShaderCode(const char * vsCode, const char * fsCode);  # Load shader from code strings
	unsigned int rlCompileShader(const char * shaderCode, int type);  # Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)
	unsigned int rlLoadShaderProgram(unsigned int vShaderId, unsigned int fShaderId);  # Load custom shader program
	void rlUnloadShaderProgram(unsigned int id);  # Unload shader program
	int rlGetLocationUniform(unsigned int shaderId, const char * uniformName);  # Get shader location uniform
	int rlGetLocationAttrib(unsigned int shaderId, const char * attribName);  # Get shader location attribute
	void rlSetUniform(int locIndex, const void * value, int uniformType, int count);  # Set shader value uniform
	void rlSetUniformMatrix(int locIndex, Matrix mat);  # Set shader value matrix
	void rlSetUniformSampler(int locIndex, unsigned int textureId);  # Set shader value sampler
	void rlSetShader(unsigned int id, int * locs);  # Set shader currently active (id and locations)
	unsigned int rlLoadComputeShaderProgram(unsigned int shaderId);  # Load compute shader program
	void rlComputeShaderDispatch(unsigned int groupX, unsigned int groupY, unsigned int groupZ);  # Dispatch compute shader (equivalent to *draw* for graphics pilepine)
	unsigned int rlLoadShaderBuffer(unsigned long long size, const void * data, int usageHint);  # Load shader storage buffer object (SSBO)
	void rlUnloadShaderBuffer(unsigned int ssboId);  # Unload shader storage buffer object (SSBO)
	void rlUpdateShaderBufferElements(unsigned int id, const void * data, unsigned long long dataSize, unsigned long long offset);  # Update SSBO buffer data
	unsigned long long rlGetShaderBufferSize(unsigned int id);  # Get SSBO buffer size
	void rlReadShaderBufferElements(unsigned int id, void * dest, unsigned long long count, unsigned long long offset);  # Bind SSBO buffer
	void rlBindShaderBuffer(unsigned int id, unsigned int index);  # Copy SSBO buffer data
	void rlCopyBuffersElements(unsigned int destId, unsigned int srcId, unsigned long long destOffset, unsigned long long srcOffset, unsigned long long count);  # Copy SSBO buffer data
	void rlBindImageTexture(unsigned int id, unsigned int index, unsigned int format, int readonly);  # Bind image texture
	Matrix rlGetMatrixModelview();  # Get internal modelview matrix
	Matrix rlGetMatrixProjection();  # Get internal projection matrix
	Matrix rlGetMatrixTransform();  # Get internal accumulated transform matrix
	Matrix rlGetMatrixProjectionStereo(int eye);  # Get internal projection matrix for stereo render (selected eye)
	Matrix rlGetMatrixViewOffsetStereo(int eye);  # Get internal view offset matrix for stereo render (selected eye)
	void rlSetMatrixProjection(Matrix proj);  # Set a custom projection matrix (replaces internal projection matrix)
	void rlSetMatrixModelview(Matrix view);  # Set a custom modelview matrix (replaces internal modelview matrix)
	void rlSetMatrixProjectionStereo(Matrix right, Matrix left);  # Set eyes projection matrices for stereo rendering
	void rlSetMatrixViewOffsetStereo(Matrix right, Matrix left);  # Set eyes view offsets matrices for stereo rendering
	void rlLoadDrawCube();  # Load and draw a cube
	void rlLoadDrawQuad();  # Load and draw a quad
	
cdef extern from "raylib.h":
	DEF RAYLIB_VERSION = "4.2"
	
	#  System/Window config flags
	ctypedef enum ConfigFlags:
		FLAG_VSYNC_HINT = 64,  #  Set to try enabling V-Sync on GPU
		FLAG_FULLSCREEN_MODE = 2,  #  Set to run program in fullscreen
		FLAG_WINDOW_RESIZABLE = 4,  #  Set to allow resizable window
		FLAG_WINDOW_UNDECORATED = 8,  #  Set to disable window decoration (frame and buttons)
		FLAG_WINDOW_HIDDEN = 128,  #  Set to hide window
		FLAG_WINDOW_MINIMIZED = 512,  #  Set to minimize window (iconify)
		FLAG_WINDOW_MAXIMIZED = 1024,  #  Set to maximize window (expanded to monitor)
		FLAG_WINDOW_UNFOCUSED = 2048,  #  Set to window non focused
		FLAG_WINDOW_TOPMOST = 4096,  #  Set to window always on top
		FLAG_WINDOW_ALWAYS_RUN = 256,  #  Set to allow windows running while minimized
		FLAG_WINDOW_TRANSPARENT = 16,  #  Set to allow transparent framebuffer
		FLAG_WINDOW_HIGHDPI = 8192,  #  Set to support HighDPI
		FLAG_WINDOW_MOUSE_PASSTHROUGH = 16384,  #  Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
		FLAG_MSAA_4X_HINT = 32,  #  Set to try enabling MSAA 4X
		FLAG_INTERLACED_HINT = 65536  #  Set to try enabling interlaced video format (for V3D)
	
	
	#  Trace log level
	ctypedef enum TraceLogLevel:
		LOG_ALL = 0,  #  Display all logs
		LOG_TRACE = 1,  #  Trace logging, intended for internal use only
		LOG_DEBUG = 2,  #  Debug logging, used for internal debugging, it should be disabled on release builds
		LOG_INFO = 3,  #  Info logging, used for program execution info
		LOG_WARNING = 4,  #  Warning logging, used on recoverable failures
		LOG_ERROR = 5,  #  Error logging, used on unrecoverable failures
		LOG_FATAL = 6,  #  Fatal logging, used to abort program: exit(EXIT_FAILURE)
		LOG_NONE = 7  #  Disable logging
	
	
	#  Keyboard keys (US keyboard layout)
	ctypedef enum KeyboardKey:
		KEY_NULL = 0,  #  Key: NULL, used for no key pressed
		KEY_APOSTROPHE = 39,  #  Key: '
		KEY_COMMA = 44,  #  Key: ,
		KEY_MINUS = 45,  #  Key: -
		KEY_PERIOD = 46,  #  Key: .
		KEY_SLASH = 47,  #  Key: /
		KEY_ZERO = 48,  #  Key: 0
		KEY_ONE = 49,  #  Key: 1
		KEY_TWO = 50,  #  Key: 2
		KEY_THREE = 51,  #  Key: 3
		KEY_FOUR = 52,  #  Key: 4
		KEY_FIVE = 53,  #  Key: 5
		KEY_SIX = 54,  #  Key: 6
		KEY_SEVEN = 55,  #  Key: 7
		KEY_EIGHT = 56,  #  Key: 8
		KEY_NINE = 57,  #  Key: 9
		KEY_SEMICOLON = 59,  #  Key: ;
		KEY_EQUAL = 61,  #  Key: =
		KEY_A = 65,  #  Key: A | a
		KEY_B = 66,  #  Key: B | b
		KEY_C = 67,  #  Key: C | c
		KEY_D = 68,  #  Key: D | d
		KEY_E = 69,  #  Key: E | e
		KEY_F = 70,  #  Key: F | f
		KEY_G = 71,  #  Key: G | g
		KEY_H = 72,  #  Key: H | h
		KEY_I = 73,  #  Key: I | i
		KEY_J = 74,  #  Key: J | j
		KEY_K = 75,  #  Key: K | k
		KEY_L = 76,  #  Key: L | l
		KEY_M = 77,  #  Key: M | m
		KEY_N = 78,  #  Key: N | n
		KEY_O = 79,  #  Key: O | o
		KEY_P = 80,  #  Key: P | p
		KEY_Q = 81,  #  Key: Q | q
		KEY_R = 82,  #  Key: R | r
		KEY_S = 83,  #  Key: S | s
		KEY_T = 84,  #  Key: T | t
		KEY_U = 85,  #  Key: U | u
		KEY_V = 86,  #  Key: V | v
		KEY_W = 87,  #  Key: W | w
		KEY_X = 88,  #  Key: X | x
		KEY_Y = 89,  #  Key: Y | y
		KEY_Z = 90,  #  Key: Z | z
		KEY_LEFT_BRACKET = 91,  #  Key: [
		KEY_BACKSLASH = 92,  #  Key: '\'
		KEY_RIGHT_BRACKET = 93,  #  Key: ]
		KEY_GRAVE = 96,  #  Key: `
		KEY_SPACE = 32,  #  Key: Space
		KEY_ESCAPE = 256,  #  Key: Esc
		KEY_ENTER = 257,  #  Key: Enter
		KEY_TAB = 258,  #  Key: Tab
		KEY_BACKSPACE = 259,  #  Key: Backspace
		KEY_INSERT = 260,  #  Key: Ins
		KEY_DELETE = 261,  #  Key: Del
		KEY_RIGHT = 262,  #  Key: Cursor right
		KEY_LEFT = 263,  #  Key: Cursor left
		KEY_DOWN = 264,  #  Key: Cursor down
		KEY_UP = 265,  #  Key: Cursor up
		KEY_PAGE_UP = 266,  #  Key: Page up
		KEY_PAGE_DOWN = 267,  #  Key: Page down
		KEY_HOME = 268,  #  Key: Home
		KEY_END = 269,  #  Key: End
		KEY_CAPS_LOCK = 280,  #  Key: Caps lock
		KEY_SCROLL_LOCK = 281,  #  Key: Scroll down
		KEY_NUM_LOCK = 282,  #  Key: Num lock
		KEY_PRINT_SCREEN = 283,  #  Key: Print screen
		KEY_PAUSE = 284,  #  Key: Pause
		KEY_F1 = 290,  #  Key: F1
		KEY_F2 = 291,  #  Key: F2
		KEY_F3 = 292,  #  Key: F3
		KEY_F4 = 293,  #  Key: F4
		KEY_F5 = 294,  #  Key: F5
		KEY_F6 = 295,  #  Key: F6
		KEY_F7 = 296,  #  Key: F7
		KEY_F8 = 297,  #  Key: F8
		KEY_F9 = 298,  #  Key: F9
		KEY_F10 = 299,  #  Key: F10
		KEY_F11 = 300,  #  Key: F11
		KEY_F12 = 301,  #  Key: F12
		KEY_LEFT_SHIFT = 340,  #  Key: Shift left
		KEY_LEFT_CONTROL = 341,  #  Key: Control left
		KEY_LEFT_ALT = 342,  #  Key: Alt left
		KEY_LEFT_SUPER = 343,  #  Key: Super left
		KEY_RIGHT_SHIFT = 344,  #  Key: Shift right
		KEY_RIGHT_CONTROL = 345,  #  Key: Control right
		KEY_RIGHT_ALT = 346,  #  Key: Alt right
		KEY_RIGHT_SUPER = 347,  #  Key: Super right
		KEY_KB_MENU = 348,  #  Key: KB menu
		KEY_KP_0 = 320,  #  Key: Keypad 0
		KEY_KP_1 = 321,  #  Key: Keypad 1
		KEY_KP_2 = 322,  #  Key: Keypad 2
		KEY_KP_3 = 323,  #  Key: Keypad 3
		KEY_KP_4 = 324,  #  Key: Keypad 4
		KEY_KP_5 = 325,  #  Key: Keypad 5
		KEY_KP_6 = 326,  #  Key: Keypad 6
		KEY_KP_7 = 327,  #  Key: Keypad 7
		KEY_KP_8 = 328,  #  Key: Keypad 8
		KEY_KP_9 = 329,  #  Key: Keypad 9
		KEY_KP_DECIMAL = 330,  #  Key: Keypad .
		KEY_KP_DIVIDE = 331,  #  Key: Keypad /
		KEY_KP_MULTIPLY = 332,  #  Key: Keypad *
		KEY_KP_SUBTRACT = 333,  #  Key: Keypad -
		KEY_KP_ADD = 334,  #  Key: Keypad +
		KEY_KP_ENTER = 335,  #  Key: Keypad Enter
		KEY_KP_EQUAL = 336,  #  Key: Keypad =
		KEY_BACK = 4,  #  Key: Android back button
		KEY_MENU = 82,  #  Key: Android menu button
		KEY_VOLUME_UP = 24,  #  Key: Android volume up button
		KEY_VOLUME_DOWN = 25  #  Key: Android volume down button
	
	
	#  Mouse buttons
	ctypedef enum MouseButton:
		MOUSE_BUTTON_LEFT = 0,  #  Mouse button left
		MOUSE_BUTTON_RIGHT = 1,  #  Mouse button right
		MOUSE_BUTTON_MIDDLE = 2,  #  Mouse button middle (pressed wheel)
		MOUSE_BUTTON_SIDE = 3,  #  Mouse button side (advanced mouse device)
		MOUSE_BUTTON_EXTRA = 4,  #  Mouse button extra (advanced mouse device)
		MOUSE_BUTTON_FORWARD = 5,  #  Mouse button fordward (advanced mouse device)
		MOUSE_BUTTON_BACK = 6  #  Mouse button back (advanced mouse device)
	
	
	#  Mouse cursor
	ctypedef enum MouseCursor:
		MOUSE_CURSOR_DEFAULT = 0,  #  Default pointer shape
		MOUSE_CURSOR_ARROW = 1,  #  Arrow shape
		MOUSE_CURSOR_IBEAM = 2,  #  Text writing cursor shape
		MOUSE_CURSOR_CROSSHAIR = 3,  #  Cross shape
		MOUSE_CURSOR_POINTING_HAND = 4,  #  Pointing hand cursor
		MOUSE_CURSOR_RESIZE_EW = 5,  #  Horizontal resize/move arrow shape
		MOUSE_CURSOR_RESIZE_NS = 6,  #  Vertical resize/move arrow shape
		MOUSE_CURSOR_RESIZE_NWSE = 7,  #  Top-left to bottom-right diagonal resize/move arrow shape
		MOUSE_CURSOR_RESIZE_NESW = 8,  #  The top-right to bottom-left diagonal resize/move arrow shape
		MOUSE_CURSOR_RESIZE_ALL = 9,  #  The omni-directional resize/move cursor shape
		MOUSE_CURSOR_NOT_ALLOWED = 10  #  The operation-not-allowed shape
	
	
	#  Gamepad buttons
	ctypedef enum GamepadButton:
		GAMEPAD_BUTTON_UNKNOWN = 0,  #  Unknown button, just for error checking
		GAMEPAD_BUTTON_LEFT_FACE_UP = 1,  #  Gamepad left DPAD up button
		GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2,  #  Gamepad left DPAD right button
		GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3,  #  Gamepad left DPAD down button
		GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4,  #  Gamepad left DPAD left button
		GAMEPAD_BUTTON_RIGHT_FACE_UP = 5,  #  Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
		GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6,  #  Gamepad right button right (i.e. PS3: Square, Xbox: X)
		GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7,  #  Gamepad right button down (i.e. PS3: Cross, Xbox: A)
		GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8,  #  Gamepad right button left (i.e. PS3: Circle, Xbox: B)
		GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9,  #  Gamepad top/back trigger left (first), it could be a trailing button
		GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10,  #  Gamepad top/back trigger left (second), it could be a trailing button
		GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11,  #  Gamepad top/back trigger right (one), it could be a trailing button
		GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12,  #  Gamepad top/back trigger right (second), it could be a trailing button
		GAMEPAD_BUTTON_MIDDLE_LEFT = 13,  #  Gamepad center buttons, left one (i.e. PS3: Select)
		GAMEPAD_BUTTON_MIDDLE = 14,  #  Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
		GAMEPAD_BUTTON_MIDDLE_RIGHT = 15,  #  Gamepad center buttons, right one (i.e. PS3: Start)
		GAMEPAD_BUTTON_LEFT_THUMB = 16,  #  Gamepad joystick pressed button left
		GAMEPAD_BUTTON_RIGHT_THUMB = 17  #  Gamepad joystick pressed button right
	
	
	#  Gamepad axis
	ctypedef enum GamepadAxis:
		GAMEPAD_AXIS_LEFT_X = 0,  #  Gamepad left stick X axis
		GAMEPAD_AXIS_LEFT_Y = 1,  #  Gamepad left stick Y axis
		GAMEPAD_AXIS_RIGHT_X = 2,  #  Gamepad right stick X axis
		GAMEPAD_AXIS_RIGHT_Y = 3,  #  Gamepad right stick Y axis
		GAMEPAD_AXIS_LEFT_TRIGGER = 4,  #  Gamepad back trigger left, pressure level: [1..-1]
		GAMEPAD_AXIS_RIGHT_TRIGGER = 5  #  Gamepad back trigger right, pressure level: [1..-1]
	
	
	#  Material map index
	ctypedef enum MaterialMapIndex:
		MATERIAL_MAP_ALBEDO = 0,  #  Albedo material (same as: MATERIAL_MAP_DIFFUSE)
		MATERIAL_MAP_METALNESS = 1,  #  Metalness material (same as: MATERIAL_MAP_SPECULAR)
		MATERIAL_MAP_NORMAL = 2,  #  Normal material
		MATERIAL_MAP_ROUGHNESS = 3,  #  Roughness material
		MATERIAL_MAP_OCCLUSION = 4,  #  Ambient occlusion material
		MATERIAL_MAP_EMISSION = 5,  #  Emission material
		MATERIAL_MAP_HEIGHT = 6,  #  Heightmap material
		MATERIAL_MAP_CUBEMAP = 7,  #  Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
		MATERIAL_MAP_IRRADIANCE = 8,  #  Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
		MATERIAL_MAP_PREFILTER = 9,  #  Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
		MATERIAL_MAP_BRDF = 10  #  Brdf material
	
	
	#  Shader location index
	ctypedef enum ShaderLocationIndex:
		SHADER_LOC_VERTEX_POSITION = 0,  #  Shader location: vertex attribute: position
		SHADER_LOC_VERTEX_TEXCOORD01 = 1,  #  Shader location: vertex attribute: texcoord01
		SHADER_LOC_VERTEX_TEXCOORD02 = 2,  #  Shader location: vertex attribute: texcoord02
		SHADER_LOC_VERTEX_NORMAL = 3,  #  Shader location: vertex attribute: normal
		SHADER_LOC_VERTEX_TANGENT = 4,  #  Shader location: vertex attribute: tangent
		SHADER_LOC_VERTEX_COLOR = 5,  #  Shader location: vertex attribute: color
		SHADER_LOC_MATRIX_MVP = 6,  #  Shader location: matrix uniform: model-view-projection
		SHADER_LOC_MATRIX_VIEW = 7,  #  Shader location: matrix uniform: view (camera transform)
		SHADER_LOC_MATRIX_PROJECTION = 8,  #  Shader location: matrix uniform: projection
		SHADER_LOC_MATRIX_MODEL = 9,  #  Shader location: matrix uniform: model (transform)
		SHADER_LOC_MATRIX_NORMAL = 10,  #  Shader location: matrix uniform: normal
		SHADER_LOC_VECTOR_VIEW = 11,  #  Shader location: vector uniform: view
		SHADER_LOC_COLOR_DIFFUSE = 12,  #  Shader location: vector uniform: diffuse color
		SHADER_LOC_COLOR_SPECULAR = 13,  #  Shader location: vector uniform: specular color
		SHADER_LOC_COLOR_AMBIENT = 14,  #  Shader location: vector uniform: ambient color
		SHADER_LOC_MAP_ALBEDO = 15,  #  Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
		SHADER_LOC_MAP_METALNESS = 16,  #  Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
		SHADER_LOC_MAP_NORMAL = 17,  #  Shader location: sampler2d texture: normal
		SHADER_LOC_MAP_ROUGHNESS = 18,  #  Shader location: sampler2d texture: roughness
		SHADER_LOC_MAP_OCCLUSION = 19,  #  Shader location: sampler2d texture: occlusion
		SHADER_LOC_MAP_EMISSION = 20,  #  Shader location: sampler2d texture: emission
		SHADER_LOC_MAP_HEIGHT = 21,  #  Shader location: sampler2d texture: height
		SHADER_LOC_MAP_CUBEMAP = 22,  #  Shader location: samplerCube texture: cubemap
		SHADER_LOC_MAP_IRRADIANCE = 23,  #  Shader location: samplerCube texture: irradiance
		SHADER_LOC_MAP_PREFILTER = 24,  #  Shader location: samplerCube texture: prefilter
		SHADER_LOC_MAP_BRDF = 25  #  Shader location: sampler2d texture: brdf
	
	
	#  Shader uniform data type
	ctypedef enum ShaderUniformDataType:
		SHADER_UNIFORM_FLOAT = 0,  #  Shader uniform type: float
		SHADER_UNIFORM_VEC2 = 1,  #  Shader uniform type: vec2 (2 float)
		SHADER_UNIFORM_VEC3 = 2,  #  Shader uniform type: vec3 (3 float)
		SHADER_UNIFORM_VEC4 = 3,  #  Shader uniform type: vec4 (4 float)
		SHADER_UNIFORM_INT = 4,  #  Shader uniform type: int
		SHADER_UNIFORM_IVEC2 = 5,  #  Shader uniform type: ivec2 (2 int)
		SHADER_UNIFORM_IVEC3 = 6,  #  Shader uniform type: ivec3 (3 int)
		SHADER_UNIFORM_IVEC4 = 7,  #  Shader uniform type: ivec4 (4 int)
		SHADER_UNIFORM_SAMPLER2D = 8  #  Shader uniform type: sampler2d
	
	
	#  Shader attribute data types
	ctypedef enum ShaderAttributeDataType:
		SHADER_ATTRIB_FLOAT = 0,  #  Shader attribute type: float
		SHADER_ATTRIB_VEC2 = 1,  #  Shader attribute type: vec2 (2 float)
		SHADER_ATTRIB_VEC3 = 2,  #  Shader attribute type: vec3 (3 float)
		SHADER_ATTRIB_VEC4 = 3  #  Shader attribute type: vec4 (4 float)
	
	
	#  Pixel formats
	ctypedef enum PixelFormat:
		PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1,  #  8 bit per pixel (no alpha)
		PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2,  #  8*2 bpp (2 channels)
		PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3,  #  16 bpp
		PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4,  #  24 bpp
		PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5,  #  16 bpp (1 bit alpha)
		PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6,  #  16 bpp (4 bit alpha)
		PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7,  #  32 bpp
		PIXELFORMAT_UNCOMPRESSED_R32 = 8,  #  32 bpp (1 channel - float)
		PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9,  #  32*3 bpp (3 channels - float)
		PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10,  #  32*4 bpp (4 channels - float)
		PIXELFORMAT_COMPRESSED_DXT1_RGB = 11,  #  4 bpp (no alpha)
		PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12,  #  4 bpp (1 bit alpha)
		PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13,  #  8 bpp
		PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14,  #  8 bpp
		PIXELFORMAT_COMPRESSED_ETC1_RGB = 15,  #  4 bpp
		PIXELFORMAT_COMPRESSED_ETC2_RGB = 16,  #  4 bpp
		PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17,  #  8 bpp
		PIXELFORMAT_COMPRESSED_PVRT_RGB = 18,  #  4 bpp
		PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19,  #  4 bpp
		PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20,  #  8 bpp
		PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21  #  2 bpp
	
	
	#  Texture parameters: filter mode
	ctypedef enum TextureFilter:
		TEXTURE_FILTER_POINT = 0,  #  No filter, just pixel approximation
		TEXTURE_FILTER_BILINEAR = 1,  #  Linear filtering
		TEXTURE_FILTER_TRILINEAR = 2,  #  Trilinear filtering (linear with mipmaps)
		TEXTURE_FILTER_ANISOTROPIC_4X = 3,  #  Anisotropic filtering 4x
		TEXTURE_FILTER_ANISOTROPIC_8X = 4,  #  Anisotropic filtering 8x
		TEXTURE_FILTER_ANISOTROPIC_16X = 5  #  Anisotropic filtering 16x
	
	
	#  Texture parameters: wrap mode
	ctypedef enum TextureWrap:
		TEXTURE_WRAP_REPEAT = 0,  #  Repeats texture in tiled mode
		TEXTURE_WRAP_CLAMP = 1,  #  Clamps texture to edge pixel in tiled mode
		TEXTURE_WRAP_MIRROR_REPEAT = 2,  #  Mirrors and repeats the texture in tiled mode
		TEXTURE_WRAP_MIRROR_CLAMP = 3  #  Mirrors and clamps to border the texture in tiled mode
	
	
	#  Cubemap layouts
	ctypedef enum CubemapLayout:
		CUBEMAP_LAYOUT_AUTO_DETECT = 0,  #  Automatically detect layout type
		CUBEMAP_LAYOUT_LINE_VERTICAL = 1,  #  Layout is defined by a vertical line with faces
		CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2,  #  Layout is defined by an horizontal line with faces
		CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3,  #  Layout is defined by a 3x4 cross with cubemap faces
		CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4,  #  Layout is defined by a 4x3 cross with cubemap faces
		CUBEMAP_LAYOUT_PANORAMA = 5  #  Layout is defined by a panorama image (equirectangular map)
	
	
	#  Font type, defines generation method
	ctypedef enum FontType:
		FONT_DEFAULT = 0,  #  Default font generation, anti-aliased
		FONT_BITMAP = 1,  #  Bitmap font generation, no anti-aliasing
		FONT_SDF = 2  #  SDF font generation, requires external shader
	
	
	#  Color blending modes (pre-defined)
	ctypedef enum BlendMode:
		BLEND_ALPHA = 0,  #  Blend textures considering alpha (default)
		BLEND_ADDITIVE = 1,  #  Blend textures adding colors
		BLEND_MULTIPLIED = 2,  #  Blend textures multiplying colors
		BLEND_ADD_COLORS = 3,  #  Blend textures adding colors (alternative)
		BLEND_SUBTRACT_COLORS = 4,  #  Blend textures subtracting colors (alternative)
		BLEND_ALPHA_PREMULTIPLY = 5,  #  Blend premultiplied textures considering alpha
		BLEND_CUSTOM = 6  #  Blend textures using custom src/dst factors (use rlSetBlendMode())
	
	
	#  Gesture
	ctypedef enum Gesture:
		GESTURE_NONE = 0,  #  No gesture
		GESTURE_TAP = 1,  #  Tap gesture
		GESTURE_DOUBLETAP = 2,  #  Double tap gesture
		GESTURE_HOLD = 4,  #  Hold gesture
		GESTURE_DRAG = 8,  #  Drag gesture
		GESTURE_SWIPE_RIGHT = 16,  #  Swipe right gesture
		GESTURE_SWIPE_LEFT = 32,  #  Swipe left gesture
		GESTURE_SWIPE_UP = 64,  #  Swipe up gesture
		GESTURE_SWIPE_DOWN = 128,  #  Swipe down gesture
		GESTURE_PINCH_IN = 256,  #  Pinch in gesture
		GESTURE_PINCH_OUT = 512  #  Pinch out gesture
	
	
	#  Camera system modes
	ctypedef enum CameraMode:
		CAMERA_CUSTOM = 0,  #  Custom camera
		CAMERA_FREE = 1,  #  Free camera
		CAMERA_ORBITAL = 2,  #  Orbital camera
		CAMERA_FIRST_PERSON = 3,  #  First person camera
		CAMERA_THIRD_PERSON = 4  #  Third person camera
	
	
	#  Camera projection
	ctypedef enum CameraProjection:
		CAMERA_PERSPECTIVE = 0,  #  Perspective projection
		CAMERA_ORTHOGRAPHIC = 1  #  Orthographic projection
	
	
	#  N-patch layout
	ctypedef enum NPatchLayout:
		NPATCH_NINE_PATCH = 0,  #  Npatch layout: 3x3 tiles
		NPATCH_THREE_PATCH_VERTICAL = 1,  #  Npatch layout: 1x3 tiles
		NPATCH_THREE_PATCH_HORIZONTAL = 2  #  Npatch layout: 3x1 tiles
	
	
	
	#  Vector2, 2 components
	ctypedef struct Vector2:
		float x;  # Vector x component
		float y;  # Vector y component
	
	#  Vector3, 3 components
	ctypedef struct Vector3:
		float x;  # Vector x component
		float y;  # Vector y component
		float z;  # Vector z component
	
	#  Vector4, 4 components
	ctypedef struct Vector4:
		float x;  # Vector x component
		float y;  # Vector y component
		float z;  # Vector z component
		float w;  # Vector w component
	
	#  Quaternion, 4 components (Vector4 alias)
	ctypedef Vector4 Quaternion
	
	#  Color, 4 components, R8G8B8A8 (32bit)
	ctypedef struct Color:
		unsigned char r;  # Color red value
		unsigned char g;  # Color green value
		unsigned char b;  # Color blue value
		unsigned char a;  # Color alpha value
	
	#  Rectangle, 4 components
	ctypedef struct Rectangle:
		float x;  # Rectangle top-left corner position x
		float y;  # Rectangle top-left corner position y
		float width;  # Rectangle width
		float height;  # Rectangle height
	
	#  Image, pixel data stored in CPU memory (RAM)
	ctypedef struct Image:
		void * data;  # Image raw data
		int width;  # Image base width
		int height;  # Image base height
		int mipmaps;  # Mipmap levels, 1 by default
		int format;  # Data format (PixelFormat type)
	
	#  Texture, tex data stored in GPU memory (VRAM)
	ctypedef struct Texture:
		unsigned int id;  # OpenGL texture id
		int width;  # Texture base width
		int height;  # Texture base height
		int mipmaps;  # Mipmap levels, 1 by default
		int format;  # Data format (PixelFormat type)
	
	#  Texture2D, same as Texture
	ctypedef Texture Texture2D
	
	#  TextureCubemap, same as Texture
	ctypedef Texture TextureCubemap
	
	#  RenderTexture, fbo for texture rendering
	ctypedef struct RenderTexture:
		unsigned int id;  # OpenGL framebuffer object id
		Texture texture;  # Color buffer attachment texture
		Texture depth;  # Depth buffer attachment texture
	
	#  RenderTexture2D, same as RenderTexture
	ctypedef RenderTexture RenderTexture2D
	
	#  NPatchInfo, n-patch layout info
	ctypedef struct NPatchInfo:
		Rectangle source;  # Texture source rectangle
		int left;  # Left border offset
		int top;  # Top border offset
		int right;  # Right border offset
		int bottom;  # Bottom border offset
		int layout;  # Layout of the n-patch: 3x3, 1x3 or 3x1
	
	#  GlyphInfo, font characters glyphs info
	ctypedef struct GlyphInfo:
		int value;  # Character value (Unicode)
		int offsetX;  # Character offset X when drawing
		int offsetY;  # Character offset Y when drawing
		int advanceX;  # Character advance position X
		Image image;  # Character image data
	
	#  Font, font texture and GlyphInfo array data
	ctypedef struct Font:
		int baseSize;  # Base size (default chars height)
		int glyphCount;  # Number of glyph characters
		int glyphPadding;  # Padding around the glyph characters
		Texture2D texture;  # Texture atlas containing the glyphs
		Rectangle * recs;  # Rectangles in texture for the glyphs
		GlyphInfo * glyphs;  # Glyphs info data
	
	#  Camera, defines position/orientation in 3d space
	ctypedef struct Camera3D:
		Vector3 position;  # Camera position
		Vector3 target;  # Camera target it looks-at
		Vector3 up;  # Camera up vector (rotation over its axis)
		float fovy;  # Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
		int projection;  # Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC
	
	#  Camera type fallback, defaults to Camera3D
	ctypedef Camera3D Camera
	
	#  Camera2D, defines position/orientation in 2d space
	ctypedef struct Camera2D:
		Vector2 offset;  # Camera offset (displacement from target)
		Vector2 target;  # Camera target (rotation and zoom origin)
		float rotation;  # Camera rotation in degrees
		float zoom;  # Camera zoom (scaling), should be 1.0f by default
	
	#  Mesh, vertex data and vao/vbo
	ctypedef struct Mesh:
		int vertexCount;  # Number of vertices stored in arrays
		int triangleCount;  # Number of triangles stored (indexed or not)
		float * vertices;  # Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
		float * texcoords;  # Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
		float * texcoords2;  # Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
		float * normals;  # Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
		float * tangents;  # Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
		unsigned char * colors;  # Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
		unsigned short * indices;  # Vertex indices (in case vertex data comes indexed)
		float * animVertices;  # Animated vertex positions (after bones transformations)
		float * animNormals;  # Animated normals (after bones transformations)
		unsigned char * boneIds;  # Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
		float * boneWeights;  # Vertex bone weight, up to 4 bones influence by vertex (skinning)
		unsigned int vaoId;  # OpenGL Vertex Array Object id
		unsigned int * vboId;  # OpenGL Vertex Buffer Objects id (default vertex data)
	
	#  Shader
	ctypedef struct Shader:
		unsigned int id;  # Shader program id
		int * locs;  # Shader locations array (RL_MAX_SHADER_LOCATIONS)
	
	#  MaterialMap
	ctypedef struct MaterialMap:
		Texture2D texture;  # Material map texture
		Color color;  # Material map color
		float value;  # Material map value
	
	#  Material, includes shader and maps
	ctypedef struct Material:
		Shader shader;  # Material shader
		MaterialMap * maps;  # Material maps array (MAX_MATERIAL_MAPS)
		float[4] params;  # Material generic parameters (if required)
	
	#  Transform, vectex transformation data
	ctypedef struct Transform:
		Vector3 translation;  # Translation
		Quaternion rotation;  # Rotation
		Vector3 scale;  # Scale
	
	#  Bone, skeletal animation bone
	ctypedef struct BoneInfo:
		char[32] name;  # Bone name
		int parent;  # Bone parent
	
	#  Model, meshes, materials and animation data
	ctypedef struct Model:
		Matrix transform;  # Local transform matrix
		int meshCount;  # Number of meshes
		int materialCount;  # Number of materials
		Mesh * meshes;  # Meshes array
		Material * materials;  # Materials array
		int * meshMaterial;  # Mesh material number
		int boneCount;  # Number of bones
		BoneInfo * bones;  # Bones information (skeleton)
		Transform * bindPose;  # Bones base transformation (pose)
	
	#  ModelAnimation
	ctypedef struct ModelAnimation:
		int boneCount;  # Number of bones
		int frameCount;  # Number of animation frames
		BoneInfo * bones;  # Bones information (skeleton)
		Transform ** framePoses;  # Poses array by frame
	
	#  Ray, ray for raycasting
	ctypedef struct Ray:
		Vector3 position;  # Ray position (origin)
		Vector3 direction;  # Ray direction
	
	#  RayCollision, ray hit information
	ctypedef struct RayCollision:
		bint hit;  # Did the ray hit something?
		float distance;  # Distance to nearest hit
		Vector3 point;  # Point of nearest hit
		Vector3 normal;  # Surface normal of hit
	
	#  BoundingBox
	ctypedef struct BoundingBox:
		Vector3 min;  # Minimum vertex box-corner
		Vector3 max;  # Maximum vertex box-corner
	
	#  Wave, audio wave data
	ctypedef struct Wave:
		unsigned int frameCount;  # Total number of frames (considering channels)
		unsigned int sampleRate;  # Frequency (samples per second)
		unsigned int sampleSize;  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
		unsigned int channels;  # Number of channels (1-mono, 2-stereo, ...)
		void * data;  # Buffer data pointer
	
	#  AudioStream, custom audio stream
	ctypedef struct AudioStream:
		rAudioBuffer * buffer;  # Pointer to internal data used by the audio system
		rAudioProcessor * processor;  # Pointer to internal data processor, useful for audio effects
		unsigned int sampleRate;  # Frequency (samples per second)
		unsigned int sampleSize;  # Bit depth (bits per sample): 8, 16, 32 (24 not supported)
		unsigned int channels;  # Number of channels (1-mono, 2-stereo, ...)
	
	#  Sound
	ctypedef struct Sound:
		AudioStream stream;  # Audio stream
		unsigned int frameCount;  # Total number of frames (considering channels)
	
	#  Music, audio stream, anything longer than ~10 seconds should be streamed
	ctypedef struct Music:
		AudioStream stream;  # Audio stream
		unsigned int frameCount;  # Total number of frames (considering channels)
		bint looping;  # Music looping enable
		int ctxType;  # Type of music context (audio filetype)
		void * ctxData;  # Audio context data, depends on type
	
	#  VrDeviceInfo, Head-Mounted-Display device parameters
	ctypedef struct VrDeviceInfo:
		int hResolution;  # Horizontal resolution in pixels
		int vResolution;  # Vertical resolution in pixels
		float hScreenSize;  # Horizontal size in meters
		float vScreenSize;  # Vertical size in meters
		float vScreenCenter;  # Screen center in meters
		float eyeToScreenDistance;  # Distance between eye and display in meters
		float lensSeparationDistance;  # Lens separation distance in meters
		float interpupillaryDistance;  # IPD (distance between pupils) in meters
		float[4] lensDistortionValues;  # Lens distortion constant parameters
		float[4] chromaAbCorrection;  # Chromatic aberration correction parameters
	
	#  VrStereoConfig, VR stereo rendering configuration for simulator
	ctypedef struct VrStereoConfig:
		Matrix[2] projection;  # VR projection matrices (per eye)
		Matrix[2] viewOffset;  # VR view offset matrices (per eye)
		float[2] leftLensCenter;  # VR left lens center
		float[2] rightLensCenter;  # VR right lens center
		float[2] leftScreenCenter;  # VR left screen center
		float[2] rightScreenCenter;  # VR right screen center
		float[2] scale;  # VR distortion scale
		float[2] scaleIn;  # VR distortion scale in
	
	#  File path list
	ctypedef struct FilePathList:
		unsigned int capacity;  # Filepaths max entries
		unsigned int count;  # Filepaths entries count
		char ** paths;  # Filepaths entries
	
	
	void InitWindow(int width, int height, const char * title);  # Initialize window and OpenGL context
	bint WindowShouldClose();  # Check if KEY_ESCAPE pressed or Close icon pressed
	void CloseWindow();  # Close window and unload OpenGL context
	bint IsWindowReady();  # Check if window has been initialized successfully
	bint IsWindowFullscreen();  # Check if window is currently fullscreen
	bint IsWindowHidden();  # Check if window is currently hidden (only PLATFORM_DESKTOP)
	bint IsWindowMinimized();  # Check if window is currently minimized (only PLATFORM_DESKTOP)
	bint IsWindowMaximized();  # Check if window is currently maximized (only PLATFORM_DESKTOP)
	bint IsWindowFocused();  # Check if window is currently focused (only PLATFORM_DESKTOP)
	bint IsWindowResized();  # Check if window has been resized last frame
	bint IsWindowState(unsigned int flag);  # Check if one specific window flag is enabled
	void SetWindowState(unsigned int flags);  # Set window configuration state using flags (only PLATFORM_DESKTOP)
	void ClearWindowState(unsigned int flags);  # Clear window configuration state flags
	void ToggleFullscreen();  # Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)
	void MaximizeWindow();  # Set window state: maximized, if resizable (only PLATFORM_DESKTOP)
	void MinimizeWindow();  # Set window state: minimized, if resizable (only PLATFORM_DESKTOP)
	void RestoreWindow();  # Set window state: not minimized/maximized (only PLATFORM_DESKTOP)
	void SetWindowIcon(Image image);  # Set icon for window (only PLATFORM_DESKTOP)
	void SetWindowTitle(const char * title);  # Set title for window (only PLATFORM_DESKTOP)
	void SetWindowPosition(int x, int y);  # Set window position on screen (only PLATFORM_DESKTOP)
	void SetWindowMonitor(int monitor);  # Set monitor for the current window (fullscreen mode)
	void SetWindowMinSize(int width, int height);  # Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)
	void SetWindowSize(int width, int height);  # Set window dimensions
	void SetWindowOpacity(float opacity);  # Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)
	void * GetWindowHandle();  # Get native window handle
	int GetScreenWidth();  # Get current screen width
	int GetScreenHeight();  # Get current screen height
	int GetRenderWidth();  # Get current render width (it considers HiDPI)
	int GetRenderHeight();  # Get current render height (it considers HiDPI)
	int GetMonitorCount();  # Get number of connected monitors
	int GetCurrentMonitor();  # Get current connected monitor
	Vector2 GetMonitorPosition(int monitor);  # Get specified monitor position
	int GetMonitorWidth(int monitor);  # Get specified monitor width (current video mode used by monitor)
	int GetMonitorHeight(int monitor);  # Get specified monitor height (current video mode used by monitor)
	int GetMonitorPhysicalWidth(int monitor);  # Get specified monitor physical width in millimetres
	int GetMonitorPhysicalHeight(int monitor);  # Get specified monitor physical height in millimetres
	int GetMonitorRefreshRate(int monitor);  # Get specified monitor refresh rate
	Vector2 GetWindowPosition();  # Get window position XY on monitor
	Vector2 GetWindowScaleDPI();  # Get window scale DPI factor
	const char * GetMonitorName(int monitor);  # Get the human-readable, UTF-8 encoded name of the primary monitor
	void SetClipboardText(const char * text);  # Set clipboard text content
	const char * GetClipboardText();  # Get clipboard text content
	void EnableEventWaiting();  # Enable waiting for events on EndDrawing(), no automatic event polling
	void DisableEventWaiting();  # Disable waiting for events on EndDrawing(), automatic events polling
	void SwapScreenBuffer();  # Swap back buffer with front buffer (screen drawing)
	void PollInputEvents();  # Register all input events
	void WaitTime(double seconds);  # Wait for some time (halt program execution)
	void ShowCursor();  # Shows cursor
	void HideCursor();  # Hides cursor
	bint IsCursorHidden();  # Check if cursor is not visible
	void EnableCursor();  # Enables cursor (unlock cursor)
	void DisableCursor();  # Disables cursor (lock cursor)
	bint IsCursorOnScreen();  # Check if cursor is on the screen
	void ClearBackground(Color color);  # Set background color (framebuffer clear color)
	void BeginDrawing();  # Setup canvas (framebuffer) to start drawing
	void EndDrawing();  # End canvas drawing and swap buffers (double buffering)
	void BeginMode2D(Camera2D camera);  # Begin 2D mode with custom camera (2D)
	void EndMode2D();  # Ends 2D mode with custom camera
	void BeginMode3D(Camera3D camera);  # Begin 3D mode with custom camera (3D)
	void EndMode3D();  # Ends 3D mode and returns to default 2D orthographic mode
	void BeginTextureMode(RenderTexture2D target);  # Begin drawing to render texture
	void EndTextureMode();  # Ends drawing to render texture
	void BeginShaderMode(Shader shader);  # Begin custom shader drawing
	void EndShaderMode();  # End custom shader drawing (use default shader)
	void BeginBlendMode(int mode);  # Begin blending mode (alpha, additive, multiplied, subtract, custom)
	void EndBlendMode();  # End blending mode (reset to default: alpha blending)
	void BeginScissorMode(int x, int y, int width, int height);  # Begin scissor mode (define screen area for following drawing)
	void EndScissorMode();  # End scissor mode
	void BeginVrStereoMode(VrStereoConfig config);  # Begin stereo rendering (requires VR simulator)
	void EndVrStereoMode();  # End stereo rendering (requires VR simulator)
	VrStereoConfig LoadVrStereoConfig(VrDeviceInfo device);  # Load VR stereo config for VR simulator device parameters
	void UnloadVrStereoConfig(VrStereoConfig config);  # Unload VR stereo config
	Shader LoadShader(const char * vsFileName, const char * fsFileName);  # Load shader from files and bind default locations
	Shader LoadShaderFromMemory(const char * vsCode, const char * fsCode);  # Load shader from code strings and bind default locations
	int GetShaderLocation(Shader shader, const char * uniformName);  # Get shader uniform location
	int GetShaderLocationAttrib(Shader shader, const char * attribName);  # Get shader attribute location
	void SetShaderValue(Shader shader, int locIndex, const void * value, int uniformType);  # Set shader uniform value
	void SetShaderValueV(Shader shader, int locIndex, const void * value, int uniformType, int count);  # Set shader uniform value vector
	void SetShaderValueMatrix(Shader shader, int locIndex, Matrix mat);  # Set shader uniform value (matrix 4x4)
	void SetShaderValueTexture(Shader shader, int locIndex, Texture2D texture);  # Set shader uniform value for texture (sampler2d)
	void UnloadShader(Shader shader);  # Unload shader from GPU memory (VRAM)
	Ray GetMouseRay(Vector2 mousePosition, Camera camera);  # Get a ray trace from mouse position
	Matrix GetCameraMatrix(Camera camera);  # Get camera transform matrix (view matrix)
	Matrix GetCameraMatrix2D(Camera2D camera);  # Get camera 2d transform matrix
	Vector2 GetWorldToScreen(Vector3 position, Camera camera);  # Get the screen space position for a 3d world space position
	Vector2 GetScreenToWorld2D(Vector2 position, Camera2D camera);  # Get the world space position for a 2d camera screen space position
	Vector2 GetWorldToScreenEx(Vector3 position, Camera camera, int width, int height);  # Get size position for a 3d world space position
	Vector2 GetWorldToScreen2D(Vector2 position, Camera2D camera);  # Get the screen space position for a 2d camera world space position
	void SetTargetFPS(int fps);  # Set target FPS (maximum)
	int GetFPS();  # Get current FPS
	float GetFrameTime();  # Get time in seconds for last frame drawn (delta time)
	double GetTime();  # Get elapsed time in seconds since InitWindow()
	int GetRandomValue(int min, int max);  # Get a random value between min and max (both included)
	void SetRandomSeed(unsigned int seed);  # Set the seed for the random number generator
	void TakeScreenshot(const char * fileName);  # Takes a screenshot of current screen (filename extension defines format)
	void SetConfigFlags(unsigned int flags);  # Setup init configuration flags (view FLAGS)
	void SetTraceLogLevel(int logLevel);  # Set the current threshold (minimum) log level
	void * MemAlloc(int size);  # Internal memory allocator
	void * MemRealloc(void * ptr, int size);  # Internal memory reallocator
	void MemFree(void * ptr);  # Internal memory free
	void OpenURL(const char * url);  # Open URL with default system browser (if available)
	unsigned char * LoadFileData(const char * fileName, unsigned int * bytesRead);  # Load file data as byte array (read)
	void UnloadFileData(unsigned char * data);  # Unload file data allocated by LoadFileData()
	bint SaveFileData(const char * fileName, void * data, unsigned int bytesToWrite);  # Save data to file from byte array (write), returns true on success
	bint ExportDataAsCode(const char * data, unsigned int size, const char * fileName);  # Export data to code (.h), returns true on success
	char * LoadFileText(const char * fileName);  # Load text data from file (read), returns a '\0' terminated string
	void UnloadFileText(char * text);  # Unload file text data allocated by LoadFileText()
	bint SaveFileText(const char * fileName, char * text);  # Save text data to file (write), string must be '\0' terminated, returns true on success
	bint FileExists(const char * fileName);  # Check if file exists
	bint DirectoryExists(const char * dirPath);  # Check if a directory path exists
	bint IsFileExtension(const char * fileName, const char * ext);  # Check file extension (including point: .png, .wav)
	int GetFileLength(const char * fileName);  # Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)
	const char * GetFileExtension(const char * fileName);  # Get pointer to extension for a filename string (includes dot: '.png')
	const char * GetFileName(const char * filePath);  # Get pointer to filename for a path string
	const char * GetFileNameWithoutExt(const char * filePath);  # Get filename string without extension (uses static string)
	const char * GetDirectoryPath(const char * filePath);  # Get full path for a given fileName with path (uses static string)
	const char * GetPrevDirectoryPath(const char * dirPath);  # Get previous directory path for a given path (uses static string)
	const char * GetWorkingDirectory();  # Get current working directory (uses static string)
	const char * GetApplicationDirectory();  # Get the directory if the running application (uses static string)
	bint ChangeDirectory(const char * dir);  # Change working directory, return true on success
	bint IsPathFile(const char * path);  # Check if a given path is a file or a directory
	FilePathList LoadDirectoryFiles(const char * dirPath);  # Load directory filepaths
	FilePathList LoadDirectoryFilesEx(const char * basePath, const char * filter, bint scanSubdirs);  # Load directory filepaths with extension filtering and recursive directory scan
	void UnloadDirectoryFiles(FilePathList files);  # Unload filepaths
	bint IsFileDropped();  # Check if a file has been dropped into window
	FilePathList LoadDroppedFiles();  # Load dropped filepaths
	void UnloadDroppedFiles(FilePathList files);  # Unload dropped filepaths
	long GetFileModTime(const char * fileName);  # Get file modification time (last write time)
	unsigned char * CompressData(const unsigned char * data, int dataSize, int * compDataSize);  # Compress data (DEFLATE algorithm), memory must be MemFree()
	unsigned char * DecompressData(const unsigned char * compData, int compDataSize, int * dataSize);  # Decompress data (DEFLATE algorithm), memory must be MemFree()
	char * EncodeDataBase64(const unsigned char * data, int dataSize, int * outputSize);  # Encode data to Base64 string, memory must be MemFree()
	unsigned char * DecodeDataBase64(const unsigned char * data, int * outputSize);  # Decode Base64 string data, memory must be MemFree()
	bint IsKeyPressed(int key);  # Check if a key has been pressed once
	bint IsKeyDown(int key);  # Check if a key is being pressed
	bint IsKeyReleased(int key);  # Check if a key has been released once
	bint IsKeyUp(int key);  # Check if a key is NOT being pressed
	void SetExitKey(int key);  # Set a custom key to exit program (default is ESC)
	int GetKeyPressed();  # Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty
	int GetCharPressed();  # Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty
	bint IsGamepadAvailable(int gamepad);  # Check if a gamepad is available
	const char * GetGamepadName(int gamepad);  # Get gamepad internal name id
	bint IsGamepadButtonPressed(int gamepad, int button);  # Check if a gamepad button has been pressed once
	bint IsGamepadButtonDown(int gamepad, int button);  # Check if a gamepad button is being pressed
	bint IsGamepadButtonReleased(int gamepad, int button);  # Check if a gamepad button has been released once
	bint IsGamepadButtonUp(int gamepad, int button);  # Check if a gamepad button is NOT being pressed
	int GetGamepadButtonPressed();  # Get the last gamepad button pressed
	int GetGamepadAxisCount(int gamepad);  # Get gamepad axis count for a gamepad
	float GetGamepadAxisMovement(int gamepad, int axis);  # Get axis movement value for a gamepad axis
	int SetGamepadMappings(const char * mappings);  # Set internal gamepad mappings (SDL_GameControllerDB)
	bint IsMouseButtonPressed(int button);  # Check if a mouse button has been pressed once
	bint IsMouseButtonDown(int button);  # Check if a mouse button is being pressed
	bint IsMouseButtonReleased(int button);  # Check if a mouse button has been released once
	bint IsMouseButtonUp(int button);  # Check if a mouse button is NOT being pressed
	int GetMouseX();  # Get mouse position X
	int GetMouseY();  # Get mouse position Y
	Vector2 GetMousePosition();  # Get mouse position XY
	Vector2 GetMouseDelta();  # Get mouse delta between frames
	void SetMousePosition(int x, int y);  # Set mouse position XY
	void SetMouseOffset(int offsetX, int offsetY);  # Set mouse offset
	void SetMouseScale(float scaleX, float scaleY);  # Set mouse scaling
	float GetMouseWheelMove();  # Get mouse wheel movement for X or Y, whichever is larger
	Vector2 GetMouseWheelMoveV();  # Get mouse wheel movement for both X and Y
	void SetMouseCursor(int cursor);  # Set mouse cursor
	int GetTouchX();  # Get touch position X for touch point 0 (relative to screen size)
	int GetTouchY();  # Get touch position Y for touch point 0 (relative to screen size)
	Vector2 GetTouchPosition(int index);  # Get touch position XY for a touch point index (relative to screen size)
	int GetTouchPointId(int index);  # Get touch point identifier for given index
	int GetTouchPointCount();  # Get number of touch points
	void SetGesturesEnabled(unsigned int flags);  # Enable a set of gestures using flags
	bint IsGestureDetected(int gesture);  # Check if a gesture have been detected
	int GetGestureDetected();  # Get latest detected gesture
	float GetGestureHoldDuration();  # Get gesture hold time in milliseconds
	Vector2 GetGestureDragVector();  # Get gesture drag vector
	float GetGestureDragAngle();  # Get gesture drag angle
	Vector2 GetGesturePinchVector();  # Get gesture pinch delta
	float GetGesturePinchAngle();  # Get gesture pinch angle
	void SetCameraMode(Camera camera, int mode);  # Set camera mode (multiple camera modes available)
	void UpdateCamera(Camera * camera);  # Update camera position for selected mode
	void SetCameraPanControl(int keyPan);  # Set camera pan key to combine with mouse movement (free camera)
	void SetCameraAltControl(int keyAlt);  # Set camera alt key to combine with mouse movement (free camera)
	void SetCameraSmoothZoomControl(int keySmoothZoom);  # Set camera smooth zoom key to combine with mouse (free camera)
	void SetCameraMoveControls(int keyFront, int keyBack, int keyRight, int keyLeft, int keyUp, int keyDown);  # Set camera move controls (1st person and 3rd person cameras)
	void SetShapesTexture(Texture2D texture, Rectangle source);  # Set texture and rectangle to be used on shapes drawing
	void DrawPixel(int posX, int posY, Color color);  # Draw a pixel
	void DrawPixelV(Vector2 position, Color color);  # Draw a pixel (Vector version)
	void DrawLine(int startPosX, int startPosY, int endPosX, int endPosY, Color color);  # Draw a line
	void DrawLineV(Vector2 startPos, Vector2 endPos, Color color);  # Draw a line (Vector version)
	void DrawLineEx(Vector2 startPos, Vector2 endPos, float thick, Color color);  # Draw a line defining thickness
	void DrawLineBezier(Vector2 startPos, Vector2 endPos, float thick, Color color);  # Draw a line using cubic-bezier curves in-out
	void DrawLineBezierQuad(Vector2 startPos, Vector2 endPos, Vector2 controlPos, float thick, Color color);  # Draw line using quadratic bezier curves with a control point
	void DrawLineBezierCubic(Vector2 startPos, Vector2 endPos, Vector2 startControlPos, Vector2 endControlPos, float thick, Color color);  # Draw line using cubic bezier curves with 2 control points
	void DrawLineStrip(Vector2 * points, int pointCount, Color color);  # Draw lines sequence
	void DrawCircle(int centerX, int centerY, float radius, Color color);  # Draw a color-filled circle
	void DrawCircleSector(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color);  # Draw a piece of a circle
	void DrawCircleSectorLines(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color);  # Draw circle sector outline
	void DrawCircleGradient(int centerX, int centerY, float radius, Color color1, Color color2);  # Draw a gradient-filled circle
	void DrawCircleV(Vector2 center, float radius, Color color);  # Draw a color-filled circle (Vector version)
	void DrawCircleLines(int centerX, int centerY, float radius, Color color);  # Draw circle outline
	void DrawEllipse(int centerX, int centerY, float radiusH, float radiusV, Color color);  # Draw ellipse
	void DrawEllipseLines(int centerX, int centerY, float radiusH, float radiusV, Color color);  # Draw ellipse outline
	void DrawRing(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color);  # Draw ring
	void DrawRingLines(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color);  # Draw ring outline
	void DrawRectangle(int posX, int posY, int width, int height, Color color);  # Draw a color-filled rectangle
	void DrawRectangleV(Vector2 position, Vector2 size, Color color);  # Draw a color-filled rectangle (Vector version)
	void DrawRectangleRec(Rectangle rec, Color color);  # Draw a color-filled rectangle
	void DrawRectanglePro(Rectangle rec, Vector2 origin, float rotation, Color color);  # Draw a color-filled rectangle with pro parameters
	void DrawRectangleGradientV(int posX, int posY, int width, int height, Color color1, Color color2);  # Draw a vertical-gradient-filled rectangle
	void DrawRectangleGradientH(int posX, int posY, int width, int height, Color color1, Color color2);  # Draw a horizontal-gradient-filled rectangle
	void DrawRectangleGradientEx(Rectangle rec, Color col1, Color col2, Color col3, Color col4);  # Draw a gradient-filled rectangle with custom vertex colors
	void DrawRectangleLines(int posX, int posY, int width, int height, Color color);  # Draw rectangle outline
	void DrawRectangleLinesEx(Rectangle rec, float lineThick, Color color);  # Draw rectangle outline with extended parameters
	void DrawRectangleRounded(Rectangle rec, float roundness, int segments, Color color);  # Draw rectangle with rounded edges
	void DrawRectangleRoundedLines(Rectangle rec, float roundness, int segments, float lineThick, Color color);  # Draw rectangle with rounded edges outline
	void DrawTriangle(Vector2 v1, Vector2 v2, Vector2 v3, Color color);  # Draw a color-filled triangle (vertex in counter-clockwise order!)
	void DrawTriangleLines(Vector2 v1, Vector2 v2, Vector2 v3, Color color);  # Draw triangle outline (vertex in counter-clockwise order!)
	void DrawTriangleFan(Vector2 * points, int pointCount, Color color);  # Draw a triangle fan defined by points (first vertex is the center)
	void DrawTriangleStrip(Vector2 * points, int pointCount, Color color);  # Draw a triangle strip defined by points
	void DrawPoly(Vector2 center, int sides, float radius, float rotation, Color color);  # Draw a regular polygon (Vector version)
	void DrawPolyLines(Vector2 center, int sides, float radius, float rotation, Color color);  # Draw a polygon outline of n sides
	void DrawPolyLinesEx(Vector2 center, int sides, float radius, float rotation, float lineThick, Color color);  # Draw a polygon outline of n sides with extended parameters
	bint CheckCollisionRecs(Rectangle rec1, Rectangle rec2);  # Check collision between two rectangles
	bint CheckCollisionCircles(Vector2 center1, float radius1, Vector2 center2, float radius2);  # Check collision between two circles
	bint CheckCollisionCircleRec(Vector2 center, float radius, Rectangle rec);  # Check collision between circle and rectangle
	bint CheckCollisionPointRec(Vector2 point, Rectangle rec);  # Check if point is inside rectangle
	bint CheckCollisionPointCircle(Vector2 point, Vector2 center, float radius);  # Check if point is inside circle
	bint CheckCollisionPointTriangle(Vector2 point, Vector2 p1, Vector2 p2, Vector2 p3);  # Check if point is inside a triangle
	bint CheckCollisionLines(Vector2 startPos1, Vector2 endPos1, Vector2 startPos2, Vector2 endPos2, Vector2 * collisionPoint);  # Check the collision between two lines defined by two points each, returns collision point by reference
	bint CheckCollisionPointLine(Vector2 point, Vector2 p1, Vector2 p2, int threshold);  # Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]
	Rectangle GetCollisionRec(Rectangle rec1, Rectangle rec2);  # Get collision rectangle for two rectangles collision
	Image LoadImage(const char * fileName);  # Load image from file into CPU memory (RAM)
	Image LoadImageRaw(const char * fileName, int width, int height, int format, int headerSize);  # Load image from RAW file data
	Image LoadImageAnim(const char * fileName, int * frames);  # Load image sequence from file (frames appended to image.data)
	Image LoadImageFromMemory(const char * fileType, const unsigned char * fileData, int dataSize);  # Load image from memory buffer, fileType refers to extension: i.e. '.png'
	Image LoadImageFromTexture(Texture2D texture);  # Load image from GPU texture data
	Image LoadImageFromScreen();  # Load image from screen buffer and (screenshot)
	void UnloadImage(Image image);  # Unload image from CPU memory (RAM)
	bint ExportImage(Image image, const char * fileName);  # Export image data to file, returns true on success
	bint ExportImageAsCode(Image image, const char * fileName);  # Export image as code file defining an array of bytes, returns true on success
	Image GenImageColor(int width, int height, Color color);  # Generate image: plain color
	Image GenImageGradientV(int width, int height, Color top, Color bottom);  # Generate image: vertical gradient
	Image GenImageGradientH(int width, int height, Color left, Color right);  # Generate image: horizontal gradient
	Image GenImageGradientRadial(int width, int height, float density, Color inner, Color outer);  # Generate image: radial gradient
	Image GenImageChecked(int width, int height, int checksX, int checksY, Color col1, Color col2);  # Generate image: checked
	Image GenImageWhiteNoise(int width, int height, float factor);  # Generate image: white noise
	Image GenImageCellular(int width, int height, int tileSize);  # Generate image: cellular algorithm, bigger tileSize means bigger cells
	Image ImageCopy(Image image);  # Create an image duplicate (useful for transformations)
	Image ImageFromImage(Image image, Rectangle rec);  # Create an image from another image piece
	Image ImageText(const char * text, int fontSize, Color color);  # Create an image from text (default font)
	Image ImageTextEx(Font font, const char * text, float fontSize, float spacing, Color tint);  # Create an image from text (custom sprite font)
	void ImageFormat(Image * image, int newFormat);  # Convert image data to desired format
	void ImageToPOT(Image * image, Color fill);  # Convert image to POT (power-of-two)
	void ImageCrop(Image * image, Rectangle crop);  # Crop an image to a defined rectangle
	void ImageAlphaCrop(Image * image, float threshold);  # Crop image depending on alpha value
	void ImageAlphaClear(Image * image, Color color, float threshold);  # Clear alpha channel to desired color
	void ImageAlphaMask(Image * image, Image alphaMask);  # Apply alpha mask to image
	void ImageAlphaPremultiply(Image * image);  # Premultiply alpha channel
	void ImageResize(Image * image, int newWidth, int newHeight);  # Resize image (Bicubic scaling algorithm)
	void ImageResizeNN(Image * image, int newWidth, int newHeight);  # Resize image (Nearest-Neighbor scaling algorithm)
	void ImageResizeCanvas(Image * image, int newWidth, int newHeight, int offsetX, int offsetY, Color fill);  # Resize canvas and fill with color
	void ImageMipmaps(Image * image);  # Compute all mipmap levels for a provided image
	void ImageDither(Image * image, int rBpp, int gBpp, int bBpp, int aBpp);  # Dither image data to 16bpp or lower (Floyd-Steinberg dithering)
	void ImageFlipVertical(Image * image);  # Flip image vertically
	void ImageFlipHorizontal(Image * image);  # Flip image horizontally
	void ImageRotateCW(Image * image);  # Rotate image clockwise 90deg
	void ImageRotateCCW(Image * image);  # Rotate image counter-clockwise 90deg
	void ImageColorTint(Image * image, Color color);  # Modify image color: tint
	void ImageColorInvert(Image * image);  # Modify image color: invert
	void ImageColorGrayscale(Image * image);  # Modify image color: grayscale
	void ImageColorContrast(Image * image, float contrast);  # Modify image color: contrast (-100 to 100)
	void ImageColorBrightness(Image * image, int brightness);  # Modify image color: brightness (-255 to 255)
	void ImageColorReplace(Image * image, Color color, Color replace);  # Modify image color: replace color
	Color * LoadImageColors(Image image);  # Load color data from image as a Color array (RGBA - 32bit)
	Color * LoadImagePalette(Image image, int maxPaletteSize, int * colorCount);  # Load colors palette from image as a Color array (RGBA - 32bit)
	void UnloadImageColors(Color * colors);  # Unload color data loaded with LoadImageColors()
	void UnloadImagePalette(Color * colors);  # Unload colors palette loaded with LoadImagePalette()
	Rectangle GetImageAlphaBorder(Image image, float threshold);  # Get image alpha border rectangle
	Color GetImageColor(Image image, int x, int y);  # Get image pixel color at (x, y) position
	void ImageClearBackground(Image * dst, Color color);  # Clear image background with given color
	void ImageDrawPixel(Image * dst, int posX, int posY, Color color);  # Draw pixel within an image
	void ImageDrawPixelV(Image * dst, Vector2 position, Color color);  # Draw pixel within an image (Vector version)
	void ImageDrawLine(Image * dst, int startPosX, int startPosY, int endPosX, int endPosY, Color color);  # Draw line within an image
	void ImageDrawLineV(Image * dst, Vector2 start, Vector2 end, Color color);  # Draw line within an image (Vector version)
	void ImageDrawCircle(Image * dst, int centerX, int centerY, int radius, Color color);  # Draw circle within an image
	void ImageDrawCircleV(Image * dst, Vector2 center, int radius, Color color);  # Draw circle within an image (Vector version)
	void ImageDrawRectangle(Image * dst, int posX, int posY, int width, int height, Color color);  # Draw rectangle within an image
	void ImageDrawRectangleV(Image * dst, Vector2 position, Vector2 size, Color color);  # Draw rectangle within an image (Vector version)
	void ImageDrawRectangleRec(Image * dst, Rectangle rec, Color color);  # Draw rectangle within an image
	void ImageDrawRectangleLines(Image * dst, Rectangle rec, int thick, Color color);  # Draw rectangle lines within an image
	void ImageDraw(Image * dst, Image src, Rectangle srcRec, Rectangle dstRec, Color tint);  # Draw a source image within a destination image (tint applied to source)
	void ImageDrawText(Image * dst, const char * text, int posX, int posY, int fontSize, Color color);  # Draw text (using default font) within an image (destination)
	void ImageDrawTextEx(Image * dst, Font font, const char * text, Vector2 position, float fontSize, float spacing, Color tint);  # Draw text (custom sprite font) within an image (destination)
	Texture2D LoadTexture(const char * fileName);  # Load texture from file into GPU memory (VRAM)
	Texture2D LoadTextureFromImage(Image image);  # Load texture from image data
	TextureCubemap LoadTextureCubemap(Image image, int layout);  # Load cubemap from image, multiple image cubemap layouts supported
	RenderTexture2D LoadRenderTexture(int width, int height);  # Load texture for rendering (framebuffer)
	void UnloadTexture(Texture2D texture);  # Unload texture from GPU memory (VRAM)
	void UnloadRenderTexture(RenderTexture2D target);  # Unload render texture from GPU memory (VRAM)
	void UpdateTexture(Texture2D texture, const void * pixels);  # Update GPU texture with new data
	void UpdateTextureRec(Texture2D texture, Rectangle rec, const void * pixels);  # Update GPU texture rectangle with new data
	void GenTextureMipmaps(Texture2D * texture);  # Generate GPU mipmaps for a texture
	void SetTextureFilter(Texture2D texture, int filter);  # Set texture scaling filter mode
	void SetTextureWrap(Texture2D texture, int wrap);  # Set texture wrapping mode
	void DrawTexture(Texture2D texture, int posX, int posY, Color tint);  # Draw a Texture2D
	void DrawTextureV(Texture2D texture, Vector2 position, Color tint);  # Draw a Texture2D with position defined as Vector2
	void DrawTextureEx(Texture2D texture, Vector2 position, float rotation, float scale, Color tint);  # Draw a Texture2D with extended parameters
	void DrawTextureRec(Texture2D texture, Rectangle source, Vector2 position, Color tint);  # Draw a part of a texture defined by a rectangle
	void DrawTextureQuad(Texture2D texture, Vector2 tiling, Vector2 offset, Rectangle quad, Color tint);  # Draw texture quad with tiling and offset parameters
	void DrawTextureTiled(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, float scale, Color tint);  # Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest.
	void DrawTexturePro(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, Color tint);  # Draw a part of a texture defined by a rectangle with 'pro' parameters
	void DrawTextureNPatch(Texture2D texture, NPatchInfo nPatchInfo, Rectangle dest, Vector2 origin, float rotation, Color tint);  # Draws a texture (or part of it) that stretches or shrinks nicely
	void DrawTexturePoly(Texture2D texture, Vector2 center, Vector2 * points, Vector2 * texcoords, int pointCount, Color tint);  # Draw a textured polygon
	Color Fade(Color color, float alpha);  # Get color with alpha applied, alpha goes from 0.0f to 1.0f
	int ColorToInt(Color color);  # Get hexadecimal value for a Color
	Vector4 ColorNormalize(Color color);  # Get Color normalized as float [0..1]
	Color ColorFromNormalized(Vector4 normalized);  # Get Color from normalized values [0..1]
	Vector3 ColorToHSV(Color color);  # Get HSV values for a Color, hue [0..360], saturation/value [0..1]
	Color ColorFromHSV(float hue, float saturation, float value);  # Get a Color from HSV values, hue [0..360], saturation/value [0..1]
	Color ColorAlpha(Color color, float alpha);  # Get color with alpha applied, alpha goes from 0.0f to 1.0f
	Color ColorAlphaBlend(Color dst, Color src, Color tint);  # Get src alpha-blended into dst color with tint
	Color GetColor(unsigned int hexValue);  # Get Color structure from hexadecimal value
	Color GetPixelColor(void * srcPtr, int format);  # Get Color from a source pixel pointer of certain format
	void SetPixelColor(void * dstPtr, Color color, int format);  # Set color formatted into destination pixel pointer
	int GetPixelDataSize(int width, int height, int format);  # Get pixel data size in bytes for certain format
	Font GetFontDefault();  # Get the default Font
	Font LoadFont(const char * fileName);  # Load font from file into GPU memory (VRAM)
	Font LoadFontEx(const char * fileName, int fontSize, int * fontChars, int glyphCount);  # Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set
	Font LoadFontFromImage(Image image, Color key, int firstChar);  # Load font from Image (XNA style)
	Font LoadFontFromMemory(const char * fileType, const unsigned char * fileData, int dataSize, int fontSize, int * fontChars, int glyphCount);  # Load font from memory buffer, fileType refers to extension: i.e. '.ttf'
	GlyphInfo * LoadFontData(const unsigned char * fileData, int dataSize, int fontSize, int * fontChars, int glyphCount, int type);  # Load font data for further use
	Image GenImageFontAtlas(const GlyphInfo * chars, Rectangle ** recs, int glyphCount, int fontSize, int padding, int packMethod);  # Generate image font atlas using chars info
	void UnloadFontData(GlyphInfo * chars, int glyphCount);  # Unload font chars info data (RAM)
	void UnloadFont(Font font);  # Unload font from GPU memory (VRAM)
	bint ExportFontAsCode(Font font, const char * fileName);  # Export font as code file, returns true on success
	void DrawFPS(int posX, int posY);  # Draw current FPS
	void DrawText(const char * text, int posX, int posY, int fontSize, Color color);  # Draw text (using default font)
	void DrawTextEx(Font font, const char * text, Vector2 position, float fontSize, float spacing, Color tint);  # Draw text using font and additional parameters
	void DrawTextPro(Font font, const char * text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint);  # Draw text using Font and pro parameters (rotation)
	void DrawTextCodepoint(Font font, int codepoint, Vector2 position, float fontSize, Color tint);  # Draw one character (codepoint)
	void DrawTextCodepoints(Font font, const int * codepoints, int count, Vector2 position, float fontSize, float spacing, Color tint);  # Draw multiple character (codepoint)
	int MeasureText(const char * text, int fontSize);  # Measure string width for default font
	Vector2 MeasureTextEx(Font font, const char * text, float fontSize, float spacing);  # Measure string size for Font
	int GetGlyphIndex(Font font, int codepoint);  # Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found
	GlyphInfo GetGlyphInfo(Font font, int codepoint);  # Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found
	Rectangle GetGlyphAtlasRec(Font font, int codepoint);  # Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found
	int * LoadCodepoints(const char * text, int * count);  # Load all codepoints from a UTF-8 text string, codepoints count returned by parameter
	void UnloadCodepoints(int * codepoints);  # Unload codepoints data from memory
	int GetCodepointCount(const char * text);  # Get total number of codepoints in a UTF-8 encoded string
	int GetCodepoint(const char * text, int * bytesProcessed);  # Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure
	const char * CodepointToUTF8(int codepoint, int * byteSize);  # Encode one codepoint into UTF-8 byte array (array length returned as parameter)
	char * TextCodepointsToUTF8(const int * codepoints, int length);  # Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)
	int TextCopy(char * dst, const char * src);  # Copy one string to another, returns bytes copied
	bint TextIsEqual(const char * text1, const char * text2);  # Check if two text string are equal
	unsigned int TextLength(const char * text);  # Get text length, checks for '\0' ending
	const char * TextSubtext(const char * text, int position, int length);  # Get a piece of a text string
	char * TextReplace(char * text, const char * replace, const char * _by);  # Replace text string (WARNING: memory must be freed!)
	char * TextInsert(const char * text, const char * insert, int position);  # Insert text in a position (WARNING: memory must be freed!)
	const char * TextJoin(const char ** textList, int count, const char * delimiter);  # Join text strings with delimiter
	const char ** TextSplit(const char * text, char delimiter, int * count);  # Split text into multiple strings
	void TextAppend(char * text, const char * append, int * position);  # Append text at specific position and move cursor!
	int TextFindIndex(const char * text, const char * find);  # Find first text occurrence within a string
	const char * TextToUpper(const char * text);  # Get upper case version of provided string
	const char * TextToLower(const char * text);  # Get lower case version of provided string
	const char * TextToPascal(const char * text);  # Get Pascal case notation version of provided string
	int TextToInteger(const char * text);  # Get integer value from text (negative values not supported)
	void DrawLine3D(Vector3 startPos, Vector3 endPos, Color color);  # Draw a line in 3D world space
	void DrawPoint3D(Vector3 position, Color color);  # Draw a point in 3D space, actually a small line
	void DrawCircle3D(Vector3 center, float radius, Vector3 rotationAxis, float rotationAngle, Color color);  # Draw a circle in 3D world space
	void DrawTriangle3D(Vector3 v1, Vector3 v2, Vector3 v3, Color color);  # Draw a color-filled triangle (vertex in counter-clockwise order!)
	void DrawTriangleStrip3D(Vector3 * points, int pointCount, Color color);  # Draw a triangle strip defined by points
	void DrawCube(Vector3 position, float width, float height, float length, Color color);  # Draw cube
	void DrawCubeV(Vector3 position, Vector3 size, Color color);  # Draw cube (Vector version)
	void DrawCubeWires(Vector3 position, float width, float height, float length, Color color);  # Draw cube wires
	void DrawCubeWiresV(Vector3 position, Vector3 size, Color color);  # Draw cube wires (Vector version)
	void DrawCubeTexture(Texture2D texture, Vector3 position, float width, float height, float length, Color color);  # Draw cube textured
	void DrawCubeTextureRec(Texture2D texture, Rectangle source, Vector3 position, float width, float height, float length, Color color);  # Draw cube with a region of a texture
	void DrawSphere(Vector3 centerPos, float radius, Color color);  # Draw sphere
	void DrawSphereEx(Vector3 centerPos, float radius, int rings, int slices, Color color);  # Draw sphere with extended parameters
	void DrawSphereWires(Vector3 centerPos, float radius, int rings, int slices, Color color);  # Draw sphere wires
	void DrawCylinder(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color);  # Draw a cylinder/cone
	void DrawCylinderEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color);  # Draw a cylinder with base at startPos and top at endPos
	void DrawCylinderWires(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color);  # Draw a cylinder/cone wires
	void DrawCylinderWiresEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color);  # Draw a cylinder wires with base at startPos and top at endPos
	void DrawPlane(Vector3 centerPos, Vector2 size, Color color);  # Draw a plane XZ
	void DrawRay(Ray ray, Color color);  # Draw a ray line
	void DrawGrid(int slices, float spacing);  # Draw a grid (centered at (0, 0, 0))
	Model LoadModel(const char * fileName);  # Load model from files (meshes and materials)
	Model LoadModelFromMesh(Mesh mesh);  # Load model from generated mesh (default material)
	void UnloadModel(Model model);  # Unload model (including meshes) from memory (RAM and/or VRAM)
	void UnloadModelKeepMeshes(Model model);  # Unload model (but not meshes) from memory (RAM and/or VRAM)
	BoundingBox GetModelBoundingBox(Model model);  # Compute model bounding box limits (considers all meshes)
	void DrawModel(Model model, Vector3 position, float scale, Color tint);  # Draw a model (with texture if set)
	void DrawModelEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint);  # Draw a model with extended parameters
	void DrawModelWires(Model model, Vector3 position, float scale, Color tint);  # Draw a model wires (with texture if set)
	void DrawModelWiresEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint);  # Draw a model wires (with texture if set) with extended parameters
	void DrawBoundingBox(BoundingBox box, Color color);  # Draw bounding box (wires)
	void DrawBillboard(Camera camera, Texture2D texture, Vector3 position, float size, Color tint);  # Draw a billboard texture
	void DrawBillboardRec(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector2 size, Color tint);  # Draw a billboard texture defined by source
	void DrawBillboardPro(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector3 up, Vector2 size, Vector2 origin, float rotation, Color tint);  # Draw a billboard texture defined by source and rotation
	void UploadMesh(Mesh * mesh, bint dynamic);  # Upload mesh vertex data in GPU and provide VAO/VBO ids
	void UpdateMeshBuffer(Mesh mesh, int index, const void * data, int dataSize, int offset);  # Update mesh vertex data in GPU for a specific buffer index
	void UnloadMesh(Mesh mesh);  # Unload mesh data from CPU and GPU
	void DrawMesh(Mesh mesh, Material material, Matrix transform);  # Draw a 3d mesh with material and transform
	void DrawMeshInstanced(Mesh mesh, Material material, const Matrix * transforms, int instances);  # Draw multiple mesh instances with material and different transforms
	bint ExportMesh(Mesh mesh, const char * fileName);  # Export mesh data to file, returns true on success
	BoundingBox GetMeshBoundingBox(Mesh mesh);  # Compute mesh bounding box limits
	void GenMeshTangents(Mesh * mesh);  # Compute mesh tangents
	Mesh GenMeshPoly(int sides, float radius);  # Generate polygonal mesh
	Mesh GenMeshPlane(float width, float length, int resX, int resZ);  # Generate plane mesh (with subdivisions)
	Mesh GenMeshCube(float width, float height, float length);  # Generate cuboid mesh
	Mesh GenMeshSphere(float radius, int rings, int slices);  # Generate sphere mesh (standard sphere)
	Mesh GenMeshHemiSphere(float radius, int rings, int slices);  # Generate half-sphere mesh (no bottom cap)
	Mesh GenMeshCylinder(float radius, float height, int slices);  # Generate cylinder mesh
	Mesh GenMeshCone(float radius, float height, int slices);  # Generate cone/pyramid mesh
	Mesh GenMeshTorus(float radius, float size, int radSeg, int sides);  # Generate torus mesh
	Mesh GenMeshKnot(float radius, float size, int radSeg, int sides);  # Generate trefoil knot mesh
	Mesh GenMeshHeightmap(Image heightmap, Vector3 size);  # Generate heightmap mesh from image data
	Mesh GenMeshCubicmap(Image cubicmap, Vector3 cubeSize);  # Generate cubes-based map mesh from image data
	Material * LoadMaterials(const char * fileName, int * materialCount);  # Load materials from model file
	Material LoadMaterialDefault();  # Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)
	void UnloadMaterial(Material material);  # Unload material from GPU memory (VRAM)
	void SetMaterialTexture(Material * material, int mapType, Texture2D texture);  # Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)
	void SetModelMeshMaterial(Model * model, int meshId, int materialId);  # Set material for a mesh
	ModelAnimation * LoadModelAnimations(const char * fileName, unsigned int * animCount);  # Load model animations from file
	void UpdateModelAnimation(Model model, ModelAnimation anim, int frame);  # Update model animation pose
	void UnloadModelAnimation(ModelAnimation anim);  # Unload animation data
	void UnloadModelAnimations(ModelAnimation * animations, unsigned int count);  # Unload animation array data
	bint IsModelAnimationValid(Model model, ModelAnimation anim);  # Check model animation skeleton match
	bint CheckCollisionSpheres(Vector3 center1, float radius1, Vector3 center2, float radius2);  # Check collision between two spheres
	bint CheckCollisionBoxes(BoundingBox box1, BoundingBox box2);  # Check collision between two bounding boxes
	bint CheckCollisionBoxSphere(BoundingBox box, Vector3 center, float radius);  # Check collision between box and sphere
	RayCollision GetRayCollisionSphere(Ray ray, Vector3 center, float radius);  # Get collision info between ray and sphere
	RayCollision GetRayCollisionBox(Ray ray, BoundingBox box);  # Get collision info between ray and box
	RayCollision GetRayCollisionMesh(Ray ray, Mesh mesh, Matrix transform);  # Get collision info between ray and mesh
	RayCollision GetRayCollisionTriangle(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3);  # Get collision info between ray and triangle
	RayCollision GetRayCollisionQuad(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3, Vector3 p4);  # Get collision info between ray and quad
	void InitAudioDevice();  # Initialize audio device and context
	void CloseAudioDevice();  # Close the audio device and context
	bint IsAudioDeviceReady();  # Check if audio device has been initialized successfully
	void SetMasterVolume(float volume);  # Set master volume (listener)
	Wave LoadWave(const char * fileName);  # Load wave data from file
	Wave LoadWaveFromMemory(const char * fileType, const unsigned char * fileData, int dataSize);  # Load wave from memory buffer, fileType refers to extension: i.e. '.wav'
	Sound LoadSound(const char * fileName);  # Load sound from file
	Sound LoadSoundFromWave(Wave wave);  # Load sound from wave data
	void UpdateSound(Sound sound, const void * data, int sampleCount);  # Update sound buffer with new data
	void UnloadWave(Wave wave);  # Unload wave data
	void UnloadSound(Sound sound);  # Unload sound
	bint ExportWave(Wave wave, const char * fileName);  # Export wave data to file, returns true on success
	bint ExportWaveAsCode(Wave wave, const char * fileName);  # Export wave sample data to code (.h), returns true on success
	void PlaySound(Sound sound);  # Play a sound
	void StopSound(Sound sound);  # Stop playing a sound
	void PauseSound(Sound sound);  # Pause a sound
	void ResumeSound(Sound sound);  # Resume a paused sound
	void PlaySoundMulti(Sound sound);  # Play a sound (using multichannel buffer pool)
	void StopSoundMulti();  # Stop any sound playing (using multichannel buffer pool)
	int GetSoundsPlaying();  # Get number of sounds playing in the multichannel
	bint IsSoundPlaying(Sound sound);  # Check if a sound is currently playing
	void SetSoundVolume(Sound sound, float volume);  # Set volume for a sound (1.0 is max level)
	void SetSoundPitch(Sound sound, float pitch);  # Set pitch for a sound (1.0 is base level)
	void SetSoundPan(Sound sound, float pan);  # Set pan for a sound (0.5 is center)
	Wave WaveCopy(Wave wave);  # Copy a wave to a new wave
	void WaveCrop(Wave * wave, int initSample, int finalSample);  # Crop a wave to defined samples range
	void WaveFormat(Wave * wave, int sampleRate, int sampleSize, int channels);  # Convert wave data to desired format
	float * LoadWaveSamples(Wave wave);  # Load samples data from wave as a 32bit float data array
	void UnloadWaveSamples(float * samples);  # Unload samples data loaded with LoadWaveSamples()
	Music LoadMusicStream(const char * fileName);  # Load music stream from file
	Music LoadMusicStreamFromMemory(const char * fileType, const unsigned char * data, int dataSize);  # Load music stream from data
	void UnloadMusicStream(Music music);  # Unload music stream
	void PlayMusicStream(Music music);  # Start music playing
	bint IsMusicStreamPlaying(Music music);  # Check if music is playing
	void UpdateMusicStream(Music music);  # Updates buffers for music streaming
	void StopMusicStream(Music music);  # Stop music playing
	void PauseMusicStream(Music music);  # Pause music playing
	void ResumeMusicStream(Music music);  # Resume playing paused music
	void SeekMusicStream(Music music, float position);  # Seek music to a position (in seconds)
	void SetMusicVolume(Music music, float volume);  # Set volume for music (1.0 is max level)
	void SetMusicPitch(Music music, float pitch);  # Set pitch for a music (1.0 is base level)
	void SetMusicPan(Music music, float pan);  # Set pan for a music (0.5 is center)
	float GetMusicTimeLength(Music music);  # Get music time length (in seconds)
	float GetMusicTimePlayed(Music music);  # Get current music time played (in seconds)
	AudioStream LoadAudioStream(unsigned int sampleRate, unsigned int sampleSize, unsigned int channels);  # Load audio stream (to stream raw audio pcm data)
	void UnloadAudioStream(AudioStream stream);  # Unload audio stream and free memory
	void UpdateAudioStream(AudioStream stream, const void * data, int frameCount);  # Update audio stream buffers with data
	bint IsAudioStreamProcessed(AudioStream stream);  # Check if any audio stream buffers requires refill
	void PlayAudioStream(AudioStream stream);  # Play audio stream
	void PauseAudioStream(AudioStream stream);  # Pause audio stream
	void ResumeAudioStream(AudioStream stream);  # Resume audio stream
	bint IsAudioStreamPlaying(AudioStream stream);  # Check if audio stream is playing
	void StopAudioStream(AudioStream stream);  # Stop audio stream
	void SetAudioStreamVolume(AudioStream stream, float volume);  # Set volume for audio stream (1.0 is max level)
	void SetAudioStreamPitch(AudioStream stream, float pitch);  # Set pitch for audio stream (1.0 is base level)
	void SetAudioStreamPan(AudioStream stream, float pan);  # Set pan for audio stream (0.5 is centered)
	void SetAudioStreamBufferSizeDefault(int size);  # Default size for new audio streams
	
cdef extern from "raymath.h":
	DEF EPSILON = 1e-06
	
	
	#  NOTE: Helper types to be used instead of array return types for *ToFloat functions
	ctypedef struct float3:
		float[3] v;
	
	#  
	ctypedef struct float16:
		float[16] v;
	
	
	float Clamp(float value, float min, float max);
	float Lerp(float start, float end, float amount);
	float Normalize(float value, float start, float end);
	float Remap(float value, float inputStart, float inputEnd, float outputStart, float outputEnd);
	float Wrap(float value, float min, float max);
	int FloatEquals(float x, float y);
	Vector2 Vector2Zero();
	Vector2 Vector2One();
	Vector2 Vector2Add(Vector2 v1, Vector2 v2);
	Vector2 Vector2AddValue(Vector2 v, float add);
	Vector2 Vector2Subtract(Vector2 v1, Vector2 v2);
	Vector2 Vector2SubtractValue(Vector2 v, float sub);
	float Vector2Length(Vector2 v);
	float Vector2LengthSqr(Vector2 v);
	float Vector2DotProduct(Vector2 v1, Vector2 v2);
	float Vector2Distance(Vector2 v1, Vector2 v2);
	float Vector2DistanceSqr(Vector2 v1, Vector2 v2);
	float Vector2Angle(Vector2 v1, Vector2 v2);
	Vector2 Vector2Scale(Vector2 v, float scale);
	Vector2 Vector2Multiply(Vector2 v1, Vector2 v2);
	Vector2 Vector2Negate(Vector2 v);
	Vector2 Vector2Divide(Vector2 v1, Vector2 v2);
	Vector2 Vector2Normalize(Vector2 v);
	Vector2 Vector2Transform(Vector2 v, Matrix mat);
	Vector2 Vector2Lerp(Vector2 v1, Vector2 v2, float amount);
	Vector2 Vector2Reflect(Vector2 v, Vector2 normal);
	Vector2 Vector2Rotate(Vector2 v, float angle);
	Vector2 Vector2MoveTowards(Vector2 v, Vector2 target, float maxDistance);
	Vector2 Vector2Invert(Vector2 v);
	Vector2 Vector2Clamp(Vector2 v, Vector2 min, Vector2 max);
	Vector2 Vector2ClampValue(Vector2 v, float min, float max);
	int Vector2Equals(Vector2 p, Vector2 q);
	Vector3 Vector3Zero();
	Vector3 Vector3One();
	Vector3 Vector3Add(Vector3 v1, Vector3 v2);
	Vector3 Vector3AddValue(Vector3 v, float add);
	Vector3 Vector3Subtract(Vector3 v1, Vector3 v2);
	Vector3 Vector3SubtractValue(Vector3 v, float sub);
	Vector3 Vector3Scale(Vector3 v, float scalar);
	Vector3 Vector3Multiply(Vector3 v1, Vector3 v2);
	Vector3 Vector3CrossProduct(Vector3 v1, Vector3 v2);
	Vector3 Vector3Perpendicular(Vector3 v);
	float Vector3Length(const Vector3 v);
	float Vector3LengthSqr(const Vector3 v);
	float Vector3DotProduct(Vector3 v1, Vector3 v2);
	float Vector3Distance(Vector3 v1, Vector3 v2);
	float Vector3DistanceSqr(Vector3 v1, Vector3 v2);
	float Vector3Angle(Vector3 v1, Vector3 v2);
	Vector3 Vector3Negate(Vector3 v);
	Vector3 Vector3Divide(Vector3 v1, Vector3 v2);
	Vector3 Vector3Normalize(Vector3 v);
	void Vector3OrthoNormalize(Vector3 * v1, Vector3 * v2);
	Vector3 Vector3Transform(Vector3 v, Matrix mat);
	Vector3 Vector3RotateByQuaternion(Vector3 v, Quaternion q);
	Vector3 Vector3RotateByAxisAngle(Vector3 v, Vector3 axis, float angle);
	Vector3 Vector3Lerp(Vector3 v1, Vector3 v2, float amount);
	Vector3 Vector3Reflect(Vector3 v, Vector3 normal);
	Vector3 Vector3Min(Vector3 v1, Vector3 v2);
	Vector3 Vector3Max(Vector3 v1, Vector3 v2);
	Vector3 Vector3Barycenter(Vector3 p, Vector3 a, Vector3 b, Vector3 c);
	Vector3 Vector3Unproject(Vector3 source, Matrix projection, Matrix view);
	float3 Vector3ToFloatV(Vector3 v);
	Vector3 Vector3Invert(Vector3 v);
	Vector3 Vector3Clamp(Vector3 v, Vector3 min, Vector3 max);
	Vector3 Vector3ClampValue(Vector3 v, float min, float max);
	int Vector3Equals(Vector3 p, Vector3 q);
	Vector3 Vector3Refract(Vector3 v, Vector3 n, float r);
	float MatrixDeterminant(Matrix mat);
	float MatrixTrace(Matrix mat);
	Matrix MatrixTranspose(Matrix mat);
	Matrix MatrixInvert(Matrix mat);
	Matrix MatrixIdentity();
	Matrix MatrixAdd(Matrix left, Matrix right);
	Matrix MatrixSubtract(Matrix left, Matrix right);
	Matrix MatrixMultiply(Matrix left, Matrix right);
	Matrix MatrixTranslate(float x, float y, float z);
	Matrix MatrixRotate(Vector3 axis, float angle);
	Matrix MatrixRotateX(float angle);
	Matrix MatrixRotateY(float angle);
	Matrix MatrixRotateZ(float angle);
	Matrix MatrixRotateXYZ(Vector3 angle);
	Matrix MatrixRotateZYX(Vector3 angle);
	Matrix MatrixScale(float x, float y, float z);
	Matrix MatrixFrustum(double left, double right, double bottom, double top, double near, double far);
	Matrix MatrixPerspective(double fovy, double aspect, double near, double far);
	Matrix MatrixOrtho(double left, double right, double bottom, double top, double near, double far);
	Matrix MatrixLookAt(Vector3 eye, Vector3 target, Vector3 up);
	float16 MatrixToFloatV(Matrix mat);
	Quaternion QuaternionAdd(Quaternion q1, Quaternion q2);
	Quaternion QuaternionAddValue(Quaternion q, float add);
	Quaternion QuaternionSubtract(Quaternion q1, Quaternion q2);
	Quaternion QuaternionSubtractValue(Quaternion q, float sub);
	Quaternion QuaternionIdentity();
	float QuaternionLength(Quaternion q);
	Quaternion QuaternionNormalize(Quaternion q);
	Quaternion QuaternionInvert(Quaternion q);
	Quaternion QuaternionMultiply(Quaternion q1, Quaternion q2);
	Quaternion QuaternionScale(Quaternion q, float mul);
	Quaternion QuaternionDivide(Quaternion q1, Quaternion q2);
	Quaternion QuaternionLerp(Quaternion q1, Quaternion q2, float amount);
	Quaternion QuaternionNlerp(Quaternion q1, Quaternion q2, float amount);
	Quaternion QuaternionSlerp(Quaternion q1, Quaternion q2, float amount);
	Quaternion QuaternionFromVector3ToVector3(Vector3 _from, Vector3 to);
	Quaternion QuaternionFromMatrix(Matrix mat);
	Matrix QuaternionToMatrix(Quaternion q);
	Quaternion QuaternionFromAxisAngle(Vector3 axis, float angle);
	void QuaternionToAxisAngle(Quaternion q, Vector3 * outAxis, float * outAngle);
	Quaternion QuaternionFromEuler(float pitch, float yaw, float roll);
	Vector3 QuaternionToEuler(Quaternion q);
	Quaternion QuaternionTransform(Quaternion q, Matrix mat);
	int QuaternionEquals(Quaternion p, Quaternion q);
	
cdef extern from "raygui.h":
	DEF RAYGUI_VERSION = "3.2"
	DEF SCROLLBAR_LEFT_SIDE = 0
	DEF SCROLLBAR_RIGHT_SIDE = 1
	DEF RAYGUI_ICON_SIZE = 16  # Size of icons in pixels (squared)
	DEF RAYGUI_ICON_MAX_ICONS = 256  # Maximum number of icons
	DEF RAYGUI_ICON_MAX_NAME_LENGTH = 32  # Maximum length of icon name id
	DEF RAYGUI_MAX_CONTROLS = 16  # Maximum number of standard controls
	DEF RAYGUI_MAX_PROPS_BASE = 16  # Maximum number of standard properties
	DEF RAYGUI_MAX_PROPS_EXTENDED = 8  # Maximum number of extended properties
	DEF KEY_RIGHT = 262
	DEF KEY_LEFT = 263
	DEF KEY_DOWN = 264
	DEF KEY_UP = 265
	DEF KEY_BACKSPACE = 259
	DEF KEY_ENTER = 257
	DEF RAYGUI_WINDOWBOX_STATUSBAR_HEIGHT = 24
	DEF RAYGUI_GROUPBOX_LINE_THICK = 1
	DEF RAYGUI_LINE_MARGIN_TEXT = 12
	DEF RAYGUI_LINE_TEXT_PADDING = 4
	DEF RAYGUI_PANEL_BORDER_WIDTH = 1
	DEF RAYGUI_TOGGLEGROUP_MAX_ITEMS = 32
	DEF RAYGUI_VALUEBOX_MAX_CHARS = 32
	DEF RAYGUI_COLORBARALPHA_CHECKED_SIZE = 10
	DEF RAYGUI_MESSAGEBOX_BUTTON_HEIGHT = 24
	DEF RAYGUI_MESSAGEBOX_BUTTON_PADDING = 12
	DEF RAYGUI_TEXTINPUTBOX_BUTTON_HEIGHT = 28
	DEF RAYGUI_TEXTINPUTBOX_BUTTON_PADDING = 12
	DEF RAYGUI_TEXTINPUTBOX_HEIGHT = 28
	DEF RAYGUI_GRID_ALPHA = 0.15
	DEF MAX_LINE_BUFFER_SIZE = 256
	DEF ICON_TEXT_PADDING = 4
	DEF RAYGUI_TEXTSPLIT_MAX_ITEMS = 128
	DEF RAYGUI_TEXTSPLIT_MAX_TEXT_SIZE = 1024
	DEF RAYGUI_TEXTFORMAT_MAX_SIZE = 256
	
	#  Gui control state
	ctypedef enum GuiState:
		STATE_NORMAL = 0,
		STATE_FOCUSED = 1,
		STATE_PRESSED = 2,
		STATE_DISABLED = 3
	
	
	#  Gui control text alignment
	ctypedef enum GuiTextAlignment:
		TEXT_ALIGN_LEFT = 0,
		TEXT_ALIGN_CENTER = 1,
		TEXT_ALIGN_RIGHT = 2
	
	
	#  Gui controls
	ctypedef enum GuiControl:
		DEFAULT = 0,
		LABEL = 1,  #  Used also for: LABELBUTTON
		BUTTON = 2,
		TOGGLE = 3,  #  Used also for: TOGGLEGROUP
		SLIDER = 4,  #  Used also for: SLIDERBAR
		PROGRESSBAR = 5,
		CHECKBOX = 6,
		COMBOBOX = 7,
		DROPDOWNBOX = 8,
		TEXTBOX = 9,  #  Used also for: TEXTBOXMULTI
		VALUEBOX = 10,
		SPINNER = 11,  #  Uses: BUTTON, VALUEBOX
		LISTVIEW = 12,
		COLORPICKER = 13,
		SCROLLBAR = 14,
		STATUSBAR = 15
	
	
	#  Gui base properties for every control
	ctypedef enum GuiControlProperty:
		BORDER_COLOR_NORMAL = 0,
		BASE_COLOR_NORMAL = 1,
		TEXT_COLOR_NORMAL = 2,
		BORDER_COLOR_FOCUSED = 3,
		BASE_COLOR_FOCUSED = 4,
		TEXT_COLOR_FOCUSED = 5,
		BORDER_COLOR_PRESSED = 6,
		BASE_COLOR_PRESSED = 7,
		TEXT_COLOR_PRESSED = 8,
		BORDER_COLOR_DISABLED = 9,
		BASE_COLOR_DISABLED = 10,
		TEXT_COLOR_DISABLED = 11,
		BORDER_WIDTH = 12,
		TEXT_PADDING = 13,
		TEXT_ALIGNMENT = 14,
		RESERVED = 15
	
	
	#  DEFAULT extended properties
	ctypedef enum GuiDefaultProperty:
		TEXT_SIZE = 16,  #  Text size (glyphs max height)
		TEXT_SPACING = 17,  #  Text spacing between glyphs
		LINE_COLOR = 18,  #  Line control color
		BACKGROUND_COLOR = 19  #  Background color
	
	
	#  Toggle/ToggleGroup
	ctypedef enum GuiToggleProperty:
		GROUP_PADDING = 16  #  ToggleGroup separation between toggles
	
	
	#  Slider/SliderBar
	ctypedef enum GuiSliderProperty:
		SLIDER_WIDTH = 16,  #  Slider size of internal bar
		SLIDER_PADDING = 17  #  Slider/SliderBar internal bar padding
	
	
	#  ProgressBar
	ctypedef enum GuiProgressBarProperty:
		PROGRESS_PADDING = 16  #  ProgressBar internal padding
	
	
	#  ScrollBar
	ctypedef enum GuiScrollBarProperty:
		ARROWS_SIZE = 16,
		ARROWS_VISIBLE = 17,
		SCROLL_SLIDER_PADDING = 18,  #  (SLIDERBAR, SLIDER_PADDING)
		SCROLL_SLIDER_SIZE = 19,
		SCROLL_PADDING = 20,
		SCROLL_SPEED = 21
	
	
	#  CheckBox
	ctypedef enum GuiCheckBoxProperty:
		CHECK_PADDING = 16  #  CheckBox internal check padding
	
	
	#  ComboBox
	ctypedef enum GuiComboBoxProperty:
		COMBO_BUTTON_WIDTH = 16,  #  ComboBox right button width
		COMBO_BUTTON_SPACING = 17  #  ComboBox button separation
	
	
	#  DropdownBox
	ctypedef enum GuiDropdownBoxProperty:
		ARROW_PADDING = 16,  #  DropdownBox arrow separation from border and items
		DROPDOWN_ITEMS_SPACING = 17  #  DropdownBox items separation
	
	
	#  TextBox/TextBoxMulti/ValueBox/Spinner
	ctypedef enum GuiTextBoxProperty:
		TEXT_INNER_PADDING = 16,  #  TextBox/TextBoxMulti/ValueBox/Spinner inner text padding
		TEXT_LINES_SPACING = 17  #  TextBoxMulti lines separation
	
	
	#  Spinner
	ctypedef enum GuiSpinnerProperty:
		SPIN_BUTTON_WIDTH = 16,  #  Spinner left/right buttons width
		SPIN_BUTTON_SPACING = 17  #  Spinner buttons separation
	
	
	#  ListView
	ctypedef enum GuiListViewProperty:
		LIST_ITEMS_HEIGHT = 16,  #  ListView items height
		LIST_ITEMS_SPACING = 17,  #  ListView items separation
		SCROLLBAR_WIDTH = 18,  #  ListView scrollbar size (usually width)
		SCROLLBAR_SIDE = 19  #  ListView scrollbar side (0-left, 1-right)
	
	
	#  ColorPicker
	ctypedef enum GuiColorPickerProperty:
		COLOR_SELECTOR_SIZE = 16,
		HUEBAR_WIDTH = 17,  #  ColorPicker right hue bar width
		HUEBAR_PADDING = 18,  #  ColorPicker right hue bar separation from panel
		HUEBAR_SELECTOR_HEIGHT = 19,  #  ColorPicker right hue bar selector height
		HUEBAR_SELECTOR_OVERFLOW = 20  #  ColorPicker right hue bar selector overflow
	
	
	ctypedef enum GuiIconName:
		ICON_NONE = 0,
		ICON_FOLDER_FILE_OPEN = 1,
		ICON_FILE_SAVE_CLASSIC = 2,
		ICON_FOLDER_OPEN = 3,
		ICON_FOLDER_SAVE = 4,
		ICON_FILE_OPEN = 5,
		ICON_FILE_SAVE = 6,
		ICON_FILE_EXPORT = 7,
		ICON_FILE_ADD = 8,
		ICON_FILE_DELETE = 9,
		ICON_FILETYPE_TEXT = 10,
		ICON_FILETYPE_AUDIO = 11,
		ICON_FILETYPE_IMAGE = 12,
		ICON_FILETYPE_PLAY = 13,
		ICON_FILETYPE_VIDEO = 14,
		ICON_FILETYPE_INFO = 15,
		ICON_FILE_COPY = 16,
		ICON_FILE_CUT = 17,
		ICON_FILE_PASTE = 18,
		ICON_CURSOR_HAND = 19,
		ICON_CURSOR_POINTER = 20,
		ICON_CURSOR_CLASSIC = 21,
		ICON_PENCIL = 22,
		ICON_PENCIL_BIG = 23,
		ICON_BRUSH_CLASSIC = 24,
		ICON_BRUSH_PAINTER = 25,
		ICON_WATER_DROP = 26,
		ICON_COLOR_PICKER = 27,
		ICON_RUBBER = 28,
		ICON_COLOR_BUCKET = 29,
		ICON_TEXT_T = 30,
		ICON_TEXT_A = 31,
		ICON_SCALE = 32,
		ICON_RESIZE = 33,
		ICON_FILTER_POINT = 34,
		ICON_FILTER_BILINEAR = 35,
		ICON_CROP = 36,
		ICON_CROP_ALPHA = 37,
		ICON_SQUARE_TOGGLE = 38,
		ICON_SYMMETRY = 39,
		ICON_SYMMETRY_HORIZONTAL = 40,
		ICON_SYMMETRY_VERTICAL = 41,
		ICON_LENS = 42,
		ICON_LENS_BIG = 43,
		ICON_EYE_ON = 44,
		ICON_EYE_OFF = 45,
		ICON_FILTER_TOP = 46,
		ICON_FILTER = 47,
		ICON_TARGET_POINT = 48,
		ICON_TARGET_SMALL = 49,
		ICON_TARGET_BIG = 50,
		ICON_TARGET_MOVE = 51,
		ICON_CURSOR_MOVE = 52,
		ICON_CURSOR_SCALE = 53,
		ICON_CURSOR_SCALE_RIGHT = 54,
		ICON_CURSOR_SCALE_LEFT = 55,
		ICON_UNDO = 56,
		ICON_REDO = 57,
		ICON_REREDO = 58,
		ICON_MUTATE = 59,
		ICON_ROTATE = 60,
		ICON_REPEAT = 61,
		ICON_SHUFFLE = 62,
		ICON_EMPTYBOX = 63,
		ICON_TARGET = 64,
		ICON_TARGET_SMALL_FILL = 65,
		ICON_TARGET_BIG_FILL = 66,
		ICON_TARGET_MOVE_FILL = 67,
		ICON_CURSOR_MOVE_FILL = 68,
		ICON_CURSOR_SCALE_FILL = 69,
		ICON_CURSOR_SCALE_RIGHT_FILL = 70,
		ICON_CURSOR_SCALE_LEFT_FILL = 71,
		ICON_UNDO_FILL = 72,
		ICON_REDO_FILL = 73,
		ICON_REREDO_FILL = 74,
		ICON_MUTATE_FILL = 75,
		ICON_ROTATE_FILL = 76,
		ICON_REPEAT_FILL = 77,
		ICON_SHUFFLE_FILL = 78,
		ICON_EMPTYBOX_SMALL = 79,
		ICON_BOX = 80,
		ICON_BOX_TOP = 81,
		ICON_BOX_TOP_RIGHT = 82,
		ICON_BOX_RIGHT = 83,
		ICON_BOX_BOTTOM_RIGHT = 84,
		ICON_BOX_BOTTOM = 85,
		ICON_BOX_BOTTOM_LEFT = 86,
		ICON_BOX_LEFT = 87,
		ICON_BOX_TOP_LEFT = 88,
		ICON_BOX_CENTER = 89,
		ICON_BOX_CIRCLE_MASK = 90,
		ICON_POT = 91,
		ICON_ALPHA_MULTIPLY = 92,
		ICON_ALPHA_CLEAR = 93,
		ICON_DITHERING = 94,
		ICON_MIPMAPS = 95,
		ICON_BOX_GRID = 96,
		ICON_GRID = 97,
		ICON_BOX_CORNERS_SMALL = 98,
		ICON_BOX_CORNERS_BIG = 99,
		ICON_FOUR_BOXES = 100,
		ICON_GRID_FILL = 101,
		ICON_BOX_MULTISIZE = 102,
		ICON_ZOOM_SMALL = 103,
		ICON_ZOOM_MEDIUM = 104,
		ICON_ZOOM_BIG = 105,
		ICON_ZOOM_ALL = 106,
		ICON_ZOOM_CENTER = 107,
		ICON_BOX_DOTS_SMALL = 108,
		ICON_BOX_DOTS_BIG = 109,
		ICON_BOX_CONCENTRIC = 110,
		ICON_BOX_GRID_BIG = 111,
		ICON_OK_TICK = 112,
		ICON_CROSS = 113,
		ICON_ARROW_LEFT = 114,
		ICON_ARROW_RIGHT = 115,
		ICON_ARROW_DOWN = 116,
		ICON_ARROW_UP = 117,
		ICON_ARROW_LEFT_FILL = 118,
		ICON_ARROW_RIGHT_FILL = 119,
		ICON_ARROW_DOWN_FILL = 120,
		ICON_ARROW_UP_FILL = 121,
		ICON_AUDIO = 122,
		ICON_FX = 123,
		ICON_WAVE = 124,
		ICON_WAVE_SINUS = 125,
		ICON_WAVE_SQUARE = 126,
		ICON_WAVE_TRIANGULAR = 127,
		ICON_CROSS_SMALL = 128,
		ICON_PLAYER_PREVIOUS = 129,
		ICON_PLAYER_PLAY_BACK = 130,
		ICON_PLAYER_PLAY = 131,
		ICON_PLAYER_PAUSE = 132,
		ICON_PLAYER_STOP = 133,
		ICON_PLAYER_NEXT = 134,
		ICON_PLAYER_RECORD = 135,
		ICON_MAGNET = 136,
		ICON_LOCK_CLOSE = 137,
		ICON_LOCK_OPEN = 138,
		ICON_CLOCK = 139,
		ICON_TOOLS = 140,
		ICON_GEAR = 141,
		ICON_GEAR_BIG = 142,
		ICON_BIN = 143,
		ICON_HAND_POINTER = 144,
		ICON_LASER = 145,
		ICON_COIN = 146,
		ICON_EXPLOSION = 147,
		ICON_1UP = 148,
		ICON_PLAYER = 149,
		ICON_PLAYER_JUMP = 150,
		ICON_KEY = 151,
		ICON_DEMON = 152,
		ICON_TEXT_POPUP = 153,
		ICON_GEAR_EX = 154,
		ICON_CRACK = 155,
		ICON_CRACK_POINTS = 156,
		ICON_STAR = 157,
		ICON_DOOR = 158,
		ICON_EXIT = 159,
		ICON_MODE_2D = 160,
		ICON_MODE_3D = 161,
		ICON_CUBE = 162,
		ICON_CUBE_FACE_TOP = 163,
		ICON_CUBE_FACE_LEFT = 164,
		ICON_CUBE_FACE_FRONT = 165,
		ICON_CUBE_FACE_BOTTOM = 166,
		ICON_CUBE_FACE_RIGHT = 167,
		ICON_CUBE_FACE_BACK = 168,
		ICON_CAMERA = 169,
		ICON_SPECIAL = 170,
		ICON_LINK_NET = 171,
		ICON_LINK_BOXES = 172,
		ICON_LINK_MULTI = 173,
		ICON_LINK = 174,
		ICON_LINK_BROKE = 175,
		ICON_TEXT_NOTES = 176,
		ICON_NOTEBOOK = 177,
		ICON_SUITCASE = 178,
		ICON_SUITCASE_ZIP = 179,
		ICON_MAILBOX = 180,
		ICON_MONITOR = 181,
		ICON_PRINTER = 182,
		ICON_PHOTO_CAMERA = 183,
		ICON_PHOTO_CAMERA_FLASH = 184,
		ICON_HOUSE = 185,
		ICON_HEART = 186,
		ICON_CORNER = 187,
		ICON_VERTICAL_BARS = 188,
		ICON_VERTICAL_BARS_FILL = 189,
		ICON_LIFE_BARS = 190,
		ICON_INFO = 191,
		ICON_CROSSLINE = 192,
		ICON_HELP = 193,
		ICON_FILETYPE_ALPHA = 194,
		ICON_FILETYPE_HOME = 195,
		ICON_LAYERS_VISIBLE = 196,
		ICON_LAYERS = 197,
		ICON_WINDOW = 198,
		ICON_HIDPI = 199,
		ICON_FILETYPE_BINARY = 200,
		ICON_HEX = 201,
		ICON_SHIELD = 202,
		ICON_FILE_NEW = 203,
		ICON_FOLDER_ADD = 204,
		ICON_ALARM = 205,
		ICON_206 = 206,
		ICON_207 = 207,
		ICON_208 = 208,
		ICON_209 = 209,
		ICON_210 = 210,
		ICON_211 = 211,
		ICON_212 = 212,
		ICON_213 = 213,
		ICON_214 = 214,
		ICON_215 = 215,
		ICON_216 = 216,
		ICON_217 = 217,
		ICON_218 = 218,
		ICON_219 = 219,
		ICON_220 = 220,
		ICON_221 = 221,
		ICON_222 = 222,
		ICON_223 = 223,
		ICON_224 = 224,
		ICON_225 = 225,
		ICON_226 = 226,
		ICON_227 = 227,
		ICON_228 = 228,
		ICON_229 = 229,
		ICON_230 = 230,
		ICON_231 = 231,
		ICON_232 = 232,
		ICON_233 = 233,
		ICON_234 = 234,
		ICON_235 = 235,
		ICON_236 = 236,
		ICON_237 = 237,
		ICON_238 = 238,
		ICON_239 = 239,
		ICON_240 = 240,
		ICON_241 = 241,
		ICON_242 = 242,
		ICON_243 = 243,
		ICON_244 = 244,
		ICON_245 = 245,
		ICON_246 = 246,
		ICON_247 = 247,
		ICON_248 = 248,
		ICON_249 = 249,
		ICON_250 = 250,
		ICON_251 = 251,
		ICON_252 = 252,
		ICON_253 = 253,
		ICON_254 = 254,
		ICON_255 = 255
	
	
	
	#  Style property
	ctypedef struct GuiStyleProp:
		unsigned short controlId;
		unsigned short propertyId;
		unsigned int propertyValue;
	
	
	void GuiEnable();  # Enable gui controls (global state)
	void GuiDisable();  # Disable gui controls (global state)
	void GuiLock();  # Lock gui controls (global state)
	void GuiUnlock();  # Unlock gui controls (global state)
	bint GuiIsLocked();  # Check if gui is locked (global state)
	void GuiFade(float alpha);  # Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f
	void GuiSetState(int state);  # Set gui state (global state)
	int GuiGetState();  # Get gui state (global state)
	void GuiSetFont(Font font);  # Set gui custom font (global state)
	Font GuiGetFont();  # Get gui custom font (global state)
	void GuiSetStyle(int control, int property, int value);  # Set one style property
	int GuiGetStyle(int control, int property);  # Get one style property
	bint GuiWindowBox(Rectangle bounds, const char * title);  # Window Box control, shows a window that can be closed
	void GuiGroupBox(Rectangle bounds, const char * text);  # Group Box control with text name
	void GuiLine(Rectangle bounds, const char * text);  # Line separator control, could contain text
	void GuiPanel(Rectangle bounds, const char * text);  # Panel control, useful to group controls
	Rectangle GuiScrollPanel(Rectangle bounds, const char * text, Rectangle content, Vector2 * scroll);  # Scroll Panel control
	void GuiLabel(Rectangle bounds, const char * text);  # Label control, shows text
	bint GuiButton(Rectangle bounds, const char * text);  # Button control, returns true when clicked
	bint GuiLabelButton(Rectangle bounds, const char * text);  # Label button control, show true when clicked
	bint GuiToggle(Rectangle bounds, const char * text, bint active);  # Toggle Button control, returns true when active
	int GuiToggleGroup(Rectangle bounds, const char * text, int active);  # Toggle Group control, returns active toggle index
	bint GuiCheckBox(Rectangle bounds, const char * text, bint checked);  # Check Box control, returns true when active
	int GuiComboBox(Rectangle bounds, const char * text, int active);  # Combo Box control, returns selected item index
	bint GuiDropdownBox(Rectangle bounds, const char * text, int * active, bint editMode);  # Dropdown Box control, returns selected item
	bint GuiSpinner(Rectangle bounds, const char * text, int * value, int minValue, int maxValue, bint editMode);  # Spinner control, returns selected value
	bint GuiValueBox(Rectangle bounds, const char * text, int * value, int minValue, int maxValue, bint editMode);  # Value Box control, updates input text with numbers
	bint GuiTextBox(Rectangle bounds, char * text, int textSize, bint editMode);  # Text Box control, updates input text
	bint GuiTextBoxMulti(Rectangle bounds, char * text, int textSize, bint editMode);  # Text Box control with multiple lines
	float GuiSlider(Rectangle bounds, const char * textLeft, const char * textRight, float value, float minValue, float maxValue);  # Slider control, returns selected value
	float GuiSliderBar(Rectangle bounds, const char * textLeft, const char * textRight, float value, float minValue, float maxValue);  # Slider Bar control, returns selected value
	float GuiProgressBar(Rectangle bounds, const char * textLeft, const char * textRight, float value, float minValue, float maxValue);  # Progress Bar control, shows current progress value
	void GuiStatusBar(Rectangle bounds, const char * text);  # Status Bar control, shows info text
	void GuiDummyRec(Rectangle bounds, const char * text);  # Dummy control for placeholders
	Vector2 GuiGrid(Rectangle bounds, const char * text, float spacing, int subdivs);  # Grid control, returns mouse cell position
	int GuiListView(Rectangle bounds, const char * text, int * scrollIndex, int active);  # List View control, returns selected list item index
	int GuiListViewEx(Rectangle bounds, const char ** text, int count, int * focus, int * scrollIndex, int active);  # List View with extended parameters
	int GuiMessageBox(Rectangle bounds, const char * title, const char * message, const char * buttons);  # Message Box control, displays a message
	int GuiTextInputBox(Rectangle bounds, const char * title, const char * message, const char * buttons, char * text, int textMaxSize, int * secretViewActive);  # Text Input Box control, ask for text, supports secret
	Color GuiColorPicker(Rectangle bounds, const char * text, Color color);  # Color Picker control (multiple color controls)
	Color GuiColorPanel(Rectangle bounds, const char * text, Color color);  # Color Panel control
	float GuiColorBarAlpha(Rectangle bounds, const char * text, float alpha);  # Color Bar Alpha control
	float GuiColorBarHue(Rectangle bounds, const char * text, float value);  # Color Bar Hue control
	void GuiLoadStyle(const char * fileName);  # Load style file over global style variable (.rgs)
	void GuiLoadStyleDefault();  # Load style default over global style
	const char * GuiIconText(int iconId, const char * text);  # Get text with icon id prepended (if supported)
	void GuiDrawIcon(int iconId, int posX, int posY, int pixelSize, Color color);
	unsigned int * GuiGetIcons();  # Get full icons data pointer
	unsigned int * GuiGetIconData(int iconId);  # Get icon bit data
	void GuiSetIconData(int iconId, unsigned int * data);  # Set icon bit data
	void GuiSetIconScale(unsigned int scale);  # Set icon scale (1 by default)
	void GuiSetIconPixel(int iconId, int x, int y);  # Set icon pixel value
	void GuiClearIconPixel(int iconId, int x, int y);  # Clear icon pixel value
	bint GuiCheckIconPixel(int iconId, int x, int y);  # Check icon pixel value

