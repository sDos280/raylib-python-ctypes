"""

raylib [models] example - loading gltf with animations

"""

import ctypes

from raypyc import *
from ctypes import *


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [models] example - loading gltf")

    camera = Camera()
    camera.position = Vector3(5.0, 5.0, 5.0)  # Camera position
    camera.target = Vector3(0.0, 2.0, 0.0)  # Camera looking at point
    camera.up = Vector3(0.0, 1.0, 0.0)  # Camera up vector (rotation towards target)
    camera.fovy = 45.0  # Camera field-of-view Y
    camera.projection = CameraProjection.CAMERA_PERSPECTIVE  # Camera mode type

    # Load gltf model
    model = load_model(b"resources/models/gltf/robot.glb")
    animsCount = c_uint(0)
    animIndex = 0
    animCurrentFrame = 0

    modelAnimations = load_model_animations(b"resources/models/gltf/robot.glb", ctypes.pointer(animsCount))

    position = Vector3(0.0, 0.0, 0.0)  # Set model position
    set_camera_mode(camera, CameraMode.CAMERA_FREE)  # Set free camera mode

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # Select current animation
        if is_key_pressed(KeyboardKey.KEY_UP): animIndex = (animIndex + 1) % animsCount
        if is_key_pressed(KeyboardKey.KEY_DOWN): animIndex = (animIndex + animsCount - 1) % animsCount

        # Update model animation
        anim = modelAnimations[animIndex]
        animCurrentFrame = (animCurrentFrame + 1) % anim.frameCount
        update_model_animation(model, anim, animCurrentFrame)

        # Update camera
        update_camera(pointer(camera))
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode_3d(camera)

        draw_model(model, position, 1.0, WHITE)  # Draw animated model
        draw_grid(10, 1.0)

        end_mode_3d()

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
