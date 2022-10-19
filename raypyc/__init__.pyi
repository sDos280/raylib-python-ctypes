from raypyc.colors import *
from raypyc.enums import *
from raypyc.structures import *


def init_window(width: int, height: int, title: bytes) -> None:
	"""Initialize window and OpenGL context"""
	...

def window_should_close() -> bool:
	"""Check if KEY_ESCAPE pressed or Close icon pressed"""
	...

def close_window() -> None:
	"""Close window and unload OpenGL context"""
	...

def is_window_ready() -> bool:
	"""Check if window has been initialized successfully"""
	...

def is_window_fullscreen() -> bool:
	"""Check if window is currently fullscreen"""
	...

def is_window_hidden() -> bool:
	"""Check if window is currently hidden (only PLATFORM_DESKTOP)"""
	...

def is_window_minimized() -> bool:
	"""Check if window is currently minimized (only PLATFORM_DESKTOP)"""
	...

def is_window_maximized() -> bool:
	"""Check if window is currently maximized (only PLATFORM_DESKTOP)"""
	...

def is_window_focused() -> bool:
	"""Check if window is currently focused (only PLATFORM_DESKTOP)"""
	...

def is_window_resized() -> bool:
	"""Check if window has been resized last frame"""
	...

def is_window_state(flag: int) -> bool:
	"""Check if one specific window flag is enabled"""
	...

def set_window_state(flags: int) -> None:
	"""Set window configuration state using flags (only PLATFORM_DESKTOP)"""
	...

def clear_window_state(flags: int) -> None:
	"""Clear window configuration state flags"""
	...

def toggle_fullscreen() -> None:
	"""Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
	...

def maximize_window() -> None:
	"""Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
	...

def minimize_window() -> None:
	"""Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
	...

def restore_window() -> None:
	"""Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
	...

def set_window_icon(image: Image) -> None:
	"""Set icon for window (only PLATFORM_DESKTOP)"""
	...

def set_window_title(title: bytes) -> None:
	"""Set title for window (only PLATFORM_DESKTOP)"""
	...

def set_window_position(x: int, y: int) -> None:
	"""Set window position on screen (only PLATFORM_DESKTOP)"""
	...

def set_window_monitor(monitor: int) -> None:
	"""Set monitor for the current window (fullscreen mode)"""
	...

def set_window_min_size(width: int, height: int) -> None:
	"""Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
	...

def set_window_size(width: int, height: int) -> None:
	"""Set window dimensions"""
	...

def set_window_opacity(opacity: float) -> None:
	"""Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
	...

def get_window_handle() -> int:
	"""Get native window handle"""
	...

def get_screen_width() -> int:
	"""Get current screen width"""
	...

def get_screen_height() -> int:
	"""Get current screen height"""
	...

def get_render_width() -> int:
	"""Get current render width (it considers HiDPI)"""
	...

def get_render_height() -> int:
	"""Get current render height (it considers HiDPI)"""
	...

def get_monitor_count() -> int:
	"""Get number of connected monitors"""
	...

def get_current_monitor() -> int:
	"""Get current connected monitor"""
	...

def get_monitor_position(monitor: int) -> Vector2:
	"""Get specified monitor position"""
	...

def get_monitor_width(monitor: int) -> int:
	"""Get specified monitor width (current video mode used by monitor)"""
	...

def get_monitor_height(monitor: int) -> int:
	"""Get specified monitor height (current video mode used by monitor)"""
	...

def get_monitor_physical_width(monitor: int) -> int:
	"""Get specified monitor physical width in millimetres"""
	...

def get_monitor_physical_height(monitor: int) -> int:
	"""Get specified monitor physical height in millimetres"""
	...

def get_monitor_refresh_rate(monitor: int) -> int:
	"""Get specified monitor refresh rate"""
	...

def get_window_position() -> Vector2:
	"""Get window position XY on monitor"""
	...

def get_window_scale_dpi() -> Vector2:
	"""Get window scale DPI factor"""
	...

def get_monitor_name(monitor: int) -> bytes:
	"""Get the human-readable, UTF-8 encoded name of the primary monitor"""
	...

def set_clipboard_text(text: bytes) -> None:
	"""Set clipboard text content"""
	...

def get_clipboard_text() -> bytes:
	"""Get clipboard text content"""
	...

def enable_event_waiting() -> None:
	"""Enable waiting for events on EndDrawing(), no automatic event polling"""
	...

def disable_event_waiting() -> None:
	"""Disable waiting for events on EndDrawing(), automatic events polling"""
	...

def swap_screen_buffer() -> None:
	"""Swap back buffer with front buffer (screen drawing)"""
	...

def poll_input_events() -> None:
	"""Register all input events"""
	...

def wait_time(seconds: float) -> None:
	"""Wait for some time (halt program execution)"""
	...

def show_cursor() -> None:
	"""Shows cursor"""
	...

def hide_cursor() -> None:
	"""Hides cursor"""
	...

def is_cursor_hidden() -> bool:
	"""Check if cursor is not visible"""
	...

def enable_cursor() -> None:
	"""Enables cursor (unlock cursor)"""
	...

def disable_cursor() -> None:
	"""Disables cursor (lock cursor)"""
	...

def is_cursor_on_screen() -> bool:
	"""Check if cursor is on the screen"""
	...

def clear_background(color: Color) -> None:
	"""Set background color (framebuffer clear color)"""
	...

def begin_drawing() -> None:
	"""Setup canvas (framebuffer) to start drawing"""
	...

def end_drawing() -> None:
	"""End canvas drawing and swap buffers (double buffering)"""
	...

def begin_mode_2d(camera: Camera2D) -> None:
	"""Begin 2D mode with custom camera (2D)"""
	...

def end_mode_2d() -> None:
	"""Ends 2D mode with custom camera"""
	...

def begin_mode_3d(camera: Camera3D) -> None:
	"""Begin 3D mode with custom camera (3D)"""
	...

def end_mode_3d() -> None:
	"""Ends 3D mode and returns to default 2D orthographic mode"""
	...

def begin_texture_mode(target: RenderTexture2D) -> None:
	"""Begin drawing to render texture"""
	...

def end_texture_mode() -> None:
	"""Ends drawing to render texture"""
	...

def begin_shader_mode(shader: Shader) -> None:
	"""Begin custom shader drawing"""
	...

def end_shader_mode() -> None:
	"""End custom shader drawing (use default shader)"""
	...

def begin_blend_mode(mode: int) -> None:
	"""Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
	...

def end_blend_mode() -> None:
	"""End blending mode (reset to default: alpha blending)"""
	...

def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None:
	"""Begin scissor mode (define screen area for following drawing)"""
	...

def end_scissor_mode() -> None:
	"""End scissor mode"""
	...

def begin_vr_stereo_mode(config: VrStereoConfig) -> None:
	"""Begin stereo rendering (requires VR simulator)"""
	...

def end_vr_stereo_mode() -> None:
	"""End stereo rendering (requires VR simulator)"""
	...

def load_vr_stereo_config(device: VrDeviceInfo) -> VrStereoConfig:
	"""Load VR stereo config for VR simulator device parameters"""
	...

def unload_vr_stereo_config(config: VrStereoConfig) -> None:
	"""Unload VR stereo config"""
	...

def load_shader(vsFileName: bytes, fsFileName: bytes) -> Shader:
	"""Load shader from files and bind default locations"""
	...

def load_shader_from_memory(vsCode: bytes, fsCode: bytes) -> Shader:
	"""Load shader from code strings and bind default locations"""
	...

def get_shader_location(shader: Shader, uniformName: bytes) -> int:
	"""Get shader uniform location"""
	...

def get_shader_location_attrib(shader: Shader, attribName: bytes) -> int:
	"""Get shader attribute location"""
	...

def set_shader_value(shader: Shader, locIndex: int, value: int, uniformType: int) -> None:
	"""Set shader uniform value"""
	...

def set_shader_value_v(shader: Shader, locIndex: int, value: int, uniformType: int, count: int) -> None:
	"""Set shader uniform value vector"""
	...

def set_shader_value_matrix(shader: Shader, locIndex: int, mat: Matrix) -> None:
	"""Set shader uniform value (matrix 4x4)"""
	...

def set_shader_value_texture(shader: Shader, locIndex: int, texture: Texture2D) -> None:
	"""Set shader uniform value for texture (sampler2d)"""
	...

def unload_shader(shader: Shader) -> None:
	"""Unload shader from GPU memory (VRAM)"""
	...

def get_mouse_ray(mousePosition: Vector2, camera: Camera) -> Ray:
	"""Get a ray trace from mouse position"""
	...

def get_camera_matrix(camera: Camera) -> Matrix:
	"""Get camera transform matrix (view matrix)"""
	...

def get_camera_matrix_2d(camera: Camera2D) -> Matrix:
	"""Get camera 2d transform matrix"""
	...

def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2:
	"""Get the screen space position for a 3d world space position"""
	...

def get_screen_to_world_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Get the world space position for a 2d camera screen space position"""
	...

def get_world_to_screen_ex(position: Vector3, camera: Camera, width: int, height: int) -> Vector2:
	"""Get size position for a 3d world space position"""
	...

def get_world_to_screen_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Get the screen space position for a 2d camera world space position"""
	...

def set_target_fps(fps: int) -> None:
	"""Set target FPS (maximum)"""
	...

def get_fps() -> int:
	"""Get current FPS"""
	...

def get_frame_time() -> float:
	"""Get time in seconds for last frame drawn (delta time)"""
	...

def get_time() -> float:
	"""Get elapsed time in seconds since InitWindow()"""
	...

def get_random_value(min: int, max: int) -> int:
	"""Get a random value between min and max (both included)"""
	...

def set_random_seed(seed: int) -> None:
	"""Set the seed for the random number generator"""
	...

def take_screenshot(fileName: bytes) -> None:
	"""Takes a screenshot of current screen (filename extension defines format)"""
	...

def set_config_flags(flags: int) -> None:
	"""Setup init configuration flags (view FLAGS)"""
	...

def trace_log(logLevel: int, text: bytes, args: ...) -> None:
	"""Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
	...

def set_trace_log_level(logLevel: int) -> None:
	"""Set the current threshold (minimum) log level"""
	...

def mem_alloc(size: int) -> int:
	"""Internal memory allocator"""
	...

def mem_realloc(ptr: int, size: int) -> int:
	"""Internal memory reallocator"""
	...

def mem_free(ptr: int) -> None:
	"""Internal memory free"""
	...

def open_url(url: bytes) -> None:
	"""Open URL with default system browser (if available)"""
	...

def load_file_data(fileName: bytes, bytesRead: POINTER(c_uint)) -> POINTER(c_ubyte):
	"""Load file data as byte array (read)"""
	...

def unload_file_data(data: POINTER(c_ubyte)) -> None:
	"""Unload file data allocated by LoadFileData()"""
	...

def save_file_data(fileName: bytes, data: int, bytesToWrite: int) -> bool:
	"""Save data to file from byte array (write), returns true on success"""
	...

def export_data_as_code(data: bytes, size: int, fileName: bytes) -> bool:
	"""Export data to code (.h), returns true on success"""
	...

def load_file_text(fileName: bytes) -> bytes:
	"""Load text data from file (read), returns a '\0' terminated string"""
	...

def unload_file_text(text: bytes) -> None:
	"""Unload file text data allocated by LoadFileText()"""
	...

def save_file_text(fileName: bytes, text: bytes) -> bool:
	"""Save text data to file (write), string must be '\0' terminated, returns true on success"""
	...

def file_exists(fileName: bytes) -> bool:
	"""Check if file exists"""
	...

def directory_exists(dirPath: bytes) -> bool:
	"""Check if a directory path exists"""
	...

def is_file_extension(fileName: bytes, ext: bytes) -> bool:
	"""Check file extension (including point: .png, .wav)"""
	...

def get_file_length(fileName: bytes) -> int:
	"""Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
	...

def get_file_extension(fileName: bytes) -> bytes:
	"""Get pointer to extension for a filename string (includes dot: '.png')"""
	...

def get_file_name(filePath: bytes) -> bytes:
	"""Get pointer to filename for a path string"""
	...

def get_file_name_without_ext(filePath: bytes) -> bytes:
	"""Get filename string without extension (uses static string)"""
	...

def get_directory_path(filePath: bytes) -> bytes:
	"""Get full path for a given fileName with path (uses static string)"""
	...

def get_prev_directory_path(dirPath: bytes) -> bytes:
	"""Get previous directory path for a given path (uses static string)"""
	...

def get_working_directory() -> bytes:
	"""Get current working directory (uses static string)"""
	...

def get_application_directory() -> bytes:
	"""Get the directory if the running application (uses static string)"""
	...

def change_directory(dir: bytes) -> bool:
	"""Change working directory, return true on success"""
	...

def is_path_file(path: bytes) -> bool:
	"""Check if a given path is a file or a directory"""
	...

def load_directory_files(dirPath: bytes) -> FilePathList:
	"""Load directory filepaths"""
	...

def load_directory_files_ex(basePath: bytes, filter: bytes, scanSubdirs: bool) -> FilePathList:
	"""Load directory filepaths with extension filtering and recursive directory scan"""
	...

def unload_directory_files(files: FilePathList) -> None:
	"""Unload filepaths"""
	...

def is_file_dropped() -> bool:
	"""Check if a file has been dropped into window"""
	...

def load_dropped_files() -> FilePathList:
	"""Load dropped filepaths"""
	...

def unload_dropped_files(files: FilePathList) -> None:
	"""Unload dropped filepaths"""
	...

def get_file_mod_time(fileName: bytes) -> int:
	"""Get file modification time (last write time)"""
	...

def compress_data(data: POINTER(c_ubyte), dataSize: int, compDataSize: POINTER(c_int)) -> POINTER(c_ubyte):
	"""Compress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def decompress_data(compData: POINTER(c_ubyte), compDataSize: int, dataSize: POINTER(c_int)) -> POINTER(c_ubyte):
	"""Decompress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def encode_data_base64(data: POINTER(c_ubyte), dataSize: int, outputSize: POINTER(c_int)) -> bytes:
	"""Encode data to Base64 string, memory must be MemFree()"""
	...

def decode_data_base64(data: POINTER(c_ubyte), outputSize: POINTER(c_int)) -> POINTER(c_ubyte):
	"""Decode Base64 string data, memory must be MemFree()"""
	...

def is_key_pressed(key: int) -> bool:
	"""Check if a key has been pressed once"""
	...

def is_key_down(key: int) -> bool:
	"""Check if a key is being pressed"""
	...

def is_key_released(key: int) -> bool:
	"""Check if a key has been released once"""
	...

def is_key_up(key: int) -> bool:
	"""Check if a key is NOT being pressed"""
	...

def set_exit_key(key: int) -> None:
	"""Set a custom key to exit program (default is ESC)"""
	...

def get_key_pressed() -> int:
	"""Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
	...

def get_char_pressed() -> int:
	"""Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
	...

def is_gamepad_available(gamepad: int) -> bool:
	"""Check if a gamepad is available"""
	...

def get_gamepad_name(gamepad: int) -> bytes:
	"""Get gamepad internal name id"""
	...

def is_gamepad_button_pressed(gamepad: int, button: int) -> bool:
	"""Check if a gamepad button has been pressed once"""
	...

def is_gamepad_button_down(gamepad: int, button: int) -> bool:
	"""Check if a gamepad button is being pressed"""
	...

def is_gamepad_button_released(gamepad: int, button: int) -> bool:
	"""Check if a gamepad button has been released once"""
	...

def is_gamepad_button_up(gamepad: int, button: int) -> bool:
	"""Check if a gamepad button is NOT being pressed"""
	...

def get_gamepad_button_pressed() -> int:
	"""Get the last gamepad button pressed"""
	...

def get_gamepad_axis_count(gamepad: int) -> int:
	"""Get gamepad axis count for a gamepad"""
	...

def get_gamepad_axis_movement(gamepad: int, axis: int) -> float:
	"""Get axis movement value for a gamepad axis"""
	...

def set_gamepad_mappings(mappings: bytes) -> int:
	"""Set internal gamepad mappings (SDL_GameControllerDB)"""
	...

def is_mouse_button_pressed(button: int) -> bool:
	"""Check if a mouse button has been pressed once"""
	...

def is_mouse_button_down(button: int) -> bool:
	"""Check if a mouse button is being pressed"""
	...

def is_mouse_button_released(button: int) -> bool:
	"""Check if a mouse button has been released once"""
	...

def is_mouse_button_up(button: int) -> bool:
	"""Check if a mouse button is NOT being pressed"""
	...

def get_mouse_x() -> int:
	"""Get mouse position X"""
	...

def get_mouse_y() -> int:
	"""Get mouse position Y"""
	...

def get_mouse_position() -> Vector2:
	"""Get mouse position XY"""
	...

def get_mouse_delta() -> Vector2:
	"""Get mouse delta between frames"""
	...

def set_mouse_position(x: int, y: int) -> None:
	"""Set mouse position XY"""
	...

def set_mouse_offset(offsetX: int, offsetY: int) -> None:
	"""Set mouse offset"""
	...

def set_mouse_scale(scaleX: float, scaleY: float) -> None:
	"""Set mouse scaling"""
	...

def get_mouse_wheel_move() -> float:
	"""Get mouse wheel movement for X or Y, whichever is larger"""
	...

def get_mouse_wheel_move_v() -> Vector2:
	"""Get mouse wheel movement for both X and Y"""
	...

def set_mouse_cursor(cursor: int) -> None:
	"""Set mouse cursor"""
	...

def get_touch_x() -> int:
	"""Get touch position X for touch point 0 (relative to screen size)"""
	...

def get_touch_y() -> int:
	"""Get touch position Y for touch point 0 (relative to screen size)"""
	...

def get_touch_position(index: int) -> Vector2:
	"""Get touch position XY for a touch point index (relative to screen size)"""
	...

def get_touch_point_id(index: int) -> int:
	"""Get touch point identifier for given index"""
	...

def get_touch_point_count() -> int:
	"""Get number of touch points"""
	...

def set_gestures_enabled(flags: int) -> None:
	"""Enable a set of gestures using flags"""
	...

def is_gesture_detected(gesture: int) -> bool:
	"""Check if a gesture have been detected"""
	...

def get_gesture_detected() -> int:
	"""Get latest detected gesture"""
	...

def get_gesture_hold_duration() -> float:
	"""Get gesture hold time in milliseconds"""
	...

def get_gesture_drag_vector() -> Vector2:
	"""Get gesture drag vector"""
	...

def get_gesture_drag_angle() -> float:
	"""Get gesture drag angle"""
	...

def get_gesture_pinch_vector() -> Vector2:
	"""Get gesture pinch delta"""
	...

def get_gesture_pinch_angle() -> float:
	"""Get gesture pinch angle"""
	...

def set_camera_mode(camera: Camera, mode: int) -> None:
	"""Set camera mode (multiple camera modes available)"""
	...

def update_camera(camera: POINTER(Camera)) -> None:
	"""Update camera position for selected mode"""
	...

def set_camera_pan_control(keyPan: int) -> None:
	"""Set camera pan key to combine with mouse movement (free camera)"""
	...

def set_camera_alt_control(keyAlt: int) -> None:
	"""Set camera alt key to combine with mouse movement (free camera)"""
	...

def set_camera_smooth_zoom_control(keySmoothZoom: int) -> None:
	"""Set camera smooth zoom key to combine with mouse (free camera)"""
	...

def set_camera_move_controls(keyFront: int, keyBack: int, keyRight: int, keyLeft: int, keyUp: int, keyDown: int) -> None:
	"""Set camera move controls (1st person and 3rd person cameras)"""
	...

def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None:
	"""Set texture and rectangle to be used on shapes drawing"""
	...

def draw_pixel(posX: int, posY: int, color: Color) -> None:
	"""Draw a pixel"""
	...

def draw_pixel_v(position: Vector2, color: Color) -> None:
	"""Draw a pixel (Vector version)"""
	...

def draw_line(startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
	"""Draw a line"""
	...

def draw_line_v(startPos: Vector2, endPos: Vector2, color: Color) -> None:
	"""Draw a line (Vector version)"""
	...

def draw_line_ex(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
	"""Draw a line defining thickness"""
	...

def draw_line_bezier(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
	"""Draw a line using cubic-bezier curves in-out"""
	...

def draw_line_bezier_quad(startPos: Vector2, endPos: Vector2, controlPos: Vector2, thick: float, color: Color) -> None:
	"""Draw line using quadratic bezier curves with a control point"""
	...

def draw_line_bezier_cubic(startPos: Vector2, endPos: Vector2, startControlPos: Vector2, endControlPos: Vector2, thick: float, color: Color) -> None:
	"""Draw line using cubic bezier curves with 2 control points"""
	...

def draw_line_strip(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	"""Draw lines sequence"""
	...

def draw_circle(centerX: int, centerY: int, radius: float, color: Color) -> None:
	"""Draw a color-filled circle"""
	...

def draw_circle_sector(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	"""Draw a piece of a circle"""
	...

def draw_circle_sector_lines(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	"""Draw circle sector outline"""
	...

def draw_circle_gradient(centerX: int, centerY: int, radius: float, color1: Color, color2: Color) -> None:
	"""Draw a gradient-filled circle"""
	...

def draw_circle_v(center: Vector2, radius: float, color: Color) -> None:
	"""Draw a color-filled circle (Vector version)"""
	...

def draw_circle_lines(centerX: int, centerY: int, radius: float, color: Color) -> None:
	"""Draw circle outline"""
	...

def draw_ellipse(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
	"""Draw ellipse"""
	...

def draw_ellipse_lines(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
	"""Draw ellipse outline"""
	...

def draw_ring(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	"""Draw ring"""
	...

def draw_ring_lines(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	"""Draw ring outline"""
	...

def draw_rectangle(posX: int, posY: int, width: int, height: int, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw a color-filled rectangle (Vector version)"""
	...

def draw_rectangle_rec(rec: Rectangle, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None:
	"""Draw a color-filled rectangle with pro parameters"""
	...

def draw_rectangle_gradient_v(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
	"""Draw a vertical-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_h(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
	"""Draw a horizontal-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
	"""Draw a gradient-filled rectangle with custom vertex colors"""
	...

def draw_rectangle_lines(posX: int, posY: int, width: int, height: int, color: Color) -> None:
	"""Draw rectangle outline"""
	...

def draw_rectangle_lines_ex(rec: Rectangle, lineThick: float, color: Color) -> None:
	"""Draw rectangle outline with extended parameters"""
	...

def draw_rectangle_rounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None:
	"""Draw rectangle with rounded edges"""
	...

def draw_rectangle_rounded_lines(rec: Rectangle, roundness: float, segments: int, lineThick: float, color: Color) -> None:
	"""Draw rectangle with rounded edges outline"""
	...

def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw triangle outline (vertex in counter-clockwise order!)"""
	...

def draw_triangle_fan(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	"""Draw a triangle fan defined by points (first vertex is the center)"""
	...

def draw_triangle_strip(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_poly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
	"""Draw a regular polygon (Vector version)"""
	...

def draw_poly_lines(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
	"""Draw a polygon outline of n sides"""
	...

def draw_poly_lines_ex(center: Vector2, sides: int, radius: float, rotation: float, lineThick: float, color: Color) -> None:
	"""Draw a polygon outline of n sides with extended parameters"""
	...

def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> bool:
	"""Check collision between two rectangles"""
	...

def check_collision_circles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool:
	"""Check collision between two circles"""
	...

def check_collision_circle_rec(center: Vector2, radius: float, rec: Rectangle) -> bool:
	"""Check collision between circle and rectangle"""
	...

def check_collision_point_rec(point: Vector2, rec: Rectangle) -> bool:
	"""Check if point is inside rectangle"""
	...

def check_collision_point_circle(point: Vector2, center: Vector2, radius: float) -> bool:
	"""Check if point is inside circle"""
	...

def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool:
	"""Check if point is inside a triangle"""
	...

def check_collision_lines(startPos1: Vector2, endPos1: Vector2, startPos2: Vector2, endPos2: Vector2, collisionPoint: POINTER(Vector2)) -> bool:
	"""Check the collision between two lines defined by two points each, returns collision point by reference"""
	...

def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: int) -> bool:
	"""Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
	...

def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle:
	"""Get collision rectangle for two rectangles collision"""
	...

def load_image(fileName: bytes) -> Image:
	"""Load image from file into CPU memory (RAM)"""
	...

def load_image_raw(fileName: bytes, width: int, height: int, format: int, headerSize: int) -> Image:
	"""Load image from RAW file data"""
	...

def load_image_anim(fileName: bytes, frames: POINTER(c_int)) -> Image:
	"""Load image sequence from file (frames appended to image.data)"""
	...

def load_image_from_memory(fileType: bytes, fileData: POINTER(c_ubyte), dataSize: int) -> Image:
	"""Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
	...

def load_image_from_texture(texture: Texture2D) -> Image:
	"""Load image from GPU texture data"""
	...

def load_image_from_screen() -> Image:
	"""Load image from screen buffer and (screenshot)"""
	...

def unload_image(image: Image) -> None:
	"""Unload image from CPU memory (RAM)"""
	...

def export_image(image: Image, fileName: bytes) -> bool:
	"""Export image data to file, returns true on success"""
	...

def export_image_as_code(image: Image, fileName: bytes) -> bool:
	"""Export image as code file defining an array of bytes, returns true on success"""
	...

def gen_image_color(width: int, height: int, color: Color) -> Image:
	"""Generate image: plain color"""
	...

def gen_image_gradient_v(width: int, height: int, top: Color, bottom: Color) -> Image:
	"""Generate image: vertical gradient"""
	...

def gen_image_gradient_h(width: int, height: int, left: Color, right: Color) -> Image:
	"""Generate image: horizontal gradient"""
	...

def gen_image_gradient_radial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
	"""Generate image: radial gradient"""
	...

def gen_image_checked(width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image:
	"""Generate image: checked"""
	...

def gen_image_white_noise(width: int, height: int, factor: float) -> Image:
	"""Generate image: white noise"""
	...

def gen_image_cellular(width: int, height: int, tileSize: int) -> Image:
	"""Generate image: cellular algorithm, bigger tileSize means bigger cells"""
	...

def image_copy(image: Image) -> Image:
	"""Create an image duplicate (useful for transformations)"""
	...

def image_from_image(image: Image, rec: Rectangle) -> Image:
	"""Create an image from another image piece"""
	...

def image_text(text: bytes, fontSize: int, color: Color) -> Image:
	"""Create an image from text (default font)"""
	...

def image_text_ex(font: Font, text: bytes, fontSize: float, spacing: float, tint: Color) -> Image:
	"""Create an image from text (custom sprite font)"""
	...

def image_format(image: POINTER(Image), newFormat: int) -> None:
	"""Convert image data to desired format"""
	...

def image_to_pot(image: POINTER(Image), fill: Color) -> None:
	"""Convert image to POT (power-of-two)"""
	...

def image_crop(image: POINTER(Image), crop: Rectangle) -> None:
	"""Crop an image to a defined rectangle"""
	...

def image_alpha_crop(image: POINTER(Image), threshold: float) -> None:
	"""Crop image depending on alpha value"""
	...

def image_alpha_clear(image: POINTER(Image), color: Color, threshold: float) -> None:
	"""Clear alpha channel to desired color"""
	...

def image_alpha_mask(image: POINTER(Image), alphaMask: Image) -> None:
	"""Apply alpha mask to image"""
	...

def image_alpha_premultiply(image: POINTER(Image)) -> None:
	"""Premultiply alpha channel"""
	...

def image_resize(image: POINTER(Image), newWidth: int, newHeight: int) -> None:
	"""Resize image (Bicubic scaling algorithm)"""
	...

def image_resize_nn(image: POINTER(Image), newWidth: int, newHeight: int) -> None:
	"""Resize image (Nearest-Neighbor scaling algorithm)"""
	...

def image_resize_canvas(image: POINTER(Image), newWidth: int, newHeight: int, offsetX: int, offsetY: int, fill: Color) -> None:
	"""Resize canvas and fill with color"""
	...

def image_mipmaps(image: POINTER(Image)) -> None:
	"""Compute all mipmap levels for a provided image"""
	...

def image_dither(image: POINTER(Image), rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None:
	"""Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
	...

def image_flip_vertical(image: POINTER(Image)) -> None:
	"""Flip image vertically"""
	...

def image_flip_horizontal(image: POINTER(Image)) -> None:
	"""Flip image horizontally"""
	...

def image_rotate_cw(image: POINTER(Image)) -> None:
	"""Rotate image clockwise 90deg"""
	...

def image_rotate_ccw(image: POINTER(Image)) -> None:
	"""Rotate image counter-clockwise 90deg"""
	...

def image_color_tint(image: POINTER(Image), color: Color) -> None:
	"""Modify image color: tint"""
	...

def image_color_invert(image: POINTER(Image)) -> None:
	"""Modify image color: invert"""
	...

def image_color_grayscale(image: POINTER(Image)) -> None:
	"""Modify image color: grayscale"""
	...

def image_color_contrast(image: POINTER(Image), contrast: float) -> None:
	"""Modify image color: contrast (-100 to 100)"""
	...

def image_color_brightness(image: POINTER(Image), brightness: int) -> None:
	"""Modify image color: brightness (-255 to 255)"""
	...

def image_color_replace(image: POINTER(Image), color: Color, replace: Color) -> None:
	"""Modify image color: replace color"""
	...

def load_image_colors(image: Image) -> POINTER(Color):
	"""Load color data from image as a Color array (RGBA - 32bit)"""
	...

def load_image_palette(image: Image, maxPaletteSize: int, colorCount: POINTER(c_int)) -> POINTER(Color):
	"""Load colors palette from image as a Color array (RGBA - 32bit)"""
	...

def unload_image_colors(colors: POINTER(Color)) -> None:
	"""Unload color data loaded with LoadImageColors()"""
	...

def unload_image_palette(colors: POINTER(Color)) -> None:
	"""Unload colors palette loaded with LoadImagePalette()"""
	...

def get_image_alpha_border(image: Image, threshold: float) -> Rectangle:
	"""Get image alpha border rectangle"""
	...

def get_image_color(image: Image, x: int, y: int) -> Color:
	"""Get image pixel color at (x, y) position"""
	...

def image_clear_background(dst: POINTER(Image), color: Color) -> None:
	"""Clear image background with given color"""
	...

def image_draw_pixel(dst: POINTER(Image), posX: int, posY: int, color: Color) -> None:
	"""Draw pixel within an image"""
	...

def image_draw_pixel_v(dst: POINTER(Image), position: Vector2, color: Color) -> None:
	"""Draw pixel within an image (Vector version)"""
	...

def image_draw_line(dst: POINTER(Image), startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
	"""Draw line within an image"""
	...

def image_draw_line_v(dst: POINTER(Image), start: Vector2, end: Vector2, color: Color) -> None:
	"""Draw line within an image (Vector version)"""
	...

def image_draw_circle(dst: POINTER(Image), centerX: int, centerY: int, radius: int, color: Color) -> None:
	"""Draw circle within an image"""
	...

def image_draw_circle_v(dst: POINTER(Image), center: Vector2, radius: int, color: Color) -> None:
	"""Draw circle within an image (Vector version)"""
	...

def image_draw_rectangle(dst: POINTER(Image), posX: int, posY: int, width: int, height: int, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_v(dst: POINTER(Image), position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw rectangle within an image (Vector version)"""
	...

def image_draw_rectangle_rec(dst: POINTER(Image), rec: Rectangle, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_lines(dst: POINTER(Image), rec: Rectangle, thick: int, color: Color) -> None:
	"""Draw rectangle lines within an image"""
	...

def image_draw(dst: POINTER(Image), src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None:
	"""Draw a source image within a destination image (tint applied to source)"""
	...

def image_draw_text(dst: POINTER(Image), text: bytes, posX: int, posY: int, fontSize: int, color: Color) -> None:
	"""Draw text (using default font) within an image (destination)"""
	...

def image_draw_text_ex(dst: POINTER(Image), font: Font, text: bytes, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	"""Draw text (custom sprite font) within an image (destination)"""
	...

def load_texture(fileName: bytes) -> Texture2D:
	"""Load texture from file into GPU memory (VRAM)"""
	...

def load_texture_from_image(image: Image) -> Texture2D:
	"""Load texture from image data"""
	...

def load_texture_cubemap(image: Image, layout: int) -> TextureCubemap:
	"""Load cubemap from image, multiple image cubemap layouts supported"""
	...

def load_render_texture(width: int, height: int) -> RenderTexture2D:
	"""Load texture for rendering (framebuffer)"""
	...

def unload_texture(texture: Texture2D) -> None:
	"""Unload texture from GPU memory (VRAM)"""
	...

def unload_render_texture(target: RenderTexture2D) -> None:
	"""Unload render texture from GPU memory (VRAM)"""
	...

def update_texture(texture: Texture2D, pixels: int) -> None:
	"""Update GPU texture with new data"""
	...

def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: int) -> None:
	"""Update GPU texture rectangle with new data"""
	...

def gen_texture_mipmaps(texture: POINTER(Texture2D)) -> None:
	"""Generate GPU mipmaps for a texture"""
	...

def set_texture_filter(texture: Texture2D, filter: int) -> None:
	"""Set texture scaling filter mode"""
	...

def set_texture_wrap(texture: Texture2D, wrap: int) -> None:
	"""Set texture wrapping mode"""
	...

def draw_texture(texture: Texture2D, posX: int, posY: int, tint: Color) -> None:
	"""Draw a Texture2D"""
	...

def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None:
	"""Draw a Texture2D with position defined as Vector2"""
	...

def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None:
	"""Draw a Texture2D with extended parameters"""
	...

def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle"""
	...

def draw_texture_quad(texture: Texture2D, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None:
	"""Draw texture quad with tiling and offset parameters"""
	...

def draw_texture_tiled(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None:
	"""Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
	...

def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle with 'pro' parameters"""
	...

def draw_texture_n_patch(texture: Texture2D, nPatchInfo: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
	"""Draws a texture (or part of it) that stretches or shrinks nicely"""
	...

def draw_texture_poly(texture: Texture2D, center: Vector2, points: POINTER(Vector2), texcoords: POINTER(Vector2), pointCount: int, tint: Color) -> None:
	"""Draw a textured polygon"""
	...

def fade(color: Color, alpha: float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_to_int(color: Color) -> int:
	"""Get hexadecimal value for a Color"""
	...

def color_normalize(color: Color) -> Vector4:
	"""Get Color normalized as float [0..1]"""
	...

def color_from_normalized(normalized: Vector4) -> Color:
	"""Get Color from normalized values [0..1]"""
	...

def color_to_hsv(color: Color) -> Vector3:
	"""Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
	...

def color_from_hsv(hue: float, saturation: float, value: float) -> Color:
	"""Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
	...

def color_alpha(color: Color, alpha: float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color:
	"""Get src alpha-blended into dst color with tint"""
	...

def get_color(hexValue: int) -> Color:
	"""Get Color structure from hexadecimal value"""
	...

def get_pixel_color(srcPtr: int, format: int) -> Color:
	"""Get Color from a source pixel pointer of certain format"""
	...

def set_pixel_color(dstPtr: int, color: Color, format: int) -> None:
	"""Set color formatted into destination pixel pointer"""
	...

def get_pixel_data_size(width: int, height: int, format: int) -> int:
	"""Get pixel data size in bytes for certain format"""
	...

def get_font_default() -> Font:
	"""Get the default Font"""
	...

def load_font(fileName: bytes) -> Font:
	"""Load font from file into GPU memory (VRAM)"""
	...

def load_font_ex(fileName: bytes, fontSize: int, fontChars: POINTER(c_int), glyphCount: int) -> Font:
	"""Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set"""
	...

def load_font_from_image(image: Image, key: Color, firstChar: int) -> Font:
	"""Load font from Image (XNA style)"""
	...

def load_font_from_memory(fileType: bytes, fileData: POINTER(c_ubyte), dataSize: int, fontSize: int, fontChars: POINTER(c_int), glyphCount: int) -> Font:
	"""Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
	...

def load_font_data(fileData: POINTER(c_ubyte), dataSize: int, fontSize: int, fontChars: POINTER(c_int), glyphCount: int, type: int) -> POINTER(GlyphInfo):
	"""Load font data for further use"""
	...

def gen_image_font_atlas(chars: POINTER(GlyphInfo), recs: POINTER(POINTER(Rectangle)), glyphCount: int, fontSize: int, padding: int, packMethod: int) -> Image:
	"""Generate image font atlas using chars info"""
	...

def unload_font_data(chars: POINTER(GlyphInfo), glyphCount: int) -> None:
	"""Unload font chars info data (RAM)"""
	...

def unload_font(font: Font) -> None:
	"""Unload font from GPU memory (VRAM)"""
	...

def export_font_as_code(font: Font, fileName: bytes) -> bool:
	"""Export font as code file, returns true on success"""
	...

def draw_fps(posX: int, posY: int) -> None:
	"""Draw current FPS"""
	...

def draw_text(text: bytes, posX: int, posY: int, fontSize: int, color: Color) -> None:
	"""Draw text (using default font)"""
	...

def draw_text_ex(font: Font, text: bytes, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	"""Draw text using font and additional parameters"""
	...

def draw_text_pro(font: Font, text: bytes, position: Vector2, origin: Vector2, rotation: float, fontSize: float, spacing: float, tint: Color) -> None:
	"""Draw text using Font and pro parameters (rotation)"""
	...

def draw_text_codepoint(font: Font, codepoint: int, position: Vector2, fontSize: float, tint: Color) -> None:
	"""Draw one character (codepoint)"""
	...

def draw_text_codepoints(font: Font, codepoints: POINTER(c_int), count: int, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	"""Draw multiple character (codepoint)"""
	...

def measure_text(text: bytes, fontSize: int) -> int:
	"""Measure string width for default font"""
	...

def measure_text_ex(font: Font, text: bytes, fontSize: float, spacing: float) -> Vector2:
	"""Measure string size for Font"""
	...

def get_glyph_index(font: Font, codepoint: int) -> int:
	"""Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_info(font: Font, codepoint: int) -> GlyphInfo:
	"""Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_atlas_rec(font: Font, codepoint: int) -> Rectangle:
	"""Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
	...

def load_codepoints(text: bytes, count: POINTER(c_int)) -> POINTER(c_int):
	"""Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
	...

def unload_codepoints(codepoints: POINTER(c_int)) -> None:
	"""Unload codepoints data from memory"""
	...

def get_codepoint_count(text: bytes) -> int:
	"""Get total number of codepoints in a UTF-8 encoded string"""
	...

def get_codepoint(text: bytes, bytesProcessed: POINTER(c_int)) -> int:
	"""Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def codepoint_to_utf8(codepoint: int, byteSize: POINTER(c_int)) -> bytes:
	"""Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
	...

def text_codepoints_to_utf8(codepoints: POINTER(c_int), length: int) -> bytes:
	"""Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)"""
	...

def text_copy(dst: bytes, src: bytes) -> int:
	"""Copy one string to another, returns bytes copied"""
	...

def text_is_equal(text1: bytes, text2: bytes) -> bool:
	"""Check if two text string are equal"""
	...

def text_length(text: bytes) -> int:
	"""Get text length, checks for '\0' ending"""
	...

def text_format(text: bytes, args: ...) -> bytes:
	"""Text formatting with variables (sprintf() style)"""
	...

def text_subtext(text: bytes, position: int, length: int) -> bytes:
	"""Get a piece of a text string"""
	...

def text_replace(text: bytes, replace: bytes, by: bytes) -> bytes:
	"""Replace text string (WARNING: memory must be freed!)"""
	...

def text_insert(text: bytes, insert: bytes, position: int) -> bytes:
	"""Insert text in a position (WARNING: memory must be freed!)"""
	...

def text_join(textList: POINTER(POINTER(c_char)), count: int, delimiter: bytes) -> bytes:
	"""Join text strings with delimiter"""
	...

def text_split(text: bytes, delimiter: bytes, count: POINTER(c_int)) -> POINTER(POINTER(c_char)):
	"""Split text into multiple strings"""
	...

def text_append(text: bytes, append: bytes, position: POINTER(c_int)) -> None:
	"""Append text at specific position and move cursor!"""
	...

def text_find_index(text: bytes, find: bytes) -> int:
	"""Find first text occurrence within a string"""
	...

def text_to_upper(text: bytes) -> bytes:
	"""Get upper case version of provided string"""
	...

def text_to_lower(text: bytes) -> bytes:
	"""Get lower case version of provided string"""
	...

def text_to_pascal(text: bytes) -> bytes:
	"""Get Pascal case notation version of provided string"""
	...

def text_to_integer(text: bytes) -> int:
	"""Get integer value from text (negative values not supported)"""
	...

def draw_line_3d(startPos: Vector3, endPos: Vector3, color: Color) -> None:
	"""Draw a line in 3D world space"""
	...

def draw_point_3d(position: Vector3, color: Color) -> None:
	"""Draw a point in 3D space, actually a small line"""
	...

def draw_circle_3d(center: Vector3, radius: float, rotationAxis: Vector3, rotationAngle: float, color: Color) -> None:
	"""Draw a circle in 3D world space"""
	...

def draw_triangle_3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_strip_3d(points: POINTER(Vector3), pointCount: int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_cube(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	"""Draw cube"""
	...

def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube (Vector version)"""
	...

def draw_cube_wires(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	"""Draw cube wires"""
	...

def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube wires (Vector version)"""
	...

def draw_cube_texture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	"""Draw cube textured"""
	...

def draw_cube_texture_rec(texture: Texture2D, source: Rectangle, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	"""Draw cube with a region of a texture"""
	...

def draw_sphere(centerPos: Vector3, radius: float, color: Color) -> None:
	"""Draw sphere"""
	...

def draw_sphere_ex(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
	"""Draw sphere with extended parameters"""
	...

def draw_sphere_wires(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
	"""Draw sphere wires"""
	...

def draw_cylinder(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
	"""Draw a cylinder/cone"""
	...

def draw_cylinder_ex(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
	"""Draw a cylinder with base at startPos and top at endPos"""
	...

def draw_cylinder_wires(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
	"""Draw a cylinder/cone wires"""
	...

def draw_cylinder_wires_ex(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
	"""Draw a cylinder wires with base at startPos and top at endPos"""
	...

def draw_plane(centerPos: Vector3, size: Vector2, color: Color) -> None:
	"""Draw a plane XZ"""
	...

def draw_ray(ray: Ray, color: Color) -> None:
	"""Draw a ray line"""
	...

def draw_grid(slices: int, spacing: float) -> None:
	"""Draw a grid (centered at (0, 0, 0))"""
	...

def load_model(fileName: bytes) -> Model:
	"""Load model from files (meshes and materials)"""
	...

def load_model_from_mesh(mesh: Mesh) -> Model:
	"""Load model from generated mesh (default material)"""
	...

def unload_model(model: Model) -> None:
	"""Unload model (including meshes) from memory (RAM and/or VRAM)"""
	...

def unload_model_keep_meshes(model: Model) -> None:
	"""Unload model (but not meshes) from memory (RAM and/or VRAM)"""
	...

def get_model_bounding_box(model: Model) -> BoundingBox:
	"""Compute model bounding box limits (considers all meshes)"""
	...

def draw_model(model: Model, position: Vector3, scale: float, tint: Color) -> None:
	"""Draw a model (with texture if set)"""
	...

def draw_model_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
	"""Draw a model with extended parameters"""
	...

def draw_model_wires(model: Model, position: Vector3, scale: float, tint: Color) -> None:
	"""Draw a model wires (with texture if set)"""
	...

def draw_model_wires_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
	"""Draw a model wires (with texture if set) with extended parameters"""
	...

def draw_bounding_box(box: BoundingBox, color: Color) -> None:
	"""Draw bounding box (wires)"""
	...

def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, size: float, tint: Color) -> None:
	"""Draw a billboard texture"""
	...

def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None:
	"""Draw a billboard texture defined by source"""
	...

def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: float, tint: Color) -> None:
	"""Draw a billboard texture defined by source and rotation"""
	...

def upload_mesh(mesh: POINTER(Mesh), dynamic: bool) -> None:
	"""Upload mesh vertex data in GPU and provide VAO/VBO ids"""
	...

def update_mesh_buffer(mesh: Mesh, index: int, data: int, dataSize: int, offset: int) -> None:
	"""Update mesh vertex data in GPU for a specific buffer index"""
	...

def unload_mesh(mesh: Mesh) -> None:
	"""Unload mesh data from CPU and GPU"""
	...

def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
	"""Draw a 3d mesh with material and transform"""
	...

def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: POINTER(Matrix), instances: int) -> None:
	"""Draw multiple mesh instances with material and different transforms"""
	...

def export_mesh(mesh: Mesh, fileName: bytes) -> bool:
	"""Export mesh data to file, returns true on success"""
	...

def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox:
	"""Compute mesh bounding box limits"""
	...

def gen_mesh_tangents(mesh: POINTER(Mesh)) -> None:
	"""Compute mesh tangents"""
	...

def gen_mesh_poly(sides: int, radius: float) -> Mesh:
	"""Generate polygonal mesh"""
	...

def gen_mesh_plane(width: float, length: float, resX: int, resZ: int) -> Mesh:
	"""Generate plane mesh (with subdivisions)"""
	...

def gen_mesh_cube(width: float, height: float, length: float) -> Mesh:
	"""Generate cuboid mesh"""
	...

def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh:
	"""Generate sphere mesh (standard sphere)"""
	...

def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh:
	"""Generate half-sphere mesh (no bottom cap)"""
	...

def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh:
	"""Generate cylinder mesh"""
	...

def gen_mesh_cone(radius: float, height: float, slices: int) -> Mesh:
	"""Generate cone/pyramid mesh"""
	...

def gen_mesh_torus(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
	"""Generate torus mesh"""
	...

def gen_mesh_knot(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
	"""Generate trefoil knot mesh"""
	...

def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh:
	"""Generate heightmap mesh from image data"""
	...

def gen_mesh_cubicmap(cubicmap: Image, cubeSize: Vector3) -> Mesh:
	"""Generate cubes-based map mesh from image data"""
	...

def load_materials(fileName: bytes, materialCount: POINTER(c_int)) -> POINTER(Material):
	"""Load materials from model file"""
	...

def load_material_default() -> Material:
	"""Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
	...

def unload_material(material: Material) -> None:
	"""Unload material from GPU memory (VRAM)"""
	...

def set_material_texture(material: POINTER(Material), mapType: int, texture: Texture2D) -> None:
	"""Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
	...

def set_model_mesh_material(model: POINTER(Model), meshId: int, materialId: int) -> None:
	"""Set material for a mesh"""
	...

def load_model_animations(fileName: bytes, animCount: POINTER(c_uint)) -> POINTER(ModelAnimation):
	"""Load model animations from file"""
	...

def update_model_animation(model: Model, anim: ModelAnimation, frame: int) -> None:
	"""Update model animation pose"""
	...

def unload_model_animation(anim: ModelAnimation) -> None:
	"""Unload animation data"""
	...

def unload_model_animations(animations: POINTER(ModelAnimation), count: int) -> None:
	"""Unload animation array data"""
	...

def is_model_animation_valid(model: Model, anim: ModelAnimation) -> bool:
	"""Check model animation skeleton match"""
	...

def check_collision_spheres(center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool:
	"""Check collision between two spheres"""
	...

def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool:
	"""Check collision between two bounding boxes"""
	...

def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: float) -> bool:
	"""Check collision between box and sphere"""
	...

def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: float) -> RayCollision:
	"""Get collision info between ray and sphere"""
	...

def get_ray_collision_box(ray: Ray, box: BoundingBox) -> RayCollision:
	"""Get collision info between ray and box"""
	...

def get_ray_collision_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision:
	"""Get collision info between ray and mesh"""
	...

def get_ray_collision_triangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayCollision:
	"""Get collision info between ray and triangle"""
	...

def get_ray_collision_quad(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3, p4: Vector3) -> RayCollision:
	"""Get collision info between ray and quad"""
	...

def init_audio_device() -> None:
	"""Initialize audio device and context"""
	...

def close_audio_device() -> None:
	"""Close the audio device and context"""
	...

def is_audio_device_ready() -> bool:
	"""Check if audio device has been initialized successfully"""
	...

def set_master_volume(volume: float) -> None:
	"""Set master volume (listener)"""
	...

def stop_sound_multi() -> None:
	"""Stop any sound playing (using multichannel buffer pool)"""
	...

def get_sounds_playing() -> int:
	"""Get number of sounds playing in the multichannel"""
	...

def unload_wave_samples(samples: POINTER(c_float)) -> None:
	"""Unload samples data loaded with LoadWaveSamples()"""
	...

def set_audio_stream_buffer_size_default(size: int) -> None:
	"""Default size for new audio streams"""
	...

def clamp(value: float, min: float, max: float) -> float:
	""""""
	...

def lerp(start: float, end: float, amount: float) -> float:
	""""""
	...

def normalize(value: float, start: float, end: float) -> float:
	""""""
	...

def remap(value: float, inputStart: float, inputEnd: float, outputStart: float, outputEnd: float) -> float:
	""""""
	...

def wrap(value: float, min: float, max: float) -> float:
	""""""
	...

def float_equals(x: float, y: float) -> int:
	""""""
	...

def vector2_zero() -> Vector2:
	""""""
	...

def vector2_one() -> Vector2:
	""""""
	...

def vector2_add(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_add_value(v: Vector2, add: float) -> Vector2:
	""""""
	...

def vector2_subtract(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_subtract_value(v: Vector2, sub: float) -> Vector2:
	""""""
	...

def vector2_length(v: Vector2) -> float:
	""""""
	...

def vector2_length_sqr(v: Vector2) -> float:
	""""""
	...

def vector_2dot_product(v1: Vector2, v2: Vector2) -> float:
	""""""
	...

def vector_2distance(v1: Vector2, v2: Vector2) -> float:
	""""""
	...

def vector_2distance_sqr(v1: Vector2, v2: Vector2) -> float:
	""""""
	...

def vector2_angle(v1: Vector2, v2: Vector2) -> float:
	""""""
	...

def vector2_scale(v: Vector2, scale: float) -> Vector2:
	""""""
	...

def vector2_multiply(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_negate(v: Vector2) -> Vector2:
	""""""
	...

def vector_2divide(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_normalize(v: Vector2) -> Vector2:
	""""""
	...

def vector2_transform(v: Vector2, mat: Matrix) -> Vector2:
	""""""
	...

def vector2_lerp(v1: Vector2, v2: Vector2, amount: float) -> Vector2:
	""""""
	...

def vector2_reflect(v: Vector2, normal: Vector2) -> Vector2:
	""""""
	...

def vector2_rotate(v: Vector2, angle: float) -> Vector2:
	""""""
	...

def vector2_move_towards(v: Vector2, target: Vector2, maxDistance: float) -> Vector2:
	""""""
	...

def vector2_invert(v: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp(v: Vector2, min: Vector2, max: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp_value(v: Vector2, min: float, max: float) -> Vector2:
	""""""
	...

def vector2_equals(p: Vector2, q: Vector2) -> int:
	""""""
	...

def vector3_zero() -> Vector3:
	""""""
	...

def vector3_one() -> Vector3:
	""""""
	...

def vector3_add(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_add_value(v: Vector3, add: float) -> Vector3:
	""""""
	...

def vector3_subtract(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_subtract_value(v: Vector3, sub: float) -> Vector3:
	""""""
	...

def vector3_scale(v: Vector3, scalar: float) -> Vector3:
	""""""
	...

def vector3_multiply(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_cross_product(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_perpendicular(v: Vector3) -> Vector3:
	""""""
	...

def vector3_length(v: Vector3) -> float:
	""""""
	...

def vector3_length_sqr(v: Vector3) -> float:
	""""""
	...

def vector_3dot_product(v1: Vector3, v2: Vector3) -> float:
	""""""
	...

def vector_3distance(v1: Vector3, v2: Vector3) -> float:
	""""""
	...

def vector_3distance_sqr(v1: Vector3, v2: Vector3) -> float:
	""""""
	...

def vector3_angle(v1: Vector3, v2: Vector3) -> float:
	""""""
	...

def vector3_negate(v: Vector3) -> Vector3:
	""""""
	...

def vector_3divide(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_normalize(v: Vector3) -> Vector3:
	""""""
	...

def vector3_ortho_normalize(v1: POINTER(Vector3), v2: POINTER(Vector3)) -> None:
	""""""
	...

def vector3_transform(v: Vector3, mat: Matrix) -> Vector3:
	""""""
	...

def vector3_rotate_by_quaternion(v: Vector3, q: Quaternion) -> Vector3:
	""""""
	...

def vector3_rotate_by_axis_angle(v: Vector3, axis: Vector3, angle: float) -> Vector3:
	""""""
	...

def vector3_lerp(v1: Vector3, v2: Vector3, amount: float) -> Vector3:
	""""""
	...

def vector3_reflect(v: Vector3, normal: Vector3) -> Vector3:
	""""""
	...

def vector3_min(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_max(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_barycenter(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> Vector3:
	""""""
	...

def vector3_unproject(source: Vector3, projection: Matrix, view: Matrix) -> Vector3:
	""""""
	...

def vector3_to_float_v(v: Vector3) -> float3:
	""""""
	...

def vector3_invert(v: Vector3) -> Vector3:
	""""""
	...

def vector3_clamp(v: Vector3, min: Vector3, max: Vector3) -> Vector3:
	""""""
	...

def vector3_clamp_value(v: Vector3, min: float, max: float) -> Vector3:
	""""""
	...

def vector3_equals(p: Vector3, q: Vector3) -> int:
	""""""
	...

def vector3_refract(v: Vector3, n: Vector3, r: float) -> Vector3:
	""""""
	...

def matrix_determinant(mat: Matrix) -> float:
	""""""
	...

def matrix_trace(mat: Matrix) -> float:
	""""""
	...

def matrix_transpose(mat: Matrix) -> Matrix:
	""""""
	...

def matrix_invert(mat: Matrix) -> Matrix:
	""""""
	...

def matrix_identity() -> Matrix:
	""""""
	...

def matrix_add(left: Matrix, right: Matrix) -> Matrix:
	""""""
	...

def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
	""""""
	...

def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
	""""""
	...

def matrix_translate(x: float, y: float, z: float) -> Matrix:
	""""""
	...

def matrix_rotate(axis: Vector3, angle: float) -> Matrix:
	""""""
	...

def matrix_rotate_x(angle: float) -> Matrix:
	""""""
	...

def matrix_rotate_y(angle: float) -> Matrix:
	""""""
	...

def matrix_rotate_z(angle: float) -> Matrix:
	""""""
	...

def matrix_rotate_xyz(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_rotate_zyx(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_scale(x: float, y: float, z: float) -> Matrix:
	""""""
	...

def matrix_frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix:
	""""""
	...

def matrix_perspective(fovy: float, aspect: float, near: float, far: float) -> Matrix:
	""""""
	...

def matrix_ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix:
	""""""
	...

def matrix_look_at(eye: Vector3, target: Vector3, up: Vector3) -> Matrix:
	""""""
	...

def matrix_to_float_v(mat: Matrix) -> float16:
	""""""
	...

def quaternion_add(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_add_value(q: Quaternion, add: float) -> Quaternion:
	""""""
	...

def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_subtract_value(q: Quaternion, sub: float) -> Quaternion:
	""""""
	...

def quaternion_identity() -> Quaternion:
	""""""
	...

def quaternion_length(q: Quaternion) -> float:
	""""""
	...

def quaternion_normalize(q: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_invert(q: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_multiply(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_scale(q: Quaternion, mul: float) -> Quaternion:
	""""""
	...

def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_lerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
	""""""
	...

def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
	""""""
	...

def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
	""""""
	...

def quaternion_from_vector3_to_vector3(_from: Vector3, to: Vector3) -> Quaternion:
	""""""
	...

def quaternion_from_matrix(mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_to_matrix(q: Quaternion) -> Matrix:
	""""""
	...

def quaternion_from_axis_angle(axis: Vector3, angle: float) -> Quaternion:
	""""""
	...

def quaternion_to_axis_angle(q: Quaternion, outAxis: POINTER(Vector3), outAngle: POINTER(c_float)) -> None:
	""""""
	...

def quaternion_from_euler(pitch: float, yaw: float, roll: float) -> Quaternion:
	""""""
	...

def quaternion_to_euler(q: Quaternion) -> Vector3:
	""""""
	...

def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_equals(p: Quaternion, q: Quaternion) -> int:
	""""""
	...

def gui_enable() -> None:
	"""Enable gui controls (global state)"""
	...

def gui_disable() -> None:
	"""Disable gui controls (global state)"""
	...

def gui_lock() -> None:
	"""Lock gui controls (global state)"""
	...

def gui_unlock() -> None:
	"""Unlock gui controls (global state)"""
	...

def gui_is_locked() -> bool:
	"""Check if gui is locked (global state)"""
	...

def gui_fade(alpha: float) -> None:
	"""Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f"""
	...

def gui_set_state(state: int) -> None:
	"""Set gui state (global state)"""
	...

def gui_get_state() -> int:
	"""Get gui state (global state)"""
	...

def gui_set_font(font: Font) -> None:
	"""Set gui custom font (global state)"""
	...

def gui_get_font() -> Font:
	"""Get gui custom font (global state)"""
	...

def gui_set_style(control: int, property: int, value: int) -> None:
	"""Set one style property"""
	...

def gui_get_style(control: int, property: int) -> int:
	"""Get one style property"""
	...

def gui_window_box(bounds: Rectangle, title: bytes) -> bool:
	"""Window Box control, shows a window that can be closed"""
	...

def gui_group_box(bounds: Rectangle, text: bytes) -> None:
	"""Group Box control with text name"""
	...

def gui_line(bounds: Rectangle, text: bytes) -> None:
	"""Line separator control, could contain text"""
	...

def gui_panel(bounds: Rectangle, text: bytes) -> None:
	"""Panel control, useful to group controls"""
	...

def gui_scroll_panel(bounds: Rectangle, text: bytes, content: Rectangle, scroll: POINTER(Vector2)) -> Rectangle:
	"""Scroll Panel control"""
	...

def gui_label(bounds: Rectangle, text: bytes) -> None:
	"""Label control, shows text"""
	...

def gui_button(bounds: Rectangle, text: bytes) -> bool:
	"""Button control, returns true when clicked"""
	...

def gui_label_button(bounds: Rectangle, text: bytes) -> bool:
	"""Label button control, show true when clicked"""
	...

def gui_toggle(bounds: Rectangle, text: bytes, active: bool) -> bool:
	"""Toggle Button control, returns true when active"""
	...

def gui_toggle_group(bounds: Rectangle, text: bytes, active: int) -> int:
	"""Toggle Group control, returns active toggle index"""
	...

def gui_check_box(bounds: Rectangle, text: bytes, checked: bool) -> bool:
	"""Check Box control, returns true when active"""
	...

def gui_combo_box(bounds: Rectangle, text: bytes, active: int) -> int:
	"""Combo Box control, returns selected item index"""
	...

def gui_dropdown_box(bounds: Rectangle, text: bytes, active: POINTER(c_int), editMode: bool) -> bool:
	"""Dropdown Box control, returns selected item"""
	...

def gui_spinner(bounds: Rectangle, text: bytes, value: POINTER(c_int), minValue: int, maxValue: int, editMode: bool) -> bool:
	"""Spinner control, returns selected value"""
	...

def gui_value_box(bounds: Rectangle, text: bytes, value: POINTER(c_int), minValue: int, maxValue: int, editMode: bool) -> bool:
	"""Value Box control, updates input text with numbers"""
	...

def gui_text_box(bounds: Rectangle, text: bytes, textSize: int, editMode: bool) -> bool:
	"""Text Box control, updates input text"""
	...

def gui_text_box_multi(bounds: Rectangle, text: bytes, textSize: int, editMode: bool) -> bool:
	"""Text Box control with multiple lines"""
	...

def gui_slider(bounds: Rectangle, textLeft: bytes, textRight: bytes, value: float, minValue: float, maxValue: float) -> float:
	"""Slider control, returns selected value"""
	...

def gui_slider_bar(bounds: Rectangle, textLeft: bytes, textRight: bytes, value: float, minValue: float, maxValue: float) -> float:
	"""Slider Bar control, returns selected value"""
	...

def gui_progress_bar(bounds: Rectangle, textLeft: bytes, textRight: bytes, value: float, minValue: float, maxValue: float) -> float:
	"""Progress Bar control, shows current progress value"""
	...

def gui_status_bar(bounds: Rectangle, text: bytes) -> None:
	"""Status Bar control, shows info text"""
	...

def gui_dummy_rec(bounds: Rectangle, text: bytes) -> None:
	"""Dummy control for placeholders"""
	...

def gui_grid(bounds: Rectangle, text: bytes, spacing: float, subdivs: int) -> Vector2:
	"""Grid control, returns mouse cell position"""
	...

def gui_list_view(bounds: Rectangle, text: bytes, scrollIndex: POINTER(c_int), active: int) -> int:
	"""List View control, returns selected list item index"""
	...

def gui_list_view_ex(bounds: Rectangle, text: POINTER(POINTER(c_char)), count: int, focus: POINTER(c_int), scrollIndex: POINTER(c_int), active: int) -> int:
	"""List View with extended parameters"""
	...

def gui_message_box(bounds: Rectangle, title: bytes, message: bytes, buttons: bytes) -> int:
	"""Message Box control, displays a message"""
	...

def gui_text_input_box(bounds: Rectangle, title: bytes, message: bytes, buttons: bytes, text: bytes, textMaxSize: int, secretViewActive: POINTER(c_int)) -> int:
	"""Text Input Box control, ask for text, supports secret"""
	...

def gui_color_picker(bounds: Rectangle, text: bytes, color: Color) -> Color:
	"""Color Picker control (multiple color controls)"""
	...

def gui_color_panel(bounds: Rectangle, text: bytes, color: Color) -> Color:
	"""Color Panel control"""
	...

def gui_color_bar_alpha(bounds: Rectangle, text: bytes, alpha: float) -> float:
	"""Color Bar Alpha control"""
	...

def gui_color_bar_hue(bounds: Rectangle, text: bytes, value: float) -> float:
	"""Color Bar Hue control"""
	...

def gui_load_style(fileName: bytes) -> None:
	"""Load style file over global style variable (.rgs)"""
	...

def gui_load_style_default() -> None:
	"""Load style default over global style"""
	...

def gui_icon_text(iconId: int, text: bytes) -> bytes:
	"""Get text with icon id prepended (if supported)"""
	...

def gui_draw_icon(iconId: int, posX: int, posY: int, pixelSize: int, color: Color) -> None:
	""""""
	...

def gui_get_icons() -> POINTER(c_uint):
	"""Get full icons data pointer"""
	...

def gui_get_icon_data(iconId: int) -> POINTER(c_uint):
	"""Get icon bit data"""
	...

def gui_set_icon_data(iconId: int, data: POINTER(c_uint)) -> None:
	"""Set icon bit data"""
	...

def gui_set_icon_scale(scale: int) -> None:
	"""Set icon scale (1 by default)"""
	...

def gui_set_icon_pixel(iconId: int, x: int, y: int) -> None:
	"""Set icon pixel value"""
	...

def gui_clear_icon_pixel(iconId: int, x: int, y: int) -> None:
	"""Clear icon pixel value"""
	...

def gui_check_icon_pixel(iconId: int, x: int, y: int) -> bool:
	"""Check icon pixel value"""
	...

