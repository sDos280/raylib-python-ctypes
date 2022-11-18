"""

raylib [text] example - Input Box

"""

import ctypes

from raypyc import *

# Definitions
# ------------------------------------------------------------------------------------
MAX_INPUT_CHARS = 9


# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [text] example - input box")

    name = (ctypes.c_char * (MAX_INPUT_CHARS + 1))(b'\0')  # NOTE: One extra space required for null terminator char '\0'

    letter_count = 0

    text_box = Rectangle(SCREEN_WIDTH / 2.0 - 100, 180, 225, 50)
    mouse_on_text = False

    frames_counter = False

    set_target_fps(10)  # Set our game to run at 10 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if check_collision_point_rec(get_mouse_position(), text_box):
            mouse_on_text = True
        else:
            mouse_on_text = False

        if mouse_on_text:
            # Set the window's cursor to the I-Beam
            set_mouse_cursor(MouseCursor.MOUSE_CURSOR_IBEAM)

            # Get char pressed (unicode character) on the queue
            key = get_char_pressed()

            # Check if more characters have been pressed on the same frame
            while key > 0:
                # NOTE: Only allow keys in range [32..125]
                if 32 <= key <= 125 and letter_count < MAX_INPUT_CHARS:
                    name[letter_count] = ctypes.c_char(key)
                    name[letter_count + 1] = b'\0'  # Add null terminator at the end of the string.
                    letter_count += 1

                key = get_char_pressed()  # Check next character in the queue

            if is_key_pressed(KeyboardKey.KEY_BACKSPACE):
                letter_count -= 1
                if letter_count < 0:
                    letter_count = 0
                name[letter_count] = b'\0'
        else:
            set_mouse_cursor(MouseCursor.MOUSE_CURSOR_DEFAULT)

        if mouse_on_text:
            frames_counter += 1
        else:
            frames_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_text(b"PLACE MOUSE OVER INPUT BOX!", 240, 140, 20, GRAY)

        draw_rectangle_rec(text_box, LIGHTGRAY)
        if mouse_on_text:
            draw_rectangle_lines(int(text_box.x), int(text_box.y), int(text_box.width), int(text_box.height), RED)
        else:
            draw_rectangle_lines(int(text_box.x), int(text_box.y), int(text_box.width), int(text_box.height), DARKGRAY)

        draw_text(name, int(text_box.x + 5), int(text_box.y + 8), 40, MAROON)

        draw_text(f"INPUT CHARS: {letter_count}/{MAX_INPUT_CHARS}".encode(), 315, 250, 20, DARKGRAY)  # we prefer to not use text_format

        if mouse_on_text:
            if letter_count < MAX_INPUT_CHARS:
                # Draw blinking underscore char
                if (frames_counter / 20) % 2 == 0:
                    draw_text(b"_", int(text_box.x + 8 + measure_text(name, 40)), int(text_box.y + 12), 40, MAROON)
            else:
                draw_text(b"Press BACKSPACE to delete chars...", 230, 300, 20, GRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
