SUPPORT_MODULE_RSHAPES: int
SUPPORT_MODULE_RTEXTURES: int
SUPPORT_MODULE_RTEXT: int  # WARNING: It requires SUPPORT_MODULE_RTEXTURES to load sprite font textures
SUPPORT_MODULE_RMODELS: int
SUPPORT_MODULE_RAUDIO: int
SUPPORT_CAMERA_SYSTEM: int
SUPPORT_GESTURES_SYSTEM: int
SUPPORT_MOUSE_GESTURES: int
SUPPORT_SSH_KEYBOARD_RPI: int
SUPPORT_WINMM_HIGHRES_TIMER: int
SUPPORT_SCREEN_CAPTURE: int
SUPPORT_GIF_RECORDING: int
SUPPORT_COMPRESSION_API: int
MAX_FILEPATH_CAPACITY: int  # Maximum file paths capacity
MAX_FILEPATH_LENGTH: int  # Maximum length for filepaths (Linux PATH_MAX default value)
MAX_KEYBOARD_KEYS: int  # Maximum number of keyboard keys supported
MAX_MOUSE_BUTTONS: int  # Maximum number of mouse buttons supported
MAX_GAMEPADS: int  # Maximum number of gamepads supported
MAX_GAMEPAD_AXIS: int  # Maximum number of axis supported (per gamepad)
MAX_GAMEPAD_BUTTONS: int  # Maximum number of buttons supported (per gamepad)
MAX_TOUCH_POINTS: int  # Maximum number of touch points supported
MAX_KEY_PRESSED_QUEUE: int  # Maximum number of keys in the key input queue
MAX_CHAR_PRESSED_QUEUE: int  # Maximum number of characters in the char input queue
MAX_DECOMPRESSION_SIZE: int  # Max size allocated for decompression in MB
RL_DEFAULT_BATCH_BUFFERS: int  # Default number of batch buffers (multi-buffering)
RL_DEFAULT_BATCH_DRAWCALLS: int  # Default number of batch draw calls (by state changes: mode, texture)
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS: int  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
RL_MAX_MATRIX_STACK_SIZE: int  # Maximum size of internal Matrix stack
RL_MAX_SHADER_LOCATIONS: int  # Maximum number of shader locations supported
RL_CULL_DISTANCE_NEAR: float  # Default projection matrix near cull distance
RL_CULL_DISTANCE_FAR: float  # Default projection matrix far cull distance
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str  # Bound by default to shader location: 0
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str  # Bound by default to shader location: 1
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str  # Bound by default to shader location: 2
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str  # Bound by default to shader location: 3
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str  # Bound by default to shader location: 4
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str  # Bound by default to shader location: 5
RL_DEFAULT_SHADER_UNIFORM_NAME_MVP: str  # model-view-projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW: str  # view matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION: str  # projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL: str  # model matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL: str  # normal matrix (transpose(inverse(matModelView))
RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR: str  # color diffuse (base tint color, multiplied by texture color)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0: str  # texture0 (texture slot active 0)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1: str  # texture1 (texture slot active 1)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2: str  # texture2 (texture slot active 2)
SUPPORT_QUADS_DRAW_MODE: int
SUPPORT_FILEFORMAT_PNG: int
SUPPORT_FILEFORMAT_GIF: int
SUPPORT_FILEFORMAT_QOI: int
SUPPORT_FILEFORMAT_DDS: int
SUPPORT_FILEFORMAT_HDR: int
SUPPORT_IMAGE_EXPORT: int
SUPPORT_IMAGE_GENERATION: int
SUPPORT_IMAGE_MANIPULATION: int
SUPPORT_DEFAULT_FONT: int
SUPPORT_FILEFORMAT_FNT: int
SUPPORT_FILEFORMAT_TTF: int
SUPPORT_TEXT_MANIPULATION: int
MAX_TEXT_BUFFER_LENGTH: int  # Size of internal static buffers used on some functions:
MAX_TEXTSPLIT_COUNT: int  # Maximum number of substrings to split: TextSplit()
SUPPORT_FILEFORMAT_OBJ: int
SUPPORT_FILEFORMAT_MTL: int
SUPPORT_FILEFORMAT_IQM: int
SUPPORT_FILEFORMAT_GLTF: int
SUPPORT_FILEFORMAT_VOX: int
SUPPORT_FILEFORMAT_M3D: int
SUPPORT_MESH_GENERATION: int
MAX_MATERIAL_MAPS: int  # Maximum number of shader maps supported
MAX_MESH_VERTEX_BUFFERS: int  # Maximum vertex buffers (VBO) per mesh
SUPPORT_FILEFORMAT_WAV: int
SUPPORT_FILEFORMAT_OGG: int
SUPPORT_FILEFORMAT_MP3: int
SUPPORT_FILEFORMAT_QOA: int
SUPPORT_FILEFORMAT_XM: int
SUPPORT_FILEFORMAT_MOD: int
AUDIO_DEVICE_CHANNELS: int  # Device output channels: stereo
AUDIO_DEVICE_SAMPLE_RATE: int  # Device sample rate (device default)
MAX_AUDIO_BUFFER_POOL_CHANNELS: int  # Maximum number of audio pool channels
SUPPORT_STANDARD_FILEIO: int
SUPPORT_TRACELOG: int
MAX_TRACELOG_MSG_LENGTH: int  # Max length of one trace-log message
RLGL_VERSION: str
RL_DEFAULT_BATCH_BUFFERS: int  # Default number of batch buffers (multi-buffering)
RL_DEFAULT_BATCH_DRAWCALLS: int  # Default number of batch draw calls (by state changes: mode, texture)
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS: int  # Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
RL_MAX_MATRIX_STACK_SIZE: int  # Maximum size of Matrix stack
RL_MAX_SHADER_LOCATIONS: int  # Maximum number of shader locations supported
RL_CULL_DISTANCE_NEAR: float  # Default near cull distance
RL_CULL_DISTANCE_FAR: float  # Default far cull distance
RL_TEXTURE_WRAP_S: int  # GL_TEXTURE_WRAP_S
RL_TEXTURE_WRAP_T: int  # GL_TEXTURE_WRAP_T
RL_TEXTURE_MAG_FILTER: int  # GL_TEXTURE_MAG_FILTER
RL_TEXTURE_MIN_FILTER: int  # GL_TEXTURE_MIN_FILTER
RL_TEXTURE_FILTER_NEAREST: int  # GL_NEAREST
RL_TEXTURE_FILTER_LINEAR: int  # GL_LINEAR
RL_TEXTURE_FILTER_MIP_NEAREST: int  # GL_NEAREST_MIPMAP_NEAREST
RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR: int  # GL_NEAREST_MIPMAP_LINEAR
RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST: int  # GL_LINEAR_MIPMAP_NEAREST
RL_TEXTURE_FILTER_MIP_LINEAR: int  # GL_LINEAR_MIPMAP_LINEAR
RL_TEXTURE_FILTER_ANISOTROPIC: int  # Anisotropic filter (custom identifier)
RL_TEXTURE_MIPMAP_BIAS_RATIO: int  # Texture mipmap bias, percentage ratio (custom identifier)
RL_TEXTURE_WRAP_REPEAT: int  # GL_REPEAT
RL_TEXTURE_WRAP_CLAMP: int  # GL_CLAMP_TO_EDGE
RL_TEXTURE_WRAP_MIRROR_REPEAT: int  # GL_MIRRORED_REPEAT
RL_TEXTURE_WRAP_MIRROR_CLAMP: int  # GL_MIRROR_CLAMP_EXT
RL_MODELVIEW: int  # GL_MODELVIEW
RL_PROJECTION: int  # GL_PROJECTION
RL_TEXTURE: int  # GL_TEXTURE
RL_LINES: int  # GL_LINES
RL_TRIANGLES: int  # GL_TRIANGLES
RL_QUADS: int  # GL_QUADS
RL_UNSIGNED_BYTE: int  # GL_UNSIGNED_BYTE
RL_FLOAT: int  # GL_FLOAT
RL_STREAM_DRAW: int  # GL_STREAM_DRAW
RL_STREAM_READ: int  # GL_STREAM_READ
RL_STREAM_COPY: int  # GL_STREAM_COPY
RL_STATIC_DRAW: int  # GL_STATIC_DRAW
RL_STATIC_READ: int  # GL_STATIC_READ
RL_STATIC_COPY: int  # GL_STATIC_COPY
RL_DYNAMIC_DRAW: int  # GL_DYNAMIC_DRAW
RL_DYNAMIC_READ: int  # GL_DYNAMIC_READ
RL_DYNAMIC_COPY: int  # GL_DYNAMIC_COPY
RL_FRAGMENT_SHADER: int  # GL_FRAGMENT_SHADER
RL_VERTEX_SHADER: int  # GL_VERTEX_SHADER
RL_COMPUTE_SHADER: int  # GL_COMPUTE_SHADER
RL_ZERO: int  # GL_ZERO
RL_ONE: int  # GL_ONE
RL_SRC_COLOR: int  # GL_SRC_COLOR
RL_ONE_MINUS_SRC_COLOR: int  # GL_ONE_MINUS_SRC_COLOR
RL_SRC_ALPHA: int  # GL_SRC_ALPHA
RL_ONE_MINUS_SRC_ALPHA: int  # GL_ONE_MINUS_SRC_ALPHA
RL_DST_ALPHA: int  # GL_DST_ALPHA
RL_ONE_MINUS_DST_ALPHA: int  # GL_ONE_MINUS_DST_ALPHA
RL_DST_COLOR: int  # GL_DST_COLOR
RL_ONE_MINUS_DST_COLOR: int  # GL_ONE_MINUS_DST_COLOR
RL_SRC_ALPHA_SATURATE: int  # GL_SRC_ALPHA_SATURATE
RL_CONSTANT_COLOR: int  # GL_CONSTANT_COLOR
RL_ONE_MINUS_CONSTANT_COLOR: int  # GL_ONE_MINUS_CONSTANT_COLOR
RL_CONSTANT_ALPHA: int  # GL_CONSTANT_ALPHA
RL_ONE_MINUS_CONSTANT_ALPHA: int  # GL_ONE_MINUS_CONSTANT_ALPHA
RL_FUNC_ADD: int  # GL_FUNC_ADD
RL_MIN: int  # GL_MIN
RL_MAX: int  # GL_MAX
RL_FUNC_SUBTRACT: int  # GL_FUNC_SUBTRACT
RL_FUNC_REVERSE_SUBTRACT: int  # GL_FUNC_REVERSE_SUBTRACT
RL_BLEND_EQUATION: int  # GL_BLEND_EQUATION
RL_BLEND_EQUATION_RGB: int  # GL_BLEND_EQUATION_RGB   // (Same as BLEND_EQUATION)
RL_BLEND_EQUATION_ALPHA: int  # GL_BLEND_EQUATION_ALPHA
RL_BLEND_DST_RGB: int  # GL_BLEND_DST_RGB
RL_BLEND_SRC_RGB: int  # GL_BLEND_SRC_RGB
RL_BLEND_DST_ALPHA: int  # GL_BLEND_DST_ALPHA
RL_BLEND_SRC_ALPHA: int  # GL_BLEND_SRC_ALPHA
RL_BLEND_COLOR: int  # GL_BLEND_COLOR
RAYLIB_VERSION_MAJOR: int
RAYLIB_VERSION_MINOR: int
RAYLIB_VERSION_PATCH: int
RAYLIB_VERSION: str
PI: float
DEG2RAD: float
RAD2DEG: float
PI: float
EPSILON: float
DEG2RAD: float
RAD2DEG: float
RAYGUI_VERSION_MAJOR: int
RAYGUI_VERSION_MINOR: int
RAYGUI_VERSION_PATCH: int
RAYGUI_VERSION: str
SCROLLBAR_LEFT_SIDE: int
SCROLLBAR_RIGHT_SIDE: int
