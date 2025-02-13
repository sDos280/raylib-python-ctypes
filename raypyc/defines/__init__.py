SUPPORT_MODULE_RSHAPES: int = 1
SUPPORT_MODULE_RTEXTURES: int = 1
SUPPORT_MODULE_RTEXT: int = 1  # WARNING: It requires SUPPORT_MODULE_RTEXTURES to load sprite font textures
SUPPORT_MODULE_RMODELS: int = 1
SUPPORT_MODULE_RAUDIO: int = 1
SUPPORT_CAMERA_SYSTEM: int = 1
SUPPORT_GESTURES_SYSTEM: int = 1
SUPPORT_RPRAND_GENERATOR: int = 1
SUPPORT_MOUSE_GESTURES: int = 1
SUPPORT_SSH_KEYBOARD_RPI: int = 1
SUPPORT_WINMM_HIGHRES_TIMER: int = 1
SUPPORT_PARTIALBUSY_WAIT_LOOP: int = 1
SUPPORT_SCREEN_CAPTURE: int = 1
SUPPORT_GIF_RECORDING: int = 1
SUPPORT_COMPRESSION_API: int = 1
SUPPORT_AUTOMATION_EVENTS: int = 1
SUPPORT_CLIPBOARD_IMAGE: int = 1
SUPPORT_FILEFORMAT_BMP: int = 1
SUPPORT_FILEFORMAT_PNG: int = 1
SUPPORT_FILEFORMAT_JPG: int = 1
MAX_FILEPATH_CAPACITY: int = 8192  # Maximum file paths capacity
MAX_FILEPATH_LENGTH: int = 4096  # Maximum length for filepaths (Linux PATH_MAX default value)
MAX_KEYBOARD_KEYS: int = 512  # Maximum number of keyboard keys supported
MAX_MOUSE_BUTTONS: int = 8  # Maximum number of mouse buttons supported
MAX_GAMEPADS: int = 4  # Maximum number of gamepads supported
MAX_GAMEPAD_AXIS: int = 8  # Maximum number of axis supported (per gamepad)
MAX_GAMEPAD_BUTTONS: int = 32  # Maximum number of buttons supported (per gamepad)
MAX_GAMEPAD_VIBRATION_TIME: float = 2.0  # Maximum vibration time in seconds
MAX_TOUCH_POINTS: int = 8  # Maximum number of touch points supported
MAX_KEY_PRESSED_QUEUE: int = 16  # Maximum number of keys in the key input queue
MAX_CHAR_PRESSED_QUEUE: int = 16  # Maximum number of characters in the char input queue
MAX_DECOMPRESSION_SIZE: int = 64  # Max size allocated for decompression in MB
MAX_AUTOMATION_EVENTS: int = 16384  # Maximum number of automation events to record
RL_SUPPORT_MESH_GPU_SKINNING: int = 1  # GPU skinning, comment if your GPU does not support more than 8 VBOs
RL_DEFAULT_BATCH_BUFFERS: int = 1  # Default number of batch buffers (multi-buffering)
RL_DEFAULT_BATCH_DRAWCALLS: int = 256  # Default number of batch draw calls (by state changes: mode, texture)
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS: int = 4  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
RL_MAX_MATRIX_STACK_SIZE: int = 32  # Maximum size of internal Matrix stack
RL_MAX_SHADER_LOCATIONS: int = 32  # Maximum number of shader locations supported
RL_CULL_DISTANCE_NEAR: float = 0.01  # Default projection matrix near cull distance
RL_CULL_DISTANCE_FAR: float = 1000.0  # Default projection matrix far cull distance
RL_DEFAULT_SHADER_ATTRIB_LOCATION_POSITION: int = 0
RL_DEFAULT_SHADER_ATTRIB_LOCATION_TEXCOORD: int = 1
RL_DEFAULT_SHADER_ATTRIB_LOCATION_NORMAL: int = 2
RL_DEFAULT_SHADER_ATTRIB_LOCATION_COLOR: int = 3
RL_DEFAULT_SHADER_ATTRIB_LOCATION_TANGENT: int = 4
RL_DEFAULT_SHADER_ATTRIB_LOCATION_TEXCOORD2: int = 5
RL_DEFAULT_SHADER_ATTRIB_LOCATION_INDICES: int = 6
RL_DEFAULT_SHADER_ATTRIB_LOCATION_BONEIDS: int = 7
RL_DEFAULT_SHADER_ATTRIB_LOCATION_BONEWEIGHTS: int = 8
RL_DEFAULT_SHADER_ATTRIB_LOCATION_INSTANCE_TX: int = 9
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str = "vertexPosition"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_POSITION
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str = "vertexTexCoord"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_TEXCOORD
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str = "vertexNormal"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_NORMAL
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str = "vertexColor"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_COLOR
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str = "vertexTangent"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_TANGENT
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str = "vertexTexCoord2"  # Bound by default to shader location: RL_DEFAULT_SHADER_ATTRIB_LOCATION_TEXCOORD2
RL_DEFAULT_SHADER_UNIFORM_NAME_MVP: str = "mvp"  # model-view-projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW: str = "matView"  # view matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION: str = "matProjection"  # projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL: str = "matModel"  # model matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL: str = "matNormal"  # normal matrix (transpose(inverse(matModelView))
RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR: str = "colDiffuse"  # color diffuse (base tint color, multiplied by texture color)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0: str = "texture0"  # texture0 (texture slot active 0)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1: str = "texture1"  # texture1 (texture slot active 1)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2: str = "texture2"  # texture2 (texture slot active 2)
SUPPORT_QUADS_DRAW_MODE: int = 1
SPLINE_SEGMENT_DIVISIONS: int = 24  # Spline segments subdivisions
SUPPORT_FILEFORMAT_GIF: int = 1
SUPPORT_FILEFORMAT_QOI: int = 1
SUPPORT_FILEFORMAT_DDS: int = 1
SUPPORT_IMAGE_EXPORT: int = 1
SUPPORT_IMAGE_GENERATION: int = 1
SUPPORT_IMAGE_MANIPULATION: int = 1
SUPPORT_DEFAULT_FONT: int = 1
SUPPORT_FILEFORMAT_TTF: int = 1
SUPPORT_FILEFORMAT_FNT: int = 1
SUPPORT_TEXT_MANIPULATION: int = 1
SUPPORT_FONT_ATLAS_WHITE_REC: int = 1
MAX_TEXT_BUFFER_LENGTH: int = 1024  # Size of internal static buffers used on some functions:
MAX_TEXTSPLIT_COUNT: int = 128  # Maximum number of substrings to split: TextSplit()
SUPPORT_FILEFORMAT_OBJ: int = 1
SUPPORT_FILEFORMAT_MTL: int = 1
SUPPORT_FILEFORMAT_IQM: int = 1
SUPPORT_FILEFORMAT_GLTF: int = 1
SUPPORT_FILEFORMAT_VOX: int = 1
SUPPORT_FILEFORMAT_M3D: int = 1
SUPPORT_MESH_GENERATION: int = 1
MAX_MATERIAL_MAPS: int = 12  # Maximum number of shader maps supported
MAX_MESH_VERTEX_BUFFERS: int = 9  # Maximum vertex buffers (VBO) per mesh
SUPPORT_FILEFORMAT_WAV: int = 1
SUPPORT_FILEFORMAT_OGG: int = 1
SUPPORT_FILEFORMAT_MP3: int = 1
SUPPORT_FILEFORMAT_QOA: int = 1
SUPPORT_FILEFORMAT_XM: int = 1
SUPPORT_FILEFORMAT_MOD: int = 1
AUDIO_DEVICE_CHANNELS: int = 2  # Device output channels: stereo
AUDIO_DEVICE_SAMPLE_RATE: int = 0  # Device sample rate (device default)
MAX_AUDIO_BUFFER_POOL_CHANNELS: int = 16  # Maximum number of audio pool channels
SUPPORT_STANDARD_FILEIO: int = 1
SUPPORT_TRACELOG: int = 1
MAX_TRACELOG_MSG_LENGTH: int = 256  # Max length of one trace-log message
RLGL_VERSION: str = "5.0"
RL_TEXTURE_WRAP_S: int = 10242  # GL_TEXTURE_WRAP_S
RL_TEXTURE_WRAP_T: int = 10243  # GL_TEXTURE_WRAP_T
RL_TEXTURE_MAG_FILTER: int = 10240  # GL_TEXTURE_MAG_FILTER
RL_TEXTURE_MIN_FILTER: int = 10241  # GL_TEXTURE_MIN_FILTER
RL_TEXTURE_FILTER_NEAREST: int = 9728  # GL_NEAREST
RL_TEXTURE_FILTER_LINEAR: int = 9729  # GL_LINEAR
RL_TEXTURE_FILTER_MIP_NEAREST: int = 9984  # GL_NEAREST_MIPMAP_NEAREST
RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR: int = 9986  # GL_NEAREST_MIPMAP_LINEAR
RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST: int = 9985  # GL_LINEAR_MIPMAP_NEAREST
RL_TEXTURE_FILTER_MIP_LINEAR: int = 9987  # GL_LINEAR_MIPMAP_LINEAR
RL_TEXTURE_FILTER_ANISOTROPIC: int = 12288  # Anisotropic filter (custom identifier)
RL_TEXTURE_MIPMAP_BIAS_RATIO: int = 16384  # Texture mipmap bias, percentage ratio (custom identifier)
RL_TEXTURE_WRAP_REPEAT: int = 10497  # GL_REPEAT
RL_TEXTURE_WRAP_CLAMP: int = 33071  # GL_CLAMP_TO_EDGE
RL_TEXTURE_WRAP_MIRROR_REPEAT: int = 33648  # GL_MIRRORED_REPEAT
RL_TEXTURE_WRAP_MIRROR_CLAMP: int = 34626  # GL_MIRROR_CLAMP_EXT
RL_MODELVIEW: int = 5888  # GL_MODELVIEW
RL_PROJECTION: int = 5889  # GL_PROJECTION
RL_TEXTURE: int = 5890  # GL_TEXTURE
RL_LINES: int = 1  # GL_LINES
RL_TRIANGLES: int = 4  # GL_TRIANGLES
RL_QUADS: int = 7  # GL_QUADS
RL_UNSIGNED_BYTE: int = 5121  # GL_UNSIGNED_BYTE
RL_FLOAT: int = 5126  # GL_FLOAT
RL_STREAM_DRAW: int = 35040  # GL_STREAM_DRAW
RL_STREAM_READ: int = 35041  # GL_STREAM_READ
RL_STREAM_COPY: int = 35042  # GL_STREAM_COPY
RL_STATIC_DRAW: int = 35044  # GL_STATIC_DRAW
RL_STATIC_READ: int = 35045  # GL_STATIC_READ
RL_STATIC_COPY: int = 35046  # GL_STATIC_COPY
RL_DYNAMIC_DRAW: int = 35048  # GL_DYNAMIC_DRAW
RL_DYNAMIC_READ: int = 35049  # GL_DYNAMIC_READ
RL_DYNAMIC_COPY: int = 35050  # GL_DYNAMIC_COPY
RL_FRAGMENT_SHADER: int = 35632  # GL_FRAGMENT_SHADER
RL_VERTEX_SHADER: int = 35633  # GL_VERTEX_SHADER
RL_COMPUTE_SHADER: int = 37305  # GL_COMPUTE_SHADER
RL_ZERO: int = 0  # GL_ZERO
RL_ONE: int = 1  # GL_ONE
RL_SRC_COLOR: int = 768  # GL_SRC_COLOR
RL_ONE_MINUS_SRC_COLOR: int = 769  # GL_ONE_MINUS_SRC_COLOR
RL_SRC_ALPHA: int = 770  # GL_SRC_ALPHA
RL_ONE_MINUS_SRC_ALPHA: int = 771  # GL_ONE_MINUS_SRC_ALPHA
RL_DST_ALPHA: int = 772  # GL_DST_ALPHA
RL_ONE_MINUS_DST_ALPHA: int = 773  # GL_ONE_MINUS_DST_ALPHA
RL_DST_COLOR: int = 774  # GL_DST_COLOR
RL_ONE_MINUS_DST_COLOR: int = 775  # GL_ONE_MINUS_DST_COLOR
RL_SRC_ALPHA_SATURATE: int = 776  # GL_SRC_ALPHA_SATURATE
RL_CONSTANT_COLOR: int = 32769  # GL_CONSTANT_COLOR
RL_ONE_MINUS_CONSTANT_COLOR: int = 32770  # GL_ONE_MINUS_CONSTANT_COLOR
RL_CONSTANT_ALPHA: int = 32771  # GL_CONSTANT_ALPHA
RL_ONE_MINUS_CONSTANT_ALPHA: int = 32772  # GL_ONE_MINUS_CONSTANT_ALPHA
RL_FUNC_ADD: int = 32774  # GL_FUNC_ADD
RL_MIN: int = 32775  # GL_MIN
RL_MAX: int = 32776  # GL_MAX
RL_FUNC_SUBTRACT: int = 32778  # GL_FUNC_SUBTRACT
RL_FUNC_REVERSE_SUBTRACT: int = 32779  # GL_FUNC_REVERSE_SUBTRACT
RL_BLEND_EQUATION: int = 32777  # GL_BLEND_EQUATION
RL_BLEND_EQUATION_RGB: int = 32777  # GL_BLEND_EQUATION_RGB   // (Same as BLEND_EQUATION)
RL_BLEND_EQUATION_ALPHA: int = 34877  # GL_BLEND_EQUATION_ALPHA
RL_BLEND_DST_RGB: int = 32968  # GL_BLEND_DST_RGB
RL_BLEND_SRC_RGB: int = 32969  # GL_BLEND_SRC_RGB
RL_BLEND_DST_ALPHA: int = 32970  # GL_BLEND_DST_ALPHA
RL_BLEND_SRC_ALPHA: int = 32971  # GL_BLEND_SRC_ALPHA
RL_BLEND_COLOR: int = 32773  # GL_BLEND_COLOR
RL_READ_FRAMEBUFFER: int = 36008  # GL_READ_FRAMEBUFFER
RL_DRAW_FRAMEBUFFER: int = 36009  # GL_DRAW_FRAMEBUFFER
RAYLIB_VERSION_MAJOR: int = 5
RAYLIB_VERSION_MINOR: int = 6
RAYLIB_VERSION_PATCH: int = 0
RAYLIB_VERSION: str = "5.6-dev"
PI: float = 3.141592653589793
DEG2RAD: float = (PI/180.0)
RAD2DEG: float = (180.0/PI)
EPSILON: float = 1e-06
RAYGUI_VERSION_MAJOR: int = 4
RAYGUI_VERSION_MINOR: int = 5
RAYGUI_VERSION_PATCH: int = 0
RAYGUI_VERSION: str = "4.5-dev"
SCROLLBAR_LEFT_SIDE: int = 0
SCROLLBAR_RIGHT_SIDE: int = 1
