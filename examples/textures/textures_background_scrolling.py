"""

raylib [textures] example - Background scrolling

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [textures] example - background scrolling")

    # NOTE: Be careful, background width must be equal or bigger than screen width
    # if not, texture should be draw more than two times for scrolling effect
    background = load_texture(b"resources/cyberpunk_street_background.png")
    midground = load_texture(b"resources/cyberpunk_street_midground.png")
    foreground = load_texture(b"resources/cyberpunk_street_foreground.png")

    scrollingBack = 0.0
    scrollingMid = 0.0
    scrollingFore = 0.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        scrollingBack -= 0.1
        scrollingMid -= 0.5
        scrollingFore -= 1.0

        # NOTE: Texture is scaled twice its size, so it sould be considered on scrolling
        if scrollingBack <= -background.width * 2: scrollingBack = 0
        if scrollingMid <= -midground.width * 2: scrollingMid = 0
        if scrollingFore <= -foreground.width * 2: scrollingFore = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(get_color(0x052c46ff))

        # Draw background image twice
        # NOTE: Texture is scaled twice its size
        draw_texture_ex(background, Vector2(scrollingBack, 20), 0.0, 2.0, WHITE)
        draw_texture_ex(background, Vector2(background.width * 2 + scrollingBack, 20), 0.0, 2.0, WHITE)

        # Draw midground image twice
        draw_texture_ex(midground, Vector2(scrollingMid, 20), 0.0, 2.0, WHITE)
        draw_texture_ex(midground, Vector2(midground.width * 2 + scrollingMid, 20), 0.0, 2.0, WHITE)

        # Draw foreground image twice
        draw_texture_ex(foreground, Vector2(scrollingFore, 70), 0.0, 2.0, WHITE)
        draw_texture_ex(foreground, Vector2(foreground.width * 2 + scrollingFore, 70), 0.0, 2.0, WHITE)

        draw_text(b"BACKGROUND SCROLLING & PARALLAX", 10, 10, 20, RED)
        draw_text(b"(c) Cyberpunk Street Environment by Luis Zuno (@ansimuz)", SCREEN_WIDTH - 330, SCREEN_HEIGHT - 20, 10, RAYWHITE)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    unload_texture(background)  # Unload background texture
    unload_texture(midground)  # Unload midground texture
    unload_texture(foreground)  # Unload foreground texture

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
