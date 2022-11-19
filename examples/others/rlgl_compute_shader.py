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
    brushSize = 8

    #  Game of Life logic compute shader
    golLogicCode = c_char_p(load_file_text(b"resources/shaders/glsl430/gol.glsl"))
    golLogicShader = c_uint(rl_compile_shader(golLogicCode, RL_COMPUTE_SHADER))
    golLogicProgram = c_uint(rl_load_compute_shader_program(golLogicShader))
    unload_file_text(golLogicCode.value)

    #  Game of Life logic render shader
    golRenderShader = load_shader(c_char_p(), b"resources/shaders/glsl430/gol_render.glsl")
    resUniformLoc = c_int(get_shader_location(golRenderShader, b"resolution"))

    #  Game of Life transfert shader (CPU<->GPU download and upload)
    golTransfertCode = c_char_p(load_file_text(b"resources/shaders/glsl430/gol_transfert.glsl"))
    golTransfertShader = c_uint(rl_compile_shader(golTransfertCode, RL_COMPUTE_SHADER))
    golTransfertProgram = c_uint(rl_load_compute_shader_program(golTransfertShader))
    # unload_file_text(golTransfertCode.value)

    #  Load shader storage buffer object (SSBO), id returned
    ssboA = c_uint(rl_load_shader_buffer(GOL_WIDTH * GOL_WIDTH * sizeof(c_int), c_void_p(), RL_DYNAMIC_COPY))
    ssboB = c_uint(rl_load_shader_buffer(GOL_WIDTH * GOL_WIDTH * sizeof(c_int), c_void_p(), RL_DYNAMIC_COPY))
    ssboTransfert = c_uint(rl_load_shader_buffer(sizeof(GolUpdateSSBO), c_void_p(), RL_DYNAMIC_COPY))

    transfertBuffer = GolUpdateSSBO()

    #  Create a white texture of the size of the window to update
    #  each pixel of the window using the fragment shader: golRenderShader
    whiteImage = gen_image_color(GOL_WIDTH, GOL_WIDTH, WHITE)
    whiteTex = load_texture_from_image(whiteImage)
    unload_image(whiteImage)
    # --------------------------------------------------------------------------------------

    #  Main game loop
    while not window_should_close():
        #  Update
        # ----------------------------------------------------------------------------------
        brushSize += int(get_mouse_wheel_move())

        if (is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT) or is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT)) and transfertBuffer.count < MAX_BUFFERED_TRANSFERTS:
            #  Buffer a new command
            transfertBuffer.commands[transfertBuffer.count].x = int(get_mouse_x() - brushSize / 2)
            transfertBuffer.commands[transfertBuffer.count].y = int(get_mouse_y() - brushSize / 2)
            transfertBuffer.commands[transfertBuffer.count].w = int(brushSize)
            transfertBuffer.commands[transfertBuffer.count].enabled = is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)
            transfertBuffer.count += 1

        elif transfertBuffer.count > 0:  # Process transfert buffer
            #  Send SSBO buffer to GPU
            rl_update_shader_buffer_elements(ssboTransfert, pointer(transfertBuffer), sizeof(GolUpdateSSBO), 0)

            #  Process SSBO commands on GPU
            rl_enable_shader(golTransfertProgram)
            rl_bind_shader_buffer(ssboA, 1)
            rl_bind_shader_buffer(ssboTransfert, 3)
            rl_compute_shader_dispatch(transfertBuffer.count, 1, 1)  # Each GPU unit will process a command!
            rl_disable_shader()

            transfertBuffer.count = 0

        else:
            #  Process game of life logic
            rl_enable_shader(golLogicProgram)
            rl_bind_shader_buffer(ssboA, 1)
            rl_bind_shader_buffer(ssboB, 2)
            rl_compute_shader_dispatch(int(GOL_WIDTH / 16), int(GOL_WIDTH / 16), 1)
            rl_disable_shader()

            #  ssboA <-> ssboB
            temp = ssboA
            ssboA = ssboB
            ssboB = temp

        rl_bind_shader_buffer(ssboA, 1)
        set_shader_value(golRenderShader, resUniformLoc, pointer(resolution), ShaderUniformDataType.SHADER_UNIFORM_VEC2)
        # ----------------------------------------------------------------------------------

        #  Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(BLANK)

        begin_shader_mode(golRenderShader)
        draw_texture(whiteTex, 0, 0, WHITE)
        end_shader_mode()

        draw_rectangle_lines(int(get_mouse_x() - brushSize / 2), int(get_mouse_y() - brushSize / 2), brushSize, brushSize, RED)

        draw_text(b"Use Mouse wheel to increase/decrease brush size", 10, 10, 20, WHITE)
        draw_fps(get_screen_width() - 100, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    #  De-Initialization
    # --------------------------------------------------------------------------------------
    #  Unload shader buffers objects.
    rl_unload_shader_buffer(ssboA)
    rl_unload_shader_buffer(ssboB)
    rl_unload_shader_buffer(ssboTransfert)

    #  Unload compute shader programs
    rl_unload_shader_program(golTransfertProgram)
    rl_unload_shader_program(golLogicProgram)

    unload_texture(whiteTex)  # Unload white texture
    unload_shader(golRenderShader)  # Unload rendering fragment shader

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
