import enum


class rlGlVersion(enum.IntEnum):
	"""OpenGL version"""
	RL_OPENGL_11: int = 1  # OpenGL 1.1
	RL_OPENGL_21: int = 2  # OpenGL 2.1 (GLSL 120)
	RL_OPENGL_33: int = 3  # OpenGL 3.3 (GLSL 330)
	RL_OPENGL_43: int = 4  # OpenGL 4.3 (using GLSL 330)
	RL_OPENGL_ES_20: int = 5  # OpenGL ES 2.0 (GLSL 100)


class rlTraceLogLevel(enum.IntEnum):
	"""Trace log level"""
	RL_LOG_ALL: int = 0  # Display all logs
	RL_LOG_TRACE: int = 1  # Trace logging, intended for internal use only
	RL_LOG_DEBUG: int = 2  # Debug logging, used for internal debugging, it should be disabled on release builds
	RL_LOG_INFO: int = 3  # Info logging, used for program execution info
	RL_LOG_WARNING: int = 4  # Warning logging, used on recoverable failures
	RL_LOG_ERROR: int = 5  # Error logging, used on unrecoverable failures
	RL_LOG_FATAL: int = 6  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	RL_LOG_NONE: int = 7  # Disable logging


class rlPixelFormat(enum.IntEnum):
	"""Texture pixel formats"""
	RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int = 1  # 8 bit per pixel (no alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int = 2  # 8*2 bpp (2 channels)
	RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5: int = 3  # 16 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8: int = 4  # 24 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int = 5  # 16 bpp (1 bit alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int = 6  # 16 bpp (4 bit alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int = 7  # 32 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R32: int = 8  # 32 bpp (1 channel - float)
	RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32: int = 9  # 32*3 bpp (3 channels - float)
	RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int = 10  # 32*4 bpp (4 channels - float)
	RL_PIXELFORMAT_COMPRESSED_DXT1_RGB: int = 11  # 4 bpp (no alpha)
	RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA: int = 12  # 4 bpp (1 bit alpha)
	RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA: int = 13  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA: int = 14  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC1_RGB: int = 15  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC2_RGB: int = 16  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int = 17  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_PVRT_RGB: int = 18  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA: int = 19  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int = 20  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int = 21  # 2 bpp


class rlTextureFilter(enum.IntEnum):
	"""Texture parameters: filter mode"""
	RL_TEXTURE_FILTER_POINT: int = 0  # No filter, just pixel approximation
	RL_TEXTURE_FILTER_BILINEAR: int = 1  # Linear filtering
	RL_TEXTURE_FILTER_TRILINEAR: int = 2  # Trilinear filtering (linear with mipmaps)
	RL_TEXTURE_FILTER_ANISOTROPIC_4X: int = 3  # Anisotropic filtering 4x
	RL_TEXTURE_FILTER_ANISOTROPIC_8X: int = 4  # Anisotropic filtering 8x
	RL_TEXTURE_FILTER_ANISOTROPIC_16X: int = 5  # Anisotropic filtering 16x


class rlBlendMode(enum.IntEnum):
	"""Color blending modes (pre-defined)"""
	RL_BLEND_ALPHA: int = 0  # Blend textures considering alpha (default)
	RL_BLEND_ADDITIVE: int = 1  # Blend textures adding colors
	RL_BLEND_MULTIPLIED: int = 2  # Blend textures multiplying colors
	RL_BLEND_ADD_COLORS: int = 3  # Blend textures adding colors (alternative)
	RL_BLEND_SUBTRACT_COLORS: int = 4  # Blend textures subtracting colors (alternative)
	RL_BLEND_ALPHA_PREMULTIPLY: int = 5  # Blend premultiplied textures considering alpha
	RL_BLEND_CUSTOM: int = 6  # Blend textures using custom src/dst factors (use rlSetBlendFactors())
	RL_BLEND_CUSTOM_SEPARATE: int = 7  # Blend textures using custom src/dst factors (use rlSetBlendFactorsSeparate())


class rlShaderLocationIndex(enum.IntEnum):
	"""Shader location point type"""
	RL_SHADER_LOC_VERTEX_POSITION: int = 0  # Shader location: vertex attribute: position
	RL_SHADER_LOC_VERTEX_TEXCOORD01: int = 1  # Shader location: vertex attribute: texcoord01
	RL_SHADER_LOC_VERTEX_TEXCOORD02: int = 2  # Shader location: vertex attribute: texcoord02
	RL_SHADER_LOC_VERTEX_NORMAL: int = 3  # Shader location: vertex attribute: normal
	RL_SHADER_LOC_VERTEX_TANGENT: int = 4  # Shader location: vertex attribute: tangent
	RL_SHADER_LOC_VERTEX_COLOR: int = 5  # Shader location: vertex attribute: color
	RL_SHADER_LOC_MATRIX_MVP: int = 6  # Shader location: matrix uniform: model-view-projection
	RL_SHADER_LOC_MATRIX_VIEW: int = 7  # Shader location: matrix uniform: view (camera transform)
	RL_SHADER_LOC_MATRIX_PROJECTION: int = 8  # Shader location: matrix uniform: projection
	RL_SHADER_LOC_MATRIX_MODEL: int = 9  # Shader location: matrix uniform: model (transform)
	RL_SHADER_LOC_MATRIX_NORMAL: int = 10  # Shader location: matrix uniform: normal
	RL_SHADER_LOC_VECTOR_VIEW: int = 11  # Shader location: vector uniform: view
	RL_SHADER_LOC_COLOR_DIFFUSE: int = 12  # Shader location: vector uniform: diffuse color
	RL_SHADER_LOC_COLOR_SPECULAR: int = 13  # Shader location: vector uniform: specular color
	RL_SHADER_LOC_COLOR_AMBIENT: int = 14  # Shader location: vector uniform: ambient color
	RL_SHADER_LOC_MAP_ALBEDO: int = 15  # Shader location: sampler2d texture: albedo (same as: RL_SHADER_LOC_MAP_DIFFUSE)
	RL_SHADER_LOC_MAP_METALNESS: int = 16  # Shader location: sampler2d texture: metalness (same as: RL_SHADER_LOC_MAP_SPECULAR)
	RL_SHADER_LOC_MAP_NORMAL: int = 17  # Shader location: sampler2d texture: normal
	RL_SHADER_LOC_MAP_ROUGHNESS: int = 18  # Shader location: sampler2d texture: roughness
	RL_SHADER_LOC_MAP_OCCLUSION: int = 19  # Shader location: sampler2d texture: occlusion
	RL_SHADER_LOC_MAP_EMISSION: int = 20  # Shader location: sampler2d texture: emission
	RL_SHADER_LOC_MAP_HEIGHT: int = 21  # Shader location: sampler2d texture: height
	RL_SHADER_LOC_MAP_CUBEMAP: int = 22  # Shader location: samplerCube texture: cubemap
	RL_SHADER_LOC_MAP_IRRADIANCE: int = 23  # Shader location: samplerCube texture: irradiance
	RL_SHADER_LOC_MAP_PREFILTER: int = 24  # Shader location: samplerCube texture: prefilter
	RL_SHADER_LOC_MAP_BRDF: int = 25  # Shader location: sampler2d texture: brdf


class rlShaderUniformDataType(enum.IntEnum):
	"""Shader uniform data type"""
	RL_SHADER_UNIFORM_FLOAT: int = 0  # Shader uniform type: float
	RL_SHADER_UNIFORM_VEC2: int = 1  # Shader uniform type: vec2 (2 float)
	RL_SHADER_UNIFORM_VEC3: int = 2  # Shader uniform type: vec3 (3 float)
	RL_SHADER_UNIFORM_VEC4: int = 3  # Shader uniform type: vec4 (4 float)
	RL_SHADER_UNIFORM_INT: int = 4  # Shader uniform type: int
	RL_SHADER_UNIFORM_IVEC2: int = 5  # Shader uniform type: ivec2 (2 int)
	RL_SHADER_UNIFORM_IVEC3: int = 6  # Shader uniform type: ivec3 (3 int)
	RL_SHADER_UNIFORM_IVEC4: int = 7  # Shader uniform type: ivec4 (4 int)
	RL_SHADER_UNIFORM_SAMPLER2D: int = 8  # Shader uniform type: sampler2d


class rlShaderAttributeDataType(enum.IntEnum):
	"""Shader attribute data types"""
	RL_SHADER_ATTRIB_FLOAT: int = 0  # Shader attribute type: float
	RL_SHADER_ATTRIB_VEC2: int = 1  # Shader attribute type: vec2 (2 float)
	RL_SHADER_ATTRIB_VEC3: int = 2  # Shader attribute type: vec3 (3 float)
	RL_SHADER_ATTRIB_VEC4: int = 3  # Shader attribute type: vec4 (4 float)


class rlFramebufferAttachType(enum.IntEnum):
	"""Framebuffer attachment type"""
	RL_ATTACHMENT_COLOR_CHANNEL0: int = 0  # Framebuffer attachment type: color 0
	RL_ATTACHMENT_COLOR_CHANNEL1: int = 1  # Framebuffer attachment type: color 1
	RL_ATTACHMENT_COLOR_CHANNEL2: int = 2  # Framebuffer attachment type: color 2
	RL_ATTACHMENT_COLOR_CHANNEL3: int = 3  # Framebuffer attachment type: color 3
	RL_ATTACHMENT_COLOR_CHANNEL4: int = 4  # Framebuffer attachment type: color 4
	RL_ATTACHMENT_COLOR_CHANNEL5: int = 5  # Framebuffer attachment type: color 5
	RL_ATTACHMENT_COLOR_CHANNEL6: int = 6  # Framebuffer attachment type: color 6
	RL_ATTACHMENT_COLOR_CHANNEL7: int = 7  # Framebuffer attachment type: color 7
	RL_ATTACHMENT_DEPTH: int = 100  # Framebuffer attachment type: depth
	RL_ATTACHMENT_STENCIL: int = 200  # Framebuffer attachment type: stencil


class rlFramebufferAttachTextureType(enum.IntEnum):
	"""Framebuffer texture attachment type"""
	RL_ATTACHMENT_CUBEMAP_POSITIVE_X: int = 0  # Framebuffer texture attachment type: cubemap, +X side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_X: int = 1  # Framebuffer texture attachment type: cubemap, -X side
	RL_ATTACHMENT_CUBEMAP_POSITIVE_Y: int = 2  # Framebuffer texture attachment type: cubemap, +Y side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y: int = 3  # Framebuffer texture attachment type: cubemap, -Y side
	RL_ATTACHMENT_CUBEMAP_POSITIVE_Z: int = 4  # Framebuffer texture attachment type: cubemap, +Z side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z: int = 5  # Framebuffer texture attachment type: cubemap, -Z side
	RL_ATTACHMENT_TEXTURE2D: int = 100  # Framebuffer texture attachment type: texture2d
	RL_ATTACHMENT_RENDERBUFFER: int = 200  # Framebuffer texture attachment type: renderbuffer


class rlCullMode(enum.IntEnum):
	"""Face culling mode"""
	RL_CULL_FACE_FRONT: int = 0
	RL_CULL_FACE_BACK: int = 1


class ConfigFlags(enum.IntEnum):
	"""System/Window config flags"""
	FLAG_VSYNC_HINT: int = 64  # Set to try enabling V-Sync on GPU
	FLAG_FULLSCREEN_MODE: int = 2  # Set to run program in fullscreen
	FLAG_WINDOW_RESIZABLE: int = 4  # Set to allow resizable window
	FLAG_WINDOW_UNDECORATED: int = 8  # Set to disable window decoration (frame and buttons)
	FLAG_WINDOW_HIDDEN: int = 128  # Set to hide window
	FLAG_WINDOW_MINIMIZED: int = 512  # Set to minimize window (iconify)
	FLAG_WINDOW_MAXIMIZED: int = 1024  # Set to maximize window (expanded to monitor)
	FLAG_WINDOW_UNFOCUSED: int = 2048  # Set to window non focused
	FLAG_WINDOW_TOPMOST: int = 4096  # Set to window always on top
	FLAG_WINDOW_ALWAYS_RUN: int = 256  # Set to allow windows running while minimized
	FLAG_WINDOW_TRANSPARENT: int = 16  # Set to allow transparent framebuffer
	FLAG_WINDOW_HIGHDPI: int = 8192  # Set to support HighDPI
	FLAG_WINDOW_MOUSE_PASSTHROUGH: int = 16384  # Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
	FLAG_MSAA_4X_HINT: int = 32  # Set to try enabling MSAA 4X
	FLAG_INTERLACED_HINT: int = 65536  # Set to try enabling interlaced video format (for V3D)


class TraceLogLevel(enum.IntEnum):
	"""Trace log level"""
	LOG_ALL: int = 0  # Display all logs
	LOG_TRACE: int = 1  # Trace logging, intended for internal use only
	LOG_DEBUG: int = 2  # Debug logging, used for internal debugging, it should be disabled on release builds
	LOG_INFO: int = 3  # Info logging, used for program execution info
	LOG_WARNING: int = 4  # Warning logging, used on recoverable failures
	LOG_ERROR: int = 5  # Error logging, used on unrecoverable failures
	LOG_FATAL: int = 6  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	LOG_NONE: int = 7  # Disable logging


class KeyboardKey(enum.IntEnum):
	"""Keyboard keys (US keyboard layout)"""
	KEY_NULL: int = 0  # Key: NULL, used for no key pressed
	KEY_APOSTROPHE: int = 39  # Key: '
	KEY_COMMA: int = 44  # Key: ,
	KEY_MINUS: int = 45  # Key: -
	KEY_PERIOD: int = 46  # Key: .
	KEY_SLASH: int = 47  # Key: /
	KEY_ZERO: int = 48  # Key: 0
	KEY_ONE: int = 49  # Key: 1
	KEY_TWO: int = 50  # Key: 2
	KEY_THREE: int = 51  # Key: 3
	KEY_FOUR: int = 52  # Key: 4
	KEY_FIVE: int = 53  # Key: 5
	KEY_SIX: int = 54  # Key: 6
	KEY_SEVEN: int = 55  # Key: 7
	KEY_EIGHT: int = 56  # Key: 8
	KEY_NINE: int = 57  # Key: 9
	KEY_SEMICOLON: int = 59  # Key: ;
	KEY_EQUAL: int = 61  # Key: =
	KEY_A: int = 65  # Key: A | a
	KEY_B: int = 66  # Key: B | b
	KEY_C: int = 67  # Key: C | c
	KEY_D: int = 68  # Key: D | d
	KEY_E: int = 69  # Key: E | e
	KEY_F: int = 70  # Key: F | f
	KEY_G: int = 71  # Key: G | g
	KEY_H: int = 72  # Key: H | h
	KEY_I: int = 73  # Key: I | i
	KEY_J: int = 74  # Key: J | j
	KEY_K: int = 75  # Key: K | k
	KEY_L: int = 76  # Key: L | l
	KEY_M: int = 77  # Key: M | m
	KEY_N: int = 78  # Key: N | n
	KEY_O: int = 79  # Key: O | o
	KEY_P: int = 80  # Key: P | p
	KEY_Q: int = 81  # Key: Q | q
	KEY_R: int = 82  # Key: R | r
	KEY_S: int = 83  # Key: S | s
	KEY_T: int = 84  # Key: T | t
	KEY_U: int = 85  # Key: U | u
	KEY_V: int = 86  # Key: V | v
	KEY_W: int = 87  # Key: W | w
	KEY_X: int = 88  # Key: X | x
	KEY_Y: int = 89  # Key: Y | y
	KEY_Z: int = 90  # Key: Z | z
	KEY_LEFT_BRACKET: int = 91  # Key: [
	KEY_BACKSLASH: int = 92  # Key: '\'
	KEY_RIGHT_BRACKET: int = 93  # Key: ]
	KEY_GRAVE: int = 96  # Key: `
	KEY_SPACE: int = 32  # Key: Space
	KEY_ESCAPE: int = 256  # Key: Esc
	KEY_ENTER: int = 257  # Key: Enter
	KEY_TAB: int = 258  # Key: Tab
	KEY_BACKSPACE: int = 259  # Key: Backspace
	KEY_INSERT: int = 260  # Key: Ins
	KEY_DELETE: int = 261  # Key: Del
	KEY_RIGHT: int = 262  # Key: Cursor right
	KEY_LEFT: int = 263  # Key: Cursor left
	KEY_DOWN: int = 264  # Key: Cursor down
	KEY_UP: int = 265  # Key: Cursor up
	KEY_PAGE_UP: int = 266  # Key: Page up
	KEY_PAGE_DOWN: int = 267  # Key: Page down
	KEY_HOME: int = 268  # Key: Home
	KEY_END: int = 269  # Key: End
	KEY_CAPS_LOCK: int = 280  # Key: Caps lock
	KEY_SCROLL_LOCK: int = 281  # Key: Scroll down
	KEY_NUM_LOCK: int = 282  # Key: Num lock
	KEY_PRINT_SCREEN: int = 283  # Key: Print screen
	KEY_PAUSE: int = 284  # Key: Pause
	KEY_F1: int = 290  # Key: F1
	KEY_F2: int = 291  # Key: F2
	KEY_F3: int = 292  # Key: F3
	KEY_F4: int = 293  # Key: F4
	KEY_F5: int = 294  # Key: F5
	KEY_F6: int = 295  # Key: F6
	KEY_F7: int = 296  # Key: F7
	KEY_F8: int = 297  # Key: F8
	KEY_F9: int = 298  # Key: F9
	KEY_F10: int = 299  # Key: F10
	KEY_F11: int = 300  # Key: F11
	KEY_F12: int = 301  # Key: F12
	KEY_LEFT_SHIFT: int = 340  # Key: Shift left
	KEY_LEFT_CONTROL: int = 341  # Key: Control left
	KEY_LEFT_ALT: int = 342  # Key: Alt left
	KEY_LEFT_SUPER: int = 343  # Key: Super left
	KEY_RIGHT_SHIFT: int = 344  # Key: Shift right
	KEY_RIGHT_CONTROL: int = 345  # Key: Control right
	KEY_RIGHT_ALT: int = 346  # Key: Alt right
	KEY_RIGHT_SUPER: int = 347  # Key: Super right
	KEY_KB_MENU: int = 348  # Key: KB menu
	KEY_KP_0: int = 320  # Key: Keypad 0
	KEY_KP_1: int = 321  # Key: Keypad 1
	KEY_KP_2: int = 322  # Key: Keypad 2
	KEY_KP_3: int = 323  # Key: Keypad 3
	KEY_KP_4: int = 324  # Key: Keypad 4
	KEY_KP_5: int = 325  # Key: Keypad 5
	KEY_KP_6: int = 326  # Key: Keypad 6
	KEY_KP_7: int = 327  # Key: Keypad 7
	KEY_KP_8: int = 328  # Key: Keypad 8
	KEY_KP_9: int = 329  # Key: Keypad 9
	KEY_KP_DECIMAL: int = 330  # Key: Keypad .
	KEY_KP_DIVIDE: int = 331  # Key: Keypad /
	KEY_KP_MULTIPLY: int = 332  # Key: Keypad *
	KEY_KP_SUBTRACT: int = 333  # Key: Keypad -
	KEY_KP_ADD: int = 334  # Key: Keypad +
	KEY_KP_ENTER: int = 335  # Key: Keypad Enter
	KEY_KP_EQUAL: int = 336  # Key: Keypad =
	KEY_BACK: int = 4  # Key: Android back button
	KEY_MENU: int = 82  # Key: Android menu button
	KEY_VOLUME_UP: int = 24  # Key: Android volume up button
	KEY_VOLUME_DOWN: int = 25  # Key: Android volume down button


class MouseButton(enum.IntEnum):
	"""Mouse buttons"""
	MOUSE_BUTTON_LEFT: int = 0  # Mouse button left
	MOUSE_BUTTON_RIGHT: int = 1  # Mouse button right
	MOUSE_BUTTON_MIDDLE: int = 2  # Mouse button middle (pressed wheel)
	MOUSE_BUTTON_SIDE: int = 3  # Mouse button side (advanced mouse device)
	MOUSE_BUTTON_EXTRA: int = 4  # Mouse button extra (advanced mouse device)
	MOUSE_BUTTON_FORWARD: int = 5  # Mouse button forward (advanced mouse device)
	MOUSE_BUTTON_BACK: int = 6  # Mouse button back (advanced mouse device)


class MouseCursor(enum.IntEnum):
	"""Mouse cursor"""
	MOUSE_CURSOR_DEFAULT: int = 0  # Default pointer shape
	MOUSE_CURSOR_ARROW: int = 1  # Arrow shape
	MOUSE_CURSOR_IBEAM: int = 2  # Text writing cursor shape
	MOUSE_CURSOR_CROSSHAIR: int = 3  # Cross shape
	MOUSE_CURSOR_POINTING_HAND: int = 4  # Pointing hand cursor
	MOUSE_CURSOR_RESIZE_EW: int = 5  # Horizontal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NS: int = 6  # Vertical resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NWSE: int = 7  # Top-left to bottom-right diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NESW: int = 8  # The top-right to bottom-left diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_ALL: int = 9  # The omnidirectional resize/move cursor shape
	MOUSE_CURSOR_NOT_ALLOWED: int = 10  # The operation-not-allowed shape


class GamepadButton(enum.IntEnum):
	"""Gamepad buttons"""
	GAMEPAD_BUTTON_UNKNOWN: int = 0  # Unknown button, just for error checking
	GAMEPAD_BUTTON_LEFT_FACE_UP: int = 1  # Gamepad left DPAD up button
	GAMEPAD_BUTTON_LEFT_FACE_RIGHT: int = 2  # Gamepad left DPAD right button
	GAMEPAD_BUTTON_LEFT_FACE_DOWN: int = 3  # Gamepad left DPAD down button
	GAMEPAD_BUTTON_LEFT_FACE_LEFT: int = 4  # Gamepad left DPAD left button
	GAMEPAD_BUTTON_RIGHT_FACE_UP: int = 5  # Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
	GAMEPAD_BUTTON_RIGHT_FACE_RIGHT: int = 6  # Gamepad right button right (i.e. PS3: Square, Xbox: X)
	GAMEPAD_BUTTON_RIGHT_FACE_DOWN: int = 7  # Gamepad right button down (i.e. PS3: Cross, Xbox: A)
	GAMEPAD_BUTTON_RIGHT_FACE_LEFT: int = 8  # Gamepad right button left (i.e. PS3: Circle, Xbox: B)
	GAMEPAD_BUTTON_LEFT_TRIGGER_1: int = 9  # Gamepad top/back trigger left (first), it could be a trailing button
	GAMEPAD_BUTTON_LEFT_TRIGGER_2: int = 10  # Gamepad top/back trigger left (second), it could be a trailing button
	GAMEPAD_BUTTON_RIGHT_TRIGGER_1: int = 11  # Gamepad top/back trigger right (one), it could be a trailing button
	GAMEPAD_BUTTON_RIGHT_TRIGGER_2: int = 12  # Gamepad top/back trigger right (second), it could be a trailing button
	GAMEPAD_BUTTON_MIDDLE_LEFT: int = 13  # Gamepad center buttons, left one (i.e. PS3: Select)
	GAMEPAD_BUTTON_MIDDLE: int = 14  # Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
	GAMEPAD_BUTTON_MIDDLE_RIGHT: int = 15  # Gamepad center buttons, right one (i.e. PS3: Start)
	GAMEPAD_BUTTON_LEFT_THUMB: int = 16  # Gamepad joystick pressed button left
	GAMEPAD_BUTTON_RIGHT_THUMB: int = 17  # Gamepad joystick pressed button right


class GamepadAxis(enum.IntEnum):
	"""Gamepad axis"""
	GAMEPAD_AXIS_LEFT_X: int = 0  # Gamepad left stick X axis
	GAMEPAD_AXIS_LEFT_Y: int = 1  # Gamepad left stick Y axis
	GAMEPAD_AXIS_RIGHT_X: int = 2  # Gamepad right stick X axis
	GAMEPAD_AXIS_RIGHT_Y: int = 3  # Gamepad right stick Y axis
	GAMEPAD_AXIS_LEFT_TRIGGER: int = 4  # Gamepad back trigger left, pressure level: [1..-1]
	GAMEPAD_AXIS_RIGHT_TRIGGER: int = 5  # Gamepad back trigger right, pressure level: [1..-1]


class MaterialMapIndex(enum.IntEnum):
	"""Material map index"""
	MATERIAL_MAP_ALBEDO: int = 0  # Albedo material (same as: MATERIAL_MAP_DIFFUSE)
	MATERIAL_MAP_METALNESS: int = 1  # Metalness material (same as: MATERIAL_MAP_SPECULAR)
	MATERIAL_MAP_NORMAL: int = 2  # Normal material
	MATERIAL_MAP_ROUGHNESS: int = 3  # Roughness material
	MATERIAL_MAP_OCCLUSION: int = 4  # Ambient occlusion material
	MATERIAL_MAP_EMISSION: int = 5  # Emission material
	MATERIAL_MAP_HEIGHT: int = 6  # Heightmap material
	MATERIAL_MAP_CUBEMAP: int = 7  # Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_IRRADIANCE: int = 8  # Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_PREFILTER: int = 9  # Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_BRDF: int = 10  # Brdf material


class ShaderLocationIndex(enum.IntEnum):
	"""Shader location index"""
	SHADER_LOC_VERTEX_POSITION: int = 0  # Shader location: vertex attribute: position
	SHADER_LOC_VERTEX_TEXCOORD01: int = 1  # Shader location: vertex attribute: texcoord01
	SHADER_LOC_VERTEX_TEXCOORD02: int = 2  # Shader location: vertex attribute: texcoord02
	SHADER_LOC_VERTEX_NORMAL: int = 3  # Shader location: vertex attribute: normal
	SHADER_LOC_VERTEX_TANGENT: int = 4  # Shader location: vertex attribute: tangent
	SHADER_LOC_VERTEX_COLOR: int = 5  # Shader location: vertex attribute: color
	SHADER_LOC_MATRIX_MVP: int = 6  # Shader location: matrix uniform: model-view-projection
	SHADER_LOC_MATRIX_VIEW: int = 7  # Shader location: matrix uniform: view (camera transform)
	SHADER_LOC_MATRIX_PROJECTION: int = 8  # Shader location: matrix uniform: projection
	SHADER_LOC_MATRIX_MODEL: int = 9  # Shader location: matrix uniform: model (transform)
	SHADER_LOC_MATRIX_NORMAL: int = 10  # Shader location: matrix uniform: normal
	SHADER_LOC_VECTOR_VIEW: int = 11  # Shader location: vector uniform: view
	SHADER_LOC_COLOR_DIFFUSE: int = 12  # Shader location: vector uniform: diffuse color
	SHADER_LOC_COLOR_SPECULAR: int = 13  # Shader location: vector uniform: specular color
	SHADER_LOC_COLOR_AMBIENT: int = 14  # Shader location: vector uniform: ambient color
	SHADER_LOC_MAP_ALBEDO: int = 15  # Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
	SHADER_LOC_MAP_METALNESS: int = 16  # Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
	SHADER_LOC_MAP_NORMAL: int = 17  # Shader location: sampler2d texture: normal
	SHADER_LOC_MAP_ROUGHNESS: int = 18  # Shader location: sampler2d texture: roughness
	SHADER_LOC_MAP_OCCLUSION: int = 19  # Shader location: sampler2d texture: occlusion
	SHADER_LOC_MAP_EMISSION: int = 20  # Shader location: sampler2d texture: emission
	SHADER_LOC_MAP_HEIGHT: int = 21  # Shader location: sampler2d texture: height
	SHADER_LOC_MAP_CUBEMAP: int = 22  # Shader location: samplerCube texture: cubemap
	SHADER_LOC_MAP_IRRADIANCE: int = 23  # Shader location: samplerCube texture: irradiance
	SHADER_LOC_MAP_PREFILTER: int = 24  # Shader location: samplerCube texture: prefilter
	SHADER_LOC_MAP_BRDF: int = 25  # Shader location: sampler2d texture: brdf


class ShaderUniformDataType(enum.IntEnum):
	"""Shader uniform data type"""
	SHADER_UNIFORM_FLOAT: int = 0  # Shader uniform type: float
	SHADER_UNIFORM_VEC2: int = 1  # Shader uniform type: vec2 (2 float)
	SHADER_UNIFORM_VEC3: int = 2  # Shader uniform type: vec3 (3 float)
	SHADER_UNIFORM_VEC4: int = 3  # Shader uniform type: vec4 (4 float)
	SHADER_UNIFORM_INT: int = 4  # Shader uniform type: int
	SHADER_UNIFORM_IVEC2: int = 5  # Shader uniform type: ivec2 (2 int)
	SHADER_UNIFORM_IVEC3: int = 6  # Shader uniform type: ivec3 (3 int)
	SHADER_UNIFORM_IVEC4: int = 7  # Shader uniform type: ivec4 (4 int)
	SHADER_UNIFORM_SAMPLER2D: int = 8  # Shader uniform type: sampler2d


class ShaderAttributeDataType(enum.IntEnum):
	"""Shader attribute data types"""
	SHADER_ATTRIB_FLOAT: int = 0  # Shader attribute type: float
	SHADER_ATTRIB_VEC2: int = 1  # Shader attribute type: vec2 (2 float)
	SHADER_ATTRIB_VEC3: int = 2  # Shader attribute type: vec3 (3 float)
	SHADER_ATTRIB_VEC4: int = 3  # Shader attribute type: vec4 (4 float)


class PixelFormat(enum.IntEnum):
	"""Pixel formats"""
	PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int = 1  # 8 bit per pixel (no alpha)
	PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int = 2  # 8*2 bpp (2 channels)
	PIXELFORMAT_UNCOMPRESSED_R5G6B5: int = 3  # 16 bpp
	PIXELFORMAT_UNCOMPRESSED_R8G8B8: int = 4  # 24 bpp
	PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int = 5  # 16 bpp (1 bit alpha)
	PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int = 6  # 16 bpp (4 bit alpha)
	PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int = 7  # 32 bpp
	PIXELFORMAT_UNCOMPRESSED_R32: int = 8  # 32 bpp (1 channel - float)
	PIXELFORMAT_UNCOMPRESSED_R32G32B32: int = 9  # 32*3 bpp (3 channels - float)
	PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int = 10  # 32*4 bpp (4 channels - float)
	PIXELFORMAT_COMPRESSED_DXT1_RGB: int = 11  # 4 bpp (no alpha)
	PIXELFORMAT_COMPRESSED_DXT1_RGBA: int = 12  # 4 bpp (1 bit alpha)
	PIXELFORMAT_COMPRESSED_DXT3_RGBA: int = 13  # 8 bpp
	PIXELFORMAT_COMPRESSED_DXT5_RGBA: int = 14  # 8 bpp
	PIXELFORMAT_COMPRESSED_ETC1_RGB: int = 15  # 4 bpp
	PIXELFORMAT_COMPRESSED_ETC2_RGB: int = 16  # 4 bpp
	PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int = 17  # 8 bpp
	PIXELFORMAT_COMPRESSED_PVRT_RGB: int = 18  # 4 bpp
	PIXELFORMAT_COMPRESSED_PVRT_RGBA: int = 19  # 4 bpp
	PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int = 20  # 8 bpp
	PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int = 21  # 2 bpp


class TextureFilter(enum.IntEnum):
	"""Texture parameters: filter mode"""
	TEXTURE_FILTER_POINT: int = 0  # No filter, just pixel approximation
	TEXTURE_FILTER_BILINEAR: int = 1  # Linear filtering
	TEXTURE_FILTER_TRILINEAR: int = 2  # Trilinear filtering (linear with mipmaps)
	TEXTURE_FILTER_ANISOTROPIC_4X: int = 3  # Anisotropic filtering 4x
	TEXTURE_FILTER_ANISOTROPIC_8X: int = 4  # Anisotropic filtering 8x
	TEXTURE_FILTER_ANISOTROPIC_16X: int = 5  # Anisotropic filtering 16x


class TextureWrap(enum.IntEnum):
	"""Texture parameters: wrap mode"""
	TEXTURE_WRAP_REPEAT: int = 0  # Repeats texture in tiled mode
	TEXTURE_WRAP_CLAMP: int = 1  # Clamps texture to edge pixel in tiled mode
	TEXTURE_WRAP_MIRROR_REPEAT: int = 2  # Mirrors and repeats the texture in tiled mode
	TEXTURE_WRAP_MIRROR_CLAMP: int = 3  # Mirrors and clamps to border the texture in tiled mode


class CubemapLayout(enum.IntEnum):
	"""Cubemap layouts"""
	CUBEMAP_LAYOUT_AUTO_DETECT: int = 0  # Automatically detect layout type
	CUBEMAP_LAYOUT_LINE_VERTICAL: int = 1  # Layout is defined by a vertical line with faces
	CUBEMAP_LAYOUT_LINE_HORIZONTAL: int = 2  # Layout is defined by a horizontal line with faces
	CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int = 3  # Layout is defined by a 3x4 cross with cubemap faces
	CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int = 4  # Layout is defined by a 4x3 cross with cubemap faces
	CUBEMAP_LAYOUT_PANORAMA: int = 5  # Layout is defined by a panorama image (equirrectangular map)


class FontType(enum.IntEnum):
	"""Font type, defines generation method"""
	FONT_DEFAULT: int = 0  # Default font generation, anti-aliased
	FONT_BITMAP: int = 1  # Bitmap font generation, no anti-aliasing
	FONT_SDF: int = 2  # SDF font generation, requires external shader


class BlendMode(enum.IntEnum):
	"""Color blending modes (pre-defined)"""
	BLEND_ALPHA: int = 0  # Blend textures considering alpha (default)
	BLEND_ADDITIVE: int = 1  # Blend textures adding colors
	BLEND_MULTIPLIED: int = 2  # Blend textures multiplying colors
	BLEND_ADD_COLORS: int = 3  # Blend textures adding colors (alternative)
	BLEND_SUBTRACT_COLORS: int = 4  # Blend textures subtracting colors (alternative)
	BLEND_ALPHA_PREMULTIPLY: int = 5  # Blend premultiplied textures considering alpha
	BLEND_CUSTOM: int = 6  # Blend textures using custom src/dst factors (use rlSetBlendFactors())
	BLEND_CUSTOM_SEPARATE: int = 7  # Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendFactorsSeparate())


class Gesture(enum.IntEnum):
	"""Gesture"""
	GESTURE_NONE: int = 0  # No gesture
	GESTURE_TAP: int = 1  # Tap gesture
	GESTURE_DOUBLETAP: int = 2  # Double tap gesture
	GESTURE_HOLD: int = 4  # Hold gesture
	GESTURE_DRAG: int = 8  # Drag gesture
	GESTURE_SWIPE_RIGHT: int = 16  # Swipe right gesture
	GESTURE_SWIPE_LEFT: int = 32  # Swipe left gesture
	GESTURE_SWIPE_UP: int = 64  # Swipe up gesture
	GESTURE_SWIPE_DOWN: int = 128  # Swipe down gesture
	GESTURE_PINCH_IN: int = 256  # Pinch in gesture
	GESTURE_PINCH_OUT: int = 512  # Pinch out gesture


class CameraMode(enum.IntEnum):
	"""Camera system modes"""
	CAMERA_CUSTOM: int = 0  # Custom camera
	CAMERA_FREE: int = 1  # Free camera
	CAMERA_ORBITAL: int = 2  # Orbital camera
	CAMERA_FIRST_PERSON: int = 3  # First person camera
	CAMERA_THIRD_PERSON: int = 4  # Third person camera


class CameraProjection(enum.IntEnum):
	"""Camera projection"""
	CAMERA_PERSPECTIVE: int = 0  # Perspective projection
	CAMERA_ORTHOGRAPHIC: int = 1  # Orthographic projection


class NPatchLayout(enum.IntEnum):
	"""N-patch layout"""
	NPATCH_NINE_PATCH: int = 0  # Npatch layout: 3x3 tiles
	NPATCH_THREE_PATCH_VERTICAL: int = 1  # Npatch layout: 1x3 tiles
	NPATCH_THREE_PATCH_HORIZONTAL: int = 2  # Npatch layout: 3x1 tiles


class GuiState(enum.IntEnum):
	"""Gui control state"""
	STATE_NORMAL: int = 0
	STATE_FOCUSED: int = 1
	STATE_PRESSED: int = 2
	STATE_DISABLED: int = 3


class GuiTextAlignment(enum.IntEnum):
	"""Gui control text alignment"""
	TEXT_ALIGN_LEFT: int = 0
	TEXT_ALIGN_CENTER: int = 1
	TEXT_ALIGN_RIGHT: int = 2


class GuiControl(enum.IntEnum):
	"""Gui controls"""
	DEFAULT: int = 0
	LABEL: int = 1  # Used also for: LABELBUTTON
	BUTTON: int = 2
	TOGGLE: int = 3  # Used also for: TOGGLEGROUP
	SLIDER: int = 4  # Used also for: SLIDERBAR
	PROGRESSBAR: int = 5
	CHECKBOX: int = 6
	COMBOBOX: int = 7
	DROPDOWNBOX: int = 8
	TEXTBOX: int = 9  # Used also for: TEXTBOXMULTI
	VALUEBOX: int = 10
	SPINNER: int = 11  # Uses: BUTTON, VALUEBOX
	LISTVIEW: int = 12
	COLORPICKER: int = 13
	SCROLLBAR: int = 14
	STATUSBAR: int = 15


class GuiControlProperty(enum.IntEnum):
	"""Gui base properties for every control"""
	BORDER_COLOR_NORMAL: int = 0
	BASE_COLOR_NORMAL: int = 1
	TEXT_COLOR_NORMAL: int = 2
	BORDER_COLOR_FOCUSED: int = 3
	BASE_COLOR_FOCUSED: int = 4
	TEXT_COLOR_FOCUSED: int = 5
	BORDER_COLOR_PRESSED: int = 6
	BASE_COLOR_PRESSED: int = 7
	TEXT_COLOR_PRESSED: int = 8
	BORDER_COLOR_DISABLED: int = 9
	BASE_COLOR_DISABLED: int = 10
	TEXT_COLOR_DISABLED: int = 11
	BORDER_WIDTH: int = 12
	TEXT_PADDING: int = 13
	TEXT_ALIGNMENT: int = 14
	RESERVED: int = 15


class GuiDefaultProperty(enum.IntEnum):
	"""DEFAULT extended properties"""
	TEXT_SIZE: int = 16  # Text size (glyphs max height)
	TEXT_SPACING: int = 17  # Text spacing between glyphs
	LINE_COLOR: int = 18  # Line control color
	BACKGROUND_COLOR: int = 19  # Background color


class GuiToggleProperty(enum.IntEnum):
	"""Toggle/ToggleGroup"""
	GROUP_PADDING: int = 16  # ToggleGroup separation between toggles


class GuiSliderProperty(enum.IntEnum):
	"""Slider/SliderBar"""
	SLIDER_WIDTH: int = 16  # Slider size of internal bar
	SLIDER_PADDING: int = 17  # Slider/SliderBar internal bar padding


class GuiProgressBarProperty(enum.IntEnum):
	"""ProgressBar"""
	PROGRESS_PADDING: int = 16  # ProgressBar internal padding


class GuiScrollBarProperty(enum.IntEnum):
	"""ScrollBar"""
	ARROWS_SIZE: int = 16
	ARROWS_VISIBLE: int = 17
	SCROLL_SLIDER_PADDING: int = 18  # (SLIDERBAR, SLIDER_PADDING)
	SCROLL_SLIDER_SIZE: int = 19
	SCROLL_PADDING: int = 20
	SCROLL_SPEED: int = 21


class GuiCheckBoxProperty(enum.IntEnum):
	"""CheckBox"""
	CHECK_PADDING: int = 16  # CheckBox internal check padding


class GuiComboBoxProperty(enum.IntEnum):
	"""ComboBox"""
	COMBO_BUTTON_WIDTH: int = 16  # ComboBox right button width
	COMBO_BUTTON_SPACING: int = 17  # ComboBox button separation


class GuiDropdownBoxProperty(enum.IntEnum):
	"""DropdownBox"""
	ARROW_PADDING: int = 16  # DropdownBox arrow separation from border and items
	DROPDOWN_ITEMS_SPACING: int = 17  # DropdownBox items separation


class GuiTextBoxProperty(enum.IntEnum):
	"""TextBox/TextBoxMulti/ValueBox/Spinner"""
	TEXT_INNER_PADDING: int = 16  # TextBox/TextBoxMulti/ValueBox/Spinner inner text padding
	TEXT_LINES_SPACING: int = 17  # TextBoxMulti lines separation
	TEXT_ALIGNMENT_VERTICAL: int = 18  # TextBoxMulti vertical alignment: 0-CENTERED, 1-UP, 2-DOWN
	TEXT_MULTILINE: int = 19  # TextBox supports multiple lines
	TEXT_WRAP_MODE: int = 20  # TextBox wrap mode for multiline: 0-NO_WRAP, 1-CHAR_WRAP, 2-WORD_WRAP


class GuiSpinnerProperty(enum.IntEnum):
	"""Spinner"""
	SPIN_BUTTON_WIDTH: int = 16  # Spinner left/right buttons width
	SPIN_BUTTON_SPACING: int = 17  # Spinner buttons separation


class GuiListViewProperty(enum.IntEnum):
	"""ListView"""
	LIST_ITEMS_HEIGHT: int = 16  # ListView items height
	LIST_ITEMS_SPACING: int = 17  # ListView items separation
	SCROLLBAR_WIDTH: int = 18  # ListView scrollbar size (usually width)
	SCROLLBAR_SIDE: int = 19  # ListView scrollbar side (0-left, 1-right)


class GuiColorPickerProperty(enum.IntEnum):
	"""ColorPicker"""
	COLOR_SELECTOR_SIZE: int = 16
	HUEBAR_WIDTH: int = 17  # ColorPicker right hue bar width
	HUEBAR_PADDING: int = 18  # ColorPicker right hue bar separation from panel
	HUEBAR_SELECTOR_HEIGHT: int = 19  # ColorPicker right hue bar selector height
	HUEBAR_SELECTOR_OVERFLOW: int = 20  # ColorPicker right hue bar selector overflow


