"""

raylib [shapes] example - Draw basic shapes 2d (rectangle, circle, line...)

"""

# Import
# ------------------------------------------------------------------------------------
from raypyc import *
from raypyc.reasings import *


# ------------------------------------------------------------------------------------

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
    ballPositionX = -100
    ballRadius = 20
    ballAlpha = 0.0

    state = 0
    framesCounter = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:  # Move ball position X with easing
            framesCounter += 1
            ballPositionX = int(ease_elastic_out(float(framesCounter), -100, SCREEN_WIDTH / 2.0 + 100, 120))

            if framesCounter >= 120:
                framesCounter = 0
                state = 1

        elif state == 1:  # Increase ball radius with easing
            framesCounter += 1
            ballRadius = int(ease_elastic_in(float(framesCounter), 20, 500, 200))

            if framesCounter >= 200:
                framesCounter = 0
                state = 2

        elif state == 2:  # Change ball alpha with easing (background color blending)
            framesCounter += 1
            ballAlpha = ease_cubic_out(float(framesCounter), 0.0, 1.0, 200)

            if framesCounter >= 200:
                framesCounter = 0
                state = 3

        elif state == 3:  # Reset state to play again
            if is_key_pressed(KeyboardKey.KEY_ENTER):
                # Reset required variables to play again
                ballPositionX = -100
                ballRadius = 20
                ballAlpha = 0.0
                state = 0

        if is_key_pressed(KeyboardKey.KEY_R): framesCounter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if state >= 2: draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, GREEN)
        draw_circle(ballPositionX, 200, float(ballRadius), fade(RED, 1.0 - ballAlpha))

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
