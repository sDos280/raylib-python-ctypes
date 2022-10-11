from colors import *
from enums import *
from structures import *


# Initialize window and OpenGL context
def init_window(width: int, height: int, title: bytes) -> None:
	pass

# Check if KEY_ESCAPE pressed or Close icon pressed
def window_should_close() -> bool:
	pass

# Close window and unload OpenGL context
def close_window() -> None:
	pass

# Check if window has been initialized successfully
def is_window_ready() -> bool:
	pass

# Check if window is currently fullscreen
def is_window_fullscreen() -> bool:
	pass

# Check if window is currently hidden (only PLATFORM_DESKTOP)
def is_window_hidden() -> bool:
	pass

# Check if window is currently minimized (only PLATFORM_DESKTOP)
def is_window_minimized() -> bool:
	pass

# Check if window is currently maximized (only PLATFORM_DESKTOP)
def is_window_maximized() -> bool:
	pass

# Check if window is currently focused (only PLATFORM_DESKTOP)
def is_window_focused() -> bool:
	pass

# Check if window has been resized last frame
def is_window_resized() -> bool:
	pass

# Check if one specific window flag is enabled
def is_window_state(flag: int) -> bool:
	pass

# Set window configuration state using flags (only PLATFORM_DESKTOP)
def set_window_state(flags: int) -> None:
	pass

# Clear window configuration state flags
def clear_window_state(flags: int) -> None:
	pass

# Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)
def toggle_fullscreen() -> None:
	pass

# Set window state: maximized, if resizable (only PLATFORM_DESKTOP)
def maximize_window() -> None:
	pass

# Set window state: minimized, if resizable (only PLATFORM_DESKTOP)
def minimize_window() -> None:
	pass

# Set window state: not minimized/maximized (only PLATFORM_DESKTOP)
def restore_window() -> None:
	pass

# Set icon for window (only PLATFORM_DESKTOP)
def set_window_icon(image: Image) -> None:
	pass

# Set title for window (only PLATFORM_DESKTOP)
def set_window_title(title: bytes) -> None:
	pass

# Set window position on screen (only PLATFORM_DESKTOP)
def set_window_position(x: int, y: int) -> None:
	pass

# Set monitor for the current window (fullscreen mode)
def set_window_monitor(monitor: int) -> None:
	pass

# Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)
def set_window_min_size(width: int, height: int) -> None:
	pass

# Set window dimensions
def set_window_size(width: int, height: int) -> None:
	pass

# Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)
def set_window_opacity(opacity: float) -> None:
	pass

# Get native window handle
def get_window_handle() -> int:
	pass

# Get current screen width
def get_screen_width() -> int:
	pass

# Get current screen height
def get_screen_height() -> int:
	pass

# Get current render width (it considers HiDPI)
def get_render_width() -> int:
	pass

# Get current render height (it considers HiDPI)
def get_render_height() -> int:
	pass

# Get number of connected monitors
def get_monitor_count() -> int:
	pass

# Get current connected monitor
def get_current_monitor() -> int:
	pass

# Get specified monitor position
def get_monitor_position(monitor: int) -> Vector2:
	pass

# Get specified monitor width (current video mode used by monitor)
def get_monitor_width(monitor: int) -> int:
	pass

# Get specified monitor height (current video mode used by monitor)
def get_monitor_height(monitor: int) -> int:
	pass

# Get specified monitor physical width in millimetres
def get_monitor_physical_width(monitor: int) -> int:
	pass

# Get specified monitor physical height in millimetres
def get_monitor_physical_height(monitor: int) -> int:
	pass

# Get specified monitor refresh rate
def get_monitor_refresh_rate(monitor: int) -> int:
	pass

# Get window position XY on monitor
def get_window_position() -> Vector2:
	pass

# Get window scale DPI factor
def get_window_scale_dpi() -> Vector2:
	pass

# Get the human-readable, UTF-8 encoded name of the primary monitor
def get_monitor_name(monitor: int) -> bytes:
	pass

# Set clipboard text content
def set_clipboard_text(text: bytes) -> None:
	pass

# Get clipboard text content
def get_clipboard_text() -> bytes:
	pass

# Enable waiting for events on EndDrawing(), no automatic event polling
def enable_event_waiting() -> None:
	pass

# Disable waiting for events on EndDrawing(), automatic events polling
def disable_event_waiting() -> None:
	pass

# Swap back buffer with front buffer (screen drawing)
def swap_screen_buffer() -> None:
	pass

# Register all input events
def poll_input_events() -> None:
	pass

# Wait for some time (halt program execution)
def wait_time(seconds: float) -> None:
	pass

# Shows cursor
def show_cursor() -> None:
	pass

# Hides cursor
def hide_cursor() -> None:
	pass

# Check if cursor is not visible
def is_cursor_hidden() -> bool:
	pass

# Enables cursor (unlock cursor)
def enable_cursor() -> None:
	pass

# Disables cursor (lock cursor)
def disable_cursor() -> None:
	pass

# Check if cursor is on the screen
def is_cursor_on_screen() -> bool:
	pass

# Set background color (framebuffer clear color)
def clear_background(color: Color) -> None:
	pass

# Setup canvas (framebuffer) to start drawing
def begin_drawing() -> None:
	pass

# End canvas drawing and swap buffers (double buffering)
def end_drawing() -> None:
	pass

# Begin 2D mode with custom camera (2D)
def begin_mode_2d(camera: Camera2D) -> None:
	pass

# Ends 2D mode with custom camera
def end_mode_2d() -> None:
	pass

# Begin 3D mode with custom camera (3D)
def begin_mode_3d(camera: Camera3D) -> None:
	pass

# Ends 3D mode and returns to default 2D orthographic mode
def end_mode_3d() -> None:
	pass

# Begin drawing to render texture
def begin_texture_mode(target: RenderTexture2D) -> None:
	pass

# Ends drawing to render texture
def end_texture_mode() -> None:
	pass

# Begin custom shader drawing
def begin_shader_mode(shader: Shader) -> None:
	pass

# End custom shader drawing (use default shader)
def end_shader_mode() -> None:
	pass

# Begin blending mode (alpha, additive, multiplied, subtract, custom)
def begin_blend_mode(mode: int) -> None:
	pass

# End blending mode (reset to default: alpha blending)
def end_blend_mode() -> None:
	pass

# Begin scissor mode (define screen area for following drawing)
def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None:
	pass

# End scissor mode
def end_scissor_mode() -> None:
	pass

# Begin stereo rendering (requires VR simulator)
def begin_vr_stereo_mode(config: VrStereoConfig) -> None:
	pass

# End stereo rendering (requires VR simulator)
def end_vr_stereo_mode() -> None:
	pass

# Load VR stereo config for VR simulator device parameters
def load_vr_stereo_config(device: VrDeviceInfo) -> VrStereoConfig:
	pass

# Unload VR stereo config
def unload_vr_stereo_config(config: VrStereoConfig) -> None:
	pass

# Load shader from files and bind default locations
def load_shader(vsFileName: bytes, fsFileName: bytes) -> Shader:
	pass

# Load shader from code strings and bind default locations
def load_shader_from_memory(vsCode: bytes, fsCode: bytes) -> Shader:
	pass

# Get shader uniform location
def get_shader_location(shader: Shader, uniformName: bytes) -> int:
	pass

# Get shader attribute location
def get_shader_location_attrib(shader: Shader, attribName: bytes) -> int:
	pass

# Set shader uniform value
def set_shader_value(shader: Shader, locIndex: int, value: int, uniformType: int) -> None:
	pass

# Set shader uniform value vector
def set_shader_value_v(shader: Shader, locIndex: int, value: int, uniformType: int, count: int) -> None:
	pass

# Set shader uniform value (matrix 4x4)
def set_shader_value_matrix(shader: Shader, locIndex: int, mat: Matrix) -> None:
	pass

# Set shader uniform value for texture (sampler2d)
def set_shader_value_texture(shader: Shader, locIndex: int, texture: Texture2D) -> None:
	pass

# Unload shader from GPU memory (VRAM)
def unload_shader(shader: Shader) -> None:
	pass

# Get a ray trace from mouse position
def get_mouse_ray(mousePosition: Vector2, camera: Camera) -> Ray:
	pass

# Get camera transform matrix (view matrix)
def get_camera_matrix(camera: Camera) -> Matrix:
	pass

# Get camera 2d transform matrix
def get_camera_matrix_2d(camera: Camera2D) -> Matrix:
	pass

# Get the screen space position for a 3d world space position
def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2:
	pass

# Get the world space position for a 2d camera screen space position
def get_screen_to_world_2d(position: Vector2, camera: Camera2D) -> Vector2:
	pass

# Get size position for a 3d world space position
def get_world_to_screen_ex(position: Vector3, camera: Camera, width: int, height: int) -> Vector2:
	pass

# Get the screen space position for a 2d camera world space position
def get_world_to_screen_2d(position: Vector2, camera: Camera2D) -> Vector2:
	pass

# Set target FPS (maximum)
def set_target_fps(fps: int) -> None:
	pass

# Get current FPS
def get_fps() -> int:
	pass

# Get time in seconds for last frame drawn (delta time)
def get_frame_time() -> float:
	pass

# Get elapsed time in seconds since InitWindow()
def get_time() -> float:
	pass

# Get a random value between min and max (both included)
def get_random_value(min: int, max: int) -> int:
	pass

# Set the seed for the random number generator
def set_random_seed(seed: int) -> None:
	pass

# Takes a screenshot of current screen (filename extension defines format)
def take_screenshot(fileName: bytes) -> None:
	pass

# Setup init configuration flags (view FLAGS)
def set_config_flags(flags: int) -> None:
	pass

# Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)
def trace_log(logLevel: int, text: bytes, args: ...) -> None:
	pass

# Set the current threshold (minimum) log level
def set_trace_log_level(logLevel: int) -> None:
	pass

# Internal memory allocator
def mem_alloc(size: int) -> int:
	pass

# Internal memory reallocator
def mem_realloc(ptr: int, size: int) -> int:
	pass

# Internal memory free
def mem_free(ptr: int) -> None:
	pass

# Open URL with default system browser (if available)
def open_url(url: bytes) -> None:
	pass

# Load file data as byte array (read)
def load_file_data(fileName: bytes, bytesRead: POINTER(c_uint)) -> POINTER(c_ubyte):  # Load file data as byte array (read)
	pass

# Unload file data allocated by LoadFileData()
def unload_file_data(data: POINTER(c_ubyte)) -> None:
	pass

# Save data to file from byte array (write), returns true on success
def save_file_data(fileName: bytes, data: int, bytesToWrite: int) -> bool:
	pass

# Export data to code (.h), returns true on success
def export_data_as_code(data: bytes, size: int, fileName: bytes) -> bool:
	pass

# Load text data from file (read), returns a '\0' terminated string
def load_file_text(fileName: bytes) -> bytes:
	pass

# Unload file text data allocated by LoadFileText()
def unload_file_text(text: bytes) -> None:
	pass

# Save text data to file (write), string must be '\0' terminated, returns true on success
def save_file_text(fileName: bytes, text: bytes) -> bool:
	pass

# Check if file exists
def file_exists(fileName: bytes) -> bool:
	pass

# Check if a directory path exists
def directory_exists(dirPath: bytes) -> bool:
	pass

# Check file extension (including point: .png, .wav)
def is_file_extension(fileName: bytes, ext: bytes) -> bool:
	pass

# Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)
def get_file_length(fileName: bytes) -> int:
	pass

# Get pointer to extension for a filename string (includes dot: '.png')
def get_file_extension(fileName: bytes) -> bytes:
	pass

# Get pointer to filename for a path string
def get_file_name(filePath: bytes) -> bytes:
	pass

# Get filename string without extension (uses static string)
def get_file_name_without_ext(filePath: bytes) -> bytes:
	pass

# Get full path for a given fileName with path (uses static string)
def get_directory_path(filePath: bytes) -> bytes:
	pass

# Get previous directory path for a given path (uses static string)
def get_prev_directory_path(dirPath: bytes) -> bytes:
	pass

# Get current working directory (uses static string)
def get_working_directory() -> bytes:
	pass

# Get the directory if the running application (uses static string)
def get_application_directory() -> bytes:
	pass

# Change working directory, return true on success
def change_directory(dir: bytes) -> bool:
	pass

# Check if a given path is a file or a directory
def is_path_file(path: bytes) -> bool:
	pass

# Load directory filepaths
def load_directory_files(dirPath: bytes) -> FilePathList:
	pass

# Load directory filepaths with extension filtering and recursive directory scan
def load_directory_files_ex(basePath: bytes, filter: bytes, scanSubdirs: bool) -> FilePathList:
	pass

# Unload filepaths
def unload_directory_files(files: FilePathList) -> None:
	pass

# Check if a file has been dropped into window
def is_file_dropped() -> bool:
	pass

# Load dropped filepaths
def load_dropped_files() -> FilePathList:
	pass

# Unload dropped filepaths
def unload_dropped_files(files: FilePathList) -> None:
	pass

# Get file modification time (last write time)
def get_file_mod_time(fileName: bytes) -> int:
	pass

# Compress data (DEFLATE algorithm), memory must be MemFree()
def compress_data(data: POINTER(c_ubyte), dataSize: int, compDataSize: POINTER(c_int)) -> POINTER(c_ubyte):  # Compress data (DEFLATE algorithm), memory must be MemFree()
	pass

# Decompress data (DEFLATE algorithm), memory must be MemFree()
def decompress_data(compData: POINTER(c_ubyte), compDataSize: int, dataSize: POINTER(c_int)) -> POINTER(c_ubyte):  # Decompress data (DEFLATE algorithm), memory must be MemFree()
	pass

# Encode data to Base64 string, memory must be MemFree()
def encode_data_base64(data: POINTER(c_ubyte), dataSize: int, outputSize: POINTER(c_int)) -> bytes:
	pass

# Decode Base64 string data, memory must be MemFree()
def decode_data_base64(data: POINTER(c_ubyte), outputSize: POINTER(c_int)) -> POINTER(c_ubyte):  # Decode Base64 string data, memory must be MemFree()
	pass

# Check if a key has been pressed once
def is_key_pressed(key: int) -> bool:
	pass

# Check if a key is being pressed
def is_key_down(key: int) -> bool:
	pass

# Check if a key has been released once
def is_key_released(key: int) -> bool:
	pass

# Check if a key is NOT being pressed
def is_key_up(key: int) -> bool:
	pass

# Set a custom key to exit program (default is ESC)
def set_exit_key(key: int) -> None:
	pass

# Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty
def get_key_pressed() -> int:
	pass

# Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty
def get_char_pressed() -> int:
	pass

# Check if a gamepad is available
def is_gamepad_available(gamepad: int) -> bool:
	pass

# Get gamepad internal name id
def get_gamepad_name(gamepad: int) -> bytes:
	pass

# Check if a gamepad button has been pressed once
def is_gamepad_button_pressed(gamepad: int, button: int) -> bool:
	pass

# Check if a gamepad button is being pressed
def is_gamepad_button_down(gamepad: int, button: int) -> bool:
	pass

# Check if a gamepad button has been released once
def is_gamepad_button_released(gamepad: int, button: int) -> bool:
	pass

# Check if a gamepad button is NOT being pressed
def is_gamepad_button_up(gamepad: int, button: int) -> bool:
	pass

# Get the last gamepad button pressed
def get_gamepad_button_pressed() -> int:
	pass

# Get gamepad axis count for a gamepad
def get_gamepad_axis_count(gamepad: int) -> int:
	pass

# Get axis movement value for a gamepad axis
def get_gamepad_axis_movement(gamepad: int, axis: int) -> float:
	pass

# Set internal gamepad mappings (SDL_GameControllerDB)
def set_gamepad_mappings(mappings: bytes) -> int:
	pass

# Check if a mouse button has been pressed once
def is_mouse_button_pressed(button: int) -> bool:
	pass

# Check if a mouse button is being pressed
def is_mouse_button_down(button: int) -> bool:
	pass

# Check if a mouse button has been released once
def is_mouse_button_released(button: int) -> bool:
	pass

# Check if a mouse button is NOT being pressed
def is_mouse_button_up(button: int) -> bool:
	pass

# Get mouse position X
def get_mouse_x() -> int:
	pass

# Get mouse position Y
def get_mouse_y() -> int:
	pass

# Get mouse position XY
def get_mouse_position() -> Vector2:
	pass

# Get mouse delta between frames
def get_mouse_delta() -> Vector2:
	pass

# Set mouse position XY
def set_mouse_position(x: int, y: int) -> None:
	pass

# Set mouse offset
def set_mouse_offset(offsetX: int, offsetY: int) -> None:
	pass

# Set mouse scaling
def set_mouse_scale(scaleX: float, scaleY: float) -> None:
	pass

# Get mouse wheel movement for X or Y, whichever is larger
def get_mouse_wheel_move() -> float:
	pass

# Get mouse wheel movement for both X and Y
def get_mouse_wheel_move_v() -> Vector2:
	pass

# Set mouse cursor
def set_mouse_cursor(cursor: int) -> None:
	pass

# Get touch position X for touch point 0 (relative to screen size)
def get_touch_x() -> int:
	pass

# Get touch position Y for touch point 0 (relative to screen size)
def get_touch_y() -> int:
	pass

# Get touch position XY for a touch point index (relative to screen size)
def get_touch_position(index: int) -> Vector2:
	pass

# Get touch point identifier for given index
def get_touch_point_id(index: int) -> int:
	pass

# Get number of touch points
def get_touch_point_count() -> int:
	pass

# Enable a set of gestures using flags
def set_gestures_enabled(flags: int) -> None:
	pass

# Check if a gesture have been detected
def is_gesture_detected(gesture: int) -> bool:
	pass

# Get latest detected gesture
def get_gesture_detected() -> int:
	pass

# Get gesture hold time in milliseconds
def get_gesture_hold_duration() -> float:
	pass

# Get gesture drag vector
def get_gesture_drag_vector() -> Vector2:
	pass

# Get gesture drag angle
def get_gesture_drag_angle() -> float:
	pass

# Get gesture pinch delta
def get_gesture_pinch_vector() -> Vector2:
	pass

# Get gesture pinch angle
def get_gesture_pinch_angle() -> float:
	pass

# Set camera mode (multiple camera modes available)
def set_camera_mode(camera: Camera, mode: int) -> None:
	pass

# Update camera position for selected mode
def update_camera(camera: POINTER(Camera)) -> None:
	pass

# Set camera pan key to combine with mouse movement (free camera)
def set_camera_pan_control(keyPan: int) -> None:
	pass

# Set camera alt key to combine with mouse movement (free camera)
def set_camera_alt_control(keyAlt: int) -> None:
	pass

# Set camera smooth zoom key to combine with mouse (free camera)
def set_camera_smooth_zoom_control(keySmoothZoom: int) -> None:
	pass

# Set camera move controls (1st person and 3rd person cameras)
def set_camera_move_controls(keyFront: int, keyBack: int, keyRight: int, keyLeft: int, keyUp: int, keyDown: int) -> None:
	pass

# Set texture and rectangle to be used on shapes drawing
def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None:
	pass

# Draw a pixel
def draw_pixel(posX: int, posY: int, color: Color) -> None:
	pass

# Draw a pixel (Vector version)
def draw_pixel_v(position: Vector2, color: Color) -> None:
	pass

# Draw a line
def draw_line(startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
	pass

# Draw a line (Vector version)
def draw_line_v(startPos: Vector2, endPos: Vector2, color: Color) -> None:
	pass

# Draw a line defining thickness
def draw_line_ex(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
	pass

# Draw a line using cubic-bezier curves in-out
def draw_line_bezier(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None:
	pass

# Draw line using quadratic bezier curves with a control point
def draw_line_bezier_quad(startPos: Vector2, endPos: Vector2, controlPos: Vector2, thick: float, color: Color) -> None:
	pass

# Draw line using cubic bezier curves with 2 control points
def draw_line_bezier_cubic(startPos: Vector2, endPos: Vector2, startControlPos: Vector2, endControlPos: Vector2, thick: float, color: Color) -> None:
	pass

# Draw lines sequence
def draw_line_strip(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	pass

# Draw a color-filled circle
def draw_circle(centerX: int, centerY: int, radius: float, color: Color) -> None:
	pass

# Draw a piece of a circle
def draw_circle_sector(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	pass

# Draw circle sector outline
def draw_circle_sector_lines(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	pass

# Draw a gradient-filled circle
def draw_circle_gradient(centerX: int, centerY: int, radius: float, color1: Color, color2: Color) -> None:
	pass

# Draw a color-filled circle (Vector version)
def draw_circle_v(center: Vector2, radius: float, color: Color) -> None:
	pass

# Draw circle outline
def draw_circle_lines(centerX: int, centerY: int, radius: float, color: Color) -> None:
	pass

# Draw ellipse
def draw_ellipse(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
	pass

# Draw ellipse outline
def draw_ellipse_lines(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
	pass

# Draw ring
def draw_ring(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	pass

# Draw ring outline
def draw_ring_lines(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
	pass

# Draw a color-filled rectangle
def draw_rectangle(posX: int, posY: int, width: int, height: int, color: Color) -> None:
	pass

# Draw a color-filled rectangle (Vector version)
def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None:
	pass

# Draw a color-filled rectangle
def draw_rectangle_rec(rec: Rectangle, color: Color) -> None:
	pass

# Draw a color-filled rectangle with pro parameters
def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None:
	pass

# Draw a vertical-gradient-filled rectangle
def draw_rectangle_gradient_v(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
	pass

# Draw a horizontal-gradient-filled rectangle
def draw_rectangle_gradient_h(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
	pass

# Draw a gradient-filled rectangle with custom vertex colors
def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
	pass

# Draw rectangle outline
def draw_rectangle_lines(posX: int, posY: int, width: int, height: int, color: Color) -> None:
	pass

# Draw rectangle outline with extended parameters
def draw_rectangle_lines_ex(rec: Rectangle, lineThick: float, color: Color) -> None:
	pass

# Draw rectangle with rounded edges
def draw_rectangle_rounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None:
	pass

# Draw rectangle with rounded edges outline
def draw_rectangle_rounded_lines(rec: Rectangle, roundness: float, segments: int, lineThick: float, color: Color) -> None:
	pass

# Draw a color-filled triangle (vertex in counter-clockwise order!)
def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	pass

# Draw triangle outline (vertex in counter-clockwise order!)
def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	pass

# Draw a triangle fan defined by points (first vertex is the center)
def draw_triangle_fan(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	pass

# Draw a triangle strip defined by points
def draw_triangle_strip(points: POINTER(Vector2), pointCount: int, color: Color) -> None:
	pass

# Draw a regular polygon (Vector version)
def draw_poly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
	pass

# Draw a polygon outline of n sides
def draw_poly_lines(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
	pass

# Draw a polygon outline of n sides with extended parameters
def draw_poly_lines_ex(center: Vector2, sides: int, radius: float, rotation: float, lineThick: float, color: Color) -> None:
	pass

# Check collision between two rectangles
def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> bool:
	pass

# Check collision between two circles
def check_collision_circles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool:
	pass

# Check collision between circle and rectangle
def check_collision_circle_rec(center: Vector2, radius: float, rec: Rectangle) -> bool:
	pass

# Check if point is inside rectangle
def check_collision_point_rec(point: Vector2, rec: Rectangle) -> bool:
	pass

# Check if point is inside circle
def check_collision_point_circle(point: Vector2, center: Vector2, radius: float) -> bool:
	pass

# Check if point is inside a triangle
def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool:
	pass

# Check if point is within a polygon described by array of vertices
def check_collision_point_poly(point: Vector2, points: POINTER(Vector2), pointCount: int) -> bool:
	pass

# Check the collision between two lines defined by two points each, returns collision point by reference
def check_collision_lines(startPos1: Vector2, endPos1: Vector2, startPos2: Vector2, endPos2: Vector2, collisionPoint: POINTER(Vector2)) -> bool:
	pass

# Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]
def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: int) -> bool:
	pass

# Get collision rectangle for two rectangles collision
def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle:
	pass

# Load image from file into CPU memory (RAM)
def load_image(fileName: bytes) -> Image:
	pass

# Load image from RAW file data
def load_image_raw(fileName: bytes, width: int, height: int, format: int, headerSize: int) -> Image:
	pass

# Load image sequence from file (frames appended to image.data)
def load_image_anim(fileName: bytes, frames: POINTER(c_int)) -> Image:
	pass

# Load image from memory buffer, fileType refers to extension: i.e. '.png'
def load_image_from_memory(fileType: bytes, fileData: POINTER(c_ubyte), dataSize: int) -> Image:
	pass

# Load image from GPU texture data
def load_image_from_texture(texture: Texture2D) -> Image:
	pass

# Load image from screen buffer and (screenshot)
def load_image_from_screen() -> Image:
	pass

# Unload image from CPU memory (RAM)
def unload_image(image: Image) -> None:
	pass

# Export image data to file, returns true on success
def export_image(image: Image, fileName: bytes) -> bool:
	pass

# Export image as code file defining an array of bytes, returns true on success
def export_image_as_code(image: Image, fileName: bytes) -> bool:
	pass

# Generate image: plain color
def gen_image_color(width: int, height: int, color: Color) -> Image:
	pass

# Generate image: vertical gradient
def gen_image_gradient_v(width: int, height: int, top: Color, bottom: Color) -> Image:
	pass

# Generate image: horizontal gradient
def gen_image_gradient_h(width: int, height: int, left: Color, right: Color) -> Image:
	pass

# Generate image: radial gradient
def gen_image_gradient_radial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
	pass

# Generate image: checked
def gen_image_checked(width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image:
	pass

# Generate image: white noise
def gen_image_white_noise(width: int, height: int, factor: float) -> Image:
	pass

# Generate image: perlin noise
def gen_image_perlin_noise(width: int, height: int, offsetX: int, offsetY: int, scale: float) -> Image:
	pass

# Generate image: cellular algorithm, bigger tileSize means bigger cells
def gen_image_cellular(width: int, height: int, tileSize: int) -> Image:
	pass

# Create an image duplicate (useful for transformations)
def image_copy(image: Image) -> Image:
	pass

# Create an image from another image piece
def image_from_image(image: Image, rec: Rectangle) -> Image:
	pass

# Create an image from text (default font)
def image_text(text: bytes, fontSize: int, color: Color) -> Image:
	pass

# Create an image from text (custom sprite font)
def image_text_ex(font: Font, text: bytes, fontSize: float, spacing: float, tint: Color) -> Image:
	pass

# Convert image data to desired format
def image_format(image: POINTER(Image), newFormat: int) -> None:
	pass

# Convert image to POT (power-of-two)
def image_to_pot(image: POINTER(Image), fill: Color) -> None:
	pass

# Crop an image to a defined rectangle
def image_crop(image: POINTER(Image), crop: Rectangle) -> None:
	pass

# Crop image depending on alpha value
def image_alpha_crop(image: POINTER(Image), threshold: float) -> None:
	pass

# Clear alpha channel to desired color
def image_alpha_clear(image: POINTER(Image), color: Color, threshold: float) -> None:
	pass

# Apply alpha mask to image
def image_alpha_mask(image: POINTER(Image), alphaMask: Image) -> None:
	pass

# Premultiply alpha channel
def image_alpha_premultiply(image: POINTER(Image)) -> None:
	pass

# Resize image (Bicubic scaling algorithm)
def image_resize(image: POINTER(Image), newWidth: int, newHeight: int) -> None:
	pass

# Resize image (Nearest-Neighbor scaling algorithm)
def image_resize_nn(image: POINTER(Image), newWidth: int, newHeight: int) -> None:
	pass

# Resize canvas and fill with color
def image_resize_canvas(image: POINTER(Image), newWidth: int, newHeight: int, offsetX: int, offsetY: int, fill: Color) -> None:
	pass

# Compute all mipmap levels for a provided image
def image_mipmaps(image: POINTER(Image)) -> None:
	pass

# Dither image data to 16bpp or lower (Floyd-Steinberg dithering)
def image_dither(image: POINTER(Image), rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None:
	pass

# Flip image vertically
def image_flip_vertical(image: POINTER(Image)) -> None:
	pass

# Flip image horizontally
def image_flip_horizontal(image: POINTER(Image)) -> None:
	pass

# Rotate image clockwise 90deg
def image_rotate_cw(image: POINTER(Image)) -> None:
	pass

# Rotate image counter-clockwise 90deg
def image_rotate_ccw(image: POINTER(Image)) -> None:
	pass

# Modify image color: tint
def image_color_tint(image: POINTER(Image), color: Color) -> None:
	pass

# Modify image color: invert
def image_color_invert(image: POINTER(Image)) -> None:
	pass

# Modify image color: grayscale
def image_color_grayscale(image: POINTER(Image)) -> None:
	pass

# Modify image color: contrast (-100 to 100)
def image_color_contrast(image: POINTER(Image), contrast: float) -> None:
	pass

# Modify image color: brightness (-255 to 255)
def image_color_brightness(image: POINTER(Image), brightness: int) -> None:
	pass

# Modify image color: replace color
def image_color_replace(image: POINTER(Image), color: Color, replace: Color) -> None:
	pass

# Load color data from image as a Color array (RGBA - 32bit)
def load_image_colors(image: Image) -> POINTER(Color):  # Load color data from image as a Color array (RGBA - 32bit)
	pass

# Load colors palette from image as a Color array (RGBA - 32bit)
def load_image_palette(image: Image, maxPaletteSize: int, colorCount: POINTER(c_int)) -> POINTER(Color):  # Load colors palette from image as a Color array (RGBA - 32bit)
	pass

# Unload color data loaded with LoadImageColors()
def unload_image_colors(colors: POINTER(Color)) -> None:
	pass

# Unload colors palette loaded with LoadImagePalette()
def unload_image_palette(colors: POINTER(Color)) -> None:
	pass

# Get image alpha border rectangle
def get_image_alpha_border(image: Image, threshold: float) -> Rectangle:
	pass

# Get image pixel color at (x, y) position
def get_image_color(image: Image, x: int, y: int) -> Color:
	pass

# Clear image background with given color
def image_clear_background(dst: POINTER(Image), color: Color) -> None:
	pass

# Draw pixel within an image
def image_draw_pixel(dst: POINTER(Image), posX: int, posY: int, color: Color) -> None:
	pass

# Draw pixel within an image (Vector version)
def image_draw_pixel_v(dst: POINTER(Image), position: Vector2, color: Color) -> None:
	pass

# Draw line within an image
def image_draw_line(dst: POINTER(Image), startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
	pass

# Draw line within an image (Vector version)
def image_draw_line_v(dst: POINTER(Image), start: Vector2, end: Vector2, color: Color) -> None:
	pass

# Draw a filled circle within an image
def image_draw_circle(dst: POINTER(Image), centerX: int, centerY: int, radius: int, color: Color) -> None:
	pass

# Draw a filled circle within an image (Vector version)
def image_draw_circle_v(dst: POINTER(Image), center: Vector2, radius: int, color: Color) -> None:
	pass

# Draw circle outline within an image
def image_draw_circle_lines(dst: POINTER(Image), centerX: int, centerY: int, radius: int, color: Color) -> None:
	pass

# Draw circle outline within an image (Vector version)
def image_draw_circle_lines_v(dst: POINTER(Image), center: Vector2, radius: int, color: Color) -> None:
	pass

# Draw rectangle within an image
def image_draw_rectangle(dst: POINTER(Image), posX: int, posY: int, width: int, height: int, color: Color) -> None:
	pass

# Draw rectangle within an image (Vector version)
def image_draw_rectangle_v(dst: POINTER(Image), position: Vector2, size: Vector2, color: Color) -> None:
	pass

# Draw rectangle within an image
def image_draw_rectangle_rec(dst: POINTER(Image), rec: Rectangle, color: Color) -> None:
	pass

# Draw rectangle lines within an image
def image_draw_rectangle_lines(dst: POINTER(Image), rec: Rectangle, thick: int, color: Color) -> None:
	pass

# Draw a source image within a destination image (tint applied to source)
def image_draw(dst: POINTER(Image), src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None:
	pass

# Draw text (using default font) within an image (destination)
def image_draw_text(dst: POINTER(Image), text: bytes, posX: int, posY: int, fontSize: int, color: Color) -> None:
	pass

# Draw text (custom sprite font) within an image (destination)
def image_draw_text_ex(dst: POINTER(Image), font: Font, text: bytes, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	pass

# Load texture from file into GPU memory (VRAM)
def load_texture(fileName: bytes) -> Texture2D:
	pass

# Load texture from image data
def load_texture_from_image(image: Image) -> Texture2D:
	pass

# Load cubemap from image, multiple image cubemap layouts supported
def load_texture_cubemap(image: Image, layout: int) -> TextureCubemap:
	pass

# Load texture for rendering (framebuffer)
def load_render_texture(width: int, height: int) -> RenderTexture2D:
	pass

# Unload texture from GPU memory (VRAM)
def unload_texture(texture: Texture2D) -> None:
	pass

# Unload render texture from GPU memory (VRAM)
def unload_render_texture(target: RenderTexture2D) -> None:
	pass

# Update GPU texture with new data
def update_texture(texture: Texture2D, pixels: int) -> None:
	pass

# Update GPU texture rectangle with new data
def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: int) -> None:
	pass

# Generate GPU mipmaps for a texture
def gen_texture_mipmaps(texture: POINTER(Texture2D)) -> None:
	pass

# Set texture scaling filter mode
def set_texture_filter(texture: Texture2D, filter: int) -> None:
	pass

# Set texture wrapping mode
def set_texture_wrap(texture: Texture2D, wrap: int) -> None:
	pass

# Draw a Texture2D
def draw_texture(texture: Texture2D, posX: int, posY: int, tint: Color) -> None:
	pass

# Draw a Texture2D with position defined as Vector2
def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None:
	pass

# Draw a Texture2D with extended parameters
def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None:
	pass

# Draw a part of a texture defined by a rectangle
def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None:
	pass

# Draw texture quad with tiling and offset parameters
def draw_texture_quad(texture: Texture2D, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None:
	pass

# Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest.
def draw_texture_tiled(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None:
	pass

# Draw a part of a texture defined by a rectangle with 'pro' parameters
def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
	pass

# Draws a texture (or part of it) that stretches or shrinks nicely
def draw_texture_n_patch(texture: Texture2D, nPatchInfo: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
	pass

# Draw a textured polygon
def draw_texture_poly(texture: Texture2D, center: Vector2, points: POINTER(Vector2), texcoords: POINTER(Vector2), pointCount: int, tint: Color) -> None:
	pass

# Get color with alpha applied, alpha goes from 0.0f to 1.0f
def fade(color: Color, alpha: float) -> Color:
	pass

# Get hexadecimal value for a Color
def color_to_int(color: Color) -> int:
	pass

# Get Color normalized as float [0..1]
def color_normalize(color: Color) -> Vector4:
	pass

# Get Color from normalized values [0..1]
def color_from_normalized(normalized: Vector4) -> Color:
	pass

# Get HSV values for a Color, hue [0..360], saturation/value [0..1]
def color_to_hsv(color: Color) -> Vector3:
	pass

# Get a Color from HSV values, hue [0..360], saturation/value [0..1]
def color_from_hsv(hue: float, saturation: float, value: float) -> Color:
	pass

# Get color with alpha applied, alpha goes from 0.0f to 1.0f
def color_alpha(color: Color, alpha: float) -> Color:
	pass

# Get src alpha-blended into dst color with tint
def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color:
	pass

# Get Color structure from hexadecimal value
def get_color(hexValue: int) -> Color:
	pass

# Get Color from a source pixel pointer of certain format
def get_pixel_color(srcPtr: int, format: int) -> Color:
	pass

# Set color formatted into destination pixel pointer
def set_pixel_color(dstPtr: int, color: Color, format: int) -> None:
	pass

# Get pixel data size in bytes for certain format
def get_pixel_data_size(width: int, height: int, format: int) -> int:
	pass

# Get the default Font
def get_font_default() -> Font:
	pass

# Load font from file into GPU memory (VRAM)
def load_font(fileName: bytes) -> Font:
	pass

# Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set
def load_font_ex(fileName: bytes, fontSize: int, fontChars: POINTER(c_int), glyphCount: int) -> Font:
	pass

# Load font from Image (XNA style)
def load_font_from_image(image: Image, key: Color, firstChar: int) -> Font:
	pass

# Load font from memory buffer, fileType refers to extension: i.e. '.ttf'
def load_font_from_memory(fileType: bytes, fileData: POINTER(c_ubyte), dataSize: int, fontSize: int, fontChars: POINTER(c_int), glyphCount: int) -> Font:
	pass

# Load font data for further use
def load_font_data(fileData: POINTER(c_ubyte), dataSize: int, fontSize: int, fontChars: POINTER(c_int), glyphCount: int, type: int) -> POINTER(GlyphInfo):  # Load font data for further use
	pass

# Generate image font atlas using chars info
def gen_image_font_atlas(chars: POINTER(GlyphInfo), recs: POINTER(POINTER(Rectangle)), glyphCount: int, fontSize: int, padding: int, packMethod: int) -> Image:
	pass

# Unload font chars info data (RAM)
def unload_font_data(chars: POINTER(GlyphInfo), glyphCount: int) -> None:
	pass

# Unload font from GPU memory (VRAM)
def unload_font(font: Font) -> None:
	pass

# Export font as code file, returns true on success
def export_font_as_code(font: Font, fileName: bytes) -> bool:
	pass

# Draw current FPS
def draw_fps(posX: int, posY: int) -> None:
	pass

# Draw text (using default font)
def draw_text(text: bytes, posX: int, posY: int, fontSize: int, color: Color) -> None:
	pass

# Draw text using font and additional parameters
def draw_text_ex(font: Font, text: bytes, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	pass

# Draw text using Font and pro parameters (rotation)
def draw_text_pro(font: Font, text: bytes, position: Vector2, origin: Vector2, rotation: float, fontSize: float, spacing: float, tint: Color) -> None:
	pass

# Draw one character (codepoint)
def draw_text_codepoint(font: Font, codepoint: int, position: Vector2, fontSize: float, tint: Color) -> None:
	pass

# Draw multiple character (codepoint)
def draw_text_codepoints(font: Font, codepoints: POINTER(c_int), count: int, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
	pass

# Measure string width for default font
def measure_text(text: bytes, fontSize: int) -> int:
	pass

# Measure string size for Font
def measure_text_ex(font: Font, text: bytes, fontSize: float, spacing: float) -> Vector2:
	pass

# Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found
def get_glyph_index(font: Font, codepoint: int) -> int:
	pass

# Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found
def get_glyph_info(font: Font, codepoint: int) -> GlyphInfo:
	pass

# Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found
def get_glyph_atlas_rec(font: Font, codepoint: int) -> Rectangle:
	pass

# Load UTF-8 text encoded from codepoints array
def load_utf8(codepoints: POINTER(c_int), length: int) -> bytes:
	pass

# Unload UTF-8 text encoded from codepoints array
def unload_utf8(text: bytes) -> None:
	pass

# Load all codepoints from a UTF-8 text string, codepoints count returned by parameter
def load_codepoints(text: bytes, count: POINTER(c_int)) -> POINTER(c_int):  # Load all codepoints from a UTF-8 text string, codepoints count returned by parameter
	pass

# Unload codepoints data from memory
def unload_codepoints(codepoints: POINTER(c_int)) -> None:
	pass

# Get total number of codepoints in a UTF-8 encoded string
def get_codepoint_count(text: bytes) -> int:
	pass

# Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure
def get_codepoint(text: bytes, codepointSize: POINTER(c_int)) -> int:
	pass

# Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure
def get_codepoint_next(text: bytes, codepointSize: POINTER(c_int)) -> int:
	pass

# Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure
def get_codepoint_previous(text: bytes, codepointSize: POINTER(c_int)) -> int:
	pass

# Encode one codepoint into UTF-8 byte array (array length returned as parameter)
def codepoint_to_utf8(codepoint: int, utf8Size: POINTER(c_int)) -> bytes:
	pass

# Copy one string to another, returns bytes copied
def text_copy(dst: bytes, src: bytes) -> int:
	pass

# Check if two text string are equal
def text_is_equal(text1: bytes, text2: bytes) -> bool:
	pass

# Get text length, checks for '\0' ending
def text_length(text: bytes) -> int:
	pass

# Text formatting with variables (sprintf() style)
def text_format(text: bytes, args: ...) -> bytes:
	pass

# Get a piece of a text string
def text_subtext(text: bytes, position: int, length: int) -> bytes:
	pass

# Replace text string (WARNING: memory must be freed!)
def text_replace(text: bytes, replace: bytes, by: bytes) -> bytes:
	pass

# Insert text in a position (WARNING: memory must be freed!)
def text_insert(text: bytes, insert: bytes, position: int) -> bytes:
	pass

# Join text strings with delimiter
def text_join(textList: POINTER(POINTER(c_char)), count: int, delimiter: bytes) -> bytes:
	pass

# Split text into multiple strings
def text_split(text: bytes, delimiter: bytes, count: POINTER(c_int)) -> POINTER(POINTER(c_char)):  # Split text into multiple strings
	pass

# Append text at specific position and move cursor!
def text_append(text: bytes, append: bytes, position: POINTER(c_int)) -> None:
	pass

# Find first text occurrence within a string
def text_find_index(text: bytes, find: bytes) -> int:
	pass

# Get upper case version of provided string
def text_to_upper(text: bytes) -> bytes:
	pass

# Get lower case version of provided string
def text_to_lower(text: bytes) -> bytes:
	pass

# Get Pascal case notation version of provided string
def text_to_pascal(text: bytes) -> bytes:
	pass

# Get integer value from text (negative values not supported)
def text_to_integer(text: bytes) -> int:
	pass

# Draw a line in 3D world space
def draw_line_3d(startPos: Vector3, endPos: Vector3, color: Color) -> None:
	pass

# Draw a point in 3D space, actually a small line
def draw_point_3d(position: Vector3, color: Color) -> None:
	pass

# Draw a circle in 3D world space
def draw_circle_3d(center: Vector3, radius: float, rotationAxis: Vector3, rotationAngle: float, color: Color) -> None:
	pass

# Draw a color-filled triangle (vertex in counter-clockwise order!)
def draw_triangle_3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None:
	pass

# Draw a triangle strip defined by points
def draw_triangle_strip_3d(points: POINTER(Vector3), pointCount: int, color: Color) -> None:
	pass

# Draw cube
def draw_cube(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	pass

# Draw cube (Vector version)
def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None:
	pass

# Draw cube wires
def draw_cube_wires(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	pass

# Draw cube wires (Vector version)
def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None:
	pass

# Draw cube textured
def draw_cube_texture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	pass

# Draw cube with a region of a texture
def draw_cube_texture_rec(texture: Texture2D, source: Rectangle, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
	pass

# Draw sphere
def draw_sphere(centerPos: Vector3, radius: float, color: Color) -> None:
	pass

# Draw sphere with extended parameters
def draw_sphere_ex(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
	pass

# Draw sphere wires
def draw_sphere_wires(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
	pass

# Draw a cylinder/cone
def draw_cylinder(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
	pass

# Draw a cylinder with base at startPos and top at endPos
def draw_cylinder_ex(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
	pass

# Draw a cylinder/cone wires
def draw_cylinder_wires(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
	pass

# Draw a cylinder wires with base at startPos and top at endPos
def draw_cylinder_wires_ex(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
	pass

# Draw a plane XZ
def draw_plane(centerPos: Vector3, size: Vector2, color: Color) -> None:
	pass

# Draw a ray line
def draw_ray(ray: Ray, color: Color) -> None:
	pass

# Draw a grid (centered at (0, 0, 0))
def draw_grid(slices: int, spacing: float) -> None:
	pass

# Load model from files (meshes and materials)
def load_model(fileName: bytes) -> Model:
	pass

# Load model from generated mesh (default material)
def load_model_from_mesh(mesh: Mesh) -> Model:
	pass

# Unload model (including meshes) from memory (RAM and/or VRAM)
def unload_model(model: Model) -> None:
	pass

# Unload model (but not meshes) from memory (RAM and/or VRAM)
def unload_model_keep_meshes(model: Model) -> None:
	pass

# Compute model bounding box limits (considers all meshes)
def get_model_bounding_box(model: Model) -> BoundingBox:
	pass

# Draw a model (with texture if set)
def draw_model(model: Model, position: Vector3, scale: float, tint: Color) -> None:
	pass

# Draw a model with extended parameters
def draw_model_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
	pass

# Draw a model wires (with texture if set)
def draw_model_wires(model: Model, position: Vector3, scale: float, tint: Color) -> None:
	pass

# Draw a model wires (with texture if set) with extended parameters
def draw_model_wires_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
	pass

# Draw bounding box (wires)
def draw_bounding_box(box: BoundingBox, color: Color) -> None:
	pass

# Draw a billboard texture
def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, size: float, tint: Color) -> None:
	pass

# Draw a billboard texture defined by source
def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None:
	pass

# Draw a billboard texture defined by source and rotation
def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: float, tint: Color) -> None:
	pass

# Upload mesh vertex data in GPU and provide VAO/VBO ids
def upload_mesh(mesh: POINTER(Mesh), dynamic: bool) -> None:
	pass

# Update mesh vertex data in GPU for a specific buffer index
def update_mesh_buffer(mesh: Mesh, index: int, data: int, dataSize: int, offset: int) -> None:
	pass

# Unload mesh data from CPU and GPU
def unload_mesh(mesh: Mesh) -> None:
	pass

# Draw a 3d mesh with material and transform
def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
	pass

# Draw multiple mesh instances with material and different transforms
def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: POINTER(Matrix), instances: int) -> None:
	pass

# Export mesh data to file, returns true on success
def export_mesh(mesh: Mesh, fileName: bytes) -> bool:
	pass

# Compute mesh bounding box limits
def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox:
	pass

# Compute mesh tangents
def gen_mesh_tangents(mesh: POINTER(Mesh)) -> None:
	pass

# Generate polygonal mesh
def gen_mesh_poly(sides: int, radius: float) -> Mesh:
	pass

# Generate plane mesh (with subdivisions)
def gen_mesh_plane(width: float, length: float, resX: int, resZ: int) -> Mesh:
	pass

# Generate cuboid mesh
def gen_mesh_cube(width: float, height: float, length: float) -> Mesh:
	pass

# Generate sphere mesh (standard sphere)
def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh:
	pass

# Generate half-sphere mesh (no bottom cap)
def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh:
	pass

# Generate cylinder mesh
def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh:
	pass

# Generate cone/pyramid mesh
def gen_mesh_cone(radius: float, height: float, slices: int) -> Mesh:
	pass

# Generate torus mesh
def gen_mesh_torus(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
	pass

# Generate trefoil knot mesh
def gen_mesh_knot(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
	pass

# Generate heightmap mesh from image data
def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh:
	pass

# Generate cubes-based map mesh from image data
def gen_mesh_cubicmap(cubicmap: Image, cubeSize: Vector3) -> Mesh:
	pass

# Load materials from model file
def load_materials(fileName: bytes, materialCount: POINTER(c_int)) -> POINTER(Material):  # Load materials from model file
	pass

# Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)
def load_material_default() -> Material:
	pass

# Unload material from GPU memory (VRAM)
def unload_material(material: Material) -> None:
	pass

# Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)
def set_material_texture(material: POINTER(Material), mapType: int, texture: Texture2D) -> None:
	pass

# Set material for a mesh
def set_model_mesh_material(model: POINTER(Model), meshId: int, materialId: int) -> None:
	pass

# Load model animations from file
def load_model_animations(fileName: bytes, animCount: POINTER(c_uint)) -> POINTER(ModelAnimation):  # Load model animations from file
	pass

# Update model animation pose
def update_model_animation(model: Model, anim: ModelAnimation, frame: int) -> None:
	pass

# Unload animation data
def unload_model_animation(anim: ModelAnimation) -> None:
	pass

# Unload animation array data
def unload_model_animations(animations: POINTER(ModelAnimation), count: int) -> None:
	pass

# Check model animation skeleton match
def is_model_animation_valid(model: Model, anim: ModelAnimation) -> bool:
	pass

# Check collision between two spheres
def check_collision_spheres(center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool:
	pass

# Check collision between two bounding boxes
def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool:
	pass

# Check collision between box and sphere
def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: float) -> bool:
	pass

# Get collision info between ray and sphere
def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: float) -> RayCollision:
	pass

# Get collision info between ray and box
def get_ray_collision_box(ray: Ray, box: BoundingBox) -> RayCollision:
	pass

# Get collision info between ray and mesh
def get_ray_collision_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision:
	pass

# Get collision info between ray and triangle
def get_ray_collision_triangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayCollision:
	pass

# Get collision info between ray and quad
def get_ray_collision_quad(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3, p4: Vector3) -> RayCollision:
	pass

# Initialize audio device and context
def init_audio_device() -> None:
	pass

# Close the audio device and context
def close_audio_device() -> None:
	pass

# Check if audio device has been initialized successfully
def is_audio_device_ready() -> bool:
	pass

# Set master volume (listener)
def set_master_volume(volume: float) -> None:
	pass

# Stop any sound playing (using multichannel buffer pool)
def stop_sound_multi() -> None:
	pass

# Get number of sounds playing in the multichannel
def get_sounds_playing() -> int:
	pass

# Unload samples data loaded with LoadWaveSamples()
def unload_wave_samples(samples: POINTER(c_float)) -> None:
	pass

# Default size for new audio streams
def set_audio_stream_buffer_size_default(size: int) -> None:
	pass

