import enum


class rlGlVersion(enum.IntEnum):
	"""OpenGL version"""
	RL_OPENGL_11: int  # OpenGL 1.1
	RL_OPENGL_21: int  # OpenGL 2.1 (GLSL 120)
	RL_OPENGL_33: int  # OpenGL 3.3 (GLSL 330)
	RL_OPENGL_43: int  # OpenGL 4.3 (using GLSL 330)
	RL_OPENGL_ES_20: int  # OpenGL ES 2.0 (GLSL 100)


class rlTraceLogLevel(enum.IntEnum):
	"""Trace log level"""
	RL_LOG_ALL: int  # Display all logs
	RL_LOG_TRACE: int  # Trace logging, intended for internal use only
	RL_LOG_DEBUG: int  # Debug logging, used for internal debugging, it should be disabled on release builds
	RL_LOG_INFO: int  # Info logging, used for program execution info
	RL_LOG_WARNING: int  # Warning logging, used on recoverable failures
	RL_LOG_ERROR: int  # Error logging, used on unrecoverable failures
	RL_LOG_FATAL: int  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	RL_LOG_NONE: int  # Disable logging


class rlPixelFormat(enum.IntEnum):
	"""Texture pixel formats"""
	RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int  # 8 bit per pixel (no alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int  # 8*2 bpp (2 channels)
	RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5: int  # 16 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8: int  # 24 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int  # 16 bpp (1 bit alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int  # 16 bpp (4 bit alpha)
	RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int  # 32 bpp
	RL_PIXELFORMAT_UNCOMPRESSED_R32: int  # 32 bpp (1 channel - float)
	RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32: int  # 32*3 bpp (3 channels - float)
	RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int  # 32*4 bpp (4 channels - float)
	RL_PIXELFORMAT_COMPRESSED_DXT1_RGB: int  # 4 bpp (no alpha)
	RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA: int  # 4 bpp (1 bit alpha)
	RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA: int  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA: int  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC1_RGB: int  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC2_RGB: int  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_PVRT_RGB: int  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA: int  # 4 bpp
	RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int  # 8 bpp
	RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int  # 2 bpp


class rlTextureFilter(enum.IntEnum):
	"""Texture parameters: filter mode"""
	RL_TEXTURE_FILTER_POINT: int  # No filter, just pixel approximation
	RL_TEXTURE_FILTER_BILINEAR: int  # Linear filtering
	RL_TEXTURE_FILTER_TRILINEAR: int  # Trilinear filtering (linear with mipmaps)
	RL_TEXTURE_FILTER_ANISOTROPIC_4X: int  # Anisotropic filtering 4x
	RL_TEXTURE_FILTER_ANISOTROPIC_8X: int  # Anisotropic filtering 8x
	RL_TEXTURE_FILTER_ANISOTROPIC_16X: int  # Anisotropic filtering 16x


class rlBlendMode(enum.IntEnum):
	"""Color blending modes (pre-defined)"""
	RL_BLEND_ALPHA: int  # Blend textures considering alpha (default)
	RL_BLEND_ADDITIVE: int  # Blend textures adding colors
	RL_BLEND_MULTIPLIED: int  # Blend textures multiplying colors
	RL_BLEND_ADD_COLORS: int  # Blend textures adding colors (alternative)
	RL_BLEND_SUBTRACT_COLORS: int  # Blend textures subtracting colors (alternative)
	RL_BLEND_ALPHA_PREMULTIPLY: int  # Blend premultiplied textures considering alpha
	RL_BLEND_CUSTOM: int  # Blend textures using custom src/dst factors (use rlSetBlendFactors())
	RL_BLEND_CUSTOM_SEPARATE: int  # Blend textures using custom src/dst factors (use rlSetBlendFactorsSeparate())


class rlShaderLocationIndex(enum.IntEnum):
	"""Shader location point type"""
	RL_SHADER_LOC_VERTEX_POSITION: int  # Shader location: vertex attribute: position
	RL_SHADER_LOC_VERTEX_TEXCOORD01: int  # Shader location: vertex attribute: texcoord01
	RL_SHADER_LOC_VERTEX_TEXCOORD02: int  # Shader location: vertex attribute: texcoord02
	RL_SHADER_LOC_VERTEX_NORMAL: int  # Shader location: vertex attribute: normal
	RL_SHADER_LOC_VERTEX_TANGENT: int  # Shader location: vertex attribute: tangent
	RL_SHADER_LOC_VERTEX_COLOR: int  # Shader location: vertex attribute: color
	RL_SHADER_LOC_MATRIX_MVP: int  # Shader location: matrix uniform: model-view-projection
	RL_SHADER_LOC_MATRIX_VIEW: int  # Shader location: matrix uniform: view (camera transform)
	RL_SHADER_LOC_MATRIX_PROJECTION: int  # Shader location: matrix uniform: projection
	RL_SHADER_LOC_MATRIX_MODEL: int  # Shader location: matrix uniform: model (transform)
	RL_SHADER_LOC_MATRIX_NORMAL: int  # Shader location: matrix uniform: normal
	RL_SHADER_LOC_VECTOR_VIEW: int  # Shader location: vector uniform: view
	RL_SHADER_LOC_COLOR_DIFFUSE: int  # Shader location: vector uniform: diffuse color
	RL_SHADER_LOC_COLOR_SPECULAR: int  # Shader location: vector uniform: specular color
	RL_SHADER_LOC_COLOR_AMBIENT: int  # Shader location: vector uniform: ambient color
	RL_SHADER_LOC_MAP_ALBEDO: int  # Shader location: sampler2d texture: albedo (same as: RL_SHADER_LOC_MAP_DIFFUSE)
	RL_SHADER_LOC_MAP_METALNESS: int  # Shader location: sampler2d texture: metalness (same as: RL_SHADER_LOC_MAP_SPECULAR)
	RL_SHADER_LOC_MAP_NORMAL: int  # Shader location: sampler2d texture: normal
	RL_SHADER_LOC_MAP_ROUGHNESS: int  # Shader location: sampler2d texture: roughness
	RL_SHADER_LOC_MAP_OCCLUSION: int  # Shader location: sampler2d texture: occlusion
	RL_SHADER_LOC_MAP_EMISSION: int  # Shader location: sampler2d texture: emission
	RL_SHADER_LOC_MAP_HEIGHT: int  # Shader location: sampler2d texture: height
	RL_SHADER_LOC_MAP_CUBEMAP: int  # Shader location: samplerCube texture: cubemap
	RL_SHADER_LOC_MAP_IRRADIANCE: int  # Shader location: samplerCube texture: irradiance
	RL_SHADER_LOC_MAP_PREFILTER: int  # Shader location: samplerCube texture: prefilter
	RL_SHADER_LOC_MAP_BRDF: int  # Shader location: sampler2d texture: brdf


class rlShaderUniformDataType(enum.IntEnum):
	"""Shader uniform data type"""
	RL_SHADER_UNIFORM_FLOAT: int  # Shader uniform type: float
	RL_SHADER_UNIFORM_VEC2: int  # Shader uniform type: vec2 (2 float)
	RL_SHADER_UNIFORM_VEC3: int  # Shader uniform type: vec3 (3 float)
	RL_SHADER_UNIFORM_VEC4: int  # Shader uniform type: vec4 (4 float)
	RL_SHADER_UNIFORM_INT: int  # Shader uniform type: int
	RL_SHADER_UNIFORM_IVEC2: int  # Shader uniform type: ivec2 (2 int)
	RL_SHADER_UNIFORM_IVEC3: int  # Shader uniform type: ivec3 (3 int)
	RL_SHADER_UNIFORM_IVEC4: int  # Shader uniform type: ivec4 (4 int)
	RL_SHADER_UNIFORM_SAMPLER2D: int  # Shader uniform type: sampler2d


class rlShaderAttributeDataType(enum.IntEnum):
	"""Shader attribute data types"""
	RL_SHADER_ATTRIB_FLOAT: int  # Shader attribute type: float
	RL_SHADER_ATTRIB_VEC2: int  # Shader attribute type: vec2 (2 float)
	RL_SHADER_ATTRIB_VEC3: int  # Shader attribute type: vec3 (3 float)
	RL_SHADER_ATTRIB_VEC4: int  # Shader attribute type: vec4 (4 float)


class rlFramebufferAttachType(enum.IntEnum):
	"""Framebuffer attachment type"""
	RL_ATTACHMENT_COLOR_CHANNEL0: int  # Framebuffer attachment type: color 0
	RL_ATTACHMENT_COLOR_CHANNEL1: int  # Framebuffer attachment type: color 1
	RL_ATTACHMENT_COLOR_CHANNEL2: int  # Framebuffer attachment type: color 2
	RL_ATTACHMENT_COLOR_CHANNEL3: int  # Framebuffer attachment type: color 3
	RL_ATTACHMENT_COLOR_CHANNEL4: int  # Framebuffer attachment type: color 4
	RL_ATTACHMENT_COLOR_CHANNEL5: int  # Framebuffer attachment type: color 5
	RL_ATTACHMENT_COLOR_CHANNEL6: int  # Framebuffer attachment type: color 6
	RL_ATTACHMENT_COLOR_CHANNEL7: int  # Framebuffer attachment type: color 7
	RL_ATTACHMENT_DEPTH: int  # Framebuffer attachment type: depth
	RL_ATTACHMENT_STENCIL: int  # Framebuffer attachment type: stencil


class rlFramebufferAttachTextureType(enum.IntEnum):
	"""Framebuffer texture attachment type"""
	RL_ATTACHMENT_CUBEMAP_POSITIVE_X: int  # Framebuffer texture attachment type: cubemap, +X side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_X: int  # Framebuffer texture attachment type: cubemap, -X side
	RL_ATTACHMENT_CUBEMAP_POSITIVE_Y: int  # Framebuffer texture attachment type: cubemap, +Y side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y: int  # Framebuffer texture attachment type: cubemap, -Y side
	RL_ATTACHMENT_CUBEMAP_POSITIVE_Z: int  # Framebuffer texture attachment type: cubemap, +Z side
	RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z: int  # Framebuffer texture attachment type: cubemap, -Z side
	RL_ATTACHMENT_TEXTURE2D: int  # Framebuffer texture attachment type: texture2d
	RL_ATTACHMENT_RENDERBUFFER: int  # Framebuffer texture attachment type: renderbuffer


class rlCullMode(enum.IntEnum):
	"""Face culling mode"""
	RL_CULL_FACE_FRONT: int
	RL_CULL_FACE_BACK: int


class ConfigFlags(enum.IntEnum):
	"""System/Window config flags"""
	FLAG_VSYNC_HINT: int  # Set to try enabling V-Sync on GPU
	FLAG_FULLSCREEN_MODE: int  # Set to run program in fullscreen
	FLAG_WINDOW_RESIZABLE: int  # Set to allow resizable window
	FLAG_WINDOW_UNDECORATED: int  # Set to disable window decoration (frame and buttons)
	FLAG_WINDOW_HIDDEN: int  # Set to hide window
	FLAG_WINDOW_MINIMIZED: int  # Set to minimize window (iconify)
	FLAG_WINDOW_MAXIMIZED: int  # Set to maximize window (expanded to monitor)
	FLAG_WINDOW_UNFOCUSED: int  # Set to window non focused
	FLAG_WINDOW_TOPMOST: int  # Set to window always on top
	FLAG_WINDOW_ALWAYS_RUN: int  # Set to allow windows running while minimized
	FLAG_WINDOW_TRANSPARENT: int  # Set to allow transparent framebuffer
	FLAG_WINDOW_HIGHDPI: int  # Set to support HighDPI
	FLAG_WINDOW_MOUSE_PASSTHROUGH: int  # Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
	FLAG_MSAA_4X_HINT: int  # Set to try enabling MSAA 4X
	FLAG_INTERLACED_HINT: int  # Set to try enabling interlaced video format (for V3D)


class TraceLogLevel(enum.IntEnum):
	"""Trace log level"""
	LOG_ALL: int  # Display all logs
	LOG_TRACE: int  # Trace logging, intended for internal use only
	LOG_DEBUG: int  # Debug logging, used for internal debugging, it should be disabled on release builds
	LOG_INFO: int  # Info logging, used for program execution info
	LOG_WARNING: int  # Warning logging, used on recoverable failures
	LOG_ERROR: int  # Error logging, used on unrecoverable failures
	LOG_FATAL: int  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	LOG_NONE: int  # Disable logging


class KeyboardKey(enum.IntEnum):
	"""Keyboard keys (US keyboard layout)"""
	KEY_NULL: int  # Key: NULL, used for no key pressed
	KEY_APOSTROPHE: int  # Key: '
	KEY_COMMA: int  # Key: ,
	KEY_MINUS: int  # Key: -
	KEY_PERIOD: int  # Key: .
	KEY_SLASH: int  # Key: /
	KEY_ZERO: int  # Key: 0
	KEY_ONE: int  # Key: 1
	KEY_TWO: int  # Key: 2
	KEY_THREE: int  # Key: 3
	KEY_FOUR: int  # Key: 4
	KEY_FIVE: int  # Key: 5
	KEY_SIX: int  # Key: 6
	KEY_SEVEN: int  # Key: 7
	KEY_EIGHT: int  # Key: 8
	KEY_NINE: int  # Key: 9
	KEY_SEMICOLON: int  # Key: ;
	KEY_EQUAL: int  # Key: =
	KEY_A: int  # Key: A | a
	KEY_B: int  # Key: B | b
	KEY_C: int  # Key: C | c
	KEY_D: int  # Key: D | d
	KEY_E: int  # Key: E | e
	KEY_F: int  # Key: F | f
	KEY_G: int  # Key: G | g
	KEY_H: int  # Key: H | h
	KEY_I: int  # Key: I | i
	KEY_J: int  # Key: J | j
	KEY_K: int  # Key: K | k
	KEY_L: int  # Key: L | l
	KEY_M: int  # Key: M | m
	KEY_N: int  # Key: N | n
	KEY_O: int  # Key: O | o
	KEY_P: int  # Key: P | p
	KEY_Q: int  # Key: Q | q
	KEY_R: int  # Key: R | r
	KEY_S: int  # Key: S | s
	KEY_T: int  # Key: T | t
	KEY_U: int  # Key: U | u
	KEY_V: int  # Key: V | v
	KEY_W: int  # Key: W | w
	KEY_X: int  # Key: X | x
	KEY_Y: int  # Key: Y | y
	KEY_Z: int  # Key: Z | z
	KEY_LEFT_BRACKET: int  # Key: [
	KEY_BACKSLASH: int  # Key: '\'
	KEY_RIGHT_BRACKET: int  # Key: ]
	KEY_GRAVE: int  # Key: `
	KEY_SPACE: int  # Key: Space
	KEY_ESCAPE: int  # Key: Esc
	KEY_ENTER: int  # Key: Enter
	KEY_TAB: int  # Key: Tab
	KEY_BACKSPACE: int  # Key: Backspace
	KEY_INSERT: int  # Key: Ins
	KEY_DELETE: int  # Key: Del
	KEY_RIGHT: int  # Key: Cursor right
	KEY_LEFT: int  # Key: Cursor left
	KEY_DOWN: int  # Key: Cursor down
	KEY_UP: int  # Key: Cursor up
	KEY_PAGE_UP: int  # Key: Page up
	KEY_PAGE_DOWN: int  # Key: Page down
	KEY_HOME: int  # Key: Home
	KEY_END: int  # Key: End
	KEY_CAPS_LOCK: int  # Key: Caps lock
	KEY_SCROLL_LOCK: int  # Key: Scroll down
	KEY_NUM_LOCK: int  # Key: Num lock
	KEY_PRINT_SCREEN: int  # Key: Print screen
	KEY_PAUSE: int  # Key: Pause
	KEY_F1: int  # Key: F1
	KEY_F2: int  # Key: F2
	KEY_F3: int  # Key: F3
	KEY_F4: int  # Key: F4
	KEY_F5: int  # Key: F5
	KEY_F6: int  # Key: F6
	KEY_F7: int  # Key: F7
	KEY_F8: int  # Key: F8
	KEY_F9: int  # Key: F9
	KEY_F10: int  # Key: F10
	KEY_F11: int  # Key: F11
	KEY_F12: int  # Key: F12
	KEY_LEFT_SHIFT: int  # Key: Shift left
	KEY_LEFT_CONTROL: int  # Key: Control left
	KEY_LEFT_ALT: int  # Key: Alt left
	KEY_LEFT_SUPER: int  # Key: Super left
	KEY_RIGHT_SHIFT: int  # Key: Shift right
	KEY_RIGHT_CONTROL: int  # Key: Control right
	KEY_RIGHT_ALT: int  # Key: Alt right
	KEY_RIGHT_SUPER: int  # Key: Super right
	KEY_KB_MENU: int  # Key: KB menu
	KEY_KP_0: int  # Key: Keypad 0
	KEY_KP_1: int  # Key: Keypad 1
	KEY_KP_2: int  # Key: Keypad 2
	KEY_KP_3: int  # Key: Keypad 3
	KEY_KP_4: int  # Key: Keypad 4
	KEY_KP_5: int  # Key: Keypad 5
	KEY_KP_6: int  # Key: Keypad 6
	KEY_KP_7: int  # Key: Keypad 7
	KEY_KP_8: int  # Key: Keypad 8
	KEY_KP_9: int  # Key: Keypad 9
	KEY_KP_DECIMAL: int  # Key: Keypad .
	KEY_KP_DIVIDE: int  # Key: Keypad /
	KEY_KP_MULTIPLY: int  # Key: Keypad *
	KEY_KP_SUBTRACT: int  # Key: Keypad -
	KEY_KP_ADD: int  # Key: Keypad +
	KEY_KP_ENTER: int  # Key: Keypad Enter
	KEY_KP_EQUAL: int  # Key: Keypad =
	KEY_BACK: int  # Key: Android back button
	KEY_MENU: int  # Key: Android menu button
	KEY_VOLUME_UP: int  # Key: Android volume up button
	KEY_VOLUME_DOWN: int  # Key: Android volume down button


class MouseButton(enum.IntEnum):
	"""Mouse buttons"""
	MOUSE_BUTTON_LEFT: int  # Mouse button left
	MOUSE_BUTTON_RIGHT: int  # Mouse button right
	MOUSE_BUTTON_MIDDLE: int  # Mouse button middle (pressed wheel)
	MOUSE_BUTTON_SIDE: int  # Mouse button side (advanced mouse device)
	MOUSE_BUTTON_EXTRA: int  # Mouse button extra (advanced mouse device)
	MOUSE_BUTTON_FORWARD: int  # Mouse button forward (advanced mouse device)
	MOUSE_BUTTON_BACK: int  # Mouse button back (advanced mouse device)


class MouseCursor(enum.IntEnum):
	"""Mouse cursor"""
	MOUSE_CURSOR_DEFAULT: int  # Default pointer shape
	MOUSE_CURSOR_ARROW: int  # Arrow shape
	MOUSE_CURSOR_IBEAM: int  # Text writing cursor shape
	MOUSE_CURSOR_CROSSHAIR: int  # Cross shape
	MOUSE_CURSOR_POINTING_HAND: int  # Pointing hand cursor
	MOUSE_CURSOR_RESIZE_EW: int  # Horizontal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NS: int  # Vertical resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NWSE: int  # Top-left to bottom-right diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NESW: int  # The top-right to bottom-left diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_ALL: int  # The omnidirectional resize/move cursor shape
	MOUSE_CURSOR_NOT_ALLOWED: int  # The operation-not-allowed shape


class GamepadButton(enum.IntEnum):
	"""Gamepad buttons"""
	GAMEPAD_BUTTON_UNKNOWN: int  # Unknown button, just for error checking
	GAMEPAD_BUTTON_LEFT_FACE_UP: int  # Gamepad left DPAD up button
	GAMEPAD_BUTTON_LEFT_FACE_RIGHT: int  # Gamepad left DPAD right button
	GAMEPAD_BUTTON_LEFT_FACE_DOWN: int  # Gamepad left DPAD down button
	GAMEPAD_BUTTON_LEFT_FACE_LEFT: int  # Gamepad left DPAD left button
	GAMEPAD_BUTTON_RIGHT_FACE_UP: int  # Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
	GAMEPAD_BUTTON_RIGHT_FACE_RIGHT: int  # Gamepad right button right (i.e. PS3: Square, Xbox: X)
	GAMEPAD_BUTTON_RIGHT_FACE_DOWN: int  # Gamepad right button down (i.e. PS3: Cross, Xbox: A)
	GAMEPAD_BUTTON_RIGHT_FACE_LEFT: int  # Gamepad right button left (i.e. PS3: Circle, Xbox: B)
	GAMEPAD_BUTTON_LEFT_TRIGGER_1: int  # Gamepad top/back trigger left (first), it could be a trailing button
	GAMEPAD_BUTTON_LEFT_TRIGGER_2: int  # Gamepad top/back trigger left (second), it could be a trailing button
	GAMEPAD_BUTTON_RIGHT_TRIGGER_1: int  # Gamepad top/back trigger right (one), it could be a trailing button
	GAMEPAD_BUTTON_RIGHT_TRIGGER_2: int  # Gamepad top/back trigger right (second), it could be a trailing button
	GAMEPAD_BUTTON_MIDDLE_LEFT: int  # Gamepad center buttons, left one (i.e. PS3: Select)
	GAMEPAD_BUTTON_MIDDLE: int  # Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
	GAMEPAD_BUTTON_MIDDLE_RIGHT: int  # Gamepad center buttons, right one (i.e. PS3: Start)
	GAMEPAD_BUTTON_LEFT_THUMB: int  # Gamepad joystick pressed button left
	GAMEPAD_BUTTON_RIGHT_THUMB: int  # Gamepad joystick pressed button right


class GamepadAxis(enum.IntEnum):
	"""Gamepad axis"""
	GAMEPAD_AXIS_LEFT_X: int  # Gamepad left stick X axis
	GAMEPAD_AXIS_LEFT_Y: int  # Gamepad left stick Y axis
	GAMEPAD_AXIS_RIGHT_X: int  # Gamepad right stick X axis
	GAMEPAD_AXIS_RIGHT_Y: int  # Gamepad right stick Y axis
	GAMEPAD_AXIS_LEFT_TRIGGER: int  # Gamepad back trigger left, pressure level: [1..-1]
	GAMEPAD_AXIS_RIGHT_TRIGGER: int  # Gamepad back trigger right, pressure level: [1..-1]


class MaterialMapIndex(enum.IntEnum):
	"""Material map index"""
	MATERIAL_MAP_ALBEDO: int  # Albedo material (same as: MATERIAL_MAP_DIFFUSE)
	MATERIAL_MAP_METALNESS: int  # Metalness material (same as: MATERIAL_MAP_SPECULAR)
	MATERIAL_MAP_NORMAL: int  # Normal material
	MATERIAL_MAP_ROUGHNESS: int  # Roughness material
	MATERIAL_MAP_OCCLUSION: int  # Ambient occlusion material
	MATERIAL_MAP_EMISSION: int  # Emission material
	MATERIAL_MAP_HEIGHT: int  # Heightmap material
	MATERIAL_MAP_CUBEMAP: int  # Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_IRRADIANCE: int  # Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_PREFILTER: int  # Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
	MATERIAL_MAP_BRDF: int  # Brdf material


class ShaderLocationIndex(enum.IntEnum):
	"""Shader location index"""
	SHADER_LOC_VERTEX_POSITION: int  # Shader location: vertex attribute: position
	SHADER_LOC_VERTEX_TEXCOORD01: int  # Shader location: vertex attribute: texcoord01
	SHADER_LOC_VERTEX_TEXCOORD02: int  # Shader location: vertex attribute: texcoord02
	SHADER_LOC_VERTEX_NORMAL: int  # Shader location: vertex attribute: normal
	SHADER_LOC_VERTEX_TANGENT: int  # Shader location: vertex attribute: tangent
	SHADER_LOC_VERTEX_COLOR: int  # Shader location: vertex attribute: color
	SHADER_LOC_MATRIX_MVP: int  # Shader location: matrix uniform: model-view-projection
	SHADER_LOC_MATRIX_VIEW: int  # Shader location: matrix uniform: view (camera transform)
	SHADER_LOC_MATRIX_PROJECTION: int  # Shader location: matrix uniform: projection
	SHADER_LOC_MATRIX_MODEL: int  # Shader location: matrix uniform: model (transform)
	SHADER_LOC_MATRIX_NORMAL: int  # Shader location: matrix uniform: normal
	SHADER_LOC_VECTOR_VIEW: int  # Shader location: vector uniform: view
	SHADER_LOC_COLOR_DIFFUSE: int  # Shader location: vector uniform: diffuse color
	SHADER_LOC_COLOR_SPECULAR: int  # Shader location: vector uniform: specular color
	SHADER_LOC_COLOR_AMBIENT: int  # Shader location: vector uniform: ambient color
	SHADER_LOC_MAP_ALBEDO: int  # Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
	SHADER_LOC_MAP_METALNESS: int  # Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
	SHADER_LOC_MAP_NORMAL: int  # Shader location: sampler2d texture: normal
	SHADER_LOC_MAP_ROUGHNESS: int  # Shader location: sampler2d texture: roughness
	SHADER_LOC_MAP_OCCLUSION: int  # Shader location: sampler2d texture: occlusion
	SHADER_LOC_MAP_EMISSION: int  # Shader location: sampler2d texture: emission
	SHADER_LOC_MAP_HEIGHT: int  # Shader location: sampler2d texture: height
	SHADER_LOC_MAP_CUBEMAP: int  # Shader location: samplerCube texture: cubemap
	SHADER_LOC_MAP_IRRADIANCE: int  # Shader location: samplerCube texture: irradiance
	SHADER_LOC_MAP_PREFILTER: int  # Shader location: samplerCube texture: prefilter
	SHADER_LOC_MAP_BRDF: int  # Shader location: sampler2d texture: brdf


class ShaderUniformDataType(enum.IntEnum):
	"""Shader uniform data type"""
	SHADER_UNIFORM_FLOAT: int  # Shader uniform type: float
	SHADER_UNIFORM_VEC2: int  # Shader uniform type: vec2 (2 float)
	SHADER_UNIFORM_VEC3: int  # Shader uniform type: vec3 (3 float)
	SHADER_UNIFORM_VEC4: int  # Shader uniform type: vec4 (4 float)
	SHADER_UNIFORM_INT: int  # Shader uniform type: int
	SHADER_UNIFORM_IVEC2: int  # Shader uniform type: ivec2 (2 int)
	SHADER_UNIFORM_IVEC3: int  # Shader uniform type: ivec3 (3 int)
	SHADER_UNIFORM_IVEC4: int  # Shader uniform type: ivec4 (4 int)
	SHADER_UNIFORM_SAMPLER2D: int  # Shader uniform type: sampler2d


class ShaderAttributeDataType(enum.IntEnum):
	"""Shader attribute data types"""
	SHADER_ATTRIB_FLOAT: int  # Shader attribute type: float
	SHADER_ATTRIB_VEC2: int  # Shader attribute type: vec2 (2 float)
	SHADER_ATTRIB_VEC3: int  # Shader attribute type: vec3 (3 float)
	SHADER_ATTRIB_VEC4: int  # Shader attribute type: vec4 (4 float)


class PixelFormat(enum.IntEnum):
	"""Pixel formats"""
	PIXELFORMAT_UNCOMPRESSED_GRAYSCALE: int  # 8 bit per pixel (no alpha)
	PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA: int  # 8*2 bpp (2 channels)
	PIXELFORMAT_UNCOMPRESSED_R5G6B5: int  # 16 bpp
	PIXELFORMAT_UNCOMPRESSED_R8G8B8: int  # 24 bpp
	PIXELFORMAT_UNCOMPRESSED_R5G5B5A1: int  # 16 bpp (1 bit alpha)
	PIXELFORMAT_UNCOMPRESSED_R4G4B4A4: int  # 16 bpp (4 bit alpha)
	PIXELFORMAT_UNCOMPRESSED_R8G8B8A8: int  # 32 bpp
	PIXELFORMAT_UNCOMPRESSED_R32: int  # 32 bpp (1 channel - float)
	PIXELFORMAT_UNCOMPRESSED_R32G32B32: int  # 32*3 bpp (3 channels - float)
	PIXELFORMAT_UNCOMPRESSED_R32G32B32A32: int  # 32*4 bpp (4 channels - float)
	PIXELFORMAT_COMPRESSED_DXT1_RGB: int  # 4 bpp (no alpha)
	PIXELFORMAT_COMPRESSED_DXT1_RGBA: int  # 4 bpp (1 bit alpha)
	PIXELFORMAT_COMPRESSED_DXT3_RGBA: int  # 8 bpp
	PIXELFORMAT_COMPRESSED_DXT5_RGBA: int  # 8 bpp
	PIXELFORMAT_COMPRESSED_ETC1_RGB: int  # 4 bpp
	PIXELFORMAT_COMPRESSED_ETC2_RGB: int  # 4 bpp
	PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA: int  # 8 bpp
	PIXELFORMAT_COMPRESSED_PVRT_RGB: int  # 4 bpp
	PIXELFORMAT_COMPRESSED_PVRT_RGBA: int  # 4 bpp
	PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA: int  # 8 bpp
	PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA: int  # 2 bpp


class TextureFilter(enum.IntEnum):
	"""Texture parameters: filter mode"""
	TEXTURE_FILTER_POINT: int  # No filter, just pixel approximation
	TEXTURE_FILTER_BILINEAR: int  # Linear filtering
	TEXTURE_FILTER_TRILINEAR: int  # Trilinear filtering (linear with mipmaps)
	TEXTURE_FILTER_ANISOTROPIC_4X: int  # Anisotropic filtering 4x
	TEXTURE_FILTER_ANISOTROPIC_8X: int  # Anisotropic filtering 8x
	TEXTURE_FILTER_ANISOTROPIC_16X: int  # Anisotropic filtering 16x


class TextureWrap(enum.IntEnum):
	"""Texture parameters: wrap mode"""
	TEXTURE_WRAP_REPEAT: int  # Repeats texture in tiled mode
	TEXTURE_WRAP_CLAMP: int  # Clamps texture to edge pixel in tiled mode
	TEXTURE_WRAP_MIRROR_REPEAT: int  # Mirrors and repeats the texture in tiled mode
	TEXTURE_WRAP_MIRROR_CLAMP: int  # Mirrors and clamps to border the texture in tiled mode


class CubemapLayout(enum.IntEnum):
	"""Cubemap layouts"""
	CUBEMAP_LAYOUT_AUTO_DETECT: int  # Automatically detect layout type
	CUBEMAP_LAYOUT_LINE_VERTICAL: int  # Layout is defined by a vertical line with faces
	CUBEMAP_LAYOUT_LINE_HORIZONTAL: int  # Layout is defined by a horizontal line with faces
	CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int  # Layout is defined by a 3x4 cross with cubemap faces
	CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int  # Layout is defined by a 4x3 cross with cubemap faces
	CUBEMAP_LAYOUT_PANORAMA: int  # Layout is defined by a panorama image (equirrectangular map)


class FontType(enum.IntEnum):
	"""Font type, defines generation method"""
	FONT_DEFAULT: int  # Default font generation, anti-aliased
	FONT_BITMAP: int  # Bitmap font generation, no anti-aliasing
	FONT_SDF: int  # SDF font generation, requires external shader


class BlendMode(enum.IntEnum):
	"""Color blending modes (pre-defined)"""
	BLEND_ALPHA: int  # Blend textures considering alpha (default)
	BLEND_ADDITIVE: int  # Blend textures adding colors
	BLEND_MULTIPLIED: int  # Blend textures multiplying colors
	BLEND_ADD_COLORS: int  # Blend textures adding colors (alternative)
	BLEND_SUBTRACT_COLORS: int  # Blend textures subtracting colors (alternative)
	BLEND_ALPHA_PREMULTIPLY: int  # Blend premultiplied textures considering alpha
	BLEND_CUSTOM: int  # Blend textures using custom src/dst factors (use rlSetBlendFactors())
	BLEND_CUSTOM_SEPARATE: int  # Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendFactorsSeparate())


class Gesture(enum.IntEnum):
	"""Gesture"""
	GESTURE_NONE: int  # No gesture
	GESTURE_TAP: int  # Tap gesture
	GESTURE_DOUBLETAP: int  # Double tap gesture
	GESTURE_HOLD: int  # Hold gesture
	GESTURE_DRAG: int  # Drag gesture
	GESTURE_SWIPE_RIGHT: int  # Swipe right gesture
	GESTURE_SWIPE_LEFT: int  # Swipe left gesture
	GESTURE_SWIPE_UP: int  # Swipe up gesture
	GESTURE_SWIPE_DOWN: int  # Swipe down gesture
	GESTURE_PINCH_IN: int  # Pinch in gesture
	GESTURE_PINCH_OUT: int  # Pinch out gesture


class CameraMode(enum.IntEnum):
	"""Camera system modes"""
	CAMERA_CUSTOM: int  # Custom camera
	CAMERA_FREE: int  # Free camera
	CAMERA_ORBITAL: int  # Orbital camera
	CAMERA_FIRST_PERSON: int  # First person camera
	CAMERA_THIRD_PERSON: int  # Third person camera


class CameraProjection(enum.IntEnum):
	"""Camera projection"""
	CAMERA_PERSPECTIVE: int  # Perspective projection
	CAMERA_ORTHOGRAPHIC: int  # Orthographic projection


class NPatchLayout(enum.IntEnum):
	"""N-patch layout"""
	NPATCH_NINE_PATCH: int  # Npatch layout: 3x3 tiles
	NPATCH_THREE_PATCH_VERTICAL: int  # Npatch layout: 1x3 tiles
	NPATCH_THREE_PATCH_HORIZONTAL: int  # Npatch layout: 3x1 tiles


class GuiState(enum.IntEnum):
	"""Gui control state"""
	STATE_NORMAL: int
	STATE_FOCUSED: int
	STATE_PRESSED: int
	STATE_DISABLED: int


class GuiTextAlignment(enum.IntEnum):
	"""Gui control text alignment"""
	TEXT_ALIGN_LEFT: int
	TEXT_ALIGN_CENTER: int
	TEXT_ALIGN_RIGHT: int


class GuiControl(enum.IntEnum):
	"""Gui controls"""
	DEFAULT: int
	LABEL: int  # Used also for: LABELBUTTON
	BUTTON: int
	TOGGLE: int  # Used also for: TOGGLEGROUP
	SLIDER: int  # Used also for: SLIDERBAR
	PROGRESSBAR: int
	CHECKBOX: int
	COMBOBOX: int
	DROPDOWNBOX: int
	TEXTBOX: int  # Used also for: TEXTBOXMULTI
	VALUEBOX: int
	SPINNER: int  # Uses: BUTTON, VALUEBOX
	LISTVIEW: int
	COLORPICKER: int
	SCROLLBAR: int
	STATUSBAR: int


class GuiControlProperty(enum.IntEnum):
	"""Gui base properties for every control"""
	BORDER_COLOR_NORMAL: int
	BASE_COLOR_NORMAL: int
	TEXT_COLOR_NORMAL: int
	BORDER_COLOR_FOCUSED: int
	BASE_COLOR_FOCUSED: int
	TEXT_COLOR_FOCUSED: int
	BORDER_COLOR_PRESSED: int
	BASE_COLOR_PRESSED: int
	TEXT_COLOR_PRESSED: int
	BORDER_COLOR_DISABLED: int
	BASE_COLOR_DISABLED: int
	TEXT_COLOR_DISABLED: int
	BORDER_WIDTH: int
	TEXT_PADDING: int
	TEXT_ALIGNMENT: int
	RESERVED: int


class GuiDefaultProperty(enum.IntEnum):
	"""DEFAULT extended properties"""
	TEXT_SIZE: int  # Text size (glyphs max height)
	TEXT_SPACING: int  # Text spacing between glyphs
	LINE_COLOR: int  # Line control color
	BACKGROUND_COLOR: int  # Background color


class GuiToggleProperty(enum.IntEnum):
	"""Toggle/ToggleGroup"""
	GROUP_PADDING: int  # ToggleGroup separation between toggles


class GuiSliderProperty(enum.IntEnum):
	"""Slider/SliderBar"""
	SLIDER_WIDTH: int  # Slider size of internal bar
	SLIDER_PADDING: int  # Slider/SliderBar internal bar padding


class GuiProgressBarProperty(enum.IntEnum):
	"""ProgressBar"""
	PROGRESS_PADDING: int  # ProgressBar internal padding


class GuiScrollBarProperty(enum.IntEnum):
	"""ScrollBar"""
	ARROWS_SIZE: int
	ARROWS_VISIBLE: int
	SCROLL_SLIDER_PADDING: int  # (SLIDERBAR, SLIDER_PADDING)
	SCROLL_SLIDER_SIZE: int
	SCROLL_PADDING: int
	SCROLL_SPEED: int


class GuiCheckBoxProperty(enum.IntEnum):
	"""CheckBox"""
	CHECK_PADDING: int  # CheckBox internal check padding


class GuiComboBoxProperty(enum.IntEnum):
	"""ComboBox"""
	COMBO_BUTTON_WIDTH: int  # ComboBox right button width
	COMBO_BUTTON_SPACING: int  # ComboBox button separation


class GuiDropdownBoxProperty(enum.IntEnum):
	"""DropdownBox"""
	ARROW_PADDING: int  # DropdownBox arrow separation from border and items
	DROPDOWN_ITEMS_SPACING: int  # DropdownBox items separation


class GuiTextBoxProperty(enum.IntEnum):
	"""TextBox/TextBoxMulti/ValueBox/Spinner"""
	TEXT_INNER_PADDING: int  # TextBox/TextBoxMulti/ValueBox/Spinner inner text padding
	TEXT_LINES_SPACING: int  # TextBoxMulti lines separation
	TEXT_ALIGNMENT_VERTICAL: int  # TextBoxMulti vertical alignment: 0-CENTERED, 1-UP, 2-DOWN
	TEXT_MULTILINE: int  # TextBox supports multiple lines
	TEXT_WRAP_MODE: int  # TextBox wrap mode for multiline: 0-NO_WRAP, 1-CHAR_WRAP, 2-WORD_WRAP


class GuiSpinnerProperty(enum.IntEnum):
	"""Spinner"""
	SPIN_BUTTON_WIDTH: int  # Spinner left/right buttons width
	SPIN_BUTTON_SPACING: int  # Spinner buttons separation


class GuiListViewProperty(enum.IntEnum):
	"""ListView"""
	LIST_ITEMS_HEIGHT: int  # ListView items height
	LIST_ITEMS_SPACING: int  # ListView items separation
	SCROLLBAR_WIDTH: int  # ListView scrollbar size (usually width)
	SCROLLBAR_SIDE: int  # ListView scrollbar side (0-left, 1-right)


class GuiColorPickerProperty(enum.IntEnum):
	"""ColorPicker"""
	COLOR_SELECTOR_SIZE: int
	HUEBAR_WIDTH: int  # ColorPicker right hue bar width
	HUEBAR_PADDING: int  # ColorPicker right hue bar separation from panel
	HUEBAR_SELECTOR_HEIGHT: int  # ColorPicker right hue bar selector height
	HUEBAR_SELECTOR_OVERFLOW: int  # ColorPicker right hue bar selector overflow


