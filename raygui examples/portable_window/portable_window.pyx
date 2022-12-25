"""

raygui - portable window

"""

from raypyc cimport *


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    SetConfigFlags(ConfigFlags.FLAG_WINDOW_UNDECORATED)
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "raygui - portable window")

    # General variables
    cdef Vector2 mouse_position = Vector2(0, 0)
    cdef Vector2 window_position = Vector2(500, 200)
    pan_offset = mouse_position
    drag_window = False

    SetWindowPosition(int(window_position.x), int(window_position.y))

    exit_window = False

    SetTargetFPS(60)
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not WindowShouldClose() and not exit_window:  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_position = GetMousePosition()

        if IsMouseButtonPressed(MouseButton.MOUSE_BUTTON_LEFT):
            if CheckCollisionPointRec(mouse_position, Rectangle(0, 0, SCREEN_WIDTH, 20)):
                drag_window = True
                pan_offset = mouse_position

        if drag_window:
            window_position.x += mouse_position.x - pan_offset.x
            window_position.y += mouse_position.y - pan_offset.y
            if IsMouseButtonReleased(MouseButton.MOUSE_BUTTON_LEFT): drag_window = False

            SetWindowPosition(int(window_position.x), int(window_position.y))
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        BeginDrawing()

        ClearBackground(Color(245, 245, 245, 255))

        exit_window = GuiWindowBox(Rectangle(0, 0, SCREEN_WIDTH, SCREEN_WIDTH), "#198# PORTABLE WINDOW")

        DrawText(f"Mouse Position: [ {mouse_position.x}, {mouse_position.y} ]".encode(), 10, 40, 10, Color(80, 80, 80, 255))

        EndDrawing()

    # De-Initialization
    # ----------------------------------------------------------------------------------
    CloseWindow()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
