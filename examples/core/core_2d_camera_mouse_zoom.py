"""

raylib [core] example - 2d camera mouse zoom

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - 2d camera mouse zoom")

    camera = Camera2D()
    camera.zoom = 1.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            delta = get_mouse_delta()
            delta = vector2_scale(delta, -1.0 / camera.zoom)

            camera.target = vector2_add(camera.target, delta)

        # Zoom based on mouse wheel
        wheel = get_mouse_wheel_move()
        if wheel != 0:
            # Get the world point that is under the mouse
            mouse_world_pos = get_screen_to_world_2d(get_mouse_position(), camera)

            # Set the offset to where the mouse is
            camera.offset = get_mouse_position()

            # Set the target to match, so that the camera maps the world space point
            # under the cursor to the screen space point under the cursor at any zoom
            camera.target = mouse_world_pos

            # Zoom increment
            ZOOM_INCREMENT = 0.125

            camera.zoom += (wheel * ZOOM_INCREMENT)
            if camera.zoom < ZOOM_INCREMENT: camera.zoom = ZOOM_INCREMENT
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(BLACK)

        begin_mode_2d(camera)

        # Draw the 3d grid, rotated 90 degrees and centered around 0,0
        # just so we have something in the XY plane
        rl_push_matrix()
        rl_translatef(0, 25 * 50, 0)
        rl_rotatef(90, 1, 0, 0)
        draw_grid(100, 50)
        rl_pop_matrix()

        # Draw a reference circle
        draw_circle(100, 100, 50, YELLOW)

        end_mode_2d()

        draw_text(b"Mouse right button drag to move, mouse wheel to zoom", 10, 10, 20, WHITE)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
