"""

raylib [rlgl] example - compute shader - Conway's Game of Life

"""

from ctypes import *

from raypyc import *

#  IMPORTANT: This must match gol*.glsl GOL_WIDTH constant.
#  This must be a multiple of 16 (check golLogic compute dispatch).
GOL_WIDTH = 768

#  Maximum amount of queued draw commands (squares draw from mouse down events).
MAX_BUFFERED_TRANSFERTS = 48


class GolUpdateCmd(Structure):
    """Game Of Life Update Command"""
    _fields_ = [
        ('x', c_uint),  # x coordinate of the gol command
        ('y', c_uint),  # y coordinate of the gol command
        ('w', c_uint),  # width of the filled zone
        ('enabled', c_uint)  # whether to enable or disable zone
    ]


#  Game Of Life Update Commands SSBO
class GolUpdateSSBO(Structure):
    """Game Of Life Update Commands SSBO"""
    _fields_ = [
        ('count', c_uint),
        ('commands', GolUpdateCmd * MAX_BUFFERED_TRANSFERTS)
    ]


# ------------------------------------------------------------------------------------
#  Program main entry point
# ------------------------------------------------------------------------------------
def main():
    #  Initialization
    # --------------------------------------------------------------------------------------
    init_window(GOL_WIDTH, GOL_WIDTH, b"raylib [rlgl] example - compute shader - game of life")

    resolution = Vector2(GOL_WIDTH, GOL_WIDTH)
    brush_size = 8

    #  Game of Life logic compute shader
    gol_logic_code = c_char_p(load_file_text(b"resources/shaders/glsl430/gol.glsl"))
    gol_logic_shader = c_uint(rl_compile_shader(gol_logic_code, RL_COMPUTE_SHADER))
    gol_logic_program = c_uint(rl_load_compute_shader_program(gol_logic_shader))
    # unload_file_text(gol_logic_code)

    #  Game of Life logic render shader
    gol_render_shader = load_shader(c_char_p(), b"resources/shaders/glsl430/gol_render.glsl")
    res_uniform_loc = c_int(get_shader_location(gol_render_shader, b"resolution"))

    #  Game of Life transfert shader (CPU<->GPU download and upload)
    gol_transfert_code = c_char_p(load_file_text(b"resources/shaders/glsl430/gol_transfert.glsl"))
    gol_transfert_shader = c_uint(rl_compile_shader(gol_transfert_code, RL_COMPUTE_SHADER))
    gol_transfert_program = c_uint(rl_load_compute_shader_program(gol_transfert_shader))
    # unload_file_text(gol_transfert_code)

    #  Load shader storage buffer object (SSBO), id returned
    ssbo_a = c_uint(rl_load_shader_buffer(GOL_WIDTH * GOL_WIDTH * sizeof(c_int), c_void_p(), RL_DYNAMIC_COPY))
    ssbo_b = c_uint(rl_load_shader_buffer(GOL_WIDTH * GOL_WIDTH * sizeof(c_int), c_void_p(), RL_DYNAMIC_COPY))
    ssbo_transfert = c_uint(rl_load_shader_buffer(sizeof(GolUpdateSSBO), c_void_p(), RL_DYNAMIC_COPY))

    transfert_buffer = GolUpdateSSBO()

    #  Create a white texture of the size of the window to update
    #  each pixel of the window using the fragment shader: golRenderShader
    white_image = gen_image_color(GOL_WIDTH, GOL_WIDTH, WHITE)
    white_tex = load_texture_from_image(white_image)
    unload_image(white_image)
    # --------------------------------------------------------------------------------------

    #  Main game loop
    while not window_should_close():
        #  Update
        # ----------------------------------------------------------------------------------
        brush_size += int(get_mouse_wheel_move())

        if (is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT) or is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT)) and transfert_buffer.count < MAX_BUFFERED_TRANSFERTS:
            #  Buffer a new command
            transfert_buffer.commands[transfert_buffer.count].x = int(get_mouse_x() - brush_size / 2)
            transfert_buffer.commands[transfert_buffer.count].y = int(get_mouse_y() - brush_size / 2)
            transfert_buffer.commands[transfert_buffer.count].w = int(brush_size)
            transfert_buffer.commands[transfert_buffer.count].enabled = is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)
            transfert_buffer.count += 1

        elif transfert_buffer.count > 0:  # Process transfert buffer
            #  Send SSBO buffer to GPU
            rl_update_shader_buffer_elements(ssbo_transfert, pointer(transfert_buffer), sizeof(GolUpdateSSBO), 0)

            #  Process SSBO commands on GPU
            rl_enable_shader(gol_transfert_program)
            rl_bind_shader_buffer(ssbo_a, 1)
            rl_bind_shader_buffer(ssbo_transfert, 3)
            rl_compute_shader_dispatch(transfert_buffer.count, 1, 1)  # Each GPU unit will process a command!
            rl_disable_shader()

            transfert_buffer.count = 0

        else:
            #  Process game of life logic
            rl_enable_shader(gol_logic_program)
            rl_bind_shader_buffer(ssbo_a, 1)
            rl_bind_shader_buffer(ssbo_b, 2)
            rl_compute_shader_dispatch(int(GOL_WIDTH / 16), int(GOL_WIDTH / 16), 1)
            rl_disable_shader()

            #  ssbo_a <-> ssbo_b
            temp = ssbo_a
            ssbo_a = ssbo_b
            ssbo_b = temp

        rl_bind_shader_buffer(ssbo_a, 1)
        set_shader_value(gol_render_shader, res_uniform_loc, pointer(resolution), ShaderUniformDataType.SHADER_UNIFORM_VEC2)
        # ----------------------------------------------------------------------------------

        #  Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(BLANK)

        begin_shader_mode(gol_render_shader)
        draw_texture(white_tex, 0, 0, WHITE)
        end_shader_mode()

        draw_rectangle_lines(int(get_mouse_x() - brush_size / 2), int(get_mouse_y() - brush_size / 2), brush_size, brush_size, RED)

        draw_text(b"Use Mouse wheel to increase/decrease brush size", 10, 10, 20, WHITE)
        draw_fps(get_screen_width() - 100, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    #  De-Initialization
    # --------------------------------------------------------------------------------------
    #  Unload shader buffers objects.
    rl_unload_shader_buffer(ssbo_a)
    rl_unload_shader_buffer(ssbo_b)
    rl_unload_shader_buffer(ssbo_transfert)

    #  Unload compute shader programs
    rl_unload_shader_program(gol_transfert_program)
    rl_unload_shader_program(gol_logic_program)

    unload_texture(white_tex)  # Unload white texture
    unload_shader(gol_render_shader)  # Unload rendering fragment shader

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
