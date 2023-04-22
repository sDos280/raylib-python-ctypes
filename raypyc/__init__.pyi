import ctypes
from raypyc.defines import *
from raypyc.defines import *
from raypyc.colors import *
from raypyc.enums import *
from raypyc.structures import *


def rl_matrix_mode(mode: ctypes.c_int) -> None:
	"""Choose the current matrix to be transformed"""
	...

def rl_push_matrix() -> None:
	"""Push the current matrix to stack"""
	...

def rl_pop_matrix() -> None:
	"""Pop latest inserted matrix from stack"""
	...

def rl_load_identity() -> None:
	"""Reset current matrix to identity matrix"""
	...

def rl_translatef(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Multiply the current matrix by a translation matrix"""
	...

def rl_rotatef(angle: ctypes.c_float, x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Multiply the current matrix by a rotation matrix"""
	...

def rl_scalef(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Multiply the current matrix by a scaling matrix"""
	...

def rl_mult_matrixf(matf: ctypes.POINTER(ctypes.c_float)) -> None:
	"""Multiply the current matrix by another matrix"""
	...

def rl_frustum(left: ctypes.c_double, right: ctypes.c_double, bottom: ctypes.c_double, top: ctypes.c_double, znear: ctypes.c_double, zfar: ctypes.c_double) -> None:
	""""""
	...

def rl_ortho(left: ctypes.c_double, right: ctypes.c_double, bottom: ctypes.c_double, top: ctypes.c_double, znear: ctypes.c_double, zfar: ctypes.c_double) -> None:
	""""""
	...

def rl_viewport(x: ctypes.c_int, y: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int) -> None:
	"""Set the viewport area"""
	...

def rl_begin(mode: ctypes.c_int) -> None:
	"""Initialize drawing mode (how to organize vertex)"""
	...

def rl_end() -> None:
	"""Finish vertex providing"""
	...

def rl_vertex2i(x: ctypes.c_int, y: ctypes.c_int) -> None:
	"""Define one vertex (position) - 2 int"""
	...

def rl_vertex2f(x: ctypes.c_float, y: ctypes.c_float) -> None:
	"""Define one vertex (position) - 2 float"""
	...

def rl_vertex3f(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Define one vertex (position) - 3 float"""
	...

def rl_tex_coord2f(x: ctypes.c_float, y: ctypes.c_float) -> None:
	"""Define one vertex (texture coordinate) - 2 float"""
	...

def rl_normal3f(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Define one vertex (normal) - 3 float"""
	...

def rl_color4ub(r: ctypes.c_ubyte, g: ctypes.c_ubyte, b: ctypes.c_ubyte, a: ctypes.c_ubyte) -> None:
	"""Define one vertex (color) - 4 byte"""
	...

def rl_color3f(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> None:
	"""Define one vertex (color) - 3 float"""
	...

def rl_color4f(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float, w: ctypes.c_float) -> None:
	"""Define one vertex (color) - 4 float"""
	...

def rl_enable_vertex_array(vaoId: ctypes.c_uint) -> ctypes.c_bool:
	"""Enable vertex array (VAO, if supported)"""
	...

def rl_disable_vertex_array() -> None:
	"""Disable vertex array (VAO, if supported)"""
	...

def rl_enable_vertex_buffer(id: ctypes.c_uint) -> None:
	"""Enable vertex buffer (VBO)"""
	...

def rl_disable_vertex_buffer() -> None:
	"""Disable vertex buffer (VBO)"""
	...

def rl_enable_vertex_buffer_element(id: ctypes.c_uint) -> None:
	"""Enable vertex buffer element (VBO element)"""
	...

def rl_disable_vertex_buffer_element() -> None:
	"""Disable vertex buffer element (VBO element)"""
	...

def rl_enable_vertex_attribute(index: ctypes.c_uint) -> None:
	"""Enable vertex attribute index"""
	...

def rl_disable_vertex_attribute(index: ctypes.c_uint) -> None:
	"""Disable vertex attribute index"""
	...

def rl_active_texture_slot(slot: ctypes.c_int) -> None:
	"""Select and active a texture slot"""
	...

def rl_enable_texture(id: ctypes.c_uint) -> None:
	"""Enable texture"""
	...

def rl_disable_texture() -> None:
	"""Disable texture"""
	...

def rl_enable_texture_cubemap(id: ctypes.c_uint) -> None:
	"""Enable texture cubemap"""
	...

def rl_disable_texture_cubemap() -> None:
	"""Disable texture cubemap"""
	...

def rl_texture_parameters(id: ctypes.c_uint, param: ctypes.c_int, value: ctypes.c_int) -> None:
	"""Set texture parameters (filter, wrap)"""
	...

def rl_cubemap_parameters(id: ctypes.c_uint, param: ctypes.c_int, value: ctypes.c_int) -> None:
	"""Set cubemap parameters (filter, wrap)"""
	...

def rl_enable_shader(id: ctypes.c_uint) -> None:
	"""Enable shader program"""
	...

def rl_disable_shader() -> None:
	"""Disable shader program"""
	...

def rl_enable_framebuffer(id: ctypes.c_uint) -> None:
	"""Enable render texture (fbo)"""
	...

def rl_disable_framebuffer() -> None:
	"""Disable render texture (fbo), return to default framebuffer"""
	...

def rl_active_draw_buffers(count: ctypes.c_int) -> None:
	"""Activate multiple draw color buffers"""
	...

def rl_enable_color_blend() -> None:
	"""Enable color blending"""
	...

def rl_disable_color_blend() -> None:
	"""Disable color blending"""
	...

def rl_enable_depth_test() -> None:
	"""Enable depth test"""
	...

def rl_disable_depth_test() -> None:
	"""Disable depth test"""
	...

def rl_enable_depth_mask() -> None:
	"""Enable depth write"""
	...

def rl_disable_depth_mask() -> None:
	"""Disable depth write"""
	...

def rl_enable_backface_culling() -> None:
	"""Enable backface culling"""
	...

def rl_disable_backface_culling() -> None:
	"""Disable backface culling"""
	...

def rl_set_cull_face(mode: ctypes.c_int) -> None:
	"""Set face culling mode"""
	...

def rl_enable_scissor_test() -> None:
	"""Enable scissor test"""
	...

def rl_disable_scissor_test() -> None:
	"""Disable scissor test"""
	...

def rl_scissor(x: ctypes.c_int, y: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int) -> None:
	"""Scissor test"""
	...

def rl_enable_wire_mode() -> None:
	"""Enable wire mode"""
	...

def rl_disable_wire_mode() -> None:
	"""Disable wire mode"""
	...

def rl_set_line_width(width: ctypes.c_float) -> None:
	"""Set the line drawing width"""
	...

def rl_get_line_width() -> ctypes.c_float:
	"""Get the line drawing width"""
	...

def rl_enable_smooth_lines() -> None:
	"""Enable line aliasing"""
	...

def rl_disable_smooth_lines() -> None:
	"""Disable line aliasing"""
	...

def rl_enable_stereo_render() -> None:
	"""Enable stereo rendering"""
	...

def rl_disable_stereo_render() -> None:
	"""Disable stereo rendering"""
	...

def rl_is_stereo_render_enabled() -> ctypes.c_bool:
	"""Check if stereo render is enabled"""
	...

def rl_clear_color(r: ctypes.c_ubyte, g: ctypes.c_ubyte, b: ctypes.c_ubyte, a: ctypes.c_ubyte) -> None:
	"""Clear color buffer with color"""
	...

def rl_clear_screen_buffers() -> None:
	"""Clear used screen buffers (color and depth)"""
	...

def rl_check_errors() -> None:
	"""Check and log OpenGL error codes"""
	...

def rl_set_blend_mode(mode: ctypes.c_int) -> None:
	"""Set blending mode"""
	...

def rl_set_blend_factors(glSrcFactor: ctypes.c_int, glDstFactor: ctypes.c_int, glEquation: ctypes.c_int) -> None:
	"""Set blending mode factor and equation (using OpenGL factors)"""
	...

def rl_set_blend_factors_separate(glSrcRGB: ctypes.c_int, glDstRGB: ctypes.c_int, glSrcAlpha: ctypes.c_int, glDstAlpha: ctypes.c_int, glEqRGB: ctypes.c_int, glEqAlpha: ctypes.c_int) -> None:
	"""Set blending mode factors and equations separately (using OpenGL factors)"""
	...

def rlgl_init(width: ctypes.c_int, height: ctypes.c_int) -> None:
	"""Initialize rlgl (buffers, shaders, textures, states)"""
	...

def rlgl_close() -> None:
	"""De-initialize rlgl (buffers, shaders, textures)"""
	...

def rl_load_extensions(loader: ctypes.c_void_p) -> None:
	"""Load OpenGL extensions (loader function required)"""
	...

def rl_get_version() -> ctypes.c_int:
	"""Get current OpenGL version"""
	...

def rl_set_framebuffer_width(width: ctypes.c_int) -> None:
	"""Set current framebuffer width"""
	...

def rl_get_framebuffer_width() -> ctypes.c_int:
	"""Get default framebuffer width"""
	...

def rl_set_framebuffer_height(height: ctypes.c_int) -> None:
	"""Set current framebuffer height"""
	...

def rl_get_framebuffer_height() -> ctypes.c_int:
	"""Get default framebuffer height"""
	...

def rl_get_texture_id_default() -> ctypes.c_uint:
	"""Get default texture id"""
	...

def rl_get_shader_id_default() -> ctypes.c_uint:
	"""Get default shader id"""
	...

def rl_get_shader_locs_default() -> ctypes.POINTER(ctypes.c_int):
	"""Get default shader locations"""
	...

def rl_load_render_batch(numBuffers: ctypes.c_int, bufferElements: ctypes.c_int) -> rlRenderBatch:
	"""Load a render batch system"""
	...

def rl_unload_render_batch(batch: rlRenderBatch) -> None:
	"""Unload render batch system"""
	...

def rl_draw_render_batch(batch: ctypes.POINTER(rlRenderBatch)) -> None:
	"""Draw render batch data (Update->Draw->Reset)"""
	...

def rl_set_render_batch_active(batch: ctypes.POINTER(rlRenderBatch)) -> None:
	"""Set the active render batch for rlgl (NULL for default internal)"""
	...

def rl_draw_render_batch_active() -> None:
	"""Update and draw internal render batch"""
	...

def rl_check_render_batch_limit(vCount: ctypes.c_int) -> ctypes.c_bool:
	"""Check internal buffer overflow for a given number of vertex"""
	...

def rl_set_texture(id: ctypes.c_uint) -> None:
	"""Set current texture for render batch and check buffers limits"""
	...

def rl_load_vertex_array() -> ctypes.c_uint:
	"""Load vertex array (vao) if supported"""
	...

def rl_load_vertex_buffer(buffer: ctypes.c_void_p, size: ctypes.c_int, dynamic: ctypes.c_bool) -> ctypes.c_uint:
	"""Load a vertex buffer attribute"""
	...

def rl_load_vertex_buffer_element(buffer: ctypes.c_void_p, size: ctypes.c_int, dynamic: ctypes.c_bool) -> ctypes.c_uint:
	"""Load a new attributes element buffer"""
	...

def rl_update_vertex_buffer(bufferId: ctypes.c_uint, data: ctypes.c_void_p, dataSize: ctypes.c_int, offset: ctypes.c_int) -> None:
	"""Update GPU buffer with new data"""
	...

def rl_update_vertex_buffer_elements(id: ctypes.c_uint, data: ctypes.c_void_p, dataSize: ctypes.c_int, offset: ctypes.c_int) -> None:
	"""Update vertex buffer elements with new data"""
	...

def rl_unload_vertex_array(vaoId: ctypes.c_uint) -> None:
	""""""
	...

def rl_unload_vertex_buffer(vboId: ctypes.c_uint) -> None:
	""""""
	...

def rl_set_vertex_attribute(index: ctypes.c_uint, compSize: ctypes.c_int, type: ctypes.c_int, normalized: ctypes.c_bool, stride: ctypes.c_int, pointer: ctypes.c_void_p) -> None:
	""""""
	...

def rl_set_vertex_attribute_divisor(index: ctypes.c_uint, divisor: ctypes.c_int) -> None:
	""""""
	...

def rl_set_vertex_attribute_default(locIndex: ctypes.c_int, value: ctypes.c_void_p, attribType: ctypes.c_int, count: ctypes.c_int) -> None:
	"""Set vertex attribute default value"""
	...

def rl_draw_vertex_array(offset: ctypes.c_int, count: ctypes.c_int) -> None:
	""""""
	...

def rl_draw_vertex_array_elements(offset: ctypes.c_int, count: ctypes.c_int, buffer: ctypes.c_void_p) -> None:
	""""""
	...

def rl_draw_vertex_array_instanced(offset: ctypes.c_int, count: ctypes.c_int, instances: ctypes.c_int) -> None:
	""""""
	...

def rl_draw_vertex_array_elements_instanced(offset: ctypes.c_int, count: ctypes.c_int, buffer: ctypes.c_void_p, instances: ctypes.c_int) -> None:
	""""""
	...

def rl_load_texture(data: ctypes.c_void_p, width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int, mipmapCount: ctypes.c_int) -> ctypes.c_uint:
	"""Load texture in GPU"""
	...

def rl_load_texture_depth(width: ctypes.c_int, height: ctypes.c_int, useRenderBuffer: ctypes.c_bool) -> ctypes.c_uint:
	"""Load depth texture/renderbuffer (to be attached to fbo)"""
	...

def rl_load_texture_cubemap(data: ctypes.c_void_p, size: ctypes.c_int, format: ctypes.c_int) -> ctypes.c_uint:
	"""Load texture cubemap"""
	...

def rl_update_texture(id: ctypes.c_uint, offsetX: ctypes.c_int, offsetY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int, data: ctypes.c_void_p) -> None:
	"""Update GPU texture with new data"""
	...

def rl_get_gl_texture_formats(format: ctypes.c_int, glInternalFormat: ctypes.POINTER(ctypes.c_uint), glFormat: ctypes.POINTER(ctypes.c_uint), glType: ctypes.POINTER(ctypes.c_uint)) -> None:
	"""Get OpenGL internal formats"""
	...

def rl_get_pixel_format_name(format: ctypes.c_uint) -> ctypes.c_char_p:
	"""Get name string for pixel format"""
	...

def rl_unload_texture(id: ctypes.c_uint) -> None:
	"""Unload texture from GPU memory"""
	...

def rl_gen_texture_mipmaps(id: ctypes.c_uint, width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int, mipmaps: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Generate mipmap data for selected texture"""
	...

def rl_read_texture_pixels(id: ctypes.c_uint, width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int) -> ctypes.c_void_p:
	"""Read texture pixel data"""
	...

def rl_read_screen_pixels(width: ctypes.c_int, height: ctypes.c_int) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Read screen pixel data (color buffer)"""
	...

def rl_load_framebuffer(width: ctypes.c_int, height: ctypes.c_int) -> ctypes.c_uint:
	"""Load an empty framebuffer"""
	...

def rl_framebuffer_attach(fboId: ctypes.c_uint, texId: ctypes.c_uint, attachType: ctypes.c_int, texType: ctypes.c_int, mipLevel: ctypes.c_int) -> None:
	"""Attach texture/renderbuffer to a framebuffer"""
	...

def rl_framebuffer_complete(id: ctypes.c_uint) -> ctypes.c_bool:
	"""Verify framebuffer is complete"""
	...

def rl_unload_framebuffer(id: ctypes.c_uint) -> None:
	"""Delete framebuffer from GPU"""
	...

def rl_load_shader_code(vsCode: ctypes.c_char_p, fsCode: ctypes.c_char_p) -> ctypes.c_uint:
	"""Load shader from code strings"""
	...

def rl_compile_shader(shaderCode: ctypes.c_char_p, type: ctypes.c_int) -> ctypes.c_uint:
	"""Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)"""
	...

def rl_load_shader_program(vShaderId: ctypes.c_uint, fShaderId: ctypes.c_uint) -> ctypes.c_uint:
	"""Load custom shader program"""
	...

def rl_unload_shader_program(id: ctypes.c_uint) -> None:
	"""Unload shader program"""
	...

def rl_get_location_uniform(shaderId: ctypes.c_uint, uniformName: ctypes.c_char_p) -> ctypes.c_int:
	"""Get shader location uniform"""
	...

def rl_get_location_attrib(shaderId: ctypes.c_uint, attribName: ctypes.c_char_p) -> ctypes.c_int:
	"""Get shader location attribute"""
	...

def rl_set_uniform(locIndex: ctypes.c_int, value: ctypes.c_void_p, uniformType: ctypes.c_int, count: ctypes.c_int) -> None:
	"""Set shader value uniform"""
	...

def rl_set_uniform_matrix(locIndex: ctypes.c_int, mat: Matrix) -> None:
	"""Set shader value matrix"""
	...

def rl_set_uniform_sampler(locIndex: ctypes.c_int, textureId: ctypes.c_uint) -> None:
	"""Set shader value sampler"""
	...

def rl_set_shader(id: ctypes.c_uint, locs: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Set shader currently active (id and locations)"""
	...

def rl_load_compute_shader_program(shaderId: ctypes.c_uint) -> ctypes.c_uint:
	"""Load compute shader program"""
	...

def rl_compute_shader_dispatch(groupX: ctypes.c_uint, groupY: ctypes.c_uint, groupZ: ctypes.c_uint) -> None:
	"""Dispatch compute shader (equivalent to *draw* for graphics pipeline)"""
	...

def rl_load_shader_buffer(size: ctypes.c_uint, data: ctypes.c_void_p, usageHint: ctypes.c_int) -> ctypes.c_uint:
	"""Load shader storage buffer object (SSBO)"""
	...

def rl_unload_shader_buffer(ssboId: ctypes.c_uint) -> None:
	"""Unload shader storage buffer object (SSBO)"""
	...

def rl_update_shader_buffer(id: ctypes.c_uint, data: ctypes.c_void_p, dataSize: ctypes.c_uint, offset: ctypes.c_uint) -> None:
	"""Update SSBO buffer data"""
	...

def rl_bind_shader_buffer(id: ctypes.c_uint, index: ctypes.c_uint) -> None:
	"""Bind SSBO buffer"""
	...

def rl_read_shader_buffer(id: ctypes.c_uint, dest: ctypes.c_void_p, count: ctypes.c_uint, offset: ctypes.c_uint) -> None:
	"""Read SSBO buffer data (GPU->CPU)"""
	...

def rl_copy_shader_buffer(destId: ctypes.c_uint, srcId: ctypes.c_uint, destOffset: ctypes.c_uint, srcOffset: ctypes.c_uint, count: ctypes.c_uint) -> None:
	"""Copy SSBO data between buffers"""
	...

def rl_get_shader_buffer_size(id: ctypes.c_uint) -> ctypes.c_uint:
	"""Get SSBO buffer size"""
	...

def rl_bind_image_texture(id: ctypes.c_uint, index: ctypes.c_uint, format: ctypes.c_int, readonly: ctypes.c_bool) -> None:
	"""Bind image texture"""
	...

def rl_get_matrix_modelview() -> Matrix:
	"""Get internal modelview matrix"""
	...

def rl_get_matrix_projection() -> Matrix:
	"""Get internal projection matrix"""
	...

def rl_get_matrix_transform() -> Matrix:
	"""Get internal accumulated transform matrix"""
	...

def rl_get_matrix_projection_stereo(eye: ctypes.c_int) -> Matrix:
	"""Get internal projection matrix for stereo render (selected eye)"""
	...

def rl_get_matrix_view_offset_stereo(eye: ctypes.c_int) -> Matrix:
	"""Get internal view offset matrix for stereo render (selected eye)"""
	...

def rl_set_matrix_projection(proj: Matrix) -> None:
	"""Set a custom projection matrix (replaces internal projection matrix)"""
	...

def rl_set_matrix_modelview(view: Matrix) -> None:
	"""Set a custom modelview matrix (replaces internal modelview matrix)"""
	...

def rl_set_matrix_projection_stereo(right: Matrix, left: Matrix) -> None:
	"""Set eyes projection matrices for stereo rendering"""
	...

def rl_set_matrix_view_offset_stereo(right: Matrix, left: Matrix) -> None:
	"""Set eyes view offsets matrices for stereo rendering"""
	...

def rl_load_draw_cube() -> None:
	"""Load and draw a cube"""
	...

def rl_load_draw_quad() -> None:
	"""Load and draw a quad"""
	...

def init_window(width: ctypes.c_int, height: ctypes.c_int, title: ctypes.c_char_p) -> None:
	"""Initialize window and OpenGL context"""
	...

def window_should_close() -> ctypes.c_bool:
	"""Check if KEY_ESCAPE pressed or Close icon pressed"""
	...

def close_window() -> None:
	"""Close window and unload OpenGL context"""
	...

def is_window_ready() -> ctypes.c_bool:
	"""Check if window has been initialized successfully"""
	...

def is_window_fullscreen() -> ctypes.c_bool:
	"""Check if window is currently fullscreen"""
	...

def is_window_hidden() -> ctypes.c_bool:
	"""Check if window is currently hidden (only PLATFORM_DESKTOP)"""
	...

def is_window_minimized() -> ctypes.c_bool:
	"""Check if window is currently minimized (only PLATFORM_DESKTOP)"""
	...

def is_window_maximized() -> ctypes.c_bool:
	"""Check if window is currently maximized (only PLATFORM_DESKTOP)"""
	...

def is_window_focused() -> ctypes.c_bool:
	"""Check if window is currently focused (only PLATFORM_DESKTOP)"""
	...

def is_window_resized() -> ctypes.c_bool:
	"""Check if window has been resized last frame"""
	...

def is_window_state(flag: ctypes.c_uint) -> ctypes.c_bool:
	"""Check if one specific window flag is enabled"""
	...

def set_window_state(flags: ctypes.c_uint) -> None:
	"""Set window configuration state using flags (only PLATFORM_DESKTOP)"""
	...

def clear_window_state(flags: ctypes.c_uint) -> None:
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
	"""Set icon for window (single image, RGBA 32bit, only PLATFORM_DESKTOP)"""
	...

def set_window_icons(images: ctypes.POINTER(Image), count: ctypes.c_int) -> None:
	"""Set icon for window (multiple images, RGBA 32bit, only PLATFORM_DESKTOP)"""
	...

def set_window_title(title: ctypes.c_char_p) -> None:
	"""Set title for window (only PLATFORM_DESKTOP)"""
	...

def set_window_position(x: ctypes.c_int, y: ctypes.c_int) -> None:
	"""Set window position on screen (only PLATFORM_DESKTOP)"""
	...

def set_window_monitor(monitor: ctypes.c_int) -> None:
	"""Set monitor for the current window (fullscreen mode)"""
	...

def set_window_min_size(width: ctypes.c_int, height: ctypes.c_int) -> None:
	"""Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
	...

def set_window_size(width: ctypes.c_int, height: ctypes.c_int) -> None:
	"""Set window dimensions"""
	...

def set_window_opacity(opacity: ctypes.c_float) -> None:
	"""Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
	...

def get_window_handle() -> ctypes.c_void_p:
	"""Get native window handle"""
	...

def get_screen_width() -> ctypes.c_int:
	"""Get current screen width"""
	...

def get_screen_height() -> ctypes.c_int:
	"""Get current screen height"""
	...

def get_render_width() -> ctypes.c_int:
	"""Get current render width (it considers HiDPI)"""
	...

def get_render_height() -> ctypes.c_int:
	"""Get current render height (it considers HiDPI)"""
	...

def get_monitor_count() -> ctypes.c_int:
	"""Get number of connected monitors"""
	...

def get_current_monitor() -> ctypes.c_int:
	"""Get current connected monitor"""
	...

def get_monitor_position(monitor: ctypes.c_int) -> Vector2:
	"""Get specified monitor position"""
	...

def get_monitor_width(monitor: ctypes.c_int) -> ctypes.c_int:
	"""Get specified monitor width (current video mode used by monitor)"""
	...

def get_monitor_height(monitor: ctypes.c_int) -> ctypes.c_int:
	"""Get specified monitor height (current video mode used by monitor)"""
	...

def get_monitor_physical_width(monitor: ctypes.c_int) -> ctypes.c_int:
	"""Get specified monitor physical width in millimetres"""
	...

def get_monitor_physical_height(monitor: ctypes.c_int) -> ctypes.c_int:
	"""Get specified monitor physical height in millimetres"""
	...

def get_monitor_refresh_rate(monitor: ctypes.c_int) -> ctypes.c_int:
	"""Get specified monitor refresh rate"""
	...

def get_window_position() -> Vector2:
	"""Get window position XY on monitor"""
	...

def get_window_scale_dpi() -> Vector2:
	"""Get window scale DPI factor"""
	...

def get_monitor_name(monitor: ctypes.c_int) -> ctypes.c_char_p:
	"""Get the human-readable, UTF-8 encoded name of the primary monitor"""
	...

def set_clipboard_text(text: ctypes.c_char_p) -> None:
	"""Set clipboard text content"""
	...

def get_clipboard_text() -> ctypes.c_char_p:
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

def wait_time(seconds: ctypes.c_double) -> None:
	"""Wait for some time (halt program execution)"""
	...

def show_cursor() -> None:
	"""Shows cursor"""
	...

def hide_cursor() -> None:
	"""Hides cursor"""
	...

def is_cursor_hidden() -> ctypes.c_bool:
	"""Check if cursor is not visible"""
	...

def enable_cursor() -> None:
	"""Enables cursor (unlock cursor)"""
	...

def disable_cursor() -> None:
	"""Disables cursor (lock cursor)"""
	...

def is_cursor_on_screen() -> ctypes.c_bool:
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

def begin_blend_mode(mode: ctypes.c_int) -> None:
	"""Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
	...

def end_blend_mode() -> None:
	"""End blending mode (reset to default: alpha blending)"""
	...

def begin_scissor_mode(x: ctypes.c_int, y: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int) -> None:
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

def load_shader(vsFileName: ctypes.c_char_p, fsFileName: ctypes.c_char_p) -> Shader:
	"""Load shader from files and bind default locations"""
	...

def load_shader_from_memory(vsCode: ctypes.c_char_p, fsCode: ctypes.c_char_p) -> Shader:
	"""Load shader from code strings and bind default locations"""
	...

def is_shader_ready(shader: Shader) -> ctypes.c_bool:
	"""Check if a shader is ready"""
	...

def get_shader_location(shader: Shader, uniformName: ctypes.c_char_p) -> ctypes.c_int:
	"""Get shader uniform location"""
	...

def get_shader_location_attrib(shader: Shader, attribName: ctypes.c_char_p) -> ctypes.c_int:
	"""Get shader attribute location"""
	...

def set_shader_value(shader: Shader, locIndex: ctypes.c_int, value: ctypes.c_void_p, uniformType: ctypes.c_int) -> None:
	"""Set shader uniform value"""
	...

def set_shader_value_v(shader: Shader, locIndex: ctypes.c_int, value: ctypes.c_void_p, uniformType: ctypes.c_int, count: ctypes.c_int) -> None:
	"""Set shader uniform value vector"""
	...

def set_shader_value_matrix(shader: Shader, locIndex: ctypes.c_int, mat: Matrix) -> None:
	"""Set shader uniform value (matrix 4x4)"""
	...

def set_shader_value_texture(shader: Shader, locIndex: ctypes.c_int, texture: Texture2D) -> None:
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

def get_world_to_screen_ex(position: Vector3, camera: Camera, width: ctypes.c_int, height: ctypes.c_int) -> Vector2:
	"""Get size position for a 3d world space position"""
	...

def get_world_to_screen_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Get the screen space position for a 2d camera world space position"""
	...

def set_target_fps(fps: ctypes.c_int) -> None:
	"""Set target FPS (maximum)"""
	...

def get_fps() -> ctypes.c_int:
	"""Get current FPS"""
	...

def get_frame_time() -> ctypes.c_float:
	"""Get time in seconds for last frame drawn (delta time)"""
	...

def get_time() -> ctypes.c_double:
	"""Get elapsed time in seconds since InitWindow()"""
	...

def get_random_value(min: ctypes.c_int, max: ctypes.c_int) -> ctypes.c_int:
	"""Get a random value between min and max (both included)"""
	...

def set_random_seed(seed: ctypes.c_uint) -> None:
	"""Set the seed for the random number generator"""
	...

def take_screenshot(fileName: ctypes.c_char_p) -> None:
	"""Takes a screenshot of current screen (filename extension defines format)"""
	...

def set_config_flags(flags: ctypes.c_uint) -> None:
	"""Setup init configuration flags (view FLAGS)"""
	...

def trace_log(logLevel: ctypes.c_int, text: ctypes.c_char_p, args: ...) -> None:
	"""Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
	...

def set_trace_log_level(logLevel: ctypes.c_int) -> None:
	"""Set the current threshold (minimum) log level"""
	...

def mem_alloc(size: ctypes.c_uint) -> ctypes.c_void_p:
	"""Internal memory allocator"""
	...

def mem_realloc(ptr: ctypes.c_void_p, size: ctypes.c_uint) -> ctypes.c_void_p:
	"""Internal memory reallocator"""
	...

def mem_free(ptr: ctypes.c_void_p) -> None:
	"""Internal memory free"""
	...

def open_url(url: ctypes.c_char_p) -> None:
	"""Open URL with default system browser (if available)"""
	...

def load_file_data(fileName: ctypes.c_char_p, bytesRead: ctypes.POINTER(ctypes.c_uint)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Load file data as byte array (read)"""
	...

def unload_file_data(data: ctypes.POINTER(ctypes.c_ubyte)) -> None:
	"""Unload file data allocated by LoadFileData()"""
	...

def save_file_data(fileName: ctypes.c_char_p, data: ctypes.c_void_p, bytesToWrite: ctypes.c_uint) -> ctypes.c_bool:
	"""Save data to file from byte array (write), returns true on success"""
	...

def export_data_as_code(data: ctypes.POINTER(ctypes.c_ubyte), size: ctypes.c_uint, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export data to code (.h), returns true on success"""
	...

def load_file_text(fileName: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Load text data from file (read), returns a '\0' terminated string"""
	...

def unload_file_text(text: ctypes.c_char_p) -> None:
	"""Unload file text data allocated by LoadFileText()"""
	...

def save_file_text(fileName: ctypes.c_char_p, text: ctypes.c_char_p) -> ctypes.c_bool:
	"""Save text data to file (write), string must be '\0' terminated, returns true on success"""
	...

def file_exists(fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Check if file exists"""
	...

def directory_exists(dirPath: ctypes.c_char_p) -> ctypes.c_bool:
	"""Check if a directory path exists"""
	...

def is_file_extension(fileName: ctypes.c_char_p, ext: ctypes.c_char_p) -> ctypes.c_bool:
	"""Check file extension (including point: .png, .wav)"""
	...

def get_file_length(fileName: ctypes.c_char_p) -> ctypes.c_int:
	"""Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
	...

def get_file_extension(fileName: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get pointer to extension for a filename string (includes dot: '.png')"""
	...

def get_file_name(filePath: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get pointer to filename for a path string"""
	...

def get_file_name_without_ext(filePath: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get filename string without extension (uses static string)"""
	...

def get_directory_path(filePath: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get full path for a given fileName with path (uses static string)"""
	...

def get_prev_directory_path(dirPath: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get previous directory path for a given path (uses static string)"""
	...

def get_working_directory() -> ctypes.c_char_p:
	"""Get current working directory (uses static string)"""
	...

def get_application_directory() -> ctypes.c_char_p:
	"""Get the directory if the running application (uses static string)"""
	...

def change_directory(dir: ctypes.c_char_p) -> ctypes.c_bool:
	"""Change working directory, return true on success"""
	...

def is_path_file(path: ctypes.c_char_p) -> ctypes.c_bool:
	"""Check if a given path is a file or a directory"""
	...

def load_directory_files(dirPath: ctypes.c_char_p) -> FilePathList:
	"""Load directory filepaths"""
	...

def load_directory_files_ex(basePath: ctypes.c_char_p, filter: ctypes.c_char_p, scanSubdirs: ctypes.c_bool) -> FilePathList:
	"""Load directory filepaths with extension filtering and recursive directory scan"""
	...

def unload_directory_files(files: FilePathList) -> None:
	"""Unload filepaths"""
	...

def is_file_dropped() -> ctypes.c_bool:
	"""Check if a file has been dropped into window"""
	...

def load_dropped_files() -> FilePathList:
	"""Load dropped filepaths"""
	...

def unload_dropped_files(files: FilePathList) -> None:
	"""Unload dropped filepaths"""
	...

def get_file_mod_time(fileName: ctypes.c_char_p) -> ctypes.c_long:
	"""Get file modification time (last write time)"""
	...

def compress_data(data: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int, compDataSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Compress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def decompress_data(compData: ctypes.POINTER(ctypes.c_ubyte), compDataSize: ctypes.c_int, dataSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Decompress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def encode_data_base64(data: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int, outputSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_char_p:
	"""Encode data to Base64 string, memory must be MemFree()"""
	...

def decode_data_base64(data: ctypes.POINTER(ctypes.c_ubyte), outputSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Decode Base64 string data, memory must be MemFree()"""
	...

def is_key_pressed(key: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a key has been pressed once"""
	...

def is_key_down(key: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a key is being pressed"""
	...

def is_key_released(key: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a key has been released once"""
	...

def is_key_up(key: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a key is NOT being pressed"""
	...

def set_exit_key(key: ctypes.c_int) -> None:
	"""Set a custom key to exit program (default is ESC)"""
	...

def get_key_pressed() -> ctypes.c_int:
	"""Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
	...

def get_char_pressed() -> ctypes.c_int:
	"""Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
	...

def is_gamepad_available(gamepad: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gamepad is available"""
	...

def get_gamepad_name(gamepad: ctypes.c_int) -> ctypes.c_char_p:
	"""Get gamepad internal name id"""
	...

def is_gamepad_button_pressed(gamepad: ctypes.c_int, button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gamepad button has been pressed once"""
	...

def is_gamepad_button_down(gamepad: ctypes.c_int, button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gamepad button is being pressed"""
	...

def is_gamepad_button_released(gamepad: ctypes.c_int, button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gamepad button has been released once"""
	...

def is_gamepad_button_up(gamepad: ctypes.c_int, button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gamepad button is NOT being pressed"""
	...

def get_gamepad_button_pressed() -> ctypes.c_int:
	"""Get the last gamepad button pressed"""
	...

def get_gamepad_axis_count(gamepad: ctypes.c_int) -> ctypes.c_int:
	"""Get gamepad axis count for a gamepad"""
	...

def get_gamepad_axis_movement(gamepad: ctypes.c_int, axis: ctypes.c_int) -> ctypes.c_float:
	"""Get axis movement value for a gamepad axis"""
	...

def set_gamepad_mappings(mappings: ctypes.c_char_p) -> ctypes.c_int:
	"""Set internal gamepad mappings (SDL_GameControllerDB)"""
	...

def is_mouse_button_pressed(button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a mouse button has been pressed once"""
	...

def is_mouse_button_down(button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a mouse button is being pressed"""
	...

def is_mouse_button_released(button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a mouse button has been released once"""
	...

def is_mouse_button_up(button: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a mouse button is NOT being pressed"""
	...

def get_mouse_x() -> ctypes.c_int:
	"""Get mouse position X"""
	...

def get_mouse_y() -> ctypes.c_int:
	"""Get mouse position Y"""
	...

def get_mouse_position() -> Vector2:
	"""Get mouse position XY"""
	...

def get_mouse_delta() -> Vector2:
	"""Get mouse delta between frames"""
	...

def set_mouse_position(x: ctypes.c_int, y: ctypes.c_int) -> None:
	"""Set mouse position XY"""
	...

def set_mouse_offset(offsetX: ctypes.c_int, offsetY: ctypes.c_int) -> None:
	"""Set mouse offset"""
	...

def set_mouse_scale(scaleX: ctypes.c_float, scaleY: ctypes.c_float) -> None:
	"""Set mouse scaling"""
	...

def get_mouse_wheel_move() -> ctypes.c_float:
	"""Get mouse wheel movement for X or Y, whichever is larger"""
	...

def get_mouse_wheel_move_v() -> Vector2:
	"""Get mouse wheel movement for both X and Y"""
	...

def set_mouse_cursor(cursor: ctypes.c_int) -> None:
	"""Set mouse cursor"""
	...

def get_touch_x() -> ctypes.c_int:
	"""Get touch position X for touch point 0 (relative to screen size)"""
	...

def get_touch_y() -> ctypes.c_int:
	"""Get touch position Y for touch point 0 (relative to screen size)"""
	...

def get_touch_position(index: ctypes.c_int) -> Vector2:
	"""Get touch position XY for a touch point index (relative to screen size)"""
	...

def get_touch_point_id(index: ctypes.c_int) -> ctypes.c_int:
	"""Get touch point identifier for given index"""
	...

def get_touch_point_count() -> ctypes.c_int:
	"""Get number of touch points"""
	...

def set_gestures_enabled(flags: ctypes.c_uint) -> None:
	"""Enable a set of gestures using flags"""
	...

def is_gesture_detected(gesture: ctypes.c_int) -> ctypes.c_bool:
	"""Check if a gesture have been detected"""
	...

def get_gesture_detected() -> ctypes.c_int:
	"""Get latest detected gesture"""
	...

def get_gesture_hold_duration() -> ctypes.c_float:
	"""Get gesture hold time in milliseconds"""
	...

def get_gesture_drag_vector() -> Vector2:
	"""Get gesture drag vector"""
	...

def get_gesture_drag_angle() -> ctypes.c_float:
	"""Get gesture drag angle"""
	...

def get_gesture_pinch_vector() -> Vector2:
	"""Get gesture pinch delta"""
	...

def get_gesture_pinch_angle() -> ctypes.c_float:
	"""Get gesture pinch angle"""
	...

def update_camera(camera: ctypes.POINTER(Camera), mode: ctypes.c_int) -> None:
	"""Update camera position for selected mode"""
	...

def update_camera_pro(camera: ctypes.POINTER(Camera), movement: Vector3, rotation: Vector3, zoom: ctypes.c_float) -> None:
	"""Update camera movement/rotation"""
	...

def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None:
	"""Set texture and rectangle to be used on shapes drawing"""
	...

def draw_pixel(posX: ctypes.c_int, posY: ctypes.c_int, color: Color) -> None:
	"""Draw a pixel"""
	...

def draw_pixel_v(position: Vector2, color: Color) -> None:
	"""Draw a pixel (Vector version)"""
	...

def draw_line(startPosX: ctypes.c_int, startPosY: ctypes.c_int, endPosX: ctypes.c_int, endPosY: ctypes.c_int, color: Color) -> None:
	"""Draw a line"""
	...

def draw_line_v(startPos: Vector2, endPos: Vector2, color: Color) -> None:
	"""Draw a line (Vector version)"""
	...

def draw_line_ex(startPos: Vector2, endPos: Vector2, thick: ctypes.c_float, color: Color) -> None:
	"""Draw a line defining thickness"""
	...

def draw_line_bezier(startPos: Vector2, endPos: Vector2, thick: ctypes.c_float, color: Color) -> None:
	"""Draw a line using cubic-bezier curves in-out"""
	...

def draw_line_bezier_quad(startPos: Vector2, endPos: Vector2, controlPos: Vector2, thick: ctypes.c_float, color: Color) -> None:
	"""Draw line using quadratic bezier curves with a control point"""
	...

def draw_line_bezier_cubic(startPos: Vector2, endPos: Vector2, startControlPos: Vector2, endControlPos: Vector2, thick: ctypes.c_float, color: Color) -> None:
	"""Draw line using cubic bezier curves with 2 control points"""
	...

def draw_line_strip(points: ctypes.POINTER(Vector2), pointCount: ctypes.c_int, color: Color) -> None:
	"""Draw lines sequence"""
	...

def draw_circle(centerX: ctypes.c_int, centerY: ctypes.c_int, radius: ctypes.c_float, color: Color) -> None:
	"""Draw a color-filled circle"""
	...

def draw_circle_sector(center: Vector2, radius: ctypes.c_float, startAngle: ctypes.c_float, endAngle: ctypes.c_float, segments: ctypes.c_int, color: Color) -> None:
	"""Draw a piece of a circle"""
	...

def draw_circle_sector_lines(center: Vector2, radius: ctypes.c_float, startAngle: ctypes.c_float, endAngle: ctypes.c_float, segments: ctypes.c_int, color: Color) -> None:
	"""Draw circle sector outline"""
	...

def draw_circle_gradient(centerX: ctypes.c_int, centerY: ctypes.c_int, radius: ctypes.c_float, color1: Color, color2: Color) -> None:
	"""Draw a gradient-filled circle"""
	...

def draw_circle_v(center: Vector2, radius: ctypes.c_float, color: Color) -> None:
	"""Draw a color-filled circle (Vector version)"""
	...

def draw_circle_lines(centerX: ctypes.c_int, centerY: ctypes.c_int, radius: ctypes.c_float, color: Color) -> None:
	"""Draw circle outline"""
	...

def draw_ellipse(centerX: ctypes.c_int, centerY: ctypes.c_int, radiusH: ctypes.c_float, radiusV: ctypes.c_float, color: Color) -> None:
	"""Draw ellipse"""
	...

def draw_ellipse_lines(centerX: ctypes.c_int, centerY: ctypes.c_int, radiusH: ctypes.c_float, radiusV: ctypes.c_float, color: Color) -> None:
	"""Draw ellipse outline"""
	...

def draw_ring(center: Vector2, innerRadius: ctypes.c_float, outerRadius: ctypes.c_float, startAngle: ctypes.c_float, endAngle: ctypes.c_float, segments: ctypes.c_int, color: Color) -> None:
	"""Draw ring"""
	...

def draw_ring_lines(center: Vector2, innerRadius: ctypes.c_float, outerRadius: ctypes.c_float, startAngle: ctypes.c_float, endAngle: ctypes.c_float, segments: ctypes.c_int, color: Color) -> None:
	"""Draw ring outline"""
	...

def draw_rectangle(posX: ctypes.c_int, posY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw a color-filled rectangle (Vector version)"""
	...

def draw_rectangle_rec(rec: Rectangle, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: ctypes.c_float, color: Color) -> None:
	"""Draw a color-filled rectangle with pro parameters"""
	...

def draw_rectangle_gradient_v(posX: ctypes.c_int, posY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, color1: Color, color2: Color) -> None:
	"""Draw a vertical-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_h(posX: ctypes.c_int, posY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, color1: Color, color2: Color) -> None:
	"""Draw a horizontal-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
	"""Draw a gradient-filled rectangle with custom vertex colors"""
	...

def draw_rectangle_lines(posX: ctypes.c_int, posY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, color: Color) -> None:
	"""Draw rectangle outline"""
	...

def draw_rectangle_lines_ex(rec: Rectangle, lineThick: ctypes.c_float, color: Color) -> None:
	"""Draw rectangle outline with extended parameters"""
	...

def draw_rectangle_rounded(rec: Rectangle, roundness: ctypes.c_float, segments: ctypes.c_int, color: Color) -> None:
	"""Draw rectangle with rounded edges"""
	...

def draw_rectangle_rounded_lines(rec: Rectangle, roundness: ctypes.c_float, segments: ctypes.c_int, lineThick: ctypes.c_float, color: Color) -> None:
	"""Draw rectangle with rounded edges outline"""
	...

def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw triangle outline (vertex in counter-clockwise order!)"""
	...

def draw_triangle_fan(points: ctypes.POINTER(Vector2), pointCount: ctypes.c_int, color: Color) -> None:
	"""Draw a triangle fan defined by points (first vertex is the center)"""
	...

def draw_triangle_strip(points: ctypes.POINTER(Vector2), pointCount: ctypes.c_int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_poly(center: Vector2, sides: ctypes.c_int, radius: ctypes.c_float, rotation: ctypes.c_float, color: Color) -> None:
	"""Draw a regular polygon (Vector version)"""
	...

def draw_poly_lines(center: Vector2, sides: ctypes.c_int, radius: ctypes.c_float, rotation: ctypes.c_float, color: Color) -> None:
	"""Draw a polygon outline of n sides"""
	...

def draw_poly_lines_ex(center: Vector2, sides: ctypes.c_int, radius: ctypes.c_float, rotation: ctypes.c_float, lineThick: ctypes.c_float, color: Color) -> None:
	"""Draw a polygon outline of n sides with extended parameters"""
	...

def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> ctypes.c_bool:
	"""Check collision between two rectangles"""
	...

def check_collision_circles(center1: Vector2, radius1: ctypes.c_float, center2: Vector2, radius2: ctypes.c_float) -> ctypes.c_bool:
	"""Check collision between two circles"""
	...

def check_collision_circle_rec(center: Vector2, radius: ctypes.c_float, rec: Rectangle) -> ctypes.c_bool:
	"""Check collision between circle and rectangle"""
	...

def check_collision_point_rec(point: Vector2, rec: Rectangle) -> ctypes.c_bool:
	"""Check if point is inside rectangle"""
	...

def check_collision_point_circle(point: Vector2, center: Vector2, radius: ctypes.c_float) -> ctypes.c_bool:
	"""Check if point is inside circle"""
	...

def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> ctypes.c_bool:
	"""Check if point is inside a triangle"""
	...

def check_collision_point_poly(point: Vector2, points: ctypes.POINTER(Vector2), pointCount: ctypes.c_int) -> ctypes.c_bool:
	"""Check if point is within a polygon described by array of vertices"""
	...

def check_collision_lines(startPos1: Vector2, endPos1: Vector2, startPos2: Vector2, endPos2: Vector2, collisionPoint: ctypes.POINTER(Vector2)) -> ctypes.c_bool:
	"""Check the collision between two lines defined by two points each, returns collision point by reference"""
	...

def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: ctypes.c_int) -> ctypes.c_bool:
	"""Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
	...

def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle:
	"""Get collision rectangle for two rectangles collision"""
	...

def load_image(fileName: ctypes.c_char_p) -> Image:
	"""Load image from file into CPU memory (RAM)"""
	...

def load_image_raw(fileName: ctypes.c_char_p, width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int, headerSize: ctypes.c_int) -> Image:
	"""Load image from RAW file data"""
	...

def load_image_anim(fileName: ctypes.c_char_p, frames: ctypes.POINTER(ctypes.c_int)) -> Image:
	"""Load image sequence from file (frames appended to image.data)"""
	...

def load_image_from_memory(fileType: ctypes.c_char_p, fileData: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int) -> Image:
	"""Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
	...

def load_image_from_texture(texture: Texture2D) -> Image:
	"""Load image from GPU texture data"""
	...

def load_image_from_screen() -> Image:
	"""Load image from screen buffer and (screenshot)"""
	...

def is_image_ready(image: Image) -> ctypes.c_bool:
	"""Check if an image is ready"""
	...

def unload_image(image: Image) -> None:
	"""Unload image from CPU memory (RAM)"""
	...

def export_image(image: Image, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export image data to file, returns true on success"""
	...

def export_image_as_code(image: Image, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export image as code file defining an array of bytes, returns true on success"""
	...

def gen_image_color(width: ctypes.c_int, height: ctypes.c_int, color: Color) -> Image:
	"""Generate image: plain color"""
	...

def gen_image_gradient_v(width: ctypes.c_int, height: ctypes.c_int, top: Color, bottom: Color) -> Image:
	"""Generate image: vertical gradient"""
	...

def gen_image_gradient_h(width: ctypes.c_int, height: ctypes.c_int, left: Color, right: Color) -> Image:
	"""Generate image: horizontal gradient"""
	...

def gen_image_gradient_radial(width: ctypes.c_int, height: ctypes.c_int, density: ctypes.c_float, inner: Color, outer: Color) -> Image:
	"""Generate image: radial gradient"""
	...

def gen_image_checked(width: ctypes.c_int, height: ctypes.c_int, checksX: ctypes.c_int, checksY: ctypes.c_int, col1: Color, col2: Color) -> Image:
	"""Generate image: checked"""
	...

def gen_image_white_noise(width: ctypes.c_int, height: ctypes.c_int, factor: ctypes.c_float) -> Image:
	"""Generate image: white noise"""
	...

def gen_image_perlin_noise(width: ctypes.c_int, height: ctypes.c_int, offsetX: ctypes.c_int, offsetY: ctypes.c_int, scale: ctypes.c_float) -> Image:
	"""Generate image: perlin noise"""
	...

def gen_image_cellular(width: ctypes.c_int, height: ctypes.c_int, tileSize: ctypes.c_int) -> Image:
	"""Generate image: cellular algorithm, bigger tileSize means bigger cells"""
	...

def gen_image_text(width: ctypes.c_int, height: ctypes.c_int, text: ctypes.c_char_p) -> Image:
	"""Generate image: grayscale image from text data"""
	...

def image_copy(image: Image) -> Image:
	"""Create an image duplicate (useful for transformations)"""
	...

def image_from_image(image: Image, rec: Rectangle) -> Image:
	"""Create an image from another image piece"""
	...

def image_text(text: ctypes.c_char_p, fontSize: ctypes.c_int, color: Color) -> Image:
	"""Create an image from text (default font)"""
	...

def image_text_ex(font: Font, text: ctypes.c_char_p, fontSize: ctypes.c_float, spacing: ctypes.c_float, tint: Color) -> Image:
	"""Create an image from text (custom sprite font)"""
	...

def image_format(image: ctypes.POINTER(Image), newFormat: ctypes.c_int) -> None:
	"""Convert image data to desired format"""
	...

def image_to_pot(image: ctypes.POINTER(Image), fill: Color) -> None:
	"""Convert image to POT (power-of-two)"""
	...

def image_crop(image: ctypes.POINTER(Image), crop: Rectangle) -> None:
	"""Crop an image to a defined rectangle"""
	...

def image_alpha_crop(image: ctypes.POINTER(Image), threshold: ctypes.c_float) -> None:
	"""Crop image depending on alpha value"""
	...

def image_alpha_clear(image: ctypes.POINTER(Image), color: Color, threshold: ctypes.c_float) -> None:
	"""Clear alpha channel to desired color"""
	...

def image_alpha_mask(image: ctypes.POINTER(Image), alphaMask: Image) -> None:
	"""Apply alpha mask to image"""
	...

def image_alpha_premultiply(image: ctypes.POINTER(Image)) -> None:
	"""Premultiply alpha channel"""
	...

def image_blur_gaussian(image: ctypes.POINTER(Image), blurSize: ctypes.c_int) -> None:
	"""Apply Gaussian blur using a box blur approximation"""
	...

def image_resize(image: ctypes.POINTER(Image), newWidth: ctypes.c_int, newHeight: ctypes.c_int) -> None:
	"""Resize image (Bicubic scaling algorithm)"""
	...

def image_resize_nn(image: ctypes.POINTER(Image), newWidth: ctypes.c_int, newHeight: ctypes.c_int) -> None:
	"""Resize image (Nearest-Neighbor scaling algorithm)"""
	...

def image_resize_canvas(image: ctypes.POINTER(Image), newWidth: ctypes.c_int, newHeight: ctypes.c_int, offsetX: ctypes.c_int, offsetY: ctypes.c_int, fill: Color) -> None:
	"""Resize canvas and fill with color"""
	...

def image_mipmaps(image: ctypes.POINTER(Image)) -> None:
	"""Compute all mipmap levels for a provided image"""
	...

def image_dither(image: ctypes.POINTER(Image), rBpp: ctypes.c_int, gBpp: ctypes.c_int, bBpp: ctypes.c_int, aBpp: ctypes.c_int) -> None:
	"""Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
	...

def image_flip_vertical(image: ctypes.POINTER(Image)) -> None:
	"""Flip image vertically"""
	...

def image_flip_horizontal(image: ctypes.POINTER(Image)) -> None:
	"""Flip image horizontally"""
	...

def image_rotate_cw(image: ctypes.POINTER(Image)) -> None:
	"""Rotate image clockwise 90deg"""
	...

def image_rotate_ccw(image: ctypes.POINTER(Image)) -> None:
	"""Rotate image counter-clockwise 90deg"""
	...

def image_color_tint(image: ctypes.POINTER(Image), color: Color) -> None:
	"""Modify image color: tint"""
	...

def image_color_invert(image: ctypes.POINTER(Image)) -> None:
	"""Modify image color: invert"""
	...

def image_color_grayscale(image: ctypes.POINTER(Image)) -> None:
	"""Modify image color: grayscale"""
	...

def image_color_contrast(image: ctypes.POINTER(Image), contrast: ctypes.c_float) -> None:
	"""Modify image color: contrast (-100 to 100)"""
	...

def image_color_brightness(image: ctypes.POINTER(Image), brightness: ctypes.c_int) -> None:
	"""Modify image color: brightness (-255 to 255)"""
	...

def image_color_replace(image: ctypes.POINTER(Image), color: Color, replace: Color) -> None:
	"""Modify image color: replace color"""
	...

def load_image_colors(image: Image) -> ctypes.POINTER(Color):
	"""Load color data from image as a Color array (RGBA - 32bit)"""
	...

def load_image_palette(image: Image, maxPaletteSize: ctypes.c_int, colorCount: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(Color):
	"""Load colors palette from image as a Color array (RGBA - 32bit)"""
	...

def unload_image_colors(colors: ctypes.POINTER(Color)) -> None:
	"""Unload color data loaded with LoadImageColors()"""
	...

def unload_image_palette(colors: ctypes.POINTER(Color)) -> None:
	"""Unload colors palette loaded with LoadImagePalette()"""
	...

def get_image_alpha_border(image: Image, threshold: ctypes.c_float) -> Rectangle:
	"""Get image alpha border rectangle"""
	...

def get_image_color(image: Image, x: ctypes.c_int, y: ctypes.c_int) -> Color:
	"""Get image pixel color at (x, y) position"""
	...

def image_clear_background(dst: ctypes.POINTER(Image), color: Color) -> None:
	"""Clear image background with given color"""
	...

def image_draw_pixel(dst: ctypes.POINTER(Image), posX: ctypes.c_int, posY: ctypes.c_int, color: Color) -> None:
	"""Draw pixel within an image"""
	...

def image_draw_pixel_v(dst: ctypes.POINTER(Image), position: Vector2, color: Color) -> None:
	"""Draw pixel within an image (Vector version)"""
	...

def image_draw_line(dst: ctypes.POINTER(Image), startPosX: ctypes.c_int, startPosY: ctypes.c_int, endPosX: ctypes.c_int, endPosY: ctypes.c_int, color: Color) -> None:
	"""Draw line within an image"""
	...

def image_draw_line_v(dst: ctypes.POINTER(Image), start: Vector2, end: Vector2, color: Color) -> None:
	"""Draw line within an image (Vector version)"""
	...

def image_draw_circle(dst: ctypes.POINTER(Image), centerX: ctypes.c_int, centerY: ctypes.c_int, radius: ctypes.c_int, color: Color) -> None:
	"""Draw a filled circle within an image"""
	...

def image_draw_circle_v(dst: ctypes.POINTER(Image), center: Vector2, radius: ctypes.c_int, color: Color) -> None:
	"""Draw a filled circle within an image (Vector version)"""
	...

def image_draw_circle_lines(dst: ctypes.POINTER(Image), centerX: ctypes.c_int, centerY: ctypes.c_int, radius: ctypes.c_int, color: Color) -> None:
	"""Draw circle outline within an image"""
	...

def image_draw_circle_lines_v(dst: ctypes.POINTER(Image), center: Vector2, radius: ctypes.c_int, color: Color) -> None:
	"""Draw circle outline within an image (Vector version)"""
	...

def image_draw_rectangle(dst: ctypes.POINTER(Image), posX: ctypes.c_int, posY: ctypes.c_int, width: ctypes.c_int, height: ctypes.c_int, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_v(dst: ctypes.POINTER(Image), position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw rectangle within an image (Vector version)"""
	...

def image_draw_rectangle_rec(dst: ctypes.POINTER(Image), rec: Rectangle, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_lines(dst: ctypes.POINTER(Image), rec: Rectangle, thick: ctypes.c_int, color: Color) -> None:
	"""Draw rectangle lines within an image"""
	...

def image_draw(dst: ctypes.POINTER(Image), src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None:
	"""Draw a source image within a destination image (tint applied to source)"""
	...

def image_draw_text(dst: ctypes.POINTER(Image), text: ctypes.c_char_p, posX: ctypes.c_int, posY: ctypes.c_int, fontSize: ctypes.c_int, color: Color) -> None:
	"""Draw text (using default font) within an image (destination)"""
	...

def image_draw_text_ex(dst: ctypes.POINTER(Image), font: Font, text: ctypes.c_char_p, position: Vector2, fontSize: ctypes.c_float, spacing: ctypes.c_float, tint: Color) -> None:
	"""Draw text (custom sprite font) within an image (destination)"""
	...

def load_texture(fileName: ctypes.c_char_p) -> Texture2D:
	"""Load texture from file into GPU memory (VRAM)"""
	...

def load_texture_from_image(image: Image) -> Texture2D:
	"""Load texture from image data"""
	...

def load_texture_cubemap(image: Image, layout: ctypes.c_int) -> TextureCubemap:
	"""Load cubemap from image, multiple image cubemap layouts supported"""
	...

def load_render_texture(width: ctypes.c_int, height: ctypes.c_int) -> RenderTexture2D:
	"""Load texture for rendering (framebuffer)"""
	...

def is_texture_ready(texture: Texture2D) -> ctypes.c_bool:
	"""Check if a texture is ready"""
	...

def unload_texture(texture: Texture2D) -> None:
	"""Unload texture from GPU memory (VRAM)"""
	...

def is_render_texture_ready(target: RenderTexture2D) -> ctypes.c_bool:
	"""Check if a render texture is ready"""
	...

def unload_render_texture(target: RenderTexture2D) -> None:
	"""Unload render texture from GPU memory (VRAM)"""
	...

def update_texture(texture: Texture2D, pixels: ctypes.c_void_p) -> None:
	"""Update GPU texture with new data"""
	...

def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: ctypes.c_void_p) -> None:
	"""Update GPU texture rectangle with new data"""
	...

def gen_texture_mipmaps(texture: ctypes.POINTER(Texture2D)) -> None:
	"""Generate GPU mipmaps for a texture"""
	...

def set_texture_filter(texture: Texture2D, filter: ctypes.c_int) -> None:
	"""Set texture scaling filter mode"""
	...

def set_texture_wrap(texture: Texture2D, wrap: ctypes.c_int) -> None:
	"""Set texture wrapping mode"""
	...

def draw_texture(texture: Texture2D, posX: ctypes.c_int, posY: ctypes.c_int, tint: Color) -> None:
	"""Draw a Texture2D"""
	...

def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None:
	"""Draw a Texture2D with position defined as Vector2"""
	...

def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: ctypes.c_float, scale: ctypes.c_float, tint: Color) -> None:
	"""Draw a Texture2D with extended parameters"""
	...

def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle"""
	...

def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: ctypes.c_float, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle with 'pro' parameters"""
	...

def draw_texture_n_patch(texture: Texture2D, nPatchInfo: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: ctypes.c_float, tint: Color) -> None:
	"""Draws a texture (or part of it) that stretches or shrinks nicely"""
	...

def fade(color: Color, alpha: ctypes.c_float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_to_int(color: Color) -> ctypes.c_int:
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

def color_from_hsv(hue: ctypes.c_float, saturation: ctypes.c_float, value: ctypes.c_float) -> Color:
	"""Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
	...

def color_tint(color: Color, tint: Color) -> Color:
	"""Get color multiplied with another color"""
	...

def color_brightness(color: Color, factor: ctypes.c_float) -> Color:
	"""Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
	...

def color_contrast(color: Color, contrast: ctypes.c_float) -> Color:
	"""Get color with contrast correction, contrast values between -1.0f and 1.0f"""
	...

def color_alpha(color: Color, alpha: ctypes.c_float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color:
	"""Get src alpha-blended into dst color with tint"""
	...

def get_color(hexValue: ctypes.c_uint) -> Color:
	"""Get Color structure from hexadecimal value"""
	...

def get_pixel_color(srcPtr: ctypes.c_void_p, format: ctypes.c_int) -> Color:
	"""Get Color from a source pixel pointer of certain format"""
	...

def set_pixel_color(dstPtr: ctypes.c_void_p, color: Color, format: ctypes.c_int) -> None:
	"""Set color formatted into destination pixel pointer"""
	...

def get_pixel_data_size(width: ctypes.c_int, height: ctypes.c_int, format: ctypes.c_int) -> ctypes.c_int:
	"""Get pixel data size in bytes for certain format"""
	...

def get_font_default() -> Font:
	"""Get the default Font"""
	...

def load_font(fileName: ctypes.c_char_p) -> Font:
	"""Load font from file into GPU memory (VRAM)"""
	...

def load_font_ex(fileName: ctypes.c_char_p, fontSize: ctypes.c_int, fontChars: ctypes.POINTER(ctypes.c_int), glyphCount: ctypes.c_int) -> Font:
	"""Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set"""
	...

def load_font_from_image(image: Image, key: Color, firstChar: ctypes.c_int) -> Font:
	"""Load font from Image (XNA style)"""
	...

def load_font_from_memory(fileType: ctypes.c_char_p, fileData: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int, fontSize: ctypes.c_int, fontChars: ctypes.POINTER(ctypes.c_int), glyphCount: ctypes.c_int) -> Font:
	"""Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
	...

def is_font_ready(font: Font) -> ctypes.c_bool:
	"""Check if a font is ready"""
	...

def load_font_data(fileData: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int, fontSize: ctypes.c_int, fontChars: ctypes.POINTER(ctypes.c_int), glyphCount: ctypes.c_int, type: ctypes.c_int) -> ctypes.POINTER(GlyphInfo):
	"""Load font data for further use"""
	...

def gen_image_font_atlas(chars: ctypes.POINTER(GlyphInfo), recs: ctypes.POINTER(ctypes.POINTER(Rectangle)), glyphCount: ctypes.c_int, fontSize: ctypes.c_int, padding: ctypes.c_int, packMethod: ctypes.c_int) -> Image:
	"""Generate image font atlas using chars info"""
	...

def unload_font_data(chars: ctypes.POINTER(GlyphInfo), glyphCount: ctypes.c_int) -> None:
	"""Unload font chars info data (RAM)"""
	...

def unload_font(font: Font) -> None:
	"""Unload font from GPU memory (VRAM)"""
	...

def export_font_as_code(font: Font, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export font as code file, returns true on success"""
	...

def draw_fps(posX: ctypes.c_int, posY: ctypes.c_int) -> None:
	"""Draw current FPS"""
	...

def draw_text(text: ctypes.c_char_p, posX: ctypes.c_int, posY: ctypes.c_int, fontSize: ctypes.c_int, color: Color) -> None:
	"""Draw text (using default font)"""
	...

def draw_text_ex(font: Font, text: ctypes.c_char_p, position: Vector2, fontSize: ctypes.c_float, spacing: ctypes.c_float, tint: Color) -> None:
	"""Draw text using font and additional parameters"""
	...

def draw_text_pro(font: Font, text: ctypes.c_char_p, position: Vector2, origin: Vector2, rotation: ctypes.c_float, fontSize: ctypes.c_float, spacing: ctypes.c_float, tint: Color) -> None:
	"""Draw text using Font and pro parameters (rotation)"""
	...

def draw_text_codepoint(font: Font, codepoint: ctypes.c_int, position: Vector2, fontSize: ctypes.c_float, tint: Color) -> None:
	"""Draw one character (codepoint)"""
	...

def draw_text_codepoints(font: Font, codepoints: ctypes.POINTER(ctypes.c_int), count: ctypes.c_int, position: Vector2, fontSize: ctypes.c_float, spacing: ctypes.c_float, tint: Color) -> None:
	"""Draw multiple character (codepoint)"""
	...

def measure_text(text: ctypes.c_char_p, fontSize: ctypes.c_int) -> ctypes.c_int:
	"""Measure string width for default font"""
	...

def measure_text_ex(font: Font, text: ctypes.c_char_p, fontSize: ctypes.c_float, spacing: ctypes.c_float) -> Vector2:
	"""Measure string size for Font"""
	...

def get_glyph_index(font: Font, codepoint: ctypes.c_int) -> ctypes.c_int:
	"""Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_info(font: Font, codepoint: ctypes.c_int) -> GlyphInfo:
	"""Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_atlas_rec(font: Font, codepoint: ctypes.c_int) -> Rectangle:
	"""Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
	...

def load_utf8(codepoints: ctypes.POINTER(ctypes.c_int), length: ctypes.c_int) -> ctypes.c_char_p:
	"""Load UTF-8 text encoded from codepoints array"""
	...

def unload_utf8(text: ctypes.c_char_p) -> None:
	"""Unload UTF-8 text encoded from codepoints array"""
	...

def load_codepoints(text: ctypes.c_char_p, count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_int):
	"""Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
	...

def unload_codepoints(codepoints: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Unload codepoints data from memory"""
	...

def get_codepoint_count(text: ctypes.c_char_p) -> ctypes.c_int:
	"""Get total number of codepoints in a UTF-8 encoded string"""
	...

def get_codepoint(text: ctypes.c_char_p, codepointSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int:
	"""Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def get_codepoint_next(text: ctypes.c_char_p, codepointSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int:
	"""Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def get_codepoint_previous(text: ctypes.c_char_p, codepointSize: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int:
	"""Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def codepoint_to_utf8(codepoint: ctypes.c_int, utf8Size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_char_p:
	"""Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
	...

def text_copy(dst: ctypes.c_char_p, src: ctypes.c_char_p) -> ctypes.c_int:
	"""Copy one string to another, returns bytes copied"""
	...

def text_is_equal(text1: ctypes.c_char_p, text2: ctypes.c_char_p) -> ctypes.c_bool:
	"""Check if two text string are equal"""
	...

def text_length(text: ctypes.c_char_p) -> ctypes.c_uint:
	"""Get text length, checks for '\0' ending"""
	...

def text_format(text: ctypes.c_char_p, args: ...) -> ctypes.c_char_p:
	"""Text formatting with variables (sprintf() style)"""
	...

def text_subtext(text: ctypes.c_char_p, position: ctypes.c_int, length: ctypes.c_int) -> ctypes.c_char_p:
	"""Get a piece of a text string"""
	...

def text_replace(text: ctypes.c_char_p, replace: ctypes.c_char_p, by: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Replace text string (WARNING: memory must be freed!)"""
	...

def text_insert(text: ctypes.c_char_p, insert: ctypes.c_char_p, position: ctypes.c_int) -> ctypes.c_char_p:
	"""Insert text in a position (WARNING: memory must be freed!)"""
	...

def text_join(textList: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int, delimiter: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Join text strings with delimiter"""
	...

def text_split(text: ctypes.c_char_p, delimiter: ctypes.c_char, count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.POINTER(ctypes.c_char)):
	"""Split text into multiple strings"""
	...

def text_append(text: ctypes.c_char_p, append: ctypes.c_char_p, position: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Append text at specific position and move cursor!"""
	...

def text_find_index(text: ctypes.c_char_p, find: ctypes.c_char_p) -> ctypes.c_int:
	"""Find first text occurrence within a string"""
	...

def text_to_upper(text: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get upper case version of provided string"""
	...

def text_to_lower(text: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get lower case version of provided string"""
	...

def text_to_pascal(text: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get Pascal case notation version of provided string"""
	...

def text_to_integer(text: ctypes.c_char_p) -> ctypes.c_int:
	"""Get integer value from text (negative values not supported)"""
	...

def draw_line_3d(startPos: Vector3, endPos: Vector3, color: Color) -> None:
	"""Draw a line in 3D world space"""
	...

def draw_point_3d(position: Vector3, color: Color) -> None:
	"""Draw a point in 3D space, actually a small line"""
	...

def draw_circle_3d(center: Vector3, radius: ctypes.c_float, rotationAxis: Vector3, rotationAngle: ctypes.c_float, color: Color) -> None:
	"""Draw a circle in 3D world space"""
	...

def draw_triangle_3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_strip_3d(points: ctypes.POINTER(Vector3), pointCount: ctypes.c_int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_cube(position: Vector3, width: ctypes.c_float, height: ctypes.c_float, length: ctypes.c_float, color: Color) -> None:
	"""Draw cube"""
	...

def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube (Vector version)"""
	...

def draw_cube_wires(position: Vector3, width: ctypes.c_float, height: ctypes.c_float, length: ctypes.c_float, color: Color) -> None:
	"""Draw cube wires"""
	...

def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube wires (Vector version)"""
	...

def draw_sphere(centerPos: Vector3, radius: ctypes.c_float, color: Color) -> None:
	"""Draw sphere"""
	...

def draw_sphere_ex(centerPos: Vector3, radius: ctypes.c_float, rings: ctypes.c_int, slices: ctypes.c_int, color: Color) -> None:
	"""Draw sphere with extended parameters"""
	...

def draw_sphere_wires(centerPos: Vector3, radius: ctypes.c_float, rings: ctypes.c_int, slices: ctypes.c_int, color: Color) -> None:
	"""Draw sphere wires"""
	...

def draw_cylinder(position: Vector3, radiusTop: ctypes.c_float, radiusBottom: ctypes.c_float, height: ctypes.c_float, slices: ctypes.c_int, color: Color) -> None:
	"""Draw a cylinder/cone"""
	...

def draw_cylinder_ex(startPos: Vector3, endPos: Vector3, startRadius: ctypes.c_float, endRadius: ctypes.c_float, sides: ctypes.c_int, color: Color) -> None:
	"""Draw a cylinder with base at startPos and top at endPos"""
	...

def draw_cylinder_wires(position: Vector3, radiusTop: ctypes.c_float, radiusBottom: ctypes.c_float, height: ctypes.c_float, slices: ctypes.c_int, color: Color) -> None:
	"""Draw a cylinder/cone wires"""
	...

def draw_cylinder_wires_ex(startPos: Vector3, endPos: Vector3, startRadius: ctypes.c_float, endRadius: ctypes.c_float, sides: ctypes.c_int, color: Color) -> None:
	"""Draw a cylinder wires with base at startPos and top at endPos"""
	...

def draw_capsule(startPos: Vector3, endPos: Vector3, radius: ctypes.c_float, slices: ctypes.c_int, rings: ctypes.c_int, color: Color) -> None:
	"""Draw a capsule with the center of its sphere caps at startPos and endPos"""
	...

def draw_capsule_wires(startPos: Vector3, endPos: Vector3, radius: ctypes.c_float, slices: ctypes.c_int, rings: ctypes.c_int, color: Color) -> None:
	"""Draw capsule wireframe with the center of its sphere caps at startPos and endPos"""
	...

def draw_plane(centerPos: Vector3, size: Vector2, color: Color) -> None:
	"""Draw a plane XZ"""
	...

def draw_ray(ray: Ray, color: Color) -> None:
	"""Draw a ray line"""
	...

def draw_grid(slices: ctypes.c_int, spacing: ctypes.c_float) -> None:
	"""Draw a grid (centered at (0, 0, 0))"""
	...

def load_model(fileName: ctypes.c_char_p) -> Model:
	"""Load model from files (meshes and materials)"""
	...

def load_model_from_mesh(mesh: Mesh) -> Model:
	"""Load model from generated mesh (default material)"""
	...

def is_model_ready(model: Model) -> ctypes.c_bool:
	"""Check if a model is ready"""
	...

def unload_model(model: Model) -> None:
	"""Unload model (including meshes) from memory (RAM and/or VRAM)"""
	...

def get_model_bounding_box(model: Model) -> BoundingBox:
	"""Compute model bounding box limits (considers all meshes)"""
	...

def draw_model(model: Model, position: Vector3, scale: ctypes.c_float, tint: Color) -> None:
	"""Draw a model (with texture if set)"""
	...

def draw_model_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: ctypes.c_float, scale: Vector3, tint: Color) -> None:
	"""Draw a model with extended parameters"""
	...

def draw_model_wires(model: Model, position: Vector3, scale: ctypes.c_float, tint: Color) -> None:
	"""Draw a model wires (with texture if set)"""
	...

def draw_model_wires_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: ctypes.c_float, scale: Vector3, tint: Color) -> None:
	"""Draw a model wires (with texture if set) with extended parameters"""
	...

def draw_bounding_box(box: BoundingBox, color: Color) -> None:
	"""Draw bounding box (wires)"""
	...

def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, size: ctypes.c_float, tint: Color) -> None:
	"""Draw a billboard texture"""
	...

def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None:
	"""Draw a billboard texture defined by source"""
	...

def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: ctypes.c_float, tint: Color) -> None:
	"""Draw a billboard texture defined by source and rotation"""
	...

def upload_mesh(mesh: ctypes.POINTER(Mesh), dynamic: ctypes.c_bool) -> None:
	"""Upload mesh vertex data in GPU and provide VAO/VBO ids"""
	...

def update_mesh_buffer(mesh: Mesh, index: ctypes.c_int, data: ctypes.c_void_p, dataSize: ctypes.c_int, offset: ctypes.c_int) -> None:
	"""Update mesh vertex data in GPU for a specific buffer index"""
	...

def unload_mesh(mesh: Mesh) -> None:
	"""Unload mesh data from CPU and GPU"""
	...

def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
	"""Draw a 3d mesh with material and transform"""
	...

def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: ctypes.POINTER(Matrix), instances: ctypes.c_int) -> None:
	"""Draw multiple mesh instances with material and different transforms"""
	...

def export_mesh(mesh: Mesh, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export mesh data to file, returns true on success"""
	...

def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox:
	"""Compute mesh bounding box limits"""
	...

def gen_mesh_tangents(mesh: ctypes.POINTER(Mesh)) -> None:
	"""Compute mesh tangents"""
	...

def gen_mesh_poly(sides: ctypes.c_int, radius: ctypes.c_float) -> Mesh:
	"""Generate polygonal mesh"""
	...

def gen_mesh_plane(width: ctypes.c_float, length: ctypes.c_float, resX: ctypes.c_int, resZ: ctypes.c_int) -> Mesh:
	"""Generate plane mesh (with subdivisions)"""
	...

def gen_mesh_cube(width: ctypes.c_float, height: ctypes.c_float, length: ctypes.c_float) -> Mesh:
	"""Generate cuboid mesh"""
	...

def gen_mesh_sphere(radius: ctypes.c_float, rings: ctypes.c_int, slices: ctypes.c_int) -> Mesh:
	"""Generate sphere mesh (standard sphere)"""
	...

def gen_mesh_hemi_sphere(radius: ctypes.c_float, rings: ctypes.c_int, slices: ctypes.c_int) -> Mesh:
	"""Generate half-sphere mesh (no bottom cap)"""
	...

def gen_mesh_cylinder(radius: ctypes.c_float, height: ctypes.c_float, slices: ctypes.c_int) -> Mesh:
	"""Generate cylinder mesh"""
	...

def gen_mesh_cone(radius: ctypes.c_float, height: ctypes.c_float, slices: ctypes.c_int) -> Mesh:
	"""Generate cone/pyramid mesh"""
	...

def gen_mesh_torus(radius: ctypes.c_float, size: ctypes.c_float, radSeg: ctypes.c_int, sides: ctypes.c_int) -> Mesh:
	"""Generate torus mesh"""
	...

def gen_mesh_knot(radius: ctypes.c_float, size: ctypes.c_float, radSeg: ctypes.c_int, sides: ctypes.c_int) -> Mesh:
	"""Generate trefoil knot mesh"""
	...

def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh:
	"""Generate heightmap mesh from image data"""
	...

def gen_mesh_cubicmap(cubicmap: Image, cubeSize: Vector3) -> Mesh:
	"""Generate cubes-based map mesh from image data"""
	...

def load_materials(fileName: ctypes.c_char_p, materialCount: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(Material):
	"""Load materials from model file"""
	...

def load_material_default() -> Material:
	"""Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
	...

def is_material_ready(material: Material) -> ctypes.c_bool:
	"""Check if a material is ready"""
	...

def unload_material(material: Material) -> None:
	"""Unload material from GPU memory (VRAM)"""
	...

def set_material_texture(material: ctypes.POINTER(Material), mapType: ctypes.c_int, texture: Texture2D) -> None:
	"""Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
	...

def set_model_mesh_material(model: ctypes.POINTER(Model), meshId: ctypes.c_int, materialId: ctypes.c_int) -> None:
	"""Set material for a mesh"""
	...

def load_model_animations(fileName: ctypes.c_char_p, animCount: ctypes.POINTER(ctypes.c_uint)) -> ctypes.POINTER(ModelAnimation):
	"""Load model animations from file"""
	...

def update_model_animation(model: Model, anim: ModelAnimation, frame: ctypes.c_int) -> None:
	"""Update model animation pose"""
	...

def unload_model_animation(anim: ModelAnimation) -> None:
	"""Unload animation data"""
	...

def unload_model_animations(animations: ctypes.POINTER(ModelAnimation), count: ctypes.c_uint) -> None:
	"""Unload animation array data"""
	...

def is_model_animation_valid(model: Model, anim: ModelAnimation) -> ctypes.c_bool:
	"""Check model animation skeleton match"""
	...

def check_collision_spheres(center1: Vector3, radius1: ctypes.c_float, center2: Vector3, radius2: ctypes.c_float) -> ctypes.c_bool:
	"""Check collision between two spheres"""
	...

def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> ctypes.c_bool:
	"""Check collision between two bounding boxes"""
	...

def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: ctypes.c_float) -> ctypes.c_bool:
	"""Check collision between box and sphere"""
	...

def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: ctypes.c_float) -> RayCollision:
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

def is_audio_device_ready() -> ctypes.c_bool:
	"""Check if audio device has been initialized successfully"""
	...

def set_master_volume(volume: ctypes.c_float) -> None:
	"""Set master volume (listener)"""
	...

def load_wave(fileName: ctypes.c_char_p) -> Wave:
	"""Load wave data from file"""
	...

def load_wave_from_memory(fileType: ctypes.c_char_p, fileData: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int) -> Wave:
	"""Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
	...

def is_wave_ready(wave: Wave) -> ctypes.c_bool:
	"""Checks if wave data is ready"""
	...

def unload_wave(wave: Wave) -> None:
	"""Unload wave data"""
	...

def export_wave(wave: Wave, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export wave data to file, returns true on success"""
	...

def export_wave_as_code(wave: Wave, fileName: ctypes.c_char_p) -> ctypes.c_bool:
	"""Export wave sample data to code (.h), returns true on success"""
	...

def wave_copy(wave: Wave) -> Wave:
	"""Copy a wave to a new wave"""
	...

def wave_crop(wave: ctypes.POINTER(Wave), initSample: ctypes.c_int, finalSample: ctypes.c_int) -> None:
	"""Crop a wave to defined samples range"""
	...

def wave_format(wave: ctypes.POINTER(Wave), sampleRate: ctypes.c_int, sampleSize: ctypes.c_int, channels: ctypes.c_int) -> None:
	"""Convert wave data to desired format"""
	...

def load_wave_samples(wave: Wave) -> ctypes.POINTER(ctypes.c_float):
	"""Load samples data from wave as a 32bit float data array"""
	...

def unload_wave_samples(samples: ctypes.POINTER(ctypes.c_float)) -> None:
	"""Unload samples data loaded with LoadWaveSamples()"""
	...

def load_music_stream(fileName: ctypes.c_char_p) -> Music:
	"""Load music stream from file"""
	...

def load_music_stream_from_memory(fileType: ctypes.c_char_p, data: ctypes.POINTER(ctypes.c_ubyte), dataSize: ctypes.c_int) -> Music:
	"""Load music stream from data"""
	...

def is_music_ready(music: Music) -> ctypes.c_bool:
	"""Checks if a music stream is ready"""
	...

def unload_music_stream(music: Music) -> None:
	"""Unload music stream"""
	...

def play_music_stream(music: Music) -> None:
	"""Start music playing"""
	...

def is_music_stream_playing(music: Music) -> ctypes.c_bool:
	"""Check if music is playing"""
	...

def update_music_stream(music: Music) -> None:
	"""Updates buffers for music streaming"""
	...

def stop_music_stream(music: Music) -> None:
	"""Stop music playing"""
	...

def pause_music_stream(music: Music) -> None:
	"""Pause music playing"""
	...

def resume_music_stream(music: Music) -> None:
	"""Resume playing paused music"""
	...

def seek_music_stream(music: Music, position: ctypes.c_float) -> None:
	"""Seek music to a position (in seconds)"""
	...

def set_music_volume(music: Music, volume: ctypes.c_float) -> None:
	"""Set volume for music (1.0 is max level)"""
	...

def set_music_pitch(music: Music, pitch: ctypes.c_float) -> None:
	"""Set pitch for a music (1.0 is base level)"""
	...

def set_music_pan(music: Music, pan: ctypes.c_float) -> None:
	"""Set pan for a music (0.5 is center)"""
	...

def get_music_time_length(music: Music) -> ctypes.c_float:
	"""Get music time length (in seconds)"""
	...

def get_music_time_played(music: Music) -> ctypes.c_float:
	"""Get current music time played (in seconds)"""
	...

def load_audio_stream(sampleRate: ctypes.c_uint, sampleSize: ctypes.c_uint, channels: ctypes.c_uint) -> AudioStream:
	"""Load audio stream (to stream raw audio pcm data)"""
	...

def is_audio_stream_ready(stream: AudioStream) -> ctypes.c_bool:
	"""Checks if an audio stream is ready"""
	...

def unload_audio_stream(stream: AudioStream) -> None:
	"""Unload audio stream and free memory"""
	...

def update_audio_stream(stream: AudioStream, data: ctypes.c_void_p, frameCount: ctypes.c_int) -> None:
	"""Update audio stream buffers with data"""
	...

def is_audio_stream_processed(stream: AudioStream) -> ctypes.c_bool:
	"""Check if any audio stream buffers requires refill"""
	...

def play_audio_stream(stream: AudioStream) -> None:
	"""Play audio stream"""
	...

def pause_audio_stream(stream: AudioStream) -> None:
	"""Pause audio stream"""
	...

def resume_audio_stream(stream: AudioStream) -> None:
	"""Resume audio stream"""
	...

def is_audio_stream_playing(stream: AudioStream) -> ctypes.c_bool:
	"""Check if audio stream is playing"""
	...

def stop_audio_stream(stream: AudioStream) -> None:
	"""Stop audio stream"""
	...

def set_audio_stream_volume(stream: AudioStream, volume: ctypes.c_float) -> None:
	"""Set volume for audio stream (1.0 is max level)"""
	...

def set_audio_stream_pitch(stream: AudioStream, pitch: ctypes.c_float) -> None:
	"""Set pitch for audio stream (1.0 is base level)"""
	...

def set_audio_stream_pan(stream: AudioStream, pan: ctypes.c_float) -> None:
	"""Set pan for audio stream (0.5 is centered)"""
	...

def set_audio_stream_buffer_size_default(size: ctypes.c_int) -> None:
	"""Default size for new audio streams"""
	...

def clamp(value: ctypes.c_float, min: ctypes.c_float, max: ctypes.c_float) -> ctypes.c_float:
	""""""
	...

def lerp(start: ctypes.c_float, end: ctypes.c_float, amount: ctypes.c_float) -> ctypes.c_float:
	""""""
	...

def normalize(value: ctypes.c_float, start: ctypes.c_float, end: ctypes.c_float) -> ctypes.c_float:
	""""""
	...

def remap(value: ctypes.c_float, inputStart: ctypes.c_float, inputEnd: ctypes.c_float, outputStart: ctypes.c_float, outputEnd: ctypes.c_float) -> ctypes.c_float:
	""""""
	...

def wrap(value: ctypes.c_float, min: ctypes.c_float, max: ctypes.c_float) -> ctypes.c_float:
	""""""
	...

def float_equals(x: ctypes.c_float, y: ctypes.c_float) -> ctypes.c_int:
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

def vector2_add_value(v: Vector2, add: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_subtract(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_subtract_value(v: Vector2, sub: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_length(v: Vector2) -> ctypes.c_float:
	""""""
	...

def vector2_length_sqr(v: Vector2) -> ctypes.c_float:
	""""""
	...

def vector_2dot_product(v1: Vector2, v2: Vector2) -> ctypes.c_float:
	""""""
	...

def vector_2distance(v1: Vector2, v2: Vector2) -> ctypes.c_float:
	""""""
	...

def vector_2distance_sqr(v1: Vector2, v2: Vector2) -> ctypes.c_float:
	""""""
	...

def vector2_angle(v1: Vector2, v2: Vector2) -> ctypes.c_float:
	""""""
	...

def vector2_line_angle(start: Vector2, end: Vector2) -> ctypes.c_float:
	""""""
	...

def vector2_scale(v: Vector2, scale: ctypes.c_float) -> Vector2:
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

def vector2_lerp(v1: Vector2, v2: Vector2, amount: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_reflect(v: Vector2, normal: Vector2) -> Vector2:
	""""""
	...

def vector2_rotate(v: Vector2, angle: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_move_towards(v: Vector2, target: Vector2, maxDistance: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_invert(v: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp(v: Vector2, min: Vector2, max: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp_value(v: Vector2, min: ctypes.c_float, max: ctypes.c_float) -> Vector2:
	""""""
	...

def vector2_equals(p: Vector2, q: Vector2) -> ctypes.c_int:
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

def vector3_add_value(v: Vector3, add: ctypes.c_float) -> Vector3:
	""""""
	...

def vector3_subtract(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_subtract_value(v: Vector3, sub: ctypes.c_float) -> Vector3:
	""""""
	...

def vector3_scale(v: Vector3, scalar: ctypes.c_float) -> Vector3:
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

def vector3_length(v: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_length_sqr(v: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_dot_product(v1: Vector3, v2: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_distance(v1: Vector3, v2: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_distance_sqr(v1: Vector3, v2: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_angle(v1: Vector3, v2: Vector3) -> ctypes.c_float:
	""""""
	...

def vector3_negate(v: Vector3) -> Vector3:
	""""""
	...

def vector3_divide(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_normalize(v: Vector3) -> Vector3:
	""""""
	...

def vector3_ortho_normalize(v1: ctypes.POINTER(Vector3), v2: ctypes.POINTER(Vector3)) -> None:
	""""""
	...

def vector3_transform(v: Vector3, mat: Matrix) -> Vector3:
	""""""
	...

def vector3_rotate_by_quaternion(v: Vector3, q: Quaternion) -> Vector3:
	""""""
	...

def vector3_rotate_by_axis_angle(v: Vector3, axis: Vector3, angle: ctypes.c_float) -> Vector3:
	""""""
	...

def vector3_lerp(v1: Vector3, v2: Vector3, amount: ctypes.c_float) -> Vector3:
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

def vector3_clamp_value(v: Vector3, min: ctypes.c_float, max: ctypes.c_float) -> Vector3:
	""""""
	...

def vector3_equals(p: Vector3, q: Vector3) -> ctypes.c_int:
	""""""
	...

def vector3_refract(v: Vector3, n: Vector3, r: ctypes.c_float) -> Vector3:
	""""""
	...

def matrix_determinant(mat: Matrix) -> ctypes.c_float:
	""""""
	...

def matrix_trace(mat: Matrix) -> ctypes.c_float:
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

def matrix_translate(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_rotate(axis: Vector3, angle: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_rotate_x(angle: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_rotate_y(angle: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_rotate_z(angle: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_rotate_xyz(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_rotate_zyx(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_scale(x: ctypes.c_float, y: ctypes.c_float, z: ctypes.c_float) -> Matrix:
	""""""
	...

def matrix_frustum(left: ctypes.c_double, right: ctypes.c_double, bottom: ctypes.c_double, top: ctypes.c_double, near: ctypes.c_double, far: ctypes.c_double) -> Matrix:
	""""""
	...

def matrix_perspective(fovy: ctypes.c_double, aspect: ctypes.c_double, near: ctypes.c_double, far: ctypes.c_double) -> Matrix:
	""""""
	...

def matrix_ortho(left: ctypes.c_double, right: ctypes.c_double, bottom: ctypes.c_double, top: ctypes.c_double, near: ctypes.c_double, far: ctypes.c_double) -> Matrix:
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

def quaternion_add_value(q: Quaternion, add: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_subtract_value(q: Quaternion, sub: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_identity() -> Quaternion:
	""""""
	...

def quaternion_length(q: Quaternion) -> ctypes.c_float:
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

def quaternion_scale(q: Quaternion, mul: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_lerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_from_vector3_to_vector3(from: Vector3, to: Vector3) -> Quaternion:
	""""""
	...

def quaternion_from_matrix(mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_to_matrix(q: Quaternion) -> Matrix:
	""""""
	...

def quaternion_from_axis_angle(axis: Vector3, angle: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_to_axis_angle(q: Quaternion, outAxis: ctypes.POINTER(Vector3), outAngle: ctypes.POINTER(ctypes.c_float)) -> None:
	""""""
	...

def quaternion_from_euler(pitch: ctypes.c_float, yaw: ctypes.c_float, roll: ctypes.c_float) -> Quaternion:
	""""""
	...

def quaternion_to_euler(q: Quaternion) -> Vector3:
	""""""
	...

def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_equals(p: Quaternion, q: Quaternion) -> ctypes.c_int:
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

def gui_is_locked() -> ctypes.c_bool:
	"""Check if gui is locked (global state)"""
	...

def gui_fade(alpha: ctypes.c_float) -> None:
	"""Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f"""
	...

def gui_set_state(state: ctypes.c_int) -> None:
	"""Set gui state (global state)"""
	...

def gui_get_state() -> ctypes.c_int:
	"""Get gui state (global state)"""
	...

def gui_set_font(font: Font) -> None:
	"""Set gui custom font (global state)"""
	...

def gui_get_font() -> Font:
	"""Get gui custom font (global state)"""
	...

def gui_set_style(control: ctypes.c_int, property: ctypes.c_int, value: ctypes.c_int) -> None:
	"""Set one style property"""
	...

def gui_get_style(control: ctypes.c_int, property: ctypes.c_int) -> ctypes.c_int:
	"""Get one style property"""
	...

def gui_window_box(bounds: Rectangle, title: ctypes.c_char_p) -> ctypes.c_bool:
	"""Window Box control, shows a window that can be closed"""
	...

def gui_group_box(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Group Box control with text name"""
	...

def gui_line(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Line separator control, could contain text"""
	...

def gui_panel(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Panel control, useful to group controls"""
	...

def gui_tab_bar(bounds: Rectangle, text: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int, active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int:
	"""Tab Bar control, returns TAB to be closed or -1"""
	...

def gui_scroll_panel(bounds: Rectangle, text: ctypes.c_char_p, content: Rectangle, scroll: ctypes.POINTER(Vector2)) -> Rectangle:
	"""Scroll Panel control"""
	...

def gui_label(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Label control, shows text"""
	...

def gui_button(bounds: Rectangle, text: ctypes.c_char_p) -> ctypes.c_bool:
	"""Button control, returns true when clicked"""
	...

def gui_label_button(bounds: Rectangle, text: ctypes.c_char_p) -> ctypes.c_bool:
	"""Label button control, show true when clicked"""
	...

def gui_toggle(bounds: Rectangle, text: ctypes.c_char_p, active: ctypes.c_bool) -> ctypes.c_bool:
	"""Toggle Button control, returns true when active"""
	...

def gui_toggle_group(bounds: Rectangle, text: ctypes.c_char_p, active: ctypes.c_int) -> ctypes.c_int:
	"""Toggle Group control, returns active toggle index"""
	...

def gui_check_box(bounds: Rectangle, text: ctypes.c_char_p, checked: ctypes.c_bool) -> ctypes.c_bool:
	"""Check Box control, returns true when active"""
	...

def gui_combo_box(bounds: Rectangle, text: ctypes.c_char_p, active: ctypes.c_int) -> ctypes.c_int:
	"""Combo Box control, returns selected item index"""
	...

def gui_dropdown_box(bounds: Rectangle, text: ctypes.c_char_p, active: ctypes.POINTER(ctypes.c_int), editMode: ctypes.c_bool) -> ctypes.c_bool:
	"""Dropdown Box control, returns selected item"""
	...

def gui_spinner(bounds: Rectangle, text: ctypes.c_char_p, value: ctypes.POINTER(ctypes.c_int), minValue: ctypes.c_int, maxValue: ctypes.c_int, editMode: ctypes.c_bool) -> ctypes.c_bool:
	"""Spinner control, returns selected value"""
	...

def gui_value_box(bounds: Rectangle, text: ctypes.c_char_p, value: ctypes.POINTER(ctypes.c_int), minValue: ctypes.c_int, maxValue: ctypes.c_int, editMode: ctypes.c_bool) -> ctypes.c_bool:
	"""Value Box control, updates input text with numbers"""
	...

def gui_text_box(bounds: Rectangle, text: ctypes.c_char_p, textSize: ctypes.c_int, editMode: ctypes.c_bool) -> ctypes.c_bool:
	"""Text Box control, updates input text"""
	...

def gui_slider(bounds: Rectangle, textLeft: ctypes.c_char_p, textRight: ctypes.c_char_p, value: ctypes.c_float, minValue: ctypes.c_float, maxValue: ctypes.c_float) -> ctypes.c_float:
	"""Slider control, returns selected value"""
	...

def gui_slider_bar(bounds: Rectangle, textLeft: ctypes.c_char_p, textRight: ctypes.c_char_p, value: ctypes.c_float, minValue: ctypes.c_float, maxValue: ctypes.c_float) -> ctypes.c_float:
	"""Slider Bar control, returns selected value"""
	...

def gui_progress_bar(bounds: Rectangle, textLeft: ctypes.c_char_p, textRight: ctypes.c_char_p, value: ctypes.c_float, minValue: ctypes.c_float, maxValue: ctypes.c_float) -> ctypes.c_float:
	"""Progress Bar control, shows current progress value"""
	...

def gui_status_bar(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Status Bar control, shows info text"""
	...

def gui_dummy_rec(bounds: Rectangle, text: ctypes.c_char_p) -> None:
	"""Dummy control for placeholders"""
	...

def gui_grid(bounds: Rectangle, text: ctypes.c_char_p, spacing: ctypes.c_float, subdivs: ctypes.c_int) -> Vector2:
	"""Grid control, returns mouse cell position"""
	...

def gui_list_view(bounds: Rectangle, text: ctypes.c_char_p, scrollIndex: ctypes.POINTER(ctypes.c_int), active: ctypes.c_int) -> ctypes.c_int:
	"""List View control, returns selected list item index"""
	...

def gui_list_view_ex(bounds: Rectangle, text: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int, focus: ctypes.POINTER(ctypes.c_int), scrollIndex: ctypes.POINTER(ctypes.c_int), active: ctypes.c_int) -> ctypes.c_int:
	"""List View with extended parameters"""
	...

def gui_message_box(bounds: Rectangle, title: ctypes.c_char_p, message: ctypes.c_char_p, buttons: ctypes.c_char_p) -> ctypes.c_int:
	"""Message Box control, displays a message"""
	...

def gui_text_input_box(bounds: Rectangle, title: ctypes.c_char_p, message: ctypes.c_char_p, buttons: ctypes.c_char_p, text: ctypes.c_char_p, textMaxSize: ctypes.c_int, secretViewActive: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int:
	"""Text Input Box control, ask for text, supports secret"""
	...

def gui_color_picker(bounds: Rectangle, text: ctypes.c_char_p, color: Color) -> Color:
	"""Color Picker control (multiple color controls)"""
	...

def gui_color_panel(bounds: Rectangle, text: ctypes.c_char_p, color: Color) -> Color:
	"""Color Panel control"""
	...

def gui_color_bar_alpha(bounds: Rectangle, text: ctypes.c_char_p, alpha: ctypes.c_float) -> ctypes.c_float:
	"""Color Bar Alpha control"""
	...

def gui_color_bar_hue(bounds: Rectangle, text: ctypes.c_char_p, value: ctypes.c_float) -> ctypes.c_float:
	"""Color Bar Hue control"""
	...

def gui_load_style(fileName: ctypes.c_char_p) -> None:
	"""Load style file over global style variable (.rgs)"""
	...

def gui_load_style_default() -> None:
	"""Load style default over global style"""
	...

def gui_enable_tooltip() -> None:
	"""Enable gui tooltips (global state)"""
	...

def gui_disable_tooltip() -> None:
	"""Disable gui tooltips (global state)"""
	...

def gui_set_tooltip(tooltip: ctypes.c_char_p) -> None:
	"""Set tooltip string"""
	...

def gui_icon_text(iconId: ctypes.c_int, text: ctypes.c_char_p) -> ctypes.c_char_p:
	"""Get text with icon id prepended (if supported)"""
	...

