"""

raylib [audio] example - Music playing (streaming)

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [audio] example - music playing (streaming)")

    init_audio_device()  # Initialize audio device

    music = load_music_stream(b"resources/country.mp3")

    play_music_stream(music)

    time_played = 0.0  # Time played normalized [0.0f..1.0f]
    pause = False  # Music playing paused

    set_target_fps(30)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        update_music_stream(music)  # Update music buffer with new stream data

        # Restart music playing (stop and play)
        if is_key_pressed(KeyboardKey.KEY_SPACE):
            stop_music_stream(music)
            play_music_stream(music)

        # Pause/Resume music playing
        if is_key_pressed(KeyboardKey.KEY_P):
            pause = not pause

            if pause:
                pause_music_stream(music)
            else:
                resume_music_stream(music)

        # Get normalized time played for current music stream
        timePlayed = get_music_time_played(music) / get_music_time_length(music)

        if timePlayed > 1.0: timePlayed = 1.0  # Make sure time played is no longer than music

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_text(b"MUSIC SHOULD BE PLAYING!", 255, 150, 20, LIGHTGRAY)

        draw_rectangle(200, 200, 400, 12, LIGHTGRAY)
        draw_rectangle(200, 200, int(timePlayed * 400.0), 12, MAROON)
        draw_rectangle_lines(200, 200, 400, 12, GRAY)

        draw_text(b"PRESS SPACE TO RESTART MUSIC", 215, 250, 20, LIGHTGRAY)
        draw_text(b"PRESS P TO PAUSE/RESUME MUSIC", 208, 280, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    unload_music_stream(music)  # Unload music stream buffers from RAM

    close_audio_device()  # Close audio device (music streaming is automatically stopped)

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
