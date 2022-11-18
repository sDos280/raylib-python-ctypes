"""

raylib [shapes] example - bouncing ball

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [shapes] example - bouncing ball")

    ball_position = Vector2(get_screen_height() / 2.0, get_screen_height() / 2.0)
    ball_speed = Vector2(5.0, 4.0)
    ball_radius = 20

    pause = False
    frames_counter = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KeyboardKey.KEY_SPACE): pause = not pause

        if not pause:
            ball_position.x += ball_speed.x
            ball_position.y += ball_speed.y

            # Check walls collision for bouncing
            if ball_position.x >= get_screen_width() - ball_radius or ball_position.x <= ball_radius: ball_speed.x *= -1.0
            if ball_position.y >= get_screen_height() - ball_radius or ball_position.y <= ball_radius: ball_speed.y *= -1.0
        else:
            frames_counter += 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_circle_v(ball_position, ball_radius, MAROON)
        draw_text(b"PRESS SPACE to PAUSE BALL MOVEMENT", 10, get_screen_height() - 25, 20, LIGHTGRAY)

        # On pause, we draw a blinking message

        if pause and (frames_counter / 30) % 2: draw_text(b"PAUSED", 350, 200, 30, GRAY)

        draw_fps(10, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
