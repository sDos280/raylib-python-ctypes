"""

raylib [core] example - Initialize 3d camera free

"""

from raypyc import *
from ctypes import c_char, c_int

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - 3d camera free")

    # Define the camera to look into our 3d world
    camera = Camera3D()
    camera.position = Vector3(10.0, 10.0, 10.0)  # Camera position
    camera.target = Vector3(0.0, 0.0, 0.0)  # Camera looking at point
    camera.up = Vector3(0.0, 1.0, 0.0)  # Camera up vector (rotation towards target)
    camera.fovy = 45.0  # Camera field-of-view Y
    camera.projection = CameraProjection.CAMERA_PERSPECTIVE  # Camera mode type

    cubePosition = Vector3(0.0, 0.0, 0.0)

    set_camera_mode(camera, CameraMode.CAMERA_FREE)  # Set a free camera mode
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        update_camera(camera)
        if is_key_down(ord('Z')): camera.target = Vector3(0.0, 0.0, 0.0)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode_3d(camera)

        draw_cube(cubePosition, 2.0, 2.0, 2.0, RED)
        draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, RED)

        draw_grid(10, 1.0)

        end_mode_3d()

        draw_rectangle(10, 10, 320, 133, fade(SKYBLUE, 0.5))
        draw_rectangle_lines(10, 10, 320, 133, BLUE)

        draw_text(b"Free camera default controls:", 20, 20, 10, BLACK)
        draw_text(b"- Mouse Wheel to Zoom in-out", 40, 40, 10, DARKGRAY)
        draw_text(b"- Mouse Wheel Pressed to Pan", 40, 60, 10, DARKGRAY)
        draw_text(b"- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, DARKGRAY)
        draw_text(b"- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, DARKGRAY)
        draw_text(b"- Z to zoom to (0, 0, 0)", 40, 120, 10, DARKGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
