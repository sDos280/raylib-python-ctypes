"""

raylib [core] example - 2d camera

"""

from raypyc import *

# Definitions
# ------------------------------------------------------------------------------------
MAX_BUILDINGS = 100


# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - 2d camera")

    player = Rectangle(400, 280, 40, 40)
    buildings = []
    build_colors = []

    spacing = 0

    for i in range(MAX_BUILDINGS):
        buildings.append(Rectangle())
        buildings[i].width = get_random_value(50, 200)
        buildings[i].height = get_random_value(100, 800)
        buildings[i].y = SCREEN_HEIGHT - 130.0 - buildings[i].height
        buildings[i].x = -6000.0 + spacing

        spacing += buildings[i].width
        build_colors.append(Color())
        build_colors[i] = Color(get_random_value(200, 240), get_random_value(200, 240), get_random_value(200, 250), 255)

    camera = Camera2D()
    camera.target = Vector2(player.x + 20.0, player.y + 20.0)
    camera.offset = Vector2(SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0)
    camera.rotation = 0.0
    camera.zoom = 1.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # Player movement
        if is_key_down(KeyboardKey.KEY_RIGHT): player.x += 2
        if is_key_down(KeyboardKey.KEY_LEFT): player.x -= 2

        # Camera target follows player
        camera.target = Vector2(player.x + 20, player.y + 20)

        # Camera rotation controls
        if is_key_down(KeyboardKey.KEY_A):
            camera.rotation -= 1
        elif is_key_down(KeyboardKey.KEY_S):
            camera.rotation += 1

        # Limit camera rotation to 80 degrees (-40 to 40)
        if camera.rotation > 40:
            camera.rotation = 40
        elif camera.rotation < -40:
            camera.rotation = -40

        # Camera zoom controls
        camera.zoom += get_mouse_wheel_move() * 0.05

        if camera.zoom > 3.0:
            camera.zoom = 3.0
        elif camera.zoom < 0.1:
            camera.zoom = 0.1

        # Camera reset (zoom and rotation)
        if is_key_pressed(KeyboardKey.KEY_R):
            camera.zoom = 1.0
            camera.rotation = 0.0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode_2d(camera)

        draw_rectangle(-6000, 320, 13000, 8000, DARKGRAY)

        for i in range(MAX_BUILDINGS): draw_rectangle_rec(buildings[i], build_colors[i])

        draw_rectangle_rec(player, RED)

        draw_line(int(camera.target.x), -SCREEN_HEIGHT * 10, int(camera.target.x), SCREEN_HEIGHT * 10, GREEN)
        draw_line(-SCREEN_WIDTH * 10, int(camera.target.y), SCREEN_WIDTH * 10, int(camera.target.y), GREEN)

        end_mode_2d()

        draw_text(b"SCREEN AREA", 640, 10, 20, RED)

        draw_rectangle(0, 0, SCREEN_WIDTH, 5, RED)
        draw_rectangle(0, 5, 5, SCREEN_HEIGHT - 10, RED)
        draw_rectangle(SCREEN_WIDTH - 5, 5, 5, SCREEN_HEIGHT - 10, RED)
        draw_rectangle(0, SCREEN_HEIGHT - 5, SCREEN_WIDTH, 5, RED)

        draw_rectangle(10, 10, 250, 113, fade(SKYBLUE, 0.5))
        draw_rectangle_lines(10, 10, 250, 113, BLUE)

        draw_text(b"Free 2d camera controls:", 20, 20, 10, BLACK)
        draw_text(b"- Right/Left to move Offset", 40, 40, 10, DARKGRAY)
        draw_text(b"- Mouse Wheel to Zoom in-out", 40, 60, 10, DARKGRAY)
        draw_text(b"- A / S to Rotate", 40, 80, 10, DARKGRAY)
        draw_text(b"- R to reset Zoom and Rotation", 40, 100, 10, DARKGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
