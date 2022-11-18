"""

raylib [shapes] example - Draw basic shapes 2d (rectangle, circle, line...)

"""

from raypyc import *
from raypyc.reasings import *


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [shapes] example - easings ball anim")

    # Ball variable value to be animated with easings
    ball_position_x = -100
    ball_radius = 20
    ball_alpha = 0.0

    state = 0
    frames_counter = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:  # Move ball position X with easing
            frames_counter += 1
            ball_position_x = int(ease_elastic_out(float(frames_counter), -100, SCREEN_WIDTH / 2.0 + 100, 120))

            if frames_counter >= 120:
                frames_counter = 0
                state = 1

        elif state == 1:  # Increase ball radius with easing
            frames_counter += 1
            ball_radius = int(ease_elastic_in(float(frames_counter), 20, 500, 200))

            if frames_counter >= 200:
                frames_counter = 0
                state = 2

        elif state == 2:  # Change ball alpha with easing (background color blending)
            frames_counter += 1
            ball_alpha = ease_cubic_out(float(frames_counter), 0.0, 1.0, 200)

            if frames_counter >= 200:
                frames_counter = 0
                state = 3

        elif state == 3:  # Reset state to play again
            if is_key_pressed(KeyboardKey.KEY_ENTER):
                # Reset required variables to play again
                ball_position_x = -100
                ball_radius = 20
                ball_alpha = 0.0
                state = 0

        if is_key_pressed(KeyboardKey.KEY_R): frames_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if state >= 2: draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, GREEN)
        draw_circle(ball_position_x, 200, float(ball_radius), fade(RED, 1.0 - ball_alpha))

        if state == 3: draw_text(b"PRESS [ENTER] TO PLAY AGAIN!", 240, 200, 20, BLACK)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
