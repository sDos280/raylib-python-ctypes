"""

raygui - portable window

"""

from raypyc import *


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    set_config_flags(ConfigFlags.FLAG_WINDOW_UNDECORATED)
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raygui - portable window")

    # General variables
    mouse_position = Vector2()
    window_position = Vector2(500, 200)
    pan_offset = mouse_position
    drag_window = False

    set_window_position(int(window_position.x), int(window_position.y))

    exit_window = False

    set_target_fps(60)
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close() and not exit_window:  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_position = get_mouse_position()

        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            if check_collision_point_rec(mouse_position, Rectangle(0, 0, SCREEN_WIDTH, 20)):
                drag_window = True
                pan_offset = mouse_position

        if drag_window:
            window_position.x += mouse_position.x - pan_offset.x
            window_position.y += mouse_position.y - pan_offset.y
            if is_mouse_button_released(MouseButton.MOUSE_BUTTON_LEFT): drag_window = False

            set_window_position(int(window_position.x), int(window_position.y))
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        exit_window = gui_window_box(Rectangle(0, 0, SCREEN_WIDTH, SCREEN_WIDTH), b"#198# PORTABLE WINDOW")

        draw_text(f"Mouse Position: [ {mouse_position.x}, {mouse_position.y} ]".encode(), 10, 40, 10, DARKGRAY)

        end_drawing()

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
