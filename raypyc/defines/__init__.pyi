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
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str  # Binded by default to shader location: 0
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str  # Binded by default to shader location: 1
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str  # Binded by default to shader location: 2
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str  # Binded by default to shader location: 3
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str  # Binded by default to shader location: 4
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str  # Binded by default to shader location: 5
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
SUPPORT_MESH_GENERATION: int
MAX_MATERIAL_MAPS: int  # Maximum number of shader maps supported
MAX_MESH_VERTEX_BUFFERS: int  # Maximum vertex buffers (VBO) per mesh
SUPPORT_FILEFORMAT_WAV: int
SUPPORT_FILEFORMAT_OGG: int
SUPPORT_FILEFORMAT_XM: int
SUPPORT_FILEFORMAT_MOD: int
SUPPORT_FILEFORMAT_MP3: int
AUDIO_DEVICE_CHANNELS: int  # Device output channels: stereo
AUDIO_DEVICE_SAMPLE_RATE: int  # Device sample rate (device default)
MAX_AUDIO_BUFFER_POOL_CHANNELS: int  # Maximum number of audio pool channels
SUPPORT_TRACELOG: int
MAX_TRACELOG_MSG_LENGTH: int  # Max length of one trace-log message
RLGL_VERSION: str
RL_DEFAULT_BATCH_BUFFER_ELEMENTS: int
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
PI: float
DEG2RAD: float
RAD2DEG: float
GL_SHADING_LANGUAGE_VERSION: int
GL_COMPRESSED_RGB_S3TC_DXT1_EXT: int
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT: int
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT: int
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT: int
GL_ETC1_RGB8_OES: int
GL_COMPRESSED_RGB8_ETC2: int
GL_COMPRESSED_RGBA8_ETC2_EAC: int
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG: int
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG: int
GL_COMPRESSED_RGBA_ASTC_4x4_KHR: int
GL_COMPRESSED_RGBA_ASTC_8x8_KHR: int
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: int
GL_TEXTURE_MAX_ANISOTROPY_EXT: int
GL_UNSIGNED_SHORT_5_6_5: int
GL_UNSIGNED_SHORT_5_5_5_1: int
GL_UNSIGNED_SHORT_4_4_4_4: int
GL_LUMINANCE: int
GL_LUMINANCE_ALPHA: int
RL_DEFAULT_SHADER_ATTRIB_NAME_POSITION: str  # Binded by default to shader location: 0
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD: str  # Binded by default to shader location: 1
RL_DEFAULT_SHADER_ATTRIB_NAME_NORMAL: str  # Binded by default to shader location: 2
RL_DEFAULT_SHADER_ATTRIB_NAME_COLOR: str  # Binded by default to shader location: 3
RL_DEFAULT_SHADER_ATTRIB_NAME_TANGENT: str  # Binded by default to shader location: 4
RL_DEFAULT_SHADER_ATTRIB_NAME_TEXCOORD2: str  # Binded by default to shader location: 5
RL_DEFAULT_SHADER_UNIFORM_NAME_MVP: str  # model-view-projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_VIEW: str  # view matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_PROJECTION: str  # projection matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_MODEL: str  # model matrix
RL_DEFAULT_SHADER_UNIFORM_NAME_NORMAL: str  # normal matrix (transpose(inverse(matModelView))
RL_DEFAULT_SHADER_UNIFORM_NAME_COLOR: str  # color diffuse (base tint color, multiplied by texture color)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE0: str  # texture0 (texture slot active 0)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE1: str  # texture1 (texture slot active 1)
RL_DEFAULT_SHADER_SAMPLER2D_NAME_TEXTURE2: str  # texture2 (texture slot active 2)
RAYLIB_VERSION: str
PI: float
DEG2RAD: float
RAD2DEG: float
PI: float
EPSILON: float
DEG2RAD: float
RAD2DEG: float
RAYGUI_VERSION: str
SCROLLBAR_LEFT_SIDE: int
SCROLLBAR_RIGHT_SIDE: int
RAYGUI_ICON_SIZE: int  # Size of icons in pixels (squared)
RAYGUI_ICON_MAX_ICONS: int  # Maximum number of icons
RAYGUI_ICON_MAX_NAME_LENGTH: int  # Maximum length of icon name id
RAYGUI_MAX_CONTROLS: int  # Maximum number of standard controls
RAYGUI_MAX_PROPS_BASE: int  # Maximum number of standard properties
RAYGUI_MAX_PROPS_EXTENDED: int  # Maximum number of extended properties
KEY_RIGHT: int
KEY_LEFT: int
KEY_DOWN: int
KEY_UP: int
KEY_BACKSPACE: int
KEY_ENTER: int
MOUSE_LEFT_BUTTON: int
RAYGUI_WINDOWBOX_STATUSBAR_HEIGHT: int
RAYGUI_GROUPBOX_LINE_THICK: int
RAYGUI_LINE_MARGIN_TEXT: int
RAYGUI_LINE_TEXT_PADDING: int
RAYGUI_PANEL_BORDER_WIDTH: int
RAYGUI_TOGGLEGROUP_MAX_ITEMS: int
RAYGUI_VALUEBOX_MAX_CHARS: int
RAYGUI_COLORBARALPHA_CHECKED_SIZE: int
RAYGUI_MESSAGEBOX_BUTTON_HEIGHT: int
RAYGUI_MESSAGEBOX_BUTTON_PADDING: int
RAYGUI_TEXTINPUTBOX_BUTTON_HEIGHT: int
RAYGUI_TEXTINPUTBOX_BUTTON_PADDING: int
RAYGUI_TEXTINPUTBOX_HEIGHT: int
RAYGUI_GRID_ALPHA: float
MAX_LINE_BUFFER_SIZE: int
ICON_TEXT_PADDING: int
RAYGUI_TEXTSPLIT_MAX_ITEMS: int
RAYGUI_TEXTSPLIT_MAX_TEXT_SIZE: int
RAYGUI_TEXTFORMAT_MAX_SIZE: int
