"""

raylib [shapes] example - Draw basic shapes 2d (rectangle, circle, line...)

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [shapes] example - basic shapes drawing")

    rotation = 0.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        rotation += 0.2
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_text(b"some basic shapes available on raylib", 20, 20, 20, DARKGRAY)

        # Circle shapes and lines
        draw_circle(int(SCREEN_WIDTH / 5), 120, 35, DARKBLUE)
        draw_circle_gradient(int(SCREEN_WIDTH / 5), 220, 60, GREEN, SKYBLUE)
        draw_circle_lines(int(SCREEN_WIDTH / 5), 340, 80, DARKBLUE)

        # Rectangle shapes and lines
        draw_rectangle(int(SCREEN_WIDTH / 4 * 2 - 60), 100, 120, 60, RED)
        draw_rectangle_gradient_h(int(SCREEN_WIDTH / 4 * 2 - 90), 170, 180, 130, MAROON, GOLD)
        draw_rectangle_lines(int(SCREEN_WIDTH / 4 * 2 - 40), 320, 80, 60, ORANGE)  # NOTE: Uses QUADS internally, not lines

        # Triangle shapes and lines
        draw_triangle(Vector2(SCREEN_WIDTH / 4.0 * 3.0, 80.0),
                      Vector2(SCREEN_WIDTH / 4.0 * 3.0 - 60.0, 150.0),
                      Vector2(SCREEN_WIDTH / 4.0 * 3.0 + 60.0, 150.0), VIOLET)

        draw_triangle_lines(Vector2(SCREEN_WIDTH / 4.0 * 3.0, 160.0),
                            Vector2(SCREEN_WIDTH / 4.0 * 3.0 - 20.0, 230.0),
                            Vector2(SCREEN_WIDTH / 4.0 * 3.0 + 20.0, 230.0), DARKBLUE)

        # Polygon shapes and lines
        draw_poly(Vector2(SCREEN_WIDTH / 4.0 * 3, 330), 6, 80, rotation, BROWN)
        draw_poly_lines(Vector2(SCREEN_WIDTH / 4.0 * 3, 330), 6, 90, rotation, BROWN)
        draw_poly_lines_ex(Vector2(SCREEN_WIDTH / 4.0 * 3, 330), 6, 85, rotation, 6, BEIGE)

        # NOTE: We draw all LINES based shapes together to optimize internal drawing,
        # this way, all LINES are rendered in a single draw pass
        draw_line(18, 42, SCREEN_WIDTH - 18, 42, BLACK)
        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
