from enum import IntEnum

class ConfigFlags(IntEnum):
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


class TraceLogLevel(IntEnum):
	"""Trace log level"""
	LOG_ALL: int = 0  # Display all logs
	LOG_TRACE: int = 1  # Trace logging, intended for internal use only
	LOG_DEBUG: int = 2  # Debug logging, used for internal debugging, it should be disabled on release builds
	LOG_INFO: int = 3  # Info logging, used for program execution info
	LOG_WARNING: int = 4  # Warning logging, used on recoverable failures
	LOG_ERROR: int = 5  # Error logging, used on unrecoverable failures
	LOG_FATAL: int = 6  # Fatal logging, used to abort program: exit(EXIT_FAILURE)
	LOG_NONE: int = 7  # Disable logging


class KeyboardKey(IntEnum):
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


class MouseButton(IntEnum):
	"""Mouse buttons"""
	MOUSE_BUTTON_LEFT: int = 0  # Mouse button left
	MOUSE_BUTTON_RIGHT: int = 1  # Mouse button right
	MOUSE_BUTTON_MIDDLE: int = 2  # Mouse button middle (pressed wheel)
	MOUSE_BUTTON_SIDE: int = 3  # Mouse button side (advanced mouse device)
	MOUSE_BUTTON_EXTRA: int = 4  # Mouse button extra (advanced mouse device)
	MOUSE_BUTTON_FORWARD: int = 5  # Mouse button fordward (advanced mouse device)
	MOUSE_BUTTON_BACK: int = 6  # Mouse button back (advanced mouse device)


class MouseCursor(IntEnum):
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
	MOUSE_CURSOR_RESIZE_ALL: int = 9  # The omni-directional resize/move cursor shape
	MOUSE_CURSOR_NOT_ALLOWED: int = 10  # The operation-not-allowed shape


class GamepadButton(IntEnum):
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


class GamepadAxis(IntEnum):
	"""Gamepad axis"""
	GAMEPAD_AXIS_LEFT_X: int = 0  # Gamepad left stick X axis
	GAMEPAD_AXIS_LEFT_Y: int = 1  # Gamepad left stick Y axis
	GAMEPAD_AXIS_RIGHT_X: int = 2  # Gamepad right stick X axis
	GAMEPAD_AXIS_RIGHT_Y: int = 3  # Gamepad right stick Y axis
	GAMEPAD_AXIS_LEFT_TRIGGER: int = 4  # Gamepad back trigger left, pressure level: [1..-1]
	GAMEPAD_AXIS_RIGHT_TRIGGER: int = 5  # Gamepad back trigger right, pressure level: [1..-1]


class MaterialMapIndex(IntEnum):
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


class ShaderLocationIndex(IntEnum):
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


class ShaderUniformDataType(IntEnum):
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


class ShaderAttributeDataType(IntEnum):
	"""Shader attribute data types"""
	SHADER_ATTRIB_FLOAT: int = 0  # Shader attribute type: float
	SHADER_ATTRIB_VEC2: int = 1  # Shader attribute type: vec2 (2 float)
	SHADER_ATTRIB_VEC3: int = 2  # Shader attribute type: vec3 (3 float)
	SHADER_ATTRIB_VEC4: int = 3  # Shader attribute type: vec4 (4 float)


class PixelFormat(IntEnum):
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


class TextureFilter(IntEnum):
	"""Texture parameters: filter mode"""
	TEXTURE_FILTER_POINT: int = 0  # No filter, just pixel approximation
	TEXTURE_FILTER_BILINEAR: int = 1  # Linear filtering
	TEXTURE_FILTER_TRILINEAR: int = 2  # Trilinear filtering (linear with mipmaps)
	TEXTURE_FILTER_ANISOTROPIC_4X: int = 3  # Anisotropic filtering 4x
	TEXTURE_FILTER_ANISOTROPIC_8X: int = 4  # Anisotropic filtering 8x
	TEXTURE_FILTER_ANISOTROPIC_16X: int = 5  # Anisotropic filtering 16x


class TextureWrap(IntEnum):
	"""Texture parameters: wrap mode"""
	TEXTURE_WRAP_REPEAT: int = 0  # Repeats texture in tiled mode
	TEXTURE_WRAP_CLAMP: int = 1  # Clamps texture to edge pixel in tiled mode
	TEXTURE_WRAP_MIRROR_REPEAT: int = 2  # Mirrors and repeats the texture in tiled mode
	TEXTURE_WRAP_MIRROR_CLAMP: int = 3  # Mirrors and clamps to border the texture in tiled mode


class CubemapLayout(IntEnum):
	"""Cubemap layouts"""
	CUBEMAP_LAYOUT_AUTO_DETECT: int = 0  # Automatically detect layout type
	CUBEMAP_LAYOUT_LINE_VERTICAL: int = 1  # Layout is defined by a vertical line with faces
	CUBEMAP_LAYOUT_LINE_HORIZONTAL: int = 2  # Layout is defined by an horizontal line with faces
	CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR: int = 3  # Layout is defined by a 3x4 cross with cubemap faces
	CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE: int = 4  # Layout is defined by a 4x3 cross with cubemap faces
	CUBEMAP_LAYOUT_PANORAMA: int = 5  # Layout is defined by a panorama image (equirectangular map)


class FontType(IntEnum):
	"""Font type, defines generation method"""
	FONT_DEFAULT: int = 0  # Default font generation, anti-aliased
	FONT_BITMAP: int = 1  # Bitmap font generation, no anti-aliasing
	FONT_SDF: int = 2  # SDF font generation, requires external shader


class BlendMode(IntEnum):
	"""Color blending modes (pre-defined)"""
	BLEND_ALPHA: int = 0  # Blend textures considering alpha (default)
	BLEND_ADDITIVE: int = 1  # Blend textures adding colors
	BLEND_MULTIPLIED: int = 2  # Blend textures multiplying colors
	BLEND_ADD_COLORS: int = 3  # Blend textures adding colors (alternative)
	BLEND_SUBTRACT_COLORS: int = 4  # Blend textures subtracting colors (alternative)
	BLEND_ALPHA_PREMULTIPLY: int = 5  # Blend premultiplied textures considering alpha
	BLEND_CUSTOM: int = 6  # Blend textures using custom src/dst factors (use rlSetBlendMode())


class Gesture(IntEnum):
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


class CameraMode(IntEnum):
	"""Camera system modes"""
	CAMERA_CUSTOM: int = 0  # Custom camera
	CAMERA_FREE: int = 1  # Free camera
	CAMERA_ORBITAL: int = 2  # Orbital camera
	CAMERA_FIRST_PERSON: int = 3  # First person camera
	CAMERA_THIRD_PERSON: int = 4  # Third person camera


class CameraProjection(IntEnum):
	"""Camera projection"""
	CAMERA_PERSPECTIVE: int = 0  # Perspective projection
	CAMERA_ORTHOGRAPHIC: int = 1  # Orthographic projection


class NPatchLayout(IntEnum):
	"""N-patch layout"""
	NPATCH_NINE_PATCH: int = 0  # Npatch layout: 3x3 tiles
	NPATCH_THREE_PATCH_VERTICAL: int = 1  # Npatch layout: 1x3 tiles
	NPATCH_THREE_PATCH_HORIZONTAL: int = 2  # Npatch layout: 3x1 tiles


class GuiState(IntEnum):
	"""Gui control state"""
	STATE_NORMAL: int = 0  # 
	STATE_FOCUSED: int = 1  # 
	STATE_PRESSED: int = 2  # 
	STATE_DISABLED: int = 3  # 


class GuiTextAlignment(IntEnum):
	"""Gui control text alignment"""
	TEXT_ALIGN_LEFT: int = 0  # 
	TEXT_ALIGN_CENTER: int = 1  # 
	TEXT_ALIGN_RIGHT: int = 2  # 


class GuiControl(IntEnum):
	"""Gui controls"""
	DEFAULT: int = 0  # 
	LABEL: int = 1  # Used also for: LABELBUTTON
	BUTTON: int = 2  # 
	TOGGLE: int = 3  # Used also for: TOGGLEGROUP
	SLIDER: int = 4  # Used also for: SLIDERBAR
	PROGRESSBAR: int = 5  # 
	CHECKBOX: int = 6  # 
	COMBOBOX: int = 7  # 
	DROPDOWNBOX: int = 8  # 
	TEXTBOX: int = 9  # Used also for: TEXTBOXMULTI
	VALUEBOX: int = 10  # 
	SPINNER: int = 11  # Uses: BUTTON, VALUEBOX
	LISTVIEW: int = 12  # 
	COLORPICKER: int = 13  # 
	SCROLLBAR: int = 14  # 
	STATUSBAR: int = 15  # 


class GuiControlProperty(IntEnum):
	"""Gui base properties for every control"""
	BORDER_COLOR_NORMAL: int = 0  # 
	BASE_COLOR_NORMAL: int = 1  # 
	TEXT_COLOR_NORMAL: int = 2  # 
	BORDER_COLOR_FOCUSED: int = 3  # 
	BASE_COLOR_FOCUSED: int = 4  # 
	TEXT_COLOR_FOCUSED: int = 5  # 
	BORDER_COLOR_PRESSED: int = 6  # 
	BASE_COLOR_PRESSED: int = 7  # 
	TEXT_COLOR_PRESSED: int = 8  # 
	BORDER_COLOR_DISABLED: int = 9  # 
	BASE_COLOR_DISABLED: int = 10  # 
	TEXT_COLOR_DISABLED: int = 11  # 
	BORDER_WIDTH: int = 12  # 
	TEXT_PADDING: int = 13  # 
	TEXT_ALIGNMENT: int = 14  # 
	RESERVED: int = 15  # 


class GuiDefaultProperty(IntEnum):
	"""DEFAULT extended properties"""
	TEXT_SIZE: int = 16  # Text size (glyphs max height)
	TEXT_SPACING: int = 17  # Text spacing between glyphs
	LINE_COLOR: int = 18  # Line control color
	BACKGROUND_COLOR: int = 19  # Background color


class GuiToggleProperty(IntEnum):
	"""Toggle/ToggleGroup"""
	GROUP_PADDING: int = 16  # ToggleGroup separation between toggles


class GuiSliderProperty(IntEnum):
	"""Slider/SliderBar"""
	SLIDER_WIDTH: int = 16  # Slider size of internal bar
	SLIDER_PADDING: int = 17  # Slider/SliderBar internal bar padding


class GuiProgressBarProperty(IntEnum):
	"""ProgressBar"""
	PROGRESS_PADDING: int = 16  # ProgressBar internal padding


class GuiScrollBarProperty(IntEnum):
	"""ScrollBar"""
	ARROWS_SIZE: int = 16  # 
	ARROWS_VISIBLE: int = 17  # 
	SCROLL_SLIDER_PADDING: int = 18  # (SLIDERBAR, SLIDER_PADDING)
	SCROLL_SLIDER_SIZE: int = 19  # 
	SCROLL_PADDING: int = 20  # 
	SCROLL_SPEED: int = 21  # 


class GuiCheckBoxProperty(IntEnum):
	"""CheckBox"""
	CHECK_PADDING: int = 16  # CheckBox internal check padding


class GuiComboBoxProperty(IntEnum):
	"""ComboBox"""
	COMBO_BUTTON_WIDTH: int = 16  # ComboBox right button width
	COMBO_BUTTON_SPACING: int = 17  # ComboBox button separation


class GuiDropdownBoxProperty(IntEnum):
	"""DropdownBox"""
	ARROW_PADDING: int = 16  # DropdownBox arrow separation from border and items
	DROPDOWN_ITEMS_SPACING: int = 17  # DropdownBox items separation


class GuiTextBoxProperty(IntEnum):
	"""TextBox/TextBoxMulti/ValueBox/Spinner"""
	TEXT_INNER_PADDING: int = 16  # TextBox/TextBoxMulti/ValueBox/Spinner inner text padding
	TEXT_LINES_SPACING: int = 17  # TextBoxMulti lines separation


class GuiSpinnerProperty(IntEnum):
	"""Spinner"""
	SPIN_BUTTON_WIDTH: int = 16  # Spinner left/right buttons width
	SPIN_BUTTON_SPACING: int = 17  # Spinner buttons separation


class GuiListViewProperty(IntEnum):
	"""ListView"""
	LIST_ITEMS_HEIGHT: int = 16  # ListView items height
	LIST_ITEMS_SPACING: int = 17  # ListView items separation
	SCROLLBAR_WIDTH: int = 18  # ListView scrollbar size (usually width)
	SCROLLBAR_SIDE: int = 19  # ListView scrollbar side (0-left, 1-right)


class GuiColorPickerProperty(IntEnum):
	"""ColorPicker"""
	COLOR_SELECTOR_SIZE: int = 16  # 
	HUEBAR_WIDTH: int = 17  # ColorPicker right hue bar width
	HUEBAR_PADDING: int = 18  # ColorPicker right hue bar separation from panel
	HUEBAR_SELECTOR_HEIGHT: int = 19  # ColorPicker right hue bar selector height
	HUEBAR_SELECTOR_OVERFLOW: int = 20  # ColorPicker right hue bar selector overflow


class GuiIconName(IntEnum):
	""""""
	ICON_NONE: int = 0  # 
	ICON_FOLDER_FILE_OPEN: int = 1  # 
	ICON_FILE_SAVE_CLASSIC: int = 2  # 
	ICON_FOLDER_OPEN: int = 3  # 
	ICON_FOLDER_SAVE: int = 4  # 
	ICON_FILE_OPEN: int = 5  # 
	ICON_FILE_SAVE: int = 6  # 
	ICON_FILE_EXPORT: int = 7  # 
	ICON_FILE_ADD: int = 8  # 
	ICON_FILE_DELETE: int = 9  # 
	ICON_FILETYPE_TEXT: int = 10  # 
	ICON_FILETYPE_AUDIO: int = 11  # 
	ICON_FILETYPE_IMAGE: int = 12  # 
	ICON_FILETYPE_PLAY: int = 13  # 
	ICON_FILETYPE_VIDEO: int = 14  # 
	ICON_FILETYPE_INFO: int = 15  # 
	ICON_FILE_COPY: int = 16  # 
	ICON_FILE_CUT: int = 17  # 
	ICON_FILE_PASTE: int = 18  # 
	ICON_CURSOR_HAND: int = 19  # 
	ICON_CURSOR_POINTER: int = 20  # 
	ICON_CURSOR_CLASSIC: int = 21  # 
	ICON_PENCIL: int = 22  # 
	ICON_PENCIL_BIG: int = 23  # 
	ICON_BRUSH_CLASSIC: int = 24  # 
	ICON_BRUSH_PAINTER: int = 25  # 
	ICON_WATER_DROP: int = 26  # 
	ICON_COLOR_PICKER: int = 27  # 
	ICON_RUBBER: int = 28  # 
	ICON_COLOR_BUCKET: int = 29  # 
	ICON_TEXT_T: int = 30  # 
	ICON_TEXT_A: int = 31  # 
	ICON_SCALE: int = 32  # 
	ICON_RESIZE: int = 33  # 
	ICON_FILTER_POINT: int = 34  # 
	ICON_FILTER_BILINEAR: int = 35  # 
	ICON_CROP: int = 36  # 
	ICON_CROP_ALPHA: int = 37  # 
	ICON_SQUARE_TOGGLE: int = 38  # 
	ICON_SYMMETRY: int = 39  # 
	ICON_SYMMETRY_HORIZONTAL: int = 40  # 
	ICON_SYMMETRY_VERTICAL: int = 41  # 
	ICON_LENS: int = 42  # 
	ICON_LENS_BIG: int = 43  # 
	ICON_EYE_ON: int = 44  # 
	ICON_EYE_OFF: int = 45  # 
	ICON_FILTER_TOP: int = 46  # 
	ICON_FILTER: int = 47  # 
	ICON_TARGET_POINT: int = 48  # 
	ICON_TARGET_SMALL: int = 49  # 
	ICON_TARGET_BIG: int = 50  # 
	ICON_TARGET_MOVE: int = 51  # 
	ICON_CURSOR_MOVE: int = 52  # 
	ICON_CURSOR_SCALE: int = 53  # 
	ICON_CURSOR_SCALE_RIGHT: int = 54  # 
	ICON_CURSOR_SCALE_LEFT: int = 55  # 
	ICON_UNDO: int = 56  # 
	ICON_REDO: int = 57  # 
	ICON_REREDO: int = 58  # 
	ICON_MUTATE: int = 59  # 
	ICON_ROTATE: int = 60  # 
	ICON_REPEAT: int = 61  # 
	ICON_SHUFFLE: int = 62  # 
	ICON_EMPTYBOX: int = 63  # 
	ICON_TARGET: int = 64  # 
	ICON_TARGET_SMALL_FILL: int = 65  # 
	ICON_TARGET_BIG_FILL: int = 66  # 
	ICON_TARGET_MOVE_FILL: int = 67  # 
	ICON_CURSOR_MOVE_FILL: int = 68  # 
	ICON_CURSOR_SCALE_FILL: int = 69  # 
	ICON_CURSOR_SCALE_RIGHT_FILL: int = 70  # 
	ICON_CURSOR_SCALE_LEFT_FILL: int = 71  # 
	ICON_UNDO_FILL: int = 72  # 
	ICON_REDO_FILL: int = 73  # 
	ICON_REREDO_FILL: int = 74  # 
	ICON_MUTATE_FILL: int = 75  # 
	ICON_ROTATE_FILL: int = 76  # 
	ICON_REPEAT_FILL: int = 77  # 
	ICON_SHUFFLE_FILL: int = 78  # 
	ICON_EMPTYBOX_SMALL: int = 79  # 
	ICON_BOX: int = 80  # 
	ICON_BOX_TOP: int = 81  # 
	ICON_BOX_TOP_RIGHT: int = 82  # 
	ICON_BOX_RIGHT: int = 83  # 
	ICON_BOX_BOTTOM_RIGHT: int = 84  # 
	ICON_BOX_BOTTOM: int = 85  # 
	ICON_BOX_BOTTOM_LEFT: int = 86  # 
	ICON_BOX_LEFT: int = 87  # 
	ICON_BOX_TOP_LEFT: int = 88  # 
	ICON_BOX_CENTER: int = 89  # 
	ICON_BOX_CIRCLE_MASK: int = 90  # 
	ICON_POT: int = 91  # 
	ICON_ALPHA_MULTIPLY: int = 92  # 
	ICON_ALPHA_CLEAR: int = 93  # 
	ICON_DITHERING: int = 94  # 
	ICON_MIPMAPS: int = 95  # 
	ICON_BOX_GRID: int = 96  # 
	ICON_GRID: int = 97  # 
	ICON_BOX_CORNERS_SMALL: int = 98  # 
	ICON_BOX_CORNERS_BIG: int = 99  # 
	ICON_FOUR_BOXES: int = 100  # 
	ICON_GRID_FILL: int = 101  # 
	ICON_BOX_MULTISIZE: int = 102  # 
	ICON_ZOOM_SMALL: int = 103  # 
	ICON_ZOOM_MEDIUM: int = 104  # 
	ICON_ZOOM_BIG: int = 105  # 
	ICON_ZOOM_ALL: int = 106  # 
	ICON_ZOOM_CENTER: int = 107  # 
	ICON_BOX_DOTS_SMALL: int = 108  # 
	ICON_BOX_DOTS_BIG: int = 109  # 
	ICON_BOX_CONCENTRIC: int = 110  # 
	ICON_BOX_GRID_BIG: int = 111  # 
	ICON_OK_TICK: int = 112  # 
	ICON_CROSS: int = 113  # 
	ICON_ARROW_LEFT: int = 114  # 
	ICON_ARROW_RIGHT: int = 115  # 
	ICON_ARROW_DOWN: int = 116  # 
	ICON_ARROW_UP: int = 117  # 
	ICON_ARROW_LEFT_FILL: int = 118  # 
	ICON_ARROW_RIGHT_FILL: int = 119  # 
	ICON_ARROW_DOWN_FILL: int = 120  # 
	ICON_ARROW_UP_FILL: int = 121  # 
	ICON_AUDIO: int = 122  # 
	ICON_FX: int = 123  # 
	ICON_WAVE: int = 124  # 
	ICON_WAVE_SINUS: int = 125  # 
	ICON_WAVE_SQUARE: int = 126  # 
	ICON_WAVE_TRIANGULAR: int = 127  # 
	ICON_CROSS_SMALL: int = 128  # 
	ICON_PLAYER_PREVIOUS: int = 129  # 
	ICON_PLAYER_PLAY_BACK: int = 130  # 
	ICON_PLAYER_PLAY: int = 131  # 
	ICON_PLAYER_PAUSE: int = 132  # 
	ICON_PLAYER_STOP: int = 133  # 
	ICON_PLAYER_NEXT: int = 134  # 
	ICON_PLAYER_RECORD: int = 135  # 
	ICON_MAGNET: int = 136  # 
	ICON_LOCK_CLOSE: int = 137  # 
	ICON_LOCK_OPEN: int = 138  # 
	ICON_CLOCK: int = 139  # 
	ICON_TOOLS: int = 140  # 
	ICON_GEAR: int = 141  # 
	ICON_GEAR_BIG: int = 142  # 
	ICON_BIN: int = 143  # 
	ICON_HAND_POINTER: int = 144  # 
	ICON_LASER: int = 145  # 
	ICON_COIN: int = 146  # 
	ICON_EXPLOSION: int = 147  # 
	ICON_1UP: int = 148  # 
	ICON_PLAYER: int = 149  # 
	ICON_PLAYER_JUMP: int = 150  # 
	ICON_KEY: int = 151  # 
	ICON_DEMON: int = 152  # 
	ICON_TEXT_POPUP: int = 153  # 
	ICON_GEAR_EX: int = 154  # 
	ICON_CRACK: int = 155  # 
	ICON_CRACK_POINTS: int = 156  # 
	ICON_STAR: int = 157  # 
	ICON_DOOR: int = 158  # 
	ICON_EXIT: int = 159  # 
	ICON_MODE_2D: int = 160  # 
	ICON_MODE_3D: int = 161  # 
	ICON_CUBE: int = 162  # 
	ICON_CUBE_FACE_TOP: int = 163  # 
	ICON_CUBE_FACE_LEFT: int = 164  # 
	ICON_CUBE_FACE_FRONT: int = 165  # 
	ICON_CUBE_FACE_BOTTOM: int = 166  # 
	ICON_CUBE_FACE_RIGHT: int = 167  # 
	ICON_CUBE_FACE_BACK: int = 168  # 
	ICON_CAMERA: int = 169  # 
	ICON_SPECIAL: int = 170  # 
	ICON_LINK_NET: int = 171  # 
	ICON_LINK_BOXES: int = 172  # 
	ICON_LINK_MULTI: int = 173  # 
	ICON_LINK: int = 174  # 
	ICON_LINK_BROKE: int = 175  # 
	ICON_TEXT_NOTES: int = 176  # 
	ICON_NOTEBOOK: int = 177  # 
	ICON_SUITCASE: int = 178  # 
	ICON_SUITCASE_ZIP: int = 179  # 
	ICON_MAILBOX: int = 180  # 
	ICON_MONITOR: int = 181  # 
	ICON_PRINTER: int = 182  # 
	ICON_PHOTO_CAMERA: int = 183  # 
	ICON_PHOTO_CAMERA_FLASH: int = 184  # 
	ICON_HOUSE: int = 185  # 
	ICON_HEART: int = 186  # 
	ICON_CORNER: int = 187  # 
	ICON_VERTICAL_BARS: int = 188  # 
	ICON_VERTICAL_BARS_FILL: int = 189  # 
	ICON_LIFE_BARS: int = 190  # 
	ICON_INFO: int = 191  # 
	ICON_CROSSLINE: int = 192  # 
	ICON_HELP: int = 193  # 
	ICON_FILETYPE_ALPHA: int = 194  # 
	ICON_FILETYPE_HOME: int = 195  # 
	ICON_LAYERS_VISIBLE: int = 196  # 
	ICON_LAYERS: int = 197  # 
	ICON_WINDOW: int = 198  # 
	ICON_HIDPI: int = 199  # 
	ICON_FILETYPE_BINARY: int = 200  # 
	ICON_HEX: int = 201  # 
	ICON_SHIELD: int = 202  # 
	ICON_FILE_NEW: int = 203  # 
	ICON_FOLDER_ADD: int = 204  # 
	ICON_ALARM: int = 205  # 
	ICON_206: int = 206  # 
	ICON_207: int = 207  # 
	ICON_208: int = 208  # 
	ICON_209: int = 209  # 
	ICON_210: int = 210  # 
	ICON_211: int = 211  # 
	ICON_212: int = 212  # 
	ICON_213: int = 213  # 
	ICON_214: int = 214  # 
	ICON_215: int = 215  # 
	ICON_216: int = 216  # 
	ICON_217: int = 217  # 
	ICON_218: int = 218  # 
	ICON_219: int = 219  # 
	ICON_220: int = 220  # 
	ICON_221: int = 221  # 
	ICON_222: int = 222  # 
	ICON_223: int = 223  # 
	ICON_224: int = 224  # 
	ICON_225: int = 225  # 
	ICON_226: int = 226  # 
	ICON_227: int = 227  # 
	ICON_228: int = 228  # 
	ICON_229: int = 229  # 
	ICON_230: int = 230  # 
	ICON_231: int = 231  # 
	ICON_232: int = 232  # 
	ICON_233: int = 233  # 
	ICON_234: int = 234  # 
	ICON_235: int = 235  # 
	ICON_236: int = 236  # 
	ICON_237: int = 237  # 
	ICON_238: int = 238  # 
	ICON_239: int = 239  # 
	ICON_240: int = 240  # 
	ICON_241: int = 241  # 
	ICON_242: int = 242  # 
	ICON_243: int = 243  # 
	ICON_244: int = 244  # 
	ICON_245: int = 245  # 
	ICON_246: int = 246  # 
	ICON_247: int = 247  # 
	ICON_248: int = 248  # 
	ICON_249: int = 249  # 
	ICON_250: int = 250  # 
	ICON_251: int = 251  # 
	ICON_252: int = 252  # 
	ICON_253: int = 253  # 
	ICON_254: int = 254  # 
	ICON_255: int = 255  # 


