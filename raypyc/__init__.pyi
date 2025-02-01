import ctypes
from raypyc.defines import *
from raypyc.colors import *
from raypyc.enums import *
from raypyc.structures import *


def rl_matrix_mode(mode: ctypes.c_int | int) -> None:
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

def rl_translatef(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Multiply the current matrix by a translation matrix"""
	...

def rl_rotatef(angle: ctypes.c_float | float, x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Multiply the current matrix by a rotation matrix"""
	...

def rl_scalef(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Multiply the current matrix by a scaling matrix"""
	...

def rl_mult_matrixf(matf: ctypes.POINTER(ctypes.c_float)) -> None:
	"""Multiply the current matrix by another matrix"""
	...

def rl_frustum(left: ctypes.c_double | float, right: ctypes.c_double | float, bottom: ctypes.c_double | float, top: ctypes.c_double | float, znear: ctypes.c_double | float, zfar: ctypes.c_double | float) -> None:
	""""""
	...

def rl_ortho(left: ctypes.c_double | float, right: ctypes.c_double | float, bottom: ctypes.c_double | float, top: ctypes.c_double | float, znear: ctypes.c_double | float, zfar: ctypes.c_double | float) -> None:
	""""""
	...

def rl_viewport(x: ctypes.c_int | int, y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Set the viewport area"""
	...

def rl_set_clip_planes(near_plane: ctypes.c_double | float, far_plane: ctypes.c_double | float) -> None:
	"""Set clip planes distances"""
	...

def rl_get_cull_distance_near() -> ctypes.c_double | float:
	"""Get cull plane distance near"""
	...

def rl_get_cull_distance_far() -> ctypes.c_double | float:
	"""Get cull plane distance far"""
	...

def rl_begin(mode: ctypes.c_int | int) -> None:
	"""Initialize drawing mode (how to organize vertex)"""
	...

def rl_end() -> None:
	"""Finish vertex providing"""
	...

def rl_vertex2i(x: ctypes.c_int | int, y: ctypes.c_int | int) -> None:
	"""Define one vertex (position) - 2 int"""
	...

def rl_vertex2f(x: ctypes.c_float | float, y: ctypes.c_float | float) -> None:
	"""Define one vertex (position) - 2 float"""
	...

def rl_vertex3f(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Define one vertex (position) - 3 float"""
	...

def rl_tex_coord2f(x: ctypes.c_float | float, y: ctypes.c_float | float) -> None:
	"""Define one vertex (texture coordinate) - 2 float"""
	...

def rl_normal3f(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Define one vertex (normal) - 3 float"""
	...

def rl_color4ub(r: ctypes.c_ubyte | int, g: ctypes.c_ubyte | int, b: ctypes.c_ubyte | int, a: ctypes.c_ubyte | int) -> None:
	"""Define one vertex (color) - 4 byte"""
	...

def rl_color3f(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> None:
	"""Define one vertex (color) - 3 float"""
	...

def rl_color4f(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float, w: ctypes.c_float | float) -> None:
	"""Define one vertex (color) - 4 float"""
	...

def rl_enable_vertex_array(vao_id: ctypes.c_uint | int) -> ctypes.c_bool | bool:
	"""Enable vertex array (VAO, if supported)"""
	...

def rl_disable_vertex_array() -> None:
	"""Disable vertex array (VAO, if supported)"""
	...

def rl_enable_vertex_buffer(id: ctypes.c_uint | int) -> None:
	"""Enable vertex buffer (VBO)"""
	...

def rl_disable_vertex_buffer() -> None:
	"""Disable vertex buffer (VBO)"""
	...

def rl_enable_vertex_buffer_element(id: ctypes.c_uint | int) -> None:
	"""Enable vertex buffer element (VBO element)"""
	...

def rl_disable_vertex_buffer_element() -> None:
	"""Disable vertex buffer element (VBO element)"""
	...

def rl_enable_vertex_attribute(index: ctypes.c_uint | int) -> None:
	"""Enable vertex attribute index"""
	...

def rl_disable_vertex_attribute(index: ctypes.c_uint | int) -> None:
	"""Disable vertex attribute index"""
	...

def rl_active_texture_slot(slot: ctypes.c_int | int) -> None:
	"""Select and active a texture slot"""
	...

def rl_enable_texture(id: ctypes.c_uint | int) -> None:
	"""Enable texture"""
	...

def rl_disable_texture() -> None:
	"""Disable texture"""
	...

def rl_enable_texture_cubemap(id: ctypes.c_uint | int) -> None:
	"""Enable texture cubemap"""
	...

def rl_disable_texture_cubemap() -> None:
	"""Disable texture cubemap"""
	...

def rl_texture_parameters(id: ctypes.c_uint | int, param: ctypes.c_int | int, value: ctypes.c_int | int) -> None:
	"""Set texture parameters (filter, wrap)"""
	...

def rl_cubemap_parameters(id: ctypes.c_uint | int, param: ctypes.c_int | int, value: ctypes.c_int | int) -> None:
	"""Set cubemap parameters (filter, wrap)"""
	...

def rl_enable_shader(id: ctypes.c_uint | int) -> None:
	"""Enable shader program"""
	...

def rl_disable_shader() -> None:
	"""Disable shader program"""
	...

def rl_enable_framebuffer(id: ctypes.c_uint | int) -> None:
	"""Enable render texture (fbo)"""
	...

def rl_disable_framebuffer() -> None:
	"""Disable render texture (fbo), return to default framebuffer"""
	...

def rl_get_active_framebuffer() -> ctypes.c_uint | int:
	"""Get the currently active render texture (fbo), 0 for default framebuffer"""
	...

def rl_active_draw_buffers(count: ctypes.c_int | int) -> None:
	"""Activate multiple draw color buffers"""
	...

def rl_blit_framebuffer(src_x: ctypes.c_int | int, src_y: ctypes.c_int | int, src_width: ctypes.c_int | int, src_height: ctypes.c_int | int, dst_x: ctypes.c_int | int, dst_y: ctypes.c_int | int, dst_width: ctypes.c_int | int, dst_height: ctypes.c_int | int, buffer_mask: ctypes.c_int | int) -> None:
	"""Blit active framebuffer to main framebuffer"""
	...

def rl_bind_framebuffer(target: ctypes.c_uint | int, framebuffer: ctypes.c_uint | int) -> None:
	"""Bind framebuffer (FBO)"""
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

def rl_color_mask(r: ctypes.c_bool | bool, g: ctypes.c_bool | bool, b: ctypes.c_bool | bool, a: ctypes.c_bool | bool) -> None:
	"""Color mask control"""
	...

def rl_set_cull_face(mode: ctypes.c_int | int) -> None:
	"""Set face culling mode"""
	...

def rl_enable_scissor_test() -> None:
	"""Enable scissor test"""
	...

def rl_disable_scissor_test() -> None:
	"""Disable scissor test"""
	...

def rl_scissor(x: ctypes.c_int | int, y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Scissor test"""
	...

def rl_enable_point_mode() -> None:
	"""Enable point mode"""
	...

def rl_disable_point_mode() -> None:
	"""Disable point mode"""
	...

def rl_enable_wire_mode() -> None:
	"""Enable wire mode"""
	...

def rl_disable_wire_mode() -> None:
	"""Disable wire mode"""
	...

def rl_set_line_width(width: ctypes.c_float | float) -> None:
	"""Set the line drawing width"""
	...

def rl_get_line_width() -> ctypes.c_float | float:
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

def rl_is_stereo_render_enabled() -> ctypes.c_bool | bool:
	"""Check if stereo render is enabled"""
	...

def rl_clear_color(r: ctypes.c_ubyte | int, g: ctypes.c_ubyte | int, b: ctypes.c_ubyte | int, a: ctypes.c_ubyte | int) -> None:
	"""Clear color buffer with color"""
	...

def rl_clear_screen_buffers() -> None:
	"""Clear used screen buffers (color and depth)"""
	...

def rl_check_errors() -> None:
	"""Check and log OpenGL error codes"""
	...

def rl_set_blend_mode(mode: ctypes.c_int | int) -> None:
	"""Set blending mode"""
	...

def rl_set_blend_factors(gl_src_factor: ctypes.c_int | int, gl_dst_factor: ctypes.c_int | int, gl_equation: ctypes.c_int | int) -> None:
	"""Set blending mode factor and equation (using OpenGL factors)"""
	...

def rl_set_blend_factors_separate(gl_src_rgb: ctypes.c_int | int, gl_dst_rgb: ctypes.c_int | int, gl_src_alpha: ctypes.c_int | int, gl_dst_alpha: ctypes.c_int | int, gl_eq_rgb: ctypes.c_int | int, gl_eq_alpha: ctypes.c_int | int) -> None:
	"""Set blending mode factors and equations separately (using OpenGL factors)"""
	...

def rlgl_init(width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Initialize rlgl (buffers, shaders, textures, states)"""
	...

def rlgl_close() -> None:
	"""De-initialize rlgl (buffers, shaders, textures)"""
	...

def rl_load_extensions(loader: ctypes.c_void_p | bytes) -> None:
	"""Load OpenGL extensions (loader function required)"""
	...

def rl_get_version() -> ctypes.c_int | int:
	"""Get current OpenGL version"""
	...

def rl_set_framebuffer_width(width: ctypes.c_int | int) -> None:
	"""Set current framebuffer width"""
	...

def rl_get_framebuffer_width() -> ctypes.c_int | int:
	"""Get default framebuffer width"""
	...

def rl_set_framebuffer_height(height: ctypes.c_int | int) -> None:
	"""Set current framebuffer height"""
	...

def rl_get_framebuffer_height() -> ctypes.c_int | int:
	"""Get default framebuffer height"""
	...

def rl_get_texture_id_default() -> ctypes.c_uint | int:
	"""Get default texture id"""
	...

def rl_get_shader_id_default() -> ctypes.c_uint | int:
	"""Get default shader id"""
	...

def rl_get_shader_locs_default() -> ctypes.POINTER(ctypes.c_int):
	"""Get default shader locations"""
	...

def rl_load_render_batch(num_buffers: ctypes.c_int | int, buffer_elements: ctypes.c_int | int) -> rlRenderBatch:
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

def rl_check_render_batch_limit(v_count: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check internal buffer overflow for a given number of vertex"""
	...

def rl_set_texture(id: ctypes.c_uint | int) -> None:
	"""Set current texture for render batch and check buffers limits"""
	...

def rl_load_vertex_array() -> ctypes.c_uint | int:
	"""Load vertex array (vao) if supported"""
	...

def rl_load_vertex_buffer(buffer: ctypes.c_void_p | bytes, size: ctypes.c_int | int, dynamic: ctypes.c_bool | bool) -> ctypes.c_uint | int:
	"""Load a vertex buffer object"""
	...

def rl_load_vertex_buffer_element(buffer: ctypes.c_void_p | bytes, size: ctypes.c_int | int, dynamic: ctypes.c_bool | bool) -> ctypes.c_uint | int:
	"""Load vertex buffer elements object"""
	...

def rl_update_vertex_buffer(buffer_id: ctypes.c_uint | int, data: ctypes.c_void_p | bytes, data_size: ctypes.c_int | int, offset: ctypes.c_int | int) -> None:
	"""Update vertex buffer object data on GPU buffer"""
	...

def rl_update_vertex_buffer_elements(id: ctypes.c_uint | int, data: ctypes.c_void_p | bytes, data_size: ctypes.c_int | int, offset: ctypes.c_int | int) -> None:
	"""Update vertex buffer elements data on GPU buffer"""
	...

def rl_unload_vertex_array(vao_id: ctypes.c_uint | int) -> None:
	"""Unload vertex array (vao)"""
	...

def rl_unload_vertex_buffer(vbo_id: ctypes.c_uint | int) -> None:
	"""Unload vertex buffer object"""
	...

def rl_set_vertex_attribute(index: ctypes.c_uint | int, comp_size: ctypes.c_int | int, type: ctypes.c_int | int, normalized: ctypes.c_bool | bool, stride: ctypes.c_int | int, offset: ctypes.c_int | int) -> None:
	"""Set vertex attribute data configuration"""
	...

def rl_set_vertex_attribute_divisor(index: ctypes.c_uint | int, divisor: ctypes.c_int | int) -> None:
	"""Set vertex attribute data divisor"""
	...

def rl_set_vertex_attribute_default(loc_index: ctypes.c_int | int, value: ctypes.c_void_p | bytes, attrib_type: ctypes.c_int | int, count: ctypes.c_int | int) -> None:
	"""Set vertex attribute default value, when attribute to provided"""
	...

def rl_draw_vertex_array(offset: ctypes.c_int | int, count: ctypes.c_int | int) -> None:
	"""Draw vertex array (currently active vao)"""
	...

def rl_draw_vertex_array_elements(offset: ctypes.c_int | int, count: ctypes.c_int | int, buffer: ctypes.c_void_p | bytes) -> None:
	"""Draw vertex array elements"""
	...

def rl_draw_vertex_array_instanced(offset: ctypes.c_int | int, count: ctypes.c_int | int, instances: ctypes.c_int | int) -> None:
	"""Draw vertex array (currently active vao) with instancing"""
	...

def rl_draw_vertex_array_elements_instanced(offset: ctypes.c_int | int, count: ctypes.c_int | int, buffer: ctypes.c_void_p | bytes, instances: ctypes.c_int | int) -> None:
	"""Draw vertex array elements with instancing"""
	...

def rl_load_texture(data: ctypes.c_void_p | bytes, width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int, mipmap_count: ctypes.c_int | int) -> ctypes.c_uint | int:
	"""Load texture data"""
	...

def rl_load_texture_depth(width: ctypes.c_int | int, height: ctypes.c_int | int, use_render_buffer: ctypes.c_bool | bool) -> ctypes.c_uint | int:
	"""Load depth texture/renderbuffer (to be attached to fbo)"""
	...

def rl_load_texture_cubemap(data: ctypes.c_void_p | bytes, size: ctypes.c_int | int, format: ctypes.c_int | int, mipmap_count: ctypes.c_int | int) -> ctypes.c_uint | int:
	"""Load texture cubemap data"""
	...

def rl_update_texture(id: ctypes.c_uint | int, offset_x: ctypes.c_int | int, offset_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int, data: ctypes.c_void_p | bytes) -> None:
	"""Update texture with new data on GPU"""
	...

def rl_get_gl_texture_formats(format: ctypes.c_int | int, gl_internal_format: ctypes.POINTER(ctypes.c_uint), gl_format: ctypes.POINTER(ctypes.c_uint), gl_type: ctypes.POINTER(ctypes.c_uint)) -> None:
	"""Get OpenGL internal formats"""
	...

def rl_get_pixel_format_name(format: ctypes.c_uint | int) -> ctypes.c_char_p | bytes:
	"""Get name string for pixel format"""
	...

def rl_unload_texture(id: ctypes.c_uint | int) -> None:
	"""Unload texture from GPU memory"""
	...

def rl_gen_texture_mipmaps(id: ctypes.c_uint | int, width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int, mipmaps: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Generate mipmap data for selected texture"""
	...

def rl_read_texture_pixels(id: ctypes.c_uint | int, width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int) -> ctypes.c_void_p | bytes:
	"""Read texture pixel data"""
	...

def rl_read_screen_pixels(width: ctypes.c_int | int, height: ctypes.c_int | int) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Read screen pixel data (color buffer)"""
	...

def rl_load_framebuffer() -> ctypes.c_uint | int:
	"""Load an empty framebuffer"""
	...

def rl_framebuffer_attach(fbo_id: ctypes.c_uint | int, tex_id: ctypes.c_uint | int, attach_type: ctypes.c_int | int, tex_type: ctypes.c_int | int, mip_level: ctypes.c_int | int) -> None:
	"""Attach texture/renderbuffer to a framebuffer"""
	...

def rl_framebuffer_complete(id: ctypes.c_uint | int) -> ctypes.c_bool | bool:
	"""Verify framebuffer is complete"""
	...

def rl_unload_framebuffer(id: ctypes.c_uint | int) -> None:
	"""Delete framebuffer from GPU"""
	...

def rl_load_shader_code(vs_code: ctypes.c_char_p | bytes, fs_code: ctypes.c_char_p | bytes) -> ctypes.c_uint | int:
	"""Load shader from code strings"""
	...

def rl_compile_shader(shader_code: ctypes.c_char_p | bytes, type: ctypes.c_int | int) -> ctypes.c_uint | int:
	"""Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)"""
	...

def rl_load_shader_program(v_shader_id: ctypes.c_uint | int, f_shader_id: ctypes.c_uint | int) -> ctypes.c_uint | int:
	"""Load custom shader program"""
	...

def rl_unload_shader_program(id: ctypes.c_uint | int) -> None:
	"""Unload shader program"""
	...

def rl_get_location_uniform(shader_id: ctypes.c_uint | int, uniform_name: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get shader location uniform"""
	...

def rl_get_location_attrib(shader_id: ctypes.c_uint | int, attrib_name: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get shader location attribute"""
	...

def rl_set_uniform(loc_index: ctypes.c_int | int, value: ctypes.c_void_p | bytes, uniform_type: ctypes.c_int | int, count: ctypes.c_int | int) -> None:
	"""Set shader value uniform"""
	...

def rl_set_uniform_matrix(loc_index: ctypes.c_int | int, mat: Matrix) -> None:
	"""Set shader value matrix"""
	...

def rl_set_uniform_matrices(loc_index: ctypes.c_int | int, mat: ctypes.POINTER(Matrix), count: ctypes.c_int | int) -> None:
	"""Set shader value matrices"""
	...

def rl_set_uniform_sampler(loc_index: ctypes.c_int | int, texture_id: ctypes.c_uint | int) -> None:
	"""Set shader value sampler"""
	...

def rl_set_shader(id: ctypes.c_uint | int, locs: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Set shader currently active (id and locations)"""
	...

def rl_load_compute_shader_program(shader_id: ctypes.c_uint | int) -> ctypes.c_uint | int:
	"""Load compute shader program"""
	...

def rl_compute_shader_dispatch(group_x: ctypes.c_uint | int, group_y: ctypes.c_uint | int, group_z: ctypes.c_uint | int) -> None:
	"""Dispatch compute shader (equivalent to *draw* for graphics pipeline)"""
	...

def rl_load_shader_buffer(size: ctypes.c_uint | int, data: ctypes.c_void_p | bytes, usage_hint: ctypes.c_int | int) -> ctypes.c_uint | int:
	"""Load shader storage buffer object (SSBO)"""
	...

def rl_unload_shader_buffer(ssbo_id: ctypes.c_uint | int) -> None:
	"""Unload shader storage buffer object (SSBO)"""
	...

def rl_update_shader_buffer(id: ctypes.c_uint | int, data: ctypes.c_void_p | bytes, data_size: ctypes.c_uint | int, offset: ctypes.c_uint | int) -> None:
	"""Update SSBO buffer data"""
	...

def rl_bind_shader_buffer(id: ctypes.c_uint | int, index: ctypes.c_uint | int) -> None:
	"""Bind SSBO buffer"""
	...

def rl_read_shader_buffer(id: ctypes.c_uint | int, dest: ctypes.c_void_p | bytes, count: ctypes.c_uint | int, offset: ctypes.c_uint | int) -> None:
	"""Read SSBO buffer data (GPU->CPU)"""
	...

def rl_copy_shader_buffer(dest_id: ctypes.c_uint | int, src_id: ctypes.c_uint | int, dest_offset: ctypes.c_uint | int, src_offset: ctypes.c_uint | int, count: ctypes.c_uint | int) -> None:
	"""Copy SSBO data between buffers"""
	...

def rl_get_shader_buffer_size(id: ctypes.c_uint | int) -> ctypes.c_uint | int:
	"""Get SSBO buffer size"""
	...

def rl_bind_image_texture(id: ctypes.c_uint | int, index: ctypes.c_uint | int, format: ctypes.c_int | int, readonly: ctypes.c_bool | bool) -> None:
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

def rl_get_matrix_projection_stereo(eye: ctypes.c_int | int) -> Matrix:
	"""Get internal projection matrix for stereo render (selected eye)"""
	...

def rl_get_matrix_view_offset_stereo(eye: ctypes.c_int | int) -> Matrix:
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

def init_window(width: ctypes.c_int | int, height: ctypes.c_int | int, title: ctypes.c_char_p | bytes) -> None:
	"""Initialize window and OpenGL context"""
	...

def close_window() -> None:
	"""Close window and unload OpenGL context"""
	...

def window_should_close() -> ctypes.c_bool | bool:
	"""Check if application should close (KEY_ESCAPE pressed or windows close icon clicked)"""
	...

def is_window_ready() -> ctypes.c_bool | bool:
	"""Check if window has been initialized successfully"""
	...

def is_window_fullscreen() -> ctypes.c_bool | bool:
	"""Check if window is currently fullscreen"""
	...

def is_window_hidden() -> ctypes.c_bool | bool:
	"""Check if window is currently hidden"""
	...

def is_window_minimized() -> ctypes.c_bool | bool:
	"""Check if window is currently minimized"""
	...

def is_window_maximized() -> ctypes.c_bool | bool:
	"""Check if window is currently maximized"""
	...

def is_window_focused() -> ctypes.c_bool | bool:
	"""Check if window is currently focused"""
	...

def is_window_resized() -> ctypes.c_bool | bool:
	"""Check if window has been resized last frame"""
	...

def is_window_state(flag: ctypes.c_uint | int) -> ctypes.c_bool | bool:
	"""Check if one specific window flag is enabled"""
	...

def set_window_state(flags: ctypes.c_uint | int) -> None:
	"""Set window configuration state using flags"""
	...

def clear_window_state(flags: ctypes.c_uint | int) -> None:
	"""Clear window configuration state flags"""
	...

def toggle_fullscreen() -> None:
	"""Toggle window state: fullscreen/windowed, resizes monitor to match window resolution"""
	...

def toggle_borderless_windowed() -> None:
	"""Toggle window state: borderless windowed, resizes window to match monitor resolution"""
	...

def maximize_window() -> None:
	"""Set window state: maximized, if resizable"""
	...

def minimize_window() -> None:
	"""Set window state: minimized, if resizable"""
	...

def restore_window() -> None:
	"""Set window state: not minimized/maximized"""
	...

def set_window_icon(image: Image) -> None:
	"""Set icon for window (single image, RGBA 32bit)"""
	...

def set_window_icons(images: ctypes.POINTER(Image), count: ctypes.c_int | int) -> None:
	"""Set icon for window (multiple images, RGBA 32bit)"""
	...

def set_window_title(title: ctypes.c_char_p | bytes) -> None:
	"""Set title for window"""
	...

def set_window_position(x: ctypes.c_int | int, y: ctypes.c_int | int) -> None:
	"""Set window position on screen"""
	...

def set_window_monitor(monitor: ctypes.c_int | int) -> None:
	"""Set monitor for the current window"""
	...

def set_window_min_size(width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
	...

def set_window_max_size(width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Set window maximum dimensions (for FLAG_WINDOW_RESIZABLE)"""
	...

def set_window_size(width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
	"""Set window dimensions"""
	...

def set_window_opacity(opacity: ctypes.c_float | float) -> None:
	"""Set window opacity [0.0f..1.0f]"""
	...

def set_window_focused() -> None:
	"""Set window focused"""
	...

def get_window_handle() -> ctypes.c_void_p | bytes:
	"""Get native window handle"""
	...

def get_screen_width() -> ctypes.c_int | int:
	"""Get current screen width"""
	...

def get_screen_height() -> ctypes.c_int | int:
	"""Get current screen height"""
	...

def get_render_width() -> ctypes.c_int | int:
	"""Get current render width (it considers HiDPI)"""
	...

def get_render_height() -> ctypes.c_int | int:
	"""Get current render height (it considers HiDPI)"""
	...

def get_monitor_count() -> ctypes.c_int | int:
	"""Get number of connected monitors"""
	...

def get_current_monitor() -> ctypes.c_int | int:
	"""Get current monitor where window is placed"""
	...

def get_monitor_position(monitor: ctypes.c_int | int) -> Vector2:
	"""Get specified monitor position"""
	...

def get_monitor_width(monitor: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get specified monitor width (current video mode used by monitor)"""
	...

def get_monitor_height(monitor: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get specified monitor height (current video mode used by monitor)"""
	...

def get_monitor_physical_width(monitor: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get specified monitor physical width in millimetres"""
	...

def get_monitor_physical_height(monitor: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get specified monitor physical height in millimetres"""
	...

def get_monitor_refresh_rate(monitor: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get specified monitor refresh rate"""
	...

def get_window_position() -> Vector2:
	"""Get window position XY on monitor"""
	...

def get_window_scale_dpi() -> Vector2:
	"""Get window scale DPI factor"""
	...

def get_monitor_name(monitor: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Get the human-readable, UTF-8 encoded name of the specified monitor"""
	...

def set_clipboard_text(text: ctypes.c_char_p | bytes) -> None:
	"""Set clipboard text content"""
	...

def get_clipboard_text() -> ctypes.c_char_p | bytes:
	"""Get clipboard text content"""
	...

def get_clipboard_image() -> Image:
	"""Get clipboard image content"""
	...

def enable_event_waiting() -> None:
	"""Enable waiting for events on EndDrawing(), no automatic event polling"""
	...

def disable_event_waiting() -> None:
	"""Disable waiting for events on EndDrawing(), automatic events polling"""
	...

def show_cursor() -> None:
	"""Shows cursor"""
	...

def hide_cursor() -> None:
	"""Hides cursor"""
	...

def is_cursor_hidden() -> ctypes.c_bool | bool:
	"""Check if cursor is not visible"""
	...

def enable_cursor() -> None:
	"""Enables cursor (unlock cursor)"""
	...

def disable_cursor() -> None:
	"""Disables cursor (lock cursor)"""
	...

def is_cursor_on_screen() -> ctypes.c_bool | bool:
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

def begin_blend_mode(mode: ctypes.c_int | int) -> None:
	"""Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
	...

def end_blend_mode() -> None:
	"""End blending mode (reset to default: alpha blending)"""
	...

def begin_scissor_mode(x: ctypes.c_int | int, y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int) -> None:
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

def load_shader(vs_file_name: ctypes.c_char_p | bytes, fs_file_name: ctypes.c_char_p | bytes) -> Shader:
	"""Load shader from files and bind default locations"""
	...

def load_shader_from_memory(vs_code: ctypes.c_char_p | bytes, fs_code: ctypes.c_char_p | bytes) -> Shader:
	"""Load shader from code strings and bind default locations"""
	...

def is_shader_valid(shader: Shader) -> ctypes.c_bool | bool:
	"""Check if a shader is valid (loaded on GPU)"""
	...

def get_shader_location(shader: Shader, uniform_name: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get shader uniform location"""
	...

def get_shader_location_attrib(shader: Shader, attrib_name: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get shader attribute location"""
	...

def set_shader_value(shader: Shader, loc_index: ctypes.c_int | int, value: ctypes.c_void_p | bytes, uniform_type: ctypes.c_int | int) -> None:
	"""Set shader uniform value"""
	...

def set_shader_value_v(shader: Shader, loc_index: ctypes.c_int | int, value: ctypes.c_void_p | bytes, uniform_type: ctypes.c_int | int, count: ctypes.c_int | int) -> None:
	"""Set shader uniform value vector"""
	...

def set_shader_value_matrix(shader: Shader, loc_index: ctypes.c_int | int, mat: Matrix) -> None:
	"""Set shader uniform value (matrix 4x4)"""
	...

def set_shader_value_texture(shader: Shader, loc_index: ctypes.c_int | int, texture: Texture2D) -> None:
	"""Set shader uniform value and bind the texture (sampler2d)"""
	...

def unload_shader(shader: Shader) -> None:
	"""Unload shader from GPU memory (VRAM)"""
	...

def get_screen_to_world_ray(position: Vector2, camera: Camera) -> Ray:
	"""Get a ray trace from screen position (i.e mouse)"""
	...

def get_screen_to_world_ray_ex(position: Vector2, camera: Camera, width: ctypes.c_int | int, height: ctypes.c_int | int) -> Ray:
	"""Get a ray trace from screen position (i.e mouse) in a viewport"""
	...

def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2:
	"""Get the screen space position for a 3d world space position"""
	...

def get_world_to_screen_ex(position: Vector3, camera: Camera, width: ctypes.c_int | int, height: ctypes.c_int | int) -> Vector2:
	"""Get size position for a 3d world space position"""
	...

def get_world_to_screen_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Get the screen space position for a 2d camera world space position"""
	...

def get_screen_to_world_2d(position: Vector2, camera: Camera2D) -> Vector2:
	"""Get the world space position for a 2d camera screen space position"""
	...

def get_camera_matrix(camera: Camera) -> Matrix:
	"""Get camera transform matrix (view matrix)"""
	...

def get_camera_matrix_2d(camera: Camera2D) -> Matrix:
	"""Get camera 2d transform matrix"""
	...

def set_target_fps(fps: ctypes.c_int | int) -> None:
	"""Set target FPS (maximum)"""
	...

def get_frame_time() -> ctypes.c_float | float:
	"""Get time in seconds for last frame drawn (delta time)"""
	...

def get_time() -> ctypes.c_double | float:
	"""Get elapsed time in seconds since InitWindow()"""
	...

def get_fps() -> ctypes.c_int | int:
	"""Get current FPS"""
	...

def swap_screen_buffer() -> None:
	"""Swap back buffer with front buffer (screen drawing)"""
	...

def poll_input_events() -> None:
	"""Register all input events"""
	...

def wait_time(seconds: ctypes.c_double | float) -> None:
	"""Wait for some time (halt program execution)"""
	...

def set_random_seed(seed: ctypes.c_uint | int) -> None:
	"""Set the seed for the random number generator"""
	...

def get_random_value(min: ctypes.c_int | int, max: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get a random value between min and max (both included)"""
	...

def load_random_sequence(count: ctypes.c_uint | int, min: ctypes.c_int | int, max: ctypes.c_int | int) -> ctypes.POINTER(ctypes.c_int):
	"""Load random values sequence, no values repeated"""
	...

def unload_random_sequence(sequence: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Unload random values sequence"""
	...

def take_screenshot(file_name: ctypes.c_char_p | bytes) -> None:
	"""Takes a screenshot of current screen (filename extension defines format)"""
	...

def set_config_flags(flags: ctypes.c_uint | int) -> None:
	"""Setup init configuration flags (view FLAGS)"""
	...

def open_url(url: ctypes.c_char_p | bytes) -> None:
	"""Open URL with default system browser (if available)"""
	...

def trace_log(log_level: ctypes.c_int | int, text: ctypes.c_char_p | bytes, args: ...) -> None:
	"""Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
	...

def set_trace_log_level(log_level: ctypes.c_int | int) -> None:
	"""Set the current threshold (minimum) log level"""
	...

def mem_alloc(size: ctypes.c_uint | int) -> ctypes.c_void_p | bytes:
	"""Internal memory allocator"""
	...

def mem_realloc(ptr: ctypes.c_void_p | bytes, size: ctypes.c_uint | int) -> ctypes.c_void_p | bytes:
	"""Internal memory reallocator"""
	...

def mem_free(ptr: ctypes.c_void_p | bytes) -> None:
	"""Internal memory free"""
	...

def load_file_data(file_name: ctypes.c_char_p | bytes, data_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Load file data as byte array (read)"""
	...

def unload_file_data(data: ctypes.POINTER(ctypes.c_ubyte)) -> None:
	"""Unload file data allocated by LoadFileData()"""
	...

def save_file_data(file_name: ctypes.c_char_p | bytes, data: ctypes.c_void_p | bytes, data_size: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Save data to file from byte array (write), returns true on success"""
	...

def export_data_as_code(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export data to code (.h), returns true on success"""
	...

def load_file_text(file_name: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Load text data from file (read), returns a '\0' terminated string"""
	...

def unload_file_text(text: ctypes.c_char_p | bytes) -> None:
	"""Unload file text data allocated by LoadFileText()"""
	...

def save_file_text(file_name: ctypes.c_char_p | bytes, text: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Save text data to file (write), string must be '\0' terminated, returns true on success"""
	...

def file_exists(file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check if file exists"""
	...

def directory_exists(dir_path: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check if a directory path exists"""
	...

def is_file_extension(file_name: ctypes.c_char_p | bytes, ext: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check file extension (including point: .png, .wav)"""
	...

def get_file_length(file_name: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
	...

def get_file_extension(file_name: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get pointer to extension for a filename string (includes dot: '.png')"""
	...

def get_file_name(file_path: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get pointer to filename for a path string"""
	...

def get_file_name_without_ext(file_path: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get filename string without extension (uses static string)"""
	...

def get_directory_path(file_path: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get full path for a given fileName with path (uses static string)"""
	...

def get_prev_directory_path(dir_path: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get previous directory path for a given path (uses static string)"""
	...

def get_working_directory() -> ctypes.c_char_p | bytes:
	"""Get current working directory (uses static string)"""
	...

def get_application_directory() -> ctypes.c_char_p | bytes:
	"""Get the directory of the running application (uses static string)"""
	...

def make_directory(dir_path: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Create directories (including full path requested), returns 0 on success"""
	...

def change_directory(dir: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Change working directory, return true on success"""
	...

def is_path_file(path: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check if a given path is a file or a directory"""
	...

def is_file_name_valid(file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check if fileName is valid for the platform/OS"""
	...

def load_directory_files(dir_path: ctypes.c_char_p | bytes) -> FilePathList:
	"""Load directory filepaths"""
	...

def load_directory_files_ex(base_path: ctypes.c_char_p | bytes, filter: ctypes.c_char_p | bytes, scan_subdirs: ctypes.c_bool | bool) -> FilePathList:
	"""Load directory filepaths with extension filtering and recursive directory scan. Use 'DIR' in the filter string to include directories in the result"""
	...

def unload_directory_files(files: FilePathList) -> None:
	"""Unload filepaths"""
	...

def is_file_dropped() -> ctypes.c_bool | bool:
	"""Check if a file has been dropped into window"""
	...

def load_dropped_files() -> FilePathList:
	"""Load dropped filepaths"""
	...

def unload_dropped_files(files: FilePathList) -> None:
	"""Unload dropped filepaths"""
	...

def get_file_mod_time(file_name: ctypes.c_char_p | bytes) -> ctypes.c_long | int:
	"""Get file modification time (last write time)"""
	...

def compress_data(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, comp_data_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Compress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def decompress_data(comp_data: ctypes.POINTER(ctypes.c_ubyte), comp_data_size: ctypes.c_int | int, data_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Decompress data (DEFLATE algorithm), memory must be MemFree()"""
	...

def encode_data_base64(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, output_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_char_p | bytes:
	"""Encode data to Base64 string, memory must be MemFree()"""
	...

def decode_data_base64(data: ctypes.POINTER(ctypes.c_ubyte), output_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Decode Base64 string data, memory must be MemFree()"""
	...

def compute_crc32(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> ctypes.c_uint | int:
	"""Compute CRC32 hash code"""
	...

def compute_md5(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> ctypes.POINTER(ctypes.c_uint):
	"""Compute MD5 hash code, returns static int[4] (16 bytes)"""
	...

def compute_sha1(data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> ctypes.POINTER(ctypes.c_uint):
	"""Compute SHA1 hash code, returns static int[5] (20 bytes)"""
	...

def load_automation_event_list(file_name: ctypes.c_char_p | bytes) -> AutomationEventList:
	"""Load automation events list from file, NULL for empty list, capacity = MAX_AUTOMATION_EVENTS"""
	...

def unload_automation_event_list(list: AutomationEventList) -> None:
	"""Unload automation events list from file"""
	...

def export_automation_event_list(list: AutomationEventList, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export automation events list as text file"""
	...

def set_automation_event_list(list: ctypes.POINTER(AutomationEventList)) -> None:
	"""Set automation event list to record to"""
	...

def set_automation_event_base_frame(frame: ctypes.c_int | int) -> None:
	"""Set automation event internal base frame to start recording"""
	...

def start_automation_event_recording() -> None:
	"""Start recording automation events (AutomationEventList must be set)"""
	...

def stop_automation_event_recording() -> None:
	"""Stop recording automation events"""
	...

def play_automation_event(event: AutomationEvent) -> None:
	"""Play a recorded automation event"""
	...

def is_key_pressed(key: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a key has been pressed once"""
	...

def is_key_pressed_repeat(key: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a key has been pressed again"""
	...

def is_key_down(key: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a key is being pressed"""
	...

def is_key_released(key: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a key has been released once"""
	...

def is_key_up(key: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a key is NOT being pressed"""
	...

def get_key_pressed() -> ctypes.c_int | int:
	"""Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
	...

def get_char_pressed() -> ctypes.c_int | int:
	"""Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
	...

def get_key_name(key: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Get name of a QWERTY key on the current keyboard layout (eg returns string 'q' for KEY_A on an AZERTY keyboard)"""
	...

def set_exit_key(key: ctypes.c_int | int) -> None:
	"""Set a custom key to exit program (default is ESC)"""
	...

def is_gamepad_available(gamepad: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a gamepad is available"""
	...

def get_gamepad_name(gamepad: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Get gamepad internal name id"""
	...

def is_gamepad_button_pressed(gamepad: ctypes.c_int | int, button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a gamepad button has been pressed once"""
	...

def is_gamepad_button_down(gamepad: ctypes.c_int | int, button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a gamepad button is being pressed"""
	...

def is_gamepad_button_released(gamepad: ctypes.c_int | int, button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a gamepad button has been released once"""
	...

def is_gamepad_button_up(gamepad: ctypes.c_int | int, button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a gamepad button is NOT being pressed"""
	...

def get_gamepad_button_pressed() -> ctypes.c_int | int:
	"""Get the last gamepad button pressed"""
	...

def get_gamepad_axis_count(gamepad: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get gamepad axis count for a gamepad"""
	...

def get_gamepad_axis_movement(gamepad: ctypes.c_int | int, axis: ctypes.c_int | int) -> ctypes.c_float | float:
	"""Get axis movement value for a gamepad axis"""
	...

def set_gamepad_mappings(mappings: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Set internal gamepad mappings (SDL_GameControllerDB)"""
	...

def set_gamepad_vibration(gamepad: ctypes.c_int | int, left_motor: ctypes.c_float | float, right_motor: ctypes.c_float | float, duration: ctypes.c_float | float) -> None:
	"""Set gamepad vibration for both motors (duration in seconds)"""
	...

def is_mouse_button_pressed(button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a mouse button has been pressed once"""
	...

def is_mouse_button_down(button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a mouse button is being pressed"""
	...

def is_mouse_button_released(button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a mouse button has been released once"""
	...

def is_mouse_button_up(button: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if a mouse button is NOT being pressed"""
	...

def get_mouse_x() -> ctypes.c_int | int:
	"""Get mouse position X"""
	...

def get_mouse_y() -> ctypes.c_int | int:
	"""Get mouse position Y"""
	...

def get_mouse_position() -> Vector2:
	"""Get mouse position XY"""
	...

def get_mouse_delta() -> Vector2:
	"""Get mouse delta between frames"""
	...

def set_mouse_position(x: ctypes.c_int | int, y: ctypes.c_int | int) -> None:
	"""Set mouse position XY"""
	...

def set_mouse_offset(offset_x: ctypes.c_int | int, offset_y: ctypes.c_int | int) -> None:
	"""Set mouse offset"""
	...

def set_mouse_scale(scale_x: ctypes.c_float | float, scale_y: ctypes.c_float | float) -> None:
	"""Set mouse scaling"""
	...

def get_mouse_wheel_move() -> ctypes.c_float | float:
	"""Get mouse wheel movement for X or Y, whichever is larger"""
	...

def get_mouse_wheel_move_v() -> Vector2:
	"""Get mouse wheel movement for both X and Y"""
	...

def set_mouse_cursor(cursor: ctypes.c_int | int) -> None:
	"""Set mouse cursor"""
	...

def get_touch_x() -> ctypes.c_int | int:
	"""Get touch position X for touch point 0 (relative to screen size)"""
	...

def get_touch_y() -> ctypes.c_int | int:
	"""Get touch position Y for touch point 0 (relative to screen size)"""
	...

def get_touch_position(index: ctypes.c_int | int) -> Vector2:
	"""Get touch position XY for a touch point index (relative to screen size)"""
	...

def get_touch_point_id(index: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get touch point identifier for given index"""
	...

def get_touch_point_count() -> ctypes.c_int | int:
	"""Get number of touch points"""
	...

def set_gestures_enabled(flags: ctypes.c_uint | int) -> None:
	"""Enable a set of gestures using flags"""
	...

def is_gesture_detected(gesture: ctypes.c_uint | int) -> ctypes.c_bool | bool:
	"""Check if a gesture have been detected"""
	...

def get_gesture_detected() -> ctypes.c_int | int:
	"""Get latest detected gesture"""
	...

def get_gesture_hold_duration() -> ctypes.c_float | float:
	"""Get gesture hold time in seconds"""
	...

def get_gesture_drag_vector() -> Vector2:
	"""Get gesture drag vector"""
	...

def get_gesture_drag_angle() -> ctypes.c_float | float:
	"""Get gesture drag angle"""
	...

def get_gesture_pinch_vector() -> Vector2:
	"""Get gesture pinch delta"""
	...

def get_gesture_pinch_angle() -> ctypes.c_float | float:
	"""Get gesture pinch angle"""
	...

def update_camera(camera: ctypes.POINTER(Camera), mode: ctypes.c_int | int) -> None:
	"""Update camera position for selected mode"""
	...

def update_camera_pro(camera: ctypes.POINTER(Camera), movement: Vector3, rotation: Vector3, zoom: ctypes.c_float | float) -> None:
	"""Update camera movement/rotation"""
	...

def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None:
	"""Set texture and rectangle to be used on shapes drawing"""
	...

def get_shapes_texture() -> Texture2D:
	"""Get texture that is used for shapes drawing"""
	...

def get_shapes_texture_rectangle() -> Rectangle:
	"""Get texture source rectangle that is used for shapes drawing"""
	...

def draw_pixel(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, color: Color) -> None:
	"""Draw a pixel using geometry [Can be slow, use with care]"""
	...

def draw_pixel_v(position: Vector2, color: Color) -> None:
	"""Draw a pixel using geometry (Vector version) [Can be slow, use with care]"""
	...

def draw_line(start_pos_x: ctypes.c_int | int, start_pos_y: ctypes.c_int | int, end_pos_x: ctypes.c_int | int, end_pos_y: ctypes.c_int | int, color: Color) -> None:
	"""Draw a line"""
	...

def draw_line_v(start_pos: Vector2, end_pos: Vector2, color: Color) -> None:
	"""Draw a line (using gl lines)"""
	...

def draw_line_ex(start_pos: Vector2, end_pos: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw a line (using triangles/quads)"""
	...

def draw_line_strip(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw lines sequence (using gl lines)"""
	...

def draw_line_bezier(start_pos: Vector2, end_pos: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw line segment cubic-bezier in-out interpolation"""
	...

def draw_circle(center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius: ctypes.c_float | float, color: Color) -> None:
	"""Draw a color-filled circle"""
	...

def draw_circle_sector(center: Vector2, radius: ctypes.c_float | float, start_angle: ctypes.c_float | float, end_angle: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw a piece of a circle"""
	...

def draw_circle_sector_lines(center: Vector2, radius: ctypes.c_float | float, start_angle: ctypes.c_float | float, end_angle: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw circle sector outline"""
	...

def draw_circle_gradient(center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius: ctypes.c_float | float, inner: Color, outer: Color) -> None:
	"""Draw a gradient-filled circle"""
	...

def draw_circle_v(center: Vector2, radius: ctypes.c_float | float, color: Color) -> None:
	"""Draw a color-filled circle (Vector version)"""
	...

def draw_circle_lines(center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius: ctypes.c_float | float, color: Color) -> None:
	"""Draw circle outline"""
	...

def draw_circle_lines_v(center: Vector2, radius: ctypes.c_float | float, color: Color) -> None:
	"""Draw circle outline (Vector version)"""
	...

def draw_ellipse(center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius_h: ctypes.c_float | float, radius_v: ctypes.c_float | float, color: Color) -> None:
	"""Draw ellipse"""
	...

def draw_ellipse_lines(center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius_h: ctypes.c_float | float, radius_v: ctypes.c_float | float, color: Color) -> None:
	"""Draw ellipse outline"""
	...

def draw_ring(center: Vector2, inner_radius: ctypes.c_float | float, outer_radius: ctypes.c_float | float, start_angle: ctypes.c_float | float, end_angle: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw ring"""
	...

def draw_ring_lines(center: Vector2, inner_radius: ctypes.c_float | float, outer_radius: ctypes.c_float | float, start_angle: ctypes.c_float | float, end_angle: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw ring outline"""
	...

def draw_rectangle(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw a color-filled rectangle (Vector version)"""
	...

def draw_rectangle_rec(rec: Rectangle, color: Color) -> None:
	"""Draw a color-filled rectangle"""
	...

def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: ctypes.c_float | float, color: Color) -> None:
	"""Draw a color-filled rectangle with pro parameters"""
	...

def draw_rectangle_gradient_v(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, top: Color, bottom: Color) -> None:
	"""Draw a vertical-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_h(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, left: Color, right: Color) -> None:
	"""Draw a horizontal-gradient-filled rectangle"""
	...

def draw_rectangle_gradient_ex(rec: Rectangle, top_left: Color, bottom_left: Color, top_right: Color, bottom_right: Color) -> None:
	"""Draw a gradient-filled rectangle with custom vertex colors"""
	...

def draw_rectangle_lines(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, color: Color) -> None:
	"""Draw rectangle outline"""
	...

def draw_rectangle_lines_ex(rec: Rectangle, line_thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw rectangle outline with extended parameters"""
	...

def draw_rectangle_rounded(rec: Rectangle, roundness: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw rectangle with rounded edges"""
	...

def draw_rectangle_rounded_lines(rec: Rectangle, roundness: ctypes.c_float | float, segments: ctypes.c_int | int, color: Color) -> None:
	"""Draw rectangle lines with rounded edges"""
	...

def draw_rectangle_rounded_lines_ex(rec: Rectangle, roundness: ctypes.c_float | float, segments: ctypes.c_int | int, line_thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw rectangle with rounded edges outline"""
	...

def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw triangle outline (vertex in counter-clockwise order!)"""
	...

def draw_triangle_fan(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw a triangle fan defined by points (first vertex is the center)"""
	...

def draw_triangle_strip(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_poly(center: Vector2, sides: ctypes.c_int | int, radius: ctypes.c_float | float, rotation: ctypes.c_float | float, color: Color) -> None:
	"""Draw a regular polygon (Vector version)"""
	...

def draw_poly_lines(center: Vector2, sides: ctypes.c_int | int, radius: ctypes.c_float | float, rotation: ctypes.c_float | float, color: Color) -> None:
	"""Draw a polygon outline of n sides"""
	...

def draw_poly_lines_ex(center: Vector2, sides: ctypes.c_int | int, radius: ctypes.c_float | float, rotation: ctypes.c_float | float, line_thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw a polygon outline of n sides with extended parameters"""
	...

def draw_spline_linear(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline: Linear, minimum 2 points"""
	...

def draw_spline_basis(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline: B-Spline, minimum 4 points"""
	...

def draw_spline_catmull_rom(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline: Catmull-Rom, minimum 4 points"""
	...

def draw_spline_bezier_quadratic(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline: Quadratic Bezier, minimum 3 points (1 control point): [p1, c2, p3, c4...]"""
	...

def draw_spline_bezier_cubic(points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline: Cubic Bezier, minimum 4 points (2 control points): [p1, c2, c3, p4, c5, c6...]"""
	...

def draw_spline_segment_linear(p1: Vector2, p2: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline segment: Linear, 2 points"""
	...

def draw_spline_segment_basis(p1: Vector2, p2: Vector2, p3: Vector2, p4: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline segment: B-Spline, 4 points"""
	...

def draw_spline_segment_catmull_rom(p1: Vector2, p2: Vector2, p3: Vector2, p4: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline segment: Catmull-Rom, 4 points"""
	...

def draw_spline_segment_bezier_quadratic(p1: Vector2, c2: Vector2, p3: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline segment: Quadratic Bezier, 2 points, 1 control point"""
	...

def draw_spline_segment_bezier_cubic(p1: Vector2, c2: Vector2, c3: Vector2, p4: Vector2, thick: ctypes.c_float | float, color: Color) -> None:
	"""Draw spline segment: Cubic Bezier, 2 points, 2 control points"""
	...

def get_spline_point_linear(start_pos: Vector2, end_pos: Vector2, t: ctypes.c_float | float) -> Vector2:
	"""Get (evaluate) spline point: Linear"""
	...

def get_spline_point_basis(p1: Vector2, p2: Vector2, p3: Vector2, p4: Vector2, t: ctypes.c_float | float) -> Vector2:
	"""Get (evaluate) spline point: B-Spline"""
	...

def get_spline_point_catmull_rom(p1: Vector2, p2: Vector2, p3: Vector2, p4: Vector2, t: ctypes.c_float | float) -> Vector2:
	"""Get (evaluate) spline point: Catmull-Rom"""
	...

def get_spline_point_bezier_quad(p1: Vector2, c2: Vector2, p3: Vector2, t: ctypes.c_float | float) -> Vector2:
	"""Get (evaluate) spline point: Quadratic Bezier"""
	...

def get_spline_point_bezier_cubic(p1: Vector2, c2: Vector2, c3: Vector2, p4: Vector2, t: ctypes.c_float | float) -> Vector2:
	"""Get (evaluate) spline point: Cubic Bezier"""
	...

def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> ctypes.c_bool | bool:
	"""Check collision between two rectangles"""
	...

def check_collision_circles(center1: Vector2, radius1: ctypes.c_float | float, center2: Vector2, radius2: ctypes.c_float | float) -> ctypes.c_bool | bool:
	"""Check collision between two circles"""
	...

def check_collision_circle_rec(center: Vector2, radius: ctypes.c_float | float, rec: Rectangle) -> ctypes.c_bool | bool:
	"""Check collision between circle and rectangle"""
	...

def check_collision_circle_line(center: Vector2, radius: ctypes.c_float | float, p1: Vector2, p2: Vector2) -> ctypes.c_bool | bool:
	"""Check if circle collides with a line created betweeen two points [p1] and [p2]"""
	...

def check_collision_point_rec(point: Vector2, rec: Rectangle) -> ctypes.c_bool | bool:
	"""Check if point is inside rectangle"""
	...

def check_collision_point_circle(point: Vector2, center: Vector2, radius: ctypes.c_float | float) -> ctypes.c_bool | bool:
	"""Check if point is inside circle"""
	...

def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> ctypes.c_bool | bool:
	"""Check if point is inside a triangle"""
	...

def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
	...

def check_collision_point_poly(point: Vector2, points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int) -> ctypes.c_bool | bool:
	"""Check if point is within a polygon described by array of vertices"""
	...

def check_collision_lines(start_pos1: Vector2, end_pos1: Vector2, start_pos2: Vector2, end_pos2: Vector2, collision_point: ctypes.POINTER(Vector2)) -> ctypes.c_bool | bool:
	"""Check the collision between two lines defined by two points each, returns collision point by reference"""
	...

def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle:
	"""Get collision rectangle for two rectangles collision"""
	...

def load_image(file_name: ctypes.c_char_p | bytes) -> Image:
	"""Load image from file into CPU memory (RAM)"""
	...

def load_image_raw(file_name: ctypes.c_char_p | bytes, width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int, header_size: ctypes.c_int | int) -> Image:
	"""Load image from RAW file data"""
	...

def load_image_anim(file_name: ctypes.c_char_p | bytes, frames: ctypes.POINTER(ctypes.c_int)) -> Image:
	"""Load image sequence from file (frames appended to image.data)"""
	...

def load_image_anim_from_memory(file_type: ctypes.c_char_p | bytes, file_data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, frames: ctypes.POINTER(ctypes.c_int)) -> Image:
	"""Load image sequence from memory buffer"""
	...

def load_image_from_memory(file_type: ctypes.c_char_p | bytes, file_data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> Image:
	"""Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
	...

def load_image_from_texture(texture: Texture2D) -> Image:
	"""Load image from GPU texture data"""
	...

def load_image_from_screen() -> Image:
	"""Load image from screen buffer and (screenshot)"""
	...

def is_image_valid(image: Image) -> ctypes.c_bool | bool:
	"""Check if an image is valid (data and parameters)"""
	...

def unload_image(image: Image) -> None:
	"""Unload image from CPU memory (RAM)"""
	...

def export_image(image: Image, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export image data to file, returns true on success"""
	...

def export_image_to_memory(image: Image, file_type: ctypes.c_char_p | bytes, file_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_ubyte):
	"""Export image to memory buffer"""
	...

def export_image_as_code(image: Image, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export image as code file defining an array of bytes, returns true on success"""
	...

def gen_image_color(width: ctypes.c_int | int, height: ctypes.c_int | int, color: Color) -> Image:
	"""Generate image: plain color"""
	...

def gen_image_gradient_linear(width: ctypes.c_int | int, height: ctypes.c_int | int, direction: ctypes.c_int | int, start: Color, end: Color) -> Image:
	"""Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient"""
	...

def gen_image_gradient_radial(width: ctypes.c_int | int, height: ctypes.c_int | int, density: ctypes.c_float | float, inner: Color, outer: Color) -> Image:
	"""Generate image: radial gradient"""
	...

def gen_image_gradient_square(width: ctypes.c_int | int, height: ctypes.c_int | int, density: ctypes.c_float | float, inner: Color, outer: Color) -> Image:
	"""Generate image: square gradient"""
	...

def gen_image_checked(width: ctypes.c_int | int, height: ctypes.c_int | int, checks_x: ctypes.c_int | int, checks_y: ctypes.c_int | int, col1: Color, col2: Color) -> Image:
	"""Generate image: checked"""
	...

def gen_image_white_noise(width: ctypes.c_int | int, height: ctypes.c_int | int, factor: ctypes.c_float | float) -> Image:
	"""Generate image: white noise"""
	...

def gen_image_perlin_noise(width: ctypes.c_int | int, height: ctypes.c_int | int, offset_x: ctypes.c_int | int, offset_y: ctypes.c_int | int, scale: ctypes.c_float | float) -> Image:
	"""Generate image: perlin noise"""
	...

def gen_image_cellular(width: ctypes.c_int | int, height: ctypes.c_int | int, tile_size: ctypes.c_int | int) -> Image:
	"""Generate image: cellular algorithm, bigger tileSize means bigger cells"""
	...

def gen_image_text(width: ctypes.c_int | int, height: ctypes.c_int | int, text: ctypes.c_char_p | bytes) -> Image:
	"""Generate image: grayscale image from text data"""
	...

def image_copy(image: Image) -> Image:
	"""Create an image duplicate (useful for transformations)"""
	...

def image_from_image(image: Image, rec: Rectangle) -> Image:
	"""Create an image from another image piece"""
	...

def image_from_channel(image: Image, selected_channel: ctypes.c_int | int) -> Image:
	"""Create an image from a selected channel of another image (GRAYSCALE)"""
	...

def image_text(text: ctypes.c_char_p | bytes, font_size: ctypes.c_int | int, color: Color) -> Image:
	"""Create an image from text (default font)"""
	...

def image_text_ex(font: Font, text: ctypes.c_char_p | bytes, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float, tint: Color) -> Image:
	"""Create an image from text (custom sprite font)"""
	...

def image_format(image: ctypes.POINTER(Image), new_format: ctypes.c_int | int) -> None:
	"""Convert image data to desired format"""
	...

def image_to_pot(image: ctypes.POINTER(Image), fill: Color) -> None:
	"""Convert image to POT (power-of-two)"""
	...

def image_crop(image: ctypes.POINTER(Image), crop: Rectangle) -> None:
	"""Crop an image to a defined rectangle"""
	...

def image_alpha_crop(image: ctypes.POINTER(Image), threshold: ctypes.c_float | float) -> None:
	"""Crop image depending on alpha value"""
	...

def image_alpha_clear(image: ctypes.POINTER(Image), color: Color, threshold: ctypes.c_float | float) -> None:
	"""Clear alpha channel to desired color"""
	...

def image_alpha_mask(image: ctypes.POINTER(Image), alpha_mask: Image) -> None:
	"""Apply alpha mask to image"""
	...

def image_alpha_premultiply(image: ctypes.POINTER(Image)) -> None:
	"""Premultiply alpha channel"""
	...

def image_blur_gaussian(image: ctypes.POINTER(Image), blur_size: ctypes.c_int | int) -> None:
	"""Apply Gaussian blur using a box blur approximation"""
	...

def image_kernel_convolution(image: ctypes.POINTER(Image), kernel: ctypes.POINTER(ctypes.c_float), kernel_size: ctypes.c_int | int) -> None:
	"""Apply custom square convolution kernel to image"""
	...

def image_resize(image: ctypes.POINTER(Image), new_width: ctypes.c_int | int, new_height: ctypes.c_int | int) -> None:
	"""Resize image (Bicubic scaling algorithm)"""
	...

def image_resize_nn(image: ctypes.POINTER(Image), new_width: ctypes.c_int | int, new_height: ctypes.c_int | int) -> None:
	"""Resize image (Nearest-Neighbor scaling algorithm)"""
	...

def image_resize_canvas(image: ctypes.POINTER(Image), new_width: ctypes.c_int | int, new_height: ctypes.c_int | int, offset_x: ctypes.c_int | int, offset_y: ctypes.c_int | int, fill: Color) -> None:
	"""Resize canvas and fill with color"""
	...

def image_mipmaps(image: ctypes.POINTER(Image)) -> None:
	"""Compute all mipmap levels for a provided image"""
	...

def image_dither(image: ctypes.POINTER(Image), r_bpp: ctypes.c_int | int, g_bpp: ctypes.c_int | int, b_bpp: ctypes.c_int | int, a_bpp: ctypes.c_int | int) -> None:
	"""Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
	...

def image_flip_vertical(image: ctypes.POINTER(Image)) -> None:
	"""Flip image vertically"""
	...

def image_flip_horizontal(image: ctypes.POINTER(Image)) -> None:
	"""Flip image horizontally"""
	...

def image_rotate(image: ctypes.POINTER(Image), degrees: ctypes.c_int | int) -> None:
	"""Rotate image by input angle in degrees (-359 to 359)"""
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

def image_color_contrast(image: ctypes.POINTER(Image), contrast: ctypes.c_float | float) -> None:
	"""Modify image color: contrast (-100 to 100)"""
	...

def image_color_brightness(image: ctypes.POINTER(Image), brightness: ctypes.c_int | int) -> None:
	"""Modify image color: brightness (-255 to 255)"""
	...

def image_color_replace(image: ctypes.POINTER(Image), color: Color, replace: Color) -> None:
	"""Modify image color: replace color"""
	...

def load_image_colors(image: Image) -> ctypes.POINTER(Color):
	"""Load color data from image as a Color array (RGBA - 32bit)"""
	...

def load_image_palette(image: Image, max_palette_size: ctypes.c_int | int, color_count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(Color):
	"""Load colors palette from image as a Color array (RGBA - 32bit)"""
	...

def unload_image_colors(colors: ctypes.POINTER(Color)) -> None:
	"""Unload color data loaded with LoadImageColors()"""
	...

def unload_image_palette(colors: ctypes.POINTER(Color)) -> None:
	"""Unload colors palette loaded with LoadImagePalette()"""
	...

def get_image_alpha_border(image: Image, threshold: ctypes.c_float | float) -> Rectangle:
	"""Get image alpha border rectangle"""
	...

def get_image_color(image: Image, x: ctypes.c_int | int, y: ctypes.c_int | int) -> Color:
	"""Get image pixel color at (x, y) position"""
	...

def image_clear_background(dst: ctypes.POINTER(Image), color: Color) -> None:
	"""Clear image background with given color"""
	...

def image_draw_pixel(dst: ctypes.POINTER(Image), pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, color: Color) -> None:
	"""Draw pixel within an image"""
	...

def image_draw_pixel_v(dst: ctypes.POINTER(Image), position: Vector2, color: Color) -> None:
	"""Draw pixel within an image (Vector version)"""
	...

def image_draw_line(dst: ctypes.POINTER(Image), start_pos_x: ctypes.c_int | int, start_pos_y: ctypes.c_int | int, end_pos_x: ctypes.c_int | int, end_pos_y: ctypes.c_int | int, color: Color) -> None:
	"""Draw line within an image"""
	...

def image_draw_line_v(dst: ctypes.POINTER(Image), start: Vector2, end: Vector2, color: Color) -> None:
	"""Draw line within an image (Vector version)"""
	...

def image_draw_line_ex(dst: ctypes.POINTER(Image), start: Vector2, end: Vector2, thick: ctypes.c_int | int, color: Color) -> None:
	"""Draw a line defining thickness within an image"""
	...

def image_draw_circle(dst: ctypes.POINTER(Image), center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius: ctypes.c_int | int, color: Color) -> None:
	"""Draw a filled circle within an image"""
	...

def image_draw_circle_v(dst: ctypes.POINTER(Image), center: Vector2, radius: ctypes.c_int | int, color: Color) -> None:
	"""Draw a filled circle within an image (Vector version)"""
	...

def image_draw_circle_lines(dst: ctypes.POINTER(Image), center_x: ctypes.c_int | int, center_y: ctypes.c_int | int, radius: ctypes.c_int | int, color: Color) -> None:
	"""Draw circle outline within an image"""
	...

def image_draw_circle_lines_v(dst: ctypes.POINTER(Image), center: Vector2, radius: ctypes.c_int | int, color: Color) -> None:
	"""Draw circle outline within an image (Vector version)"""
	...

def image_draw_rectangle(dst: ctypes.POINTER(Image), pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, width: ctypes.c_int | int, height: ctypes.c_int | int, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_v(dst: ctypes.POINTER(Image), position: Vector2, size: Vector2, color: Color) -> None:
	"""Draw rectangle within an image (Vector version)"""
	...

def image_draw_rectangle_rec(dst: ctypes.POINTER(Image), rec: Rectangle, color: Color) -> None:
	"""Draw rectangle within an image"""
	...

def image_draw_rectangle_lines(dst: ctypes.POINTER(Image), rec: Rectangle, thick: ctypes.c_int | int, color: Color) -> None:
	"""Draw rectangle lines within an image"""
	...

def image_draw_triangle(dst: ctypes.POINTER(Image), v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw triangle within an image"""
	...

def image_draw_triangle_ex(dst: ctypes.POINTER(Image), v1: Vector2, v2: Vector2, v3: Vector2, c1: Color, c2: Color, c3: Color) -> None:
	"""Draw triangle with interpolated colors within an image"""
	...

def image_draw_triangle_lines(dst: ctypes.POINTER(Image), v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
	"""Draw triangle outline within an image"""
	...

def image_draw_triangle_fan(dst: ctypes.POINTER(Image), points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw a triangle fan defined by points within an image (first vertex is the center)"""
	...

def image_draw_triangle_strip(dst: ctypes.POINTER(Image), points: ctypes.POINTER(Vector2), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw a triangle strip defined by points within an image"""
	...

def image_draw(dst: ctypes.POINTER(Image), src: Image, src_rec: Rectangle, dst_rec: Rectangle, tint: Color) -> None:
	"""Draw a source image within a destination image (tint applied to source)"""
	...

def image_draw_text(dst: ctypes.POINTER(Image), text: ctypes.c_char_p | bytes, pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, font_size: ctypes.c_int | int, color: Color) -> None:
	"""Draw text (using default font) within an image (destination)"""
	...

def image_draw_text_ex(dst: ctypes.POINTER(Image), font: Font, text: ctypes.c_char_p | bytes, position: Vector2, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float, tint: Color) -> None:
	"""Draw text (custom sprite font) within an image (destination)"""
	...

def load_texture(file_name: ctypes.c_char_p | bytes) -> Texture2D:
	"""Load texture from file into GPU memory (VRAM)"""
	...

def load_texture_from_image(image: Image) -> Texture2D:
	"""Load texture from image data"""
	...

def load_texture_cubemap(image: Image, layout: ctypes.c_int | int) -> TextureCubemap:
	"""Load cubemap from image, multiple image cubemap layouts supported"""
	...

def load_render_texture(width: ctypes.c_int | int, height: ctypes.c_int | int) -> RenderTexture2D:
	"""Load texture for rendering (framebuffer)"""
	...

def is_texture_valid(texture: Texture2D) -> ctypes.c_bool | bool:
	"""Check if a texture is valid (loaded in GPU)"""
	...

def unload_texture(texture: Texture2D) -> None:
	"""Unload texture from GPU memory (VRAM)"""
	...

def is_render_texture_valid(target: RenderTexture2D) -> ctypes.c_bool | bool:
	"""Check if a render texture is valid (loaded in GPU)"""
	...

def unload_render_texture(target: RenderTexture2D) -> None:
	"""Unload render texture from GPU memory (VRAM)"""
	...

def update_texture(texture: Texture2D, pixels: ctypes.c_void_p | bytes) -> None:
	"""Update GPU texture with new data"""
	...

def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: ctypes.c_void_p | bytes) -> None:
	"""Update GPU texture rectangle with new data"""
	...

def gen_texture_mipmaps(texture: ctypes.POINTER(Texture2D)) -> None:
	"""Generate GPU mipmaps for a texture"""
	...

def set_texture_filter(texture: Texture2D, filter: ctypes.c_int | int) -> None:
	"""Set texture scaling filter mode"""
	...

def set_texture_wrap(texture: Texture2D, wrap: ctypes.c_int | int) -> None:
	"""Set texture wrapping mode"""
	...

def draw_texture(texture: Texture2D, pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, tint: Color) -> None:
	"""Draw a Texture2D"""
	...

def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None:
	"""Draw a Texture2D with position defined as Vector2"""
	...

def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: ctypes.c_float | float, scale: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a Texture2D with extended parameters"""
	...

def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle"""
	...

def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a part of a texture defined by a rectangle with 'pro' parameters"""
	...

def draw_texture_n_patch(texture: Texture2D, n_patch_info: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: ctypes.c_float | float, tint: Color) -> None:
	"""Draws a texture (or part of it) that stretches or shrinks nicely"""
	...

def color_is_equal(col1: Color, col2: Color) -> ctypes.c_bool | bool:
	"""Check if two colors are equal"""
	...

def fade(color: Color, alpha: ctypes.c_float | float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_to_int(color: Color) -> ctypes.c_int | int:
	"""Get hexadecimal value for a Color (0xRRGGBBAA)"""
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

def color_from_hsv(hue: ctypes.c_float | float, saturation: ctypes.c_float | float, value: ctypes.c_float | float) -> Color:
	"""Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
	...

def color_tint(color: Color, tint: Color) -> Color:
	"""Get color multiplied with another color"""
	...

def color_brightness(color: Color, factor: ctypes.c_float | float) -> Color:
	"""Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
	...

def color_contrast(color: Color, contrast: ctypes.c_float | float) -> Color:
	"""Get color with contrast correction, contrast values between -1.0f and 1.0f"""
	...

def color_alpha(color: Color, alpha: ctypes.c_float | float) -> Color:
	"""Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
	...

def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color:
	"""Get src alpha-blended into dst color with tint"""
	...

def color_lerp(color1: Color, color2: Color, factor: ctypes.c_float | float) -> Color:
	"""Get color lerp interpolation between two colors, factor [0.0f..1.0f]"""
	...

def get_color(hex_value: ctypes.c_uint | int) -> Color:
	"""Get Color structure from hexadecimal value"""
	...

def get_pixel_color(src_ptr: ctypes.c_void_p | bytes, format: ctypes.c_int | int) -> Color:
	"""Get Color from a source pixel pointer of certain format"""
	...

def set_pixel_color(dst_ptr: ctypes.c_void_p | bytes, color: Color, format: ctypes.c_int | int) -> None:
	"""Set color formatted into destination pixel pointer"""
	...

def get_pixel_data_size(width: ctypes.c_int | int, height: ctypes.c_int | int, format: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get pixel data size in bytes for certain format"""
	...

def get_font_default() -> Font:
	"""Get the default Font"""
	...

def load_font(file_name: ctypes.c_char_p | bytes) -> Font:
	"""Load font from file into GPU memory (VRAM)"""
	...

def load_font_ex(file_name: ctypes.c_char_p | bytes, font_size: ctypes.c_int | int, codepoints: ctypes.POINTER(ctypes.c_int), codepoint_count: ctypes.c_int | int) -> Font:
	"""Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character set, font size is provided in pixels height"""
	...

def load_font_from_image(image: Image, key: Color, first_char: ctypes.c_int | int) -> Font:
	"""Load font from Image (XNA style)"""
	...

def load_font_from_memory(file_type: ctypes.c_char_p | bytes, file_data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, font_size: ctypes.c_int | int, codepoints: ctypes.POINTER(ctypes.c_int), codepoint_count: ctypes.c_int | int) -> Font:
	"""Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
	...

def is_font_valid(font: Font) -> ctypes.c_bool | bool:
	"""Check if a font is valid (font data loaded, WARNING: GPU texture not checked)"""
	...

def load_font_data(file_data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int, font_size: ctypes.c_int | int, codepoints: ctypes.POINTER(ctypes.c_int), codepoint_count: ctypes.c_int | int, type: ctypes.c_int | int) -> ctypes.POINTER(GlyphInfo):
	"""Load font data for further use"""
	...

def gen_image_font_atlas(glyphs: ctypes.POINTER(GlyphInfo), glyph_recs: ctypes.POINTER(ctypes.POINTER(Rectangle)), glyph_count: ctypes.c_int | int, font_size: ctypes.c_int | int, padding: ctypes.c_int | int, pack_method: ctypes.c_int | int) -> Image:
	"""Generate image font atlas using chars info"""
	...

def unload_font_data(glyphs: ctypes.POINTER(GlyphInfo), glyph_count: ctypes.c_int | int) -> None:
	"""Unload font chars info data (RAM)"""
	...

def unload_font(font: Font) -> None:
	"""Unload font from GPU memory (VRAM)"""
	...

def export_font_as_code(font: Font, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export font as code file, returns true on success"""
	...

def draw_fps(pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int) -> None:
	"""Draw current FPS"""
	...

def draw_text(text: ctypes.c_char_p | bytes, pos_x: ctypes.c_int | int, pos_y: ctypes.c_int | int, font_size: ctypes.c_int | int, color: Color) -> None:
	"""Draw text (using default font)"""
	...

def draw_text_ex(font: Font, text: ctypes.c_char_p | bytes, position: Vector2, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float, tint: Color) -> None:
	"""Draw text using font and additional parameters"""
	...

def draw_text_pro(font: Font, text: ctypes.c_char_p | bytes, position: Vector2, origin: Vector2, rotation: ctypes.c_float | float, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float, tint: Color) -> None:
	"""Draw text using Font and pro parameters (rotation)"""
	...

def draw_text_codepoint(font: Font, codepoint: ctypes.c_int | int, position: Vector2, font_size: ctypes.c_float | float, tint: Color) -> None:
	"""Draw one character (codepoint)"""
	...

def draw_text_codepoints(font: Font, codepoints: ctypes.POINTER(ctypes.c_int), codepoint_count: ctypes.c_int | int, position: Vector2, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float, tint: Color) -> None:
	"""Draw multiple character (codepoint)"""
	...

def set_text_line_spacing(spacing: ctypes.c_int | int) -> None:
	"""Set vertical line spacing when drawing with line-breaks"""
	...

def measure_text(text: ctypes.c_char_p | bytes, font_size: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Measure string width for default font"""
	...

def measure_text_ex(font: Font, text: ctypes.c_char_p | bytes, font_size: ctypes.c_float | float, spacing: ctypes.c_float | float) -> Vector2:
	"""Measure string size for Font"""
	...

def get_glyph_index(font: Font, codepoint: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_info(font: Font, codepoint: ctypes.c_int | int) -> GlyphInfo:
	"""Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
	...

def get_glyph_atlas_rec(font: Font, codepoint: ctypes.c_int | int) -> Rectangle:
	"""Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
	...

def load_utf8(codepoints: ctypes.POINTER(ctypes.c_int), length: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Load UTF-8 text encoded from codepoints array"""
	...

def unload_utf8(text: ctypes.c_char_p | bytes) -> None:
	"""Unload UTF-8 text encoded from codepoints array"""
	...

def load_codepoints(text: ctypes.c_char_p | bytes, count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.c_int):
	"""Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
	...

def unload_codepoints(codepoints: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Unload codepoints data from memory"""
	...

def get_codepoint_count(text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get total number of codepoints in a UTF-8 encoded string"""
	...

def get_codepoint(text: ctypes.c_char_p | bytes, codepoint_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def get_codepoint_next(text: ctypes.c_char_p | bytes, codepoint_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def get_codepoint_previous(text: ctypes.c_char_p | bytes, codepoint_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
	...

def codepoint_to_utf8(codepoint: ctypes.c_int | int, utf8_size: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_char_p | bytes:
	"""Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
	...

def text_copy(dst: ctypes.c_char_p | bytes, src: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Copy one string to another, returns bytes copied"""
	...

def text_is_equal(text1: ctypes.c_char_p | bytes, text2: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Check if two text string are equal"""
	...

def text_length(text: ctypes.c_char_p | bytes) -> ctypes.c_uint | int:
	"""Get text length, checks for '\0' ending"""
	...

def text_format(text: ctypes.c_char_p | bytes, args: ...) -> ctypes.c_char_p | bytes:
	"""Text formatting with variables (sprintf() style)"""
	...

def text_subtext(text: ctypes.c_char_p | bytes, position: ctypes.c_int | int, length: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Get a piece of a text string"""
	...

def text_replace(text: ctypes.c_char_p | bytes, replace: ctypes.c_char_p | bytes, by: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Replace text string (WARNING: memory must be freed!)"""
	...

def text_insert(text: ctypes.c_char_p | bytes, insert: ctypes.c_char_p | bytes, position: ctypes.c_int | int) -> ctypes.c_char_p | bytes:
	"""Insert text in a position (WARNING: memory must be freed!)"""
	...

def text_join(text_list: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int | int, delimiter: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Join text strings with delimiter"""
	...

def text_split(text: ctypes.c_char_p | bytes, delimiter: ctypes.c_char, count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ctypes.POINTER(ctypes.c_char)):
	"""Split text into multiple strings"""
	...

def text_append(text: ctypes.c_char_p | bytes, append: ctypes.c_char_p | bytes, position: ctypes.POINTER(ctypes.c_int)) -> None:
	"""Append text at specific position and move cursor!"""
	...

def text_find_index(text: ctypes.c_char_p | bytes, find: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Find first text occurrence within a string"""
	...

def text_to_upper(text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get upper case version of provided string"""
	...

def text_to_lower(text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get lower case version of provided string"""
	...

def text_to_pascal(text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get Pascal case notation version of provided string"""
	...

def text_to_snake(text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get Snake case notation version of provided string"""
	...

def text_to_camel(text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get Camel case notation version of provided string"""
	...

def text_to_integer(text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Get integer value from text"""
	...

def text_to_float(text: ctypes.c_char_p | bytes) -> ctypes.c_float | float:
	"""Get float value from text"""
	...

def draw_line_3d(start_pos: Vector3, end_pos: Vector3, color: Color) -> None:
	"""Draw a line in 3D world space"""
	...

def draw_point_3d(position: Vector3, color: Color) -> None:
	"""Draw a point in 3D space, actually a small line"""
	...

def draw_circle_3d(center: Vector3, radius: ctypes.c_float | float, rotation_axis: Vector3, rotation_angle: ctypes.c_float | float, color: Color) -> None:
	"""Draw a circle in 3D world space"""
	...

def draw_triangle_3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None:
	"""Draw a color-filled triangle (vertex in counter-clockwise order!)"""
	...

def draw_triangle_strip_3d(points: ctypes.POINTER(Vector3), point_count: ctypes.c_int | int, color: Color) -> None:
	"""Draw a triangle strip defined by points"""
	...

def draw_cube(position: Vector3, width: ctypes.c_float | float, height: ctypes.c_float | float, length: ctypes.c_float | float, color: Color) -> None:
	"""Draw cube"""
	...

def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube (Vector version)"""
	...

def draw_cube_wires(position: Vector3, width: ctypes.c_float | float, height: ctypes.c_float | float, length: ctypes.c_float | float, color: Color) -> None:
	"""Draw cube wires"""
	...

def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None:
	"""Draw cube wires (Vector version)"""
	...

def draw_sphere(center_pos: Vector3, radius: ctypes.c_float | float, color: Color) -> None:
	"""Draw sphere"""
	...

def draw_sphere_ex(center_pos: Vector3, radius: ctypes.c_float | float, rings: ctypes.c_int | int, slices: ctypes.c_int | int, color: Color) -> None:
	"""Draw sphere with extended parameters"""
	...

def draw_sphere_wires(center_pos: Vector3, radius: ctypes.c_float | float, rings: ctypes.c_int | int, slices: ctypes.c_int | int, color: Color) -> None:
	"""Draw sphere wires"""
	...

def draw_cylinder(position: Vector3, radius_top: ctypes.c_float | float, radius_bottom: ctypes.c_float | float, height: ctypes.c_float | float, slices: ctypes.c_int | int, color: Color) -> None:
	"""Draw a cylinder/cone"""
	...

def draw_cylinder_ex(start_pos: Vector3, end_pos: Vector3, start_radius: ctypes.c_float | float, end_radius: ctypes.c_float | float, sides: ctypes.c_int | int, color: Color) -> None:
	"""Draw a cylinder with base at startPos and top at endPos"""
	...

def draw_cylinder_wires(position: Vector3, radius_top: ctypes.c_float | float, radius_bottom: ctypes.c_float | float, height: ctypes.c_float | float, slices: ctypes.c_int | int, color: Color) -> None:
	"""Draw a cylinder/cone wires"""
	...

def draw_cylinder_wires_ex(start_pos: Vector3, end_pos: Vector3, start_radius: ctypes.c_float | float, end_radius: ctypes.c_float | float, sides: ctypes.c_int | int, color: Color) -> None:
	"""Draw a cylinder wires with base at startPos and top at endPos"""
	...

def draw_capsule(start_pos: Vector3, end_pos: Vector3, radius: ctypes.c_float | float, slices: ctypes.c_int | int, rings: ctypes.c_int | int, color: Color) -> None:
	"""Draw a capsule with the center of its sphere caps at startPos and endPos"""
	...

def draw_capsule_wires(start_pos: Vector3, end_pos: Vector3, radius: ctypes.c_float | float, slices: ctypes.c_int | int, rings: ctypes.c_int | int, color: Color) -> None:
	"""Draw capsule wireframe with the center of its sphere caps at startPos and endPos"""
	...

def draw_plane(center_pos: Vector3, size: Vector2, color: Color) -> None:
	"""Draw a plane XZ"""
	...

def draw_ray(ray: Ray, color: Color) -> None:
	"""Draw a ray line"""
	...

def draw_grid(slices: ctypes.c_int | int, spacing: ctypes.c_float | float) -> None:
	"""Draw a grid (centered at (0, 0, 0))"""
	...

def load_model(file_name: ctypes.c_char_p | bytes) -> Model:
	"""Load model from files (meshes and materials)"""
	...

def load_model_from_mesh(mesh: Mesh) -> Model:
	"""Load model from generated mesh (default material)"""
	...

def is_model_valid(model: Model) -> ctypes.c_bool | bool:
	"""Check if a model is valid (loaded in GPU, VAO/VBOs)"""
	...

def unload_model(model: Model) -> None:
	"""Unload model (including meshes) from memory (RAM and/or VRAM)"""
	...

def get_model_bounding_box(model: Model) -> BoundingBox:
	"""Compute model bounding box limits (considers all meshes)"""
	...

def draw_model(model: Model, position: Vector3, scale: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a model (with texture if set)"""
	...

def draw_model_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: ctypes.c_float | float, scale: Vector3, tint: Color) -> None:
	"""Draw a model with extended parameters"""
	...

def draw_model_wires(model: Model, position: Vector3, scale: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a model wires (with texture if set)"""
	...

def draw_model_wires_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: ctypes.c_float | float, scale: Vector3, tint: Color) -> None:
	"""Draw a model wires (with texture if set) with extended parameters"""
	...

def draw_model_points(model: Model, position: Vector3, scale: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a model as points"""
	...

def draw_model_points_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: ctypes.c_float | float, scale: Vector3, tint: Color) -> None:
	"""Draw a model as points with extended parameters"""
	...

def draw_bounding_box(box: BoundingBox, color: Color) -> None:
	"""Draw bounding box (wires)"""
	...

def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, scale: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a billboard texture"""
	...

def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None:
	"""Draw a billboard texture defined by source"""
	...

def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: ctypes.c_float | float, tint: Color) -> None:
	"""Draw a billboard texture defined by source and rotation"""
	...

def upload_mesh(mesh: ctypes.POINTER(Mesh), dynamic: ctypes.c_bool | bool) -> None:
	"""Upload mesh vertex data in GPU and provide VAO/VBO ids"""
	...

def update_mesh_buffer(mesh: Mesh, index: ctypes.c_int | int, data: ctypes.c_void_p | bytes, data_size: ctypes.c_int | int, offset: ctypes.c_int | int) -> None:
	"""Update mesh vertex data in GPU for a specific buffer index"""
	...

def unload_mesh(mesh: Mesh) -> None:
	"""Unload mesh data from CPU and GPU"""
	...

def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
	"""Draw a 3d mesh with material and transform"""
	...

def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: ctypes.POINTER(Matrix), instances: ctypes.c_int | int) -> None:
	"""Draw multiple mesh instances with material and different transforms"""
	...

def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox:
	"""Compute mesh bounding box limits"""
	...

def gen_mesh_tangents(mesh: ctypes.POINTER(Mesh)) -> None:
	"""Compute mesh tangents"""
	...

def export_mesh(mesh: Mesh, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export mesh data to file, returns true on success"""
	...

def export_mesh_as_code(mesh: Mesh, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export mesh as code file (.h) defining multiple arrays of vertex attributes"""
	...

def gen_mesh_poly(sides: ctypes.c_int | int, radius: ctypes.c_float | float) -> Mesh:
	"""Generate polygonal mesh"""
	...

def gen_mesh_plane(width: ctypes.c_float | float, length: ctypes.c_float | float, res_x: ctypes.c_int | int, res_z: ctypes.c_int | int) -> Mesh:
	"""Generate plane mesh (with subdivisions)"""
	...

def gen_mesh_cube(width: ctypes.c_float | float, height: ctypes.c_float | float, length: ctypes.c_float | float) -> Mesh:
	"""Generate cuboid mesh"""
	...

def gen_mesh_sphere(radius: ctypes.c_float | float, rings: ctypes.c_int | int, slices: ctypes.c_int | int) -> Mesh:
	"""Generate sphere mesh (standard sphere)"""
	...

def gen_mesh_hemi_sphere(radius: ctypes.c_float | float, rings: ctypes.c_int | int, slices: ctypes.c_int | int) -> Mesh:
	"""Generate half-sphere mesh (no bottom cap)"""
	...

def gen_mesh_cylinder(radius: ctypes.c_float | float, height: ctypes.c_float | float, slices: ctypes.c_int | int) -> Mesh:
	"""Generate cylinder mesh"""
	...

def gen_mesh_cone(radius: ctypes.c_float | float, height: ctypes.c_float | float, slices: ctypes.c_int | int) -> Mesh:
	"""Generate cone/pyramid mesh"""
	...

def gen_mesh_torus(radius: ctypes.c_float | float, size: ctypes.c_float | float, rad_seg: ctypes.c_int | int, sides: ctypes.c_int | int) -> Mesh:
	"""Generate torus mesh"""
	...

def gen_mesh_knot(radius: ctypes.c_float | float, size: ctypes.c_float | float, rad_seg: ctypes.c_int | int, sides: ctypes.c_int | int) -> Mesh:
	"""Generate trefoil knot mesh"""
	...

def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh:
	"""Generate heightmap mesh from image data"""
	...

def gen_mesh_cubicmap(cubicmap: Image, cube_size: Vector3) -> Mesh:
	"""Generate cubes-based map mesh from image data"""
	...

def load_materials(file_name: ctypes.c_char_p | bytes, material_count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(Material):
	"""Load materials from model file"""
	...

def load_material_default() -> Material:
	"""Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
	...

def is_material_valid(material: Material) -> ctypes.c_bool | bool:
	"""Check if a material is valid (shader assigned, map textures loaded in GPU)"""
	...

def unload_material(material: Material) -> None:
	"""Unload material from GPU memory (VRAM)"""
	...

def set_material_texture(material: ctypes.POINTER(Material), map_type: ctypes.c_int | int, texture: Texture2D) -> None:
	"""Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
	...

def set_model_mesh_material(model: ctypes.POINTER(Model), mesh_id: ctypes.c_int | int, material_id: ctypes.c_int | int) -> None:
	"""Set material for a mesh"""
	...

def load_model_animations(file_name: ctypes.c_char_p | bytes, anim_count: ctypes.POINTER(ctypes.c_int)) -> ctypes.POINTER(ModelAnimation):
	"""Load model animations from file"""
	...

def update_model_animation(model: Model, anim: ModelAnimation, frame: ctypes.c_int | int) -> None:
	"""Update model animation pose (CPU)"""
	...

def update_model_animation_bones(model: Model, anim: ModelAnimation, frame: ctypes.c_int | int) -> None:
	"""Update model animation mesh bone matrices (GPU skinning)"""
	...

def unload_model_animation(anim: ModelAnimation) -> None:
	"""Unload animation data"""
	...

def unload_model_animations(animations: ctypes.POINTER(ModelAnimation), anim_count: ctypes.c_int | int) -> None:
	"""Unload animation array data"""
	...

def is_model_animation_valid(model: Model, anim: ModelAnimation) -> ctypes.c_bool | bool:
	"""Check model animation skeleton match"""
	...

def check_collision_spheres(center1: Vector3, radius1: ctypes.c_float | float, center2: Vector3, radius2: ctypes.c_float | float) -> ctypes.c_bool | bool:
	"""Check collision between two spheres"""
	...

def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> ctypes.c_bool | bool:
	"""Check collision between two bounding boxes"""
	...

def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: ctypes.c_float | float) -> ctypes.c_bool | bool:
	"""Check collision between box and sphere"""
	...

def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: ctypes.c_float | float) -> RayCollision:
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

def is_audio_device_ready() -> ctypes.c_bool | bool:
	"""Check if audio device has been initialized successfully"""
	...

def set_master_volume(volume: ctypes.c_float | float) -> None:
	"""Set master volume (listener)"""
	...

def get_master_volume() -> ctypes.c_float | float:
	"""Get master volume (listener)"""
	...

def load_wave(file_name: ctypes.c_char_p | bytes) -> Wave:
	"""Load wave data from file"""
	...

def load_wave_from_memory(file_type: ctypes.c_char_p | bytes, file_data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> Wave:
	"""Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
	...

def is_wave_valid(wave: Wave) -> ctypes.c_bool | bool:
	"""Checks if wave data is valid (data loaded and parameters)"""
	...

def unload_wave(wave: Wave) -> None:
	"""Unload wave data"""
	...

def export_wave(wave: Wave, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export wave data to file, returns true on success"""
	...

def export_wave_as_code(wave: Wave, file_name: ctypes.c_char_p | bytes) -> ctypes.c_bool | bool:
	"""Export wave sample data to code (.h), returns true on success"""
	...

def wave_copy(wave: Wave) -> Wave:
	"""Copy a wave to a new wave"""
	...

def wave_crop(wave: ctypes.POINTER(Wave), init_frame: ctypes.c_int | int, final_frame: ctypes.c_int | int) -> None:
	"""Crop a wave to defined frames range"""
	...

def wave_format(wave: ctypes.POINTER(Wave), sample_rate: ctypes.c_int | int, sample_size: ctypes.c_int | int, channels: ctypes.c_int | int) -> None:
	"""Convert wave data to desired format"""
	...

def load_wave_samples(wave: Wave) -> ctypes.POINTER(ctypes.c_float):
	"""Load samples data from wave as a 32bit float data array"""
	...

def unload_wave_samples(samples: ctypes.POINTER(ctypes.c_float)) -> None:
	"""Unload samples data loaded with LoadWaveSamples()"""
	...

def load_music_stream(file_name: ctypes.c_char_p | bytes) -> Music:
	"""Load music stream from file"""
	...

def load_music_stream_from_memory(file_type: ctypes.c_char_p | bytes, data: ctypes.POINTER(ctypes.c_ubyte), data_size: ctypes.c_int | int) -> Music:
	"""Load music stream from data"""
	...

def is_music_valid(music: Music) -> ctypes.c_bool | bool:
	"""Checks if a music stream is valid (context and buffers initialized)"""
	...

def unload_music_stream(music: Music) -> None:
	"""Unload music stream"""
	...

def play_music_stream(music: Music) -> None:
	"""Start music playing"""
	...

def is_music_stream_playing(music: Music) -> ctypes.c_bool | bool:
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

def seek_music_stream(music: Music, position: ctypes.c_float | float) -> None:
	"""Seek music to a position (in seconds)"""
	...

def set_music_volume(music: Music, volume: ctypes.c_float | float) -> None:
	"""Set volume for music (1.0 is max level)"""
	...

def set_music_pitch(music: Music, pitch: ctypes.c_float | float) -> None:
	"""Set pitch for a music (1.0 is base level)"""
	...

def set_music_pan(music: Music, pan: ctypes.c_float | float) -> None:
	"""Set pan for a music (0.5 is center)"""
	...

def get_music_time_length(music: Music) -> ctypes.c_float | float:
	"""Get music time length (in seconds)"""
	...

def get_music_time_played(music: Music) -> ctypes.c_float | float:
	"""Get current music time played (in seconds)"""
	...

def load_audio_stream(sample_rate: ctypes.c_uint | int, sample_size: ctypes.c_uint | int, channels: ctypes.c_uint | int) -> AudioStream:
	"""Load audio stream (to stream raw audio pcm data)"""
	...

def is_audio_stream_valid(stream: AudioStream) -> ctypes.c_bool | bool:
	"""Checks if an audio stream is valid (buffers initialized)"""
	...

def unload_audio_stream(stream: AudioStream) -> None:
	"""Unload audio stream and free memory"""
	...

def update_audio_stream(stream: AudioStream, data: ctypes.c_void_p | bytes, frame_count: ctypes.c_int | int) -> None:
	"""Update audio stream buffers with data"""
	...

def is_audio_stream_processed(stream: AudioStream) -> ctypes.c_bool | bool:
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

def is_audio_stream_playing(stream: AudioStream) -> ctypes.c_bool | bool:
	"""Check if audio stream is playing"""
	...

def stop_audio_stream(stream: AudioStream) -> None:
	"""Stop audio stream"""
	...

def set_audio_stream_volume(stream: AudioStream, volume: ctypes.c_float | float) -> None:
	"""Set volume for audio stream (1.0 is max level)"""
	...

def set_audio_stream_pitch(stream: AudioStream, pitch: ctypes.c_float | float) -> None:
	"""Set pitch for audio stream (1.0 is base level)"""
	...

def set_audio_stream_pan(stream: AudioStream, pan: ctypes.c_float | float) -> None:
	"""Set pan for audio stream (0.5 is centered)"""
	...

def set_audio_stream_buffer_size_default(size: ctypes.c_int | int) -> None:
	"""Default size for new audio streams"""
	...

def clamp(value: ctypes.c_float | float, min: ctypes.c_float | float, max: ctypes.c_float | float) -> ctypes.c_float | float:
	""""""
	...

def lerp(start: ctypes.c_float | float, end: ctypes.c_float | float, amount: ctypes.c_float | float) -> ctypes.c_float | float:
	""""""
	...

def normalize(value: ctypes.c_float | float, start: ctypes.c_float | float, end: ctypes.c_float | float) -> ctypes.c_float | float:
	""""""
	...

def remap(value: ctypes.c_float | float, input_start: ctypes.c_float | float, input_end: ctypes.c_float | float, output_start: ctypes.c_float | float, output_end: ctypes.c_float | float) -> ctypes.c_float | float:
	""""""
	...

def wrap(value: ctypes.c_float | float, min: ctypes.c_float | float, max: ctypes.c_float | float) -> ctypes.c_float | float:
	""""""
	...

def float_equals(x: ctypes.c_float | float, y: ctypes.c_float | float) -> ctypes.c_int | int:
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

def vector2_add_value(v: Vector2, add: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_subtract(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_subtract_value(v: Vector2, sub: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_length(v: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_length_sqr(v: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_dot_product(v1: Vector2, v2: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_cross_product(v1: Vector2, v2: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_distance(v1: Vector2, v2: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_distance_sqr(v1: Vector2, v2: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_angle(v1: Vector2, v2: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_line_angle(start: Vector2, end: Vector2) -> ctypes.c_float | float:
	""""""
	...

def vector2_scale(v: Vector2, scale: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_multiply(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_negate(v: Vector2) -> Vector2:
	""""""
	...

def vector2_divide(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_normalize(v: Vector2) -> Vector2:
	""""""
	...

def vector2_transform(v: Vector2, mat: Matrix) -> Vector2:
	""""""
	...

def vector2_lerp(v1: Vector2, v2: Vector2, amount: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_reflect(v: Vector2, normal: Vector2) -> Vector2:
	""""""
	...

def vector2_min(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_max(v1: Vector2, v2: Vector2) -> Vector2:
	""""""
	...

def vector2_rotate(v: Vector2, angle: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_move_towards(v: Vector2, target: Vector2, max_distance: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_invert(v: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp(v: Vector2, min: Vector2, max: Vector2) -> Vector2:
	""""""
	...

def vector2_clamp_value(v: Vector2, min: ctypes.c_float | float, max: ctypes.c_float | float) -> Vector2:
	""""""
	...

def vector2_equals(p: Vector2, q: Vector2) -> ctypes.c_int | int:
	""""""
	...

def vector2_refract(v: Vector2, n: Vector2, r: ctypes.c_float | float) -> Vector2:
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

def vector3_add_value(v: Vector3, add: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_subtract(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_subtract_value(v: Vector3, sub: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_scale(v: Vector3, scalar: ctypes.c_float | float) -> Vector3:
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

def vector3_length(v: Vector3) -> ctypes.c_float | float:
	""""""
	...

def vector3_length_sqr(v: Vector3) -> ctypes.c_float | float:
	""""""
	...

def vector3_dot_product(v1: Vector3, v2: Vector3) -> ctypes.c_float | float:
	""""""
	...

def vector3_distance(v1: Vector3, v2: Vector3) -> ctypes.c_float | float:
	""""""
	...

def vector3_distance_sqr(v1: Vector3, v2: Vector3) -> ctypes.c_float | float:
	""""""
	...

def vector3_angle(v1: Vector3, v2: Vector3) -> ctypes.c_float | float:
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

def vector3_project(v1: Vector3, v2: Vector3) -> Vector3:
	""""""
	...

def vector3_reject(v1: Vector3, v2: Vector3) -> Vector3:
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

def vector3_rotate_by_axis_angle(v: Vector3, axis: Vector3, angle: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_move_towards(v: Vector3, target: Vector3, max_distance: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_lerp(v1: Vector3, v2: Vector3, amount: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_cubic_hermite(v1: Vector3, tangent1: Vector3, v2: Vector3, tangent2: Vector3, amount: ctypes.c_float | float) -> Vector3:
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

def vector3_clamp_value(v: Vector3, min: ctypes.c_float | float, max: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector3_equals(p: Vector3, q: Vector3) -> ctypes.c_int | int:
	""""""
	...

def vector3_refract(v: Vector3, n: Vector3, r: ctypes.c_float | float) -> Vector3:
	""""""
	...

def vector4_zero() -> Vector4:
	""""""
	...

def vector4_one() -> Vector4:
	""""""
	...

def vector4_add(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_add_value(v: Vector4, add: ctypes.c_float | float) -> Vector4:
	""""""
	...

def vector4_subtract(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_subtract_value(v: Vector4, add: ctypes.c_float | float) -> Vector4:
	""""""
	...

def vector4_length(v: Vector4) -> ctypes.c_float | float:
	""""""
	...

def vector4_length_sqr(v: Vector4) -> ctypes.c_float | float:
	""""""
	...

def vector4_dot_product(v1: Vector4, v2: Vector4) -> ctypes.c_float | float:
	""""""
	...

def vector4_distance(v1: Vector4, v2: Vector4) -> ctypes.c_float | float:
	""""""
	...

def vector4_distance_sqr(v1: Vector4, v2: Vector4) -> ctypes.c_float | float:
	""""""
	...

def vector4_scale(v: Vector4, scale: ctypes.c_float | float) -> Vector4:
	""""""
	...

def vector4_multiply(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_negate(v: Vector4) -> Vector4:
	""""""
	...

def vector4_divide(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_normalize(v: Vector4) -> Vector4:
	""""""
	...

def vector4_min(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_max(v1: Vector4, v2: Vector4) -> Vector4:
	""""""
	...

def vector4_lerp(v1: Vector4, v2: Vector4, amount: ctypes.c_float | float) -> Vector4:
	""""""
	...

def vector4_move_towards(v: Vector4, target: Vector4, max_distance: ctypes.c_float | float) -> Vector4:
	""""""
	...

def vector4_invert(v: Vector4) -> Vector4:
	""""""
	...

def vector4_equals(p: Vector4, q: Vector4) -> ctypes.c_int | int:
	""""""
	...

def matrix_determinant(mat: Matrix) -> ctypes.c_float | float:
	""""""
	...

def matrix_trace(mat: Matrix) -> ctypes.c_float | float:
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

def matrix_translate(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_rotate(axis: Vector3, angle: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_rotate_x(angle: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_rotate_y(angle: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_rotate_z(angle: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_rotate_xyz(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_rotate_zyx(angle: Vector3) -> Matrix:
	""""""
	...

def matrix_scale(x: ctypes.c_float | float, y: ctypes.c_float | float, z: ctypes.c_float | float) -> Matrix:
	""""""
	...

def matrix_frustum(left: ctypes.c_double | float, right: ctypes.c_double | float, bottom: ctypes.c_double | float, top: ctypes.c_double | float, near_plane: ctypes.c_double | float, far_plane: ctypes.c_double | float) -> Matrix:
	""""""
	...

def matrix_perspective(fov_y: ctypes.c_double | float, aspect: ctypes.c_double | float, near_plane: ctypes.c_double | float, far_plane: ctypes.c_double | float) -> Matrix:
	""""""
	...

def matrix_ortho(left: ctypes.c_double | float, right: ctypes.c_double | float, bottom: ctypes.c_double | float, top: ctypes.c_double | float, near_plane: ctypes.c_double | float, far_plane: ctypes.c_double | float) -> Matrix:
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

def quaternion_add_value(q: Quaternion, add: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_subtract_value(q: Quaternion, sub: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_identity() -> Quaternion:
	""""""
	...

def quaternion_length(q: Quaternion) -> ctypes.c_float | float:
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

def quaternion_scale(q: Quaternion, mul: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion:
	""""""
	...

def quaternion_lerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_cubic_hermite_spline(q1: Quaternion, out_tangent1: Quaternion, q2: Quaternion, in_tangent2: Quaternion, t: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_from_vector3_to_vector3(var_from: Vector3, to: Vector3) -> Quaternion:
	""""""
	...

def quaternion_from_matrix(mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_to_matrix(q: Quaternion) -> Matrix:
	""""""
	...

def quaternion_from_axis_angle(axis: Vector3, angle: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_to_axis_angle(q: Quaternion, out_axis: ctypes.POINTER(Vector3), out_angle: ctypes.POINTER(ctypes.c_float)) -> None:
	""""""
	...

def quaternion_from_euler(pitch: ctypes.c_float | float, yaw: ctypes.c_float | float, roll: ctypes.c_float | float) -> Quaternion:
	""""""
	...

def quaternion_to_euler(q: Quaternion) -> Vector3:
	""""""
	...

def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion:
	""""""
	...

def quaternion_equals(p: Quaternion, q: Quaternion) -> ctypes.c_int | int:
	""""""
	...

def matrix_decompose(mat: Matrix, translation: ctypes.POINTER(Vector3), rotation: ctypes.POINTER(Quaternion), scale: ctypes.POINTER(Vector3)) -> None:
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

def gui_is_locked() -> ctypes.c_bool | bool:
	"""Check if gui is locked (global state)"""
	...

def gui_set_alpha(alpha: ctypes.c_float | float) -> None:
	"""Set gui controls alpha (global state), alpha goes from 0.0f to 1.0f"""
	...

def gui_set_state(state: ctypes.c_int | int) -> None:
	"""Set gui state (global state)"""
	...

def gui_get_state() -> ctypes.c_int | int:
	"""Get gui state (global state)"""
	...

def gui_set_font(font: Font) -> None:
	"""Set gui custom font (global state)"""
	...

def gui_get_font() -> Font:
	"""Get gui custom font (global state)"""
	...

def gui_set_style(control: ctypes.c_int | int, property: ctypes.c_int | int, value: ctypes.c_int | int) -> None:
	"""Set one style property"""
	...

def gui_get_style(control: ctypes.c_int | int, property: ctypes.c_int | int) -> ctypes.c_int | int:
	"""Get one style property"""
	...

def gui_load_style(file_name: ctypes.c_char_p | bytes) -> None:
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

def gui_set_tooltip(tooltip: ctypes.c_char_p | bytes) -> None:
	"""Set tooltip string"""
	...

def gui_icon_text(icon_id: ctypes.c_int | int, text: ctypes.c_char_p | bytes) -> ctypes.c_char_p | bytes:
	"""Get text with icon id prepended (if supported)"""
	...

def gui_window_box(bounds: Rectangle, title: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Window Box control, shows a window that can be closed"""
	...

def gui_group_box(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Group Box control with text name"""
	...

def gui_line(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Line separator control, could contain text"""
	...

def gui_panel(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Panel control, useful to group controls"""
	...

def gui_tab_bar(bounds: Rectangle, text: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int | int, active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Tab Bar control, returns TAB to be closed or -1"""
	...

def gui_scroll_panel(bounds: Rectangle, text: ctypes.c_char_p | bytes, content: Rectangle, scroll: ctypes.POINTER(Vector2), view: ctypes.POINTER(Rectangle)) -> ctypes.c_int | int:
	"""Scroll Panel control"""
	...

def gui_label(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Label control"""
	...

def gui_button(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Button control, returns true when clicked"""
	...

def gui_label_button(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Label button control, returns true when clicked"""
	...

def gui_toggle(bounds: Rectangle, text: ctypes.c_char_p | bytes, active: ctypes.POINTER(ctypes.c_bool)) -> ctypes.c_int | int:
	"""Toggle Button control"""
	...

def gui_toggle_group(bounds: Rectangle, text: ctypes.c_char_p | bytes, active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Toggle Group control"""
	...

def gui_toggle_slider(bounds: Rectangle, text: ctypes.c_char_p | bytes, active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Toggle Slider control"""
	...

def gui_check_box(bounds: Rectangle, text: ctypes.c_char_p | bytes, checked: ctypes.POINTER(ctypes.c_bool)) -> ctypes.c_int | int:
	"""Check Box control, returns true when active"""
	...

def gui_combo_box(bounds: Rectangle, text: ctypes.c_char_p | bytes, active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""Combo Box control"""
	...

def gui_dropdown_box(bounds: Rectangle, text: ctypes.c_char_p | bytes, active: ctypes.POINTER(ctypes.c_int), edit_mode: ctypes.c_bool | bool) -> ctypes.c_int | int:
	"""Dropdown Box control"""
	...

def gui_spinner(bounds: Rectangle, text: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_int), min_value: ctypes.c_int | int, max_value: ctypes.c_int | int, edit_mode: ctypes.c_bool | bool) -> ctypes.c_int | int:
	"""Spinner control"""
	...

def gui_value_box(bounds: Rectangle, text: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_int), min_value: ctypes.c_int | int, max_value: ctypes.c_int | int, edit_mode: ctypes.c_bool | bool) -> ctypes.c_int | int:
	"""Value Box control, updates input text with numbers"""
	...

def gui_value_box_float(bounds: Rectangle, text: ctypes.c_char_p | bytes, text_value: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_float), edit_mode: ctypes.c_bool | bool) -> ctypes.c_int | int:
	"""Value box control for float values"""
	...

def gui_text_box(bounds: Rectangle, text: ctypes.c_char_p | bytes, text_size: ctypes.c_int | int, edit_mode: ctypes.c_bool | bool) -> ctypes.c_int | int:
	"""Text Box control, updates input text"""
	...

def gui_slider(bounds: Rectangle, text_left: ctypes.c_char_p | bytes, text_right: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_float), min_value: ctypes.c_float | float, max_value: ctypes.c_float | float) -> ctypes.c_int | int:
	"""Slider control"""
	...

def gui_slider_bar(bounds: Rectangle, text_left: ctypes.c_char_p | bytes, text_right: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_float), min_value: ctypes.c_float | float, max_value: ctypes.c_float | float) -> ctypes.c_int | int:
	"""Slider Bar control"""
	...

def gui_progress_bar(bounds: Rectangle, text_left: ctypes.c_char_p | bytes, text_right: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_float), min_value: ctypes.c_float | float, max_value: ctypes.c_float | float) -> ctypes.c_int | int:
	"""Progress Bar control"""
	...

def gui_status_bar(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Status Bar control, shows info text"""
	...

def gui_dummy_rec(bounds: Rectangle, text: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Dummy control for placeholders"""
	...

def gui_grid(bounds: Rectangle, text: ctypes.c_char_p | bytes, spacing: ctypes.c_float | float, subdivs: ctypes.c_int | int, mouse_cell: ctypes.POINTER(Vector2)) -> ctypes.c_int | int:
	"""Grid control"""
	...

def gui_list_view(bounds: Rectangle, text: ctypes.c_char_p | bytes, scroll_index: ctypes.POINTER(ctypes.c_int), active: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""List View control"""
	...

def gui_list_view_ex(bounds: Rectangle, text: ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), count: ctypes.c_int | int, scroll_index: ctypes.POINTER(ctypes.c_int), active: ctypes.POINTER(ctypes.c_int), focus: ctypes.POINTER(ctypes.c_int)) -> ctypes.c_int | int:
	"""List View with extended parameters"""
	...

def gui_message_box(bounds: Rectangle, title: ctypes.c_char_p | bytes, message: ctypes.c_char_p | bytes, buttons: ctypes.c_char_p | bytes) -> ctypes.c_int | int:
	"""Message Box control, displays a message"""
	...

def gui_text_input_box(bounds: Rectangle, title: ctypes.c_char_p | bytes, message: ctypes.c_char_p | bytes, buttons: ctypes.c_char_p | bytes, text: ctypes.c_char_p | bytes, text_max_size: ctypes.c_int | int, secret_view_active: ctypes.POINTER(ctypes.c_bool)) -> ctypes.c_int | int:
	"""Text Input Box control, ask for text, supports secret"""
	...

def gui_color_picker(bounds: Rectangle, text: ctypes.c_char_p | bytes, color: ctypes.POINTER(Color)) -> ctypes.c_int | int:
	"""Color Picker control (multiple color controls)"""
	...

def gui_color_panel(bounds: Rectangle, text: ctypes.c_char_p | bytes, color: ctypes.POINTER(Color)) -> ctypes.c_int | int:
	"""Color Panel control"""
	...

def gui_color_bar_alpha(bounds: Rectangle, text: ctypes.c_char_p | bytes, alpha: ctypes.POINTER(ctypes.c_float)) -> ctypes.c_int | int:
	"""Color Bar Alpha control"""
	...

def gui_color_bar_hue(bounds: Rectangle, text: ctypes.c_char_p | bytes, value: ctypes.POINTER(ctypes.c_float)) -> ctypes.c_int | int:
	"""Color Bar Hue control"""
	...

def gui_color_picker_hsv(bounds: Rectangle, text: ctypes.c_char_p | bytes, color_hsv: ctypes.POINTER(Vector3)) -> ctypes.c_int | int:
	"""Color Picker control that avoids conversion to RGB on each call (multiple color controls)"""
	...

def gui_color_panel_hsv(bounds: Rectangle, text: ctypes.c_char_p | bytes, color_hsv: ctypes.POINTER(Vector3)) -> ctypes.c_int | int:
	"""Color Panel control that updates Hue-Saturation-Value color value, used by GuiColorPickerHSV()"""
	...

