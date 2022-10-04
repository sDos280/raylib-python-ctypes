from structures import *
from typing import (Union)

def init_window(width: int, height: int, title: Union[bytes, None]) -> None:
	"""Initialize window and OpenGL context"""
	pass

def window_should_close() -> bool:
	"""Check if KEY_ESCAPE pressed or Close icon pressed"""
	pass

def close_window() -> None:
	"""Close window and unload OpenGL context"""
	pass

def is_window_ready() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_fullscreen() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_hidden() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_minimized() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_maximized() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_focused() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_resized() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def is_window_state(flag: int) -> bool:
	"""Check if window has been initialized successfully"""
	pass

def set_window_state(flags: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def clear_window_state(flags: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def toggle_fullscreen() -> None:
	"""Check if window has been initialized successfully"""
	pass

def maximize_window() -> None:
	"""Check if window has been initialized successfully"""
	pass

def minimize_window() -> None:
	"""Check if window has been initialized successfully"""
	pass

def restore_window() -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_icon(image: Image) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_title(title: Union[bytes, None]) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_position(x: int, y: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_monitor(monitor: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_min_size(width: int, height: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_size(width: int, height: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_window_opacity(opacity: float) -> None:
	"""Check if window has been initialized successfully"""
	pass

def get_window_handle() -> Union[int, None]:
	"""Check if window has been initialized successfully"""
	pass

def get_screen_width() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_screen_height() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_render_width() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_render_height() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_count() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_current_monitor() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_position(monitor: int) -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_width(monitor: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_height(monitor: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_physical_width(monitor: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_physical_height(monitor: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_refresh_rate(monitor: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_window_position() -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_window_scale_dpi() -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_monitor_name(monitor: int) -> Union[bytes, None]:
	"""Check if window has been initialized successfully"""
	pass

def set_clipboard_text(text: Union[bytes, None]) -> None:
	"""Check if window has been initialized successfully"""
	pass

def get_clipboard_text() -> Union[bytes, None]:
	"""Check if window has been initialized successfully"""
	pass

def enable_event_waiting() -> None:
	"""Check if window has been initialized successfully"""
	pass

def disable_event_waiting() -> None:
	"""Check if window has been initialized successfully"""
	pass

def swap_screen_buffer() -> None:
	"""Check if window has been initialized successfully"""
	pass

def poll_input_events() -> None:
	"""Check if window has been initialized successfully"""
	pass

def wait_time(seconds: float) -> None:
	"""Check if window has been initialized successfully"""
	pass

def show_cursor() -> None:
	"""Check if window has been initialized successfully"""
	pass

def hide_cursor() -> None:
	"""Check if window has been initialized successfully"""
	pass

def is_cursor_hidden() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def enable_cursor() -> None:
	"""Check if window has been initialized successfully"""
	pass

def disable_cursor() -> None:
	"""Check if window has been initialized successfully"""
	pass

def is_cursor_on_screen() -> bool:
	"""Check if window has been initialized successfully"""
	pass

def clear_background(color: Color) -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_drawing() -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_drawing() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_mode_2d(camera: Camera2D) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_mode_2d() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_mode_3d(camera: Camera3D) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_mode_3d() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_texture_mode(target: RenderTexture2D) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_texture_mode() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_shader_mode(shader: Shader) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_shader_mode() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_blend_mode(mode: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_blend_mode() -> None:
	"""Check if window has been initialized successfully"""
	pass

def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_scissor_mode() -> None:
	"""Check if window has been initialized successfully"""
	pass

def end_vr_stereo_mode() -> None:
	"""Check if window has been initialized successfully"""
	pass

def load_shader(vsFileName: Union[bytes, None], fsFileName: Union[bytes, None]) -> Shader:
	"""Check if window has been initialized successfully"""
	pass

def load_shader_from_memory(vsCode: Union[bytes, None], fsCode: Union[bytes, None]) -> Shader:
	"""Check if window has been initialized successfully"""
	pass

def get_shader_location(shader: Shader, uniformName: Union[bytes, None]) -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_shader_location_attrib(shader: Shader, attribName: Union[bytes, None]) -> int:
	"""Check if window has been initialized successfully"""
	pass

def set_shader_value(shader: Shader, locIndex: int, value: Union[int, None], uniformType: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_shader_value_v(shader: Shader, locIndex: int, value: Union[int, None], uniformType: int, count: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_shader_value_matrix(shader: Shader, locIndex: int, mat: Matrix) -> None:
	"""Check if window has been initialized successfully"""
	pass

def set_shader_value_texture(shader: Shader, locIndex: int, texture: Texture2D) -> None:
	"""Check if window has been initialized successfully"""
	pass

def unload_shader(shader: Shader) -> None:
	"""Check if window has been initialized successfully"""
	pass

def get_mouse_ray(mousePosition: Vector2, camera: Camera) -> Ray:
	"""Check if window has been initialized successfully"""
	pass

def get_camera_matrix(camera: Camera) -> Matrix:
	"""Check if window has been initialized successfully"""
	pass

def get_camera_matrix_2d(camera: Camera2D) -> Matrix:
	"""Check if window has been initialized successfully"""
	pass

def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_screen_to_world_2d(position: Vector3, camera: Camera2D) -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_world_to_screen_ex(position: Vector3, camera: Camera2D, width: int, height: int) -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def get_world_to_screen_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Check if window has been initialized successfully"""
	pass

def set_target_fps(fps: int) -> None:
	"""Check if window has been initialized successfully"""
	pass

def get_fps() -> int:
	"""Check if window has been initialized successfully"""
	pass

def get_frame_time() -> float:
	"""Check if window has been initialized successfully"""
	pass

def get_time() -> float:
	"""Check if window has been initialized successfully"""
	pass

def get_random_value(min: int, max: int) -> int:
	"""Check if window has been initialized successfully"""
	pass

