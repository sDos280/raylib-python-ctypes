from enum import IntEnum

#  System/Window config flags
class ConfigFlags(IntEnum):
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


#  Trace log level
class TraceLogLevel(IntEnum):
	LOG_ALL: int  # Display all logs
	LOG_TRACE: int  # Trace logging, intended for internal use only
	LOG_DEBUG: int  # Debug logging, used for internal debugging, it should be disabled on release builds
	LOG_INFO: int  # Info logging, used for program execution info
	LOG_WARNING: int  # Warning logging, used on recoverable failures
	LOG_ERROR: int  # Error logging, used on unrecoverable failures
	LOG_FATAL: int  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	LOG_NONE: int  # Disable logging


#  Keyboard keys (US keyboard layout)
class KeyboardKey(IntEnum):
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


#  Mouse buttons
class MouseButton(IntEnum):
	MOUSE_BUTTON_LEFT: int  # Mouse button left
	MOUSE_BUTTON_RIGHT: int  # Mouse button right
	MOUSE_BUTTON_MIDDLE: int  # Mouse button middle (pressed wheel)
	MOUSE_BUTTON_SIDE: int  # Mouse button side (advanced mouse device)
	MOUSE_BUTTON_EXTRA: int  # Mouse button extra (advanced mouse device)
	MOUSE_BUTTON_FORWARD: int  # Mouse button forward (advanced mouse device)
	MOUSE_BUTTON_BACK: int  # Mouse button back (advanced mouse device)


#  Mouse cursor
class MouseCursor(IntEnum):
	MOUSE_CURSOR_DEFAULT: int  # Default pointer shape
	MOUSE_CURSOR_ARROW: int  # Arrow shape
	MOUSE_CURSOR_IBEAM: int  # Text writing cursor shape
	MOUSE_CURSOR_CROSSHAIR: int  # Cross shape
	MOUSE_CURSOR_POINTING_HAND: int  # Pointing hand cursor
	MOUSE_CURSOR_RESIZE_EW: int  # Horizontal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NS: int  # Vertical resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NWSE: int  # Top-left to bottom-right diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_NESW: int  # The top-right to bottom-left diagonal resize/move arrow shape
	MOUSE_CURSOR_RESIZE_ALL: int  # The omni-directional resize/move cursor shape
	MOUSE_CURSOR_NOT_ALLOWED: int  # The operation-not-allowed shape


#  Gamepad buttons
class GamepadButton(IntEnum):
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


#  Gamepad axis
class GamepadAxis(IntEnum):
	GAMEPAD_AXIS_LEFT_X: int  # Gamepad left stick X axis
	GAMEPAD_AXIS_LEFT_Y: int  # Gamepad left stick Y axis
	GAMEPAD_AXIS_RIGHT_X: int  # Gamepad right stick X axis
	GAMEPAD_AXIS_RIGHT_Y: int  # Gamepad right stick Y axis
	GAMEPAD_AXIS_LEFT_TRIGGER: int  # Gamepad back trigger left, pressure level: [1..-1]
	GAMEPAD_AXIS_RIGHT_TRIGGER: int  # Gamepad back trigger right, pressure level: [1..-1]


#  Material map index
class MaterialMapIndex(IntEnum):
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


#  Shader location index
class ShaderLocationIndex(IntEnum):
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


#  Shader uniform data type
class ShaderUniformDataType(IntEnum):
	SHADER_UNIFORM_FLOAT: int  # Shader uniform type: float
	SHADER_UNIFORM_VEC2: int  # Shader uniform type: vec2 (2 float)
	SHADER_UNIFORM_VEC3: int  # Shader uniform type: vec3 (3 float)
	SHADER_UNIFORM_VEC4: int  # Shader uniform type: vec4 (4 float)
	SHADER_UNIFORM_INT: int  # Shader uniform type: int
	SHADER_UNIFORM_IVEC2: int  # Shader uniform type: ivec2 (2 int)
	SHADER_UNIFORM_IVEC3: int  # Shader uniform type: ivec3 (3 int)
	SHADER_UNIFORM_IVEC4: int  # Shader uniform type: ivec4 (4 int)
	SHADER_UNIFORM_SAMPLER2D: int  # Shader uniform type: sampler2d


#  Shader attribute data types
class ShaderAttributeDataType(IntEnum):
	SHADER_ATTRIB_FLOAT: int  # Shader attribute type: float
	SHADER_ATTRIB_VEC2: int  # Shader attribute type: vec2 (2 float)
	SHADER_ATTRIB_VEC3: int  # Shader attribute type: vec3 (3 float)
	SHADER_ATTRIB_VEC4: int  # Shader attribute type: vec4 (4 float)


#  Pixel formats
class PixelFormat(IntEnum):
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


#  Texture parameters: filter mode
class TextureFilter(IntEnum):
	TEXTURE_FILTER_POINT: int  # No filter, just pixel approximation
	TEXTURE_FILTER_BILINEAR: int  # Linear filtering
	TEXTURE_FILTER_TRILINEAR: int  # Trilinear filtering (linear with mipmaps)
	TEXTURE_FILTER_ANISOTROPIC_4X: int  # Anisotropic filtering 4x
	TEXTURE_FILTER_ANISOTROPIC_8X: int  # Anisotropic filtering 8x
	TEXTURE_FILTER_ANISOTROPIC_16X: int  # Anisotropic filtering 16x


#  Texture parameters: wrap mode
class TextureWrap(IntEnum):
	TEXTURE_WRAP_REPEAT: int  # Repeats texture in tiled mode
	TEXTURE_WRAP_CLAMP: int  # Clamps texture to edge pixel in tiled mode
	TEXTURE_WRAP_MIRROR_REPEAT: int  # Mirrors and repeats the texture in tiled mode
	TEXTURE_WRAP_MIRROR_CLAMP: int  # Mirrors and clamps to border the texture in tiled mode


#  Cubemap layouts
class CubemapLayout(IntEnum):
	CUBEMAP_LAYOUT_AUTO_DETECT: int  # Automatically detect layout type
	CUBEMAP_LAYOUT_LINE_VERTICAL: int  # Layout is defined by a vertical line with faces
	CUBEMAP_LAYOUT_LINE_HORIZONTAL: int  # Layout is defined by an horizontal line with faces
	CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int  # Layout is defined by a 3x4 cross with cubemap faces
	CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int  # Layout is defined by a 4x3 cross with cubemap faces
	CUBEMAP_LAYOUT_PANORAMA: int  # Layout is defined by a panorama image (equirectangular map)


#  Font type, defines generation method
class FontType(IntEnum):
	FONT_DEFAULT: int  # Default font generation, anti-aliased
	FONT_BITMAP: int  # Bitmap font generation, no anti-aliasing
	FONT_SDF: int  # SDF font generation, requires external shader


#  Color blending modes (pre-defined)
class BlendMode(IntEnum):
	BLEND_ALPHA: int  # Blend textures considering alpha (default)
	BLEND_ADDITIVE: int  # Blend textures adding colors
	BLEND_MULTIPLIED: int  # Blend textures multiplying colors
	BLEND_ADD_COLORS: int  # Blend textures adding colors (alternative)
	BLEND_SUBTRACT_COLORS: int  # Blend textures subtracting colors (alternative)
	BLEND_ALPHA_PREMULTIPLY: int  # Blend premultiplied textures considering alpha
	BLEND_CUSTOM: int  # Blend textures using custom src/dst factors (use rlSetBlendMode())
	BLEND_CUSTOM_SEPARATE: int  # Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendModeSeparate())


#  Gesture
class Gesture(IntEnum):
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


#  Camera system modes
class CameraMode(IntEnum):
	CAMERA_CUSTOM: int  # Custom camera
	CAMERA_FREE: int  # Free camera
	CAMERA_ORBITAL: int  # Orbital camera
	CAMERA_FIRST_PERSON: int  # First person camera
	CAMERA_THIRD_PERSON: int  # Third person camera


#  Camera projection
class CameraProjection(IntEnum):
	CAMERA_PERSPECTIVE: int  # Perspective projection
	CAMERA_ORTHOGRAPHIC: int  # Orthographic projection


#  N-patch layout
class NPatchLayout(IntEnum):
	NPATCH_NINE_PATCH: int  # Npatch layout: 3x3 tiles
	NPATCH_THREE_PATCH_VERTICAL: int  # Npatch layout: 1x3 tiles
	NPATCH_THREE_PATCH_HORIZONTAL: int  # Npatch layout: 3x1 tiles


