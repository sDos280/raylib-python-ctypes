"""

raylib [shaders] example - Julia sets

"""

from ctypes import pointer, c_float

from raypyc import *

# Definitions
# ------------------------------------------------------------------------------------
POINTS_OF_INTEREST = [
    [-0.348827, 0.607167],
    [-0.786268, 0.169728],
    [-0.8, 0.156],
    [0.285, 0.0],
    [-0.835, -0.2321],
    [-0.70176, -0.3842]
]


# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    # set_config_flags(ConfigFlags.FLAG_WINDOW_HIGHDPI)
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [shaders] example - julia sets")

    # Load julia set shader
    # NOTE: Defining 0 (NULL) for vertex shader forces usage of internal default vertex shader
    shader = load_shader(None, b"resources/shaders/glsl330/julia_set.fs")

    # Create a RenderTexture2D to be used for render to texture
    target = load_render_texture(get_screen_width(), get_screen_height())

    # c constant to use in z^2 + c
    c = (c_float * 2)(POINTS_OF_INTEREST[0][0], POINTS_OF_INTEREST[0][1])

    # Offset and zoom to draw the julia set at. (centered on screen and default size)
    offset = (c_float * 2)(-get_screen_width() / 2, -get_screen_height() / 2)
    zoom = 1.0

    offset_speed = Vector2(0.0, 0.0)

    # Get variable (uniform) locations on the shader to connect with the program
    # NOTE: If uniform variable could not be found in the shader, function returns -1
    c_loc = get_shader_location(shader, b"c")
    zoom_loc = get_shader_location(shader, b"zoom")
    offset_loc = get_shader_location(shader, b"offset")

    # Tell the shader what the screen dimensions, zoom, offset and c are
    screen_dims = (c_float * 2)(get_screen_width(), (get_screen_height()))
    set_shader_value(shader, get_shader_location(shader, b"screenDims"), pointer(screen_dims), ShaderUniformDataType.SHADER_UNIFORM_VEC2)

    set_shader_value(shader, c_loc, c, ShaderUniformDataType.SHADER_UNIFORM_VEC2)
    set_shader_value(shader, zoom_loc, pointer(c_float(zoom)), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, offset_loc, offset, ShaderUniformDataType.SHADER_UNIFORM_VEC2)

    increment_speed = 0  # Multiplier of speed to change c value
    show_controls = True  # Show controls
    pause = False  # Pause animation

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # Press [1 - 6] to reset c to a point of interest
        if is_key_pressed(KeyboardKey.KEY_ONE) or \
                is_key_pressed(KeyboardKey.KEY_TWO) or \
                is_key_pressed(KeyboardKey.KEY_THREE) or \
                is_key_pressed(KeyboardKey.KEY_FOUR) or \
                is_key_pressed(KeyboardKey.KEY_FIVE) or \
                is_key_pressed(KeyboardKey.KEY_SIX):

            if is_key_pressed(KeyboardKey.KEY_ONE):
                c[0] = POINTS_OF_INTEREST[0][0]
                c[1] = POINTS_OF_INTEREST[0][1]
            elif is_key_pressed(KeyboardKey.KEY_TWO):
                c[0] = POINTS_OF_INTEREST[1][0]
                c[1] = POINTS_OF_INTEREST[1][1]
            elif is_key_pressed(KeyboardKey.KEY_THREE):
                c[0] = POINTS_OF_INTEREST[2][0]
                c[1] = POINTS_OF_INTEREST[2][1]
            elif is_key_pressed(KeyboardKey.KEY_FOUR):
                c[0] = POINTS_OF_INTEREST[3][0]
                c[1] = POINTS_OF_INTEREST[3][1]
            elif is_key_pressed(KeyboardKey.KEY_FIVE):
                c[0] = POINTS_OF_INTEREST[4][0]
                c[1] = POINTS_OF_INTEREST[4][1]
            elif is_key_pressed(KeyboardKey.KEY_SIX):
                c[0] = POINTS_OF_INTEREST[5][0]
                c[1] = POINTS_OF_INTEREST[5][1]

            set_shader_value(shader, c_loc, c, ShaderUniformDataType.SHADER_UNIFORM_VEC2)

        if is_key_pressed(KeyboardKey.KEY_SPACE): pause = not pause  # Pause animation (c change)
        if is_key_pressed(KeyboardKey.KEY_F1): show_controls = not show_controls  # Toggle whether to show controls

        if not pause:
            if is_key_pressed(KeyboardKey.KEY_RIGHT):
                increment_speed += 1
            elif is_key_pressed(KeyboardKey.KEY_LEFT):
                increment_speed -= 1

            # TODO: The idea is to zoom and move around with mouse
            # Probably offset movement should be proportional to zoom level
            if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT) or is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
                if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT): zoom += zoom * 0.003
                if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT): zoom -= zoom * 0.003

                mouse_pos = get_mouse_position()

                offset_speed.x = mouse_pos.x - float(SCREEN_WIDTH / 2)
                offset_speed.y = mouse_pos.y - float(SCREEN_HEIGHT / 2)

                # Slowly move camera to targetOffset
                offset[0] += get_frame_time() * offset_speed.x * 0.8
                offset[1] += get_frame_time() * offset_speed.y * 0.8
            else:
                offset_speed = Vector2(0.0, 0.0)

            set_shader_value(shader, zoom_loc, pointer(c_float(zoom)), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
            set_shader_value(shader, offset_loc, offset, ShaderUniformDataType.SHADER_UNIFORM_VEC2)

            # Increment c value with time
            amount = get_frame_time() * increment_speed * 0.0005
            c[0] += amount
            c[1] += amount

            set_shader_value(shader, c_loc, c, ShaderUniformDataType.SHADER_UNIFORM_VEC2)
            # ----------------------------------------------------------------------------------

            # Draw
            # ----------------------------------------------------------------------------------
            # Using a render texture to draw Julia set
            begin_texture_mode(target)  # Enable drawing to texture
            clear_background(RAYWHITE)  # Clear the render texture
            # Draw a rectangle in shader mode to be used as shader canvas
            # NOTE: Rectangle uses font white character texture coordinates,
            # so shader can not be applied here directly because input vertexTexCoord
            # do not represent full screen coordinates (space where want to apply shader)
            draw_rectangle(0, 0, get_screen_width(), get_screen_height(), BLACK)
            end_texture_mode()

            begin_drawing()
            clear_background(RAYWHITE)  # Clear screen background

            # Draw the saved texture and rendered julia set with shader
            # NOTE: We do not invert texture on Y, already considered inside shader
            begin_shader_mode(shader)
            # WARNING: If FLAG_WINDOW_HIGHDPI is enabled, HighDPI monitor scaling should be considered
            # when rendering the RenderTexture2D to fit in the HighDPI scaled Window
            draw_texture_ex(Texture2D(target.texture.id, target.texture.width, target.texture.height, target.texture.mipmaps, target.texture.format), Vector2(0.0, 0.0), 0.0, 1.0, WHITE)
            end_shader_mode()

            if show_controls:
                draw_text(b"Press Mouse buttons right/left to zoom in/out and move", 10, 15, 10, RAYWHITE)
                draw_text(b"Press KEY_F1 to toggle these controls", 10, 30, 10, RAYWHITE)
                draw_text(b"Press KEYS [1 - 6] to change point of interest", 10, 45, 10, RAYWHITE)
                draw_text(b"Press KEY_LEFT | KEY_RIGHT to change speed", 10, 60, 10, RAYWHITE)
                draw_text(b"Press KEY_SPACE to pause movement animation", 10, 75, 10, RAYWHITE)
            end_drawing()
            # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    unload_shader(shader)  # Unload shader
    unload_render_texture(target)  # Unload render texture

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
