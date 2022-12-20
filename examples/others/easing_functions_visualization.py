"""
Reasings Visualization.
Copyright 2022 James R. Byerly. No Rights Reserved.
(python/raypyc implementation)
original example: https://github.com/dv-extrarius/raylib-easings-vis
Note: python 3.11+ is required to run this example

You may use this under the terms of the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication,
which is available at https://creativecommons.org/publicdomain/zero/1.0/
"""

from raypyc import *
from raypyc.reasings import *

# Definitions
# ------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRAPH_OFFSET_X = 50
GRAPH_OFFSET_Y = 50
GRAPH_WIDTH = 500
GRAPH_HEIGHT = 500

SIT_STILL_TIME = 0.25
TIMR_SPAN = 3.0

EASING_FUNCTION_NAMES = [
    b"EaseLinearNone",
    b"EaseLinearIn",
    b"EaseLinearOut",
    b"EaseLinearInOut",
    b"EaseSineIn",
    b"EaseSineOut",
    b"EaseSineInOut",
    b"EaseCircIn",
    b"EaseCircOut",
    b"EaseCircInOut",
    b"EaseQuadIn",
    b"EaseQuadOut",
    b"EaseQuadInOut",
    b"EaseExpoIn",
    b"EaseExpoOut",
    b"EaseExpoInOut",
    b"EaseBackIn",
    b"EaseBackOut",
    b"EaseBackInOut",
    b"EaseBounceIn",
    b"EaseBounceOut",
    b"EaseBounceInOut",
    b"EaseElasticIn",
    b"EaseElasticOut",
    b"EaseElasticInOut"
]


def calculate_easing(function: int, time: float, startValue: float, deltaValue: float, duration: float) -> float:
    match function % 25:
        # Ease Linear
        case 0:
            return ease_linear_none(time, startValue, deltaValue, duration)
        case 1:
            return ease_linear_in(time, startValue, deltaValue, duration)
        case 2:
            return ease_linear_out(time, startValue, deltaValue, duration)
        case 3:
            return ease_linear_in_out(time, startValue, deltaValue, duration)

        # Ease Sine
        case 4:
            return ease_sine_in(time, startValue, deltaValue, duration)
        case 5:
            return ease_sine_out(time, startValue, deltaValue, duration)
        case 6:
            return ease_sine_in_out(time, startValue, deltaValue, duration)

        # Ease Circ
        case 7:
            return ease_circ_in(time, startValue, deltaValue, duration)
        case 8:
            return ease_circ_out(time, startValue, deltaValue, duration)
        case 9:
            return ease_circ_in_out(time, startValue, deltaValue, duration)

        # Ease Quad
        case 10:
            return ease_quad_in(time, startValue, deltaValue, duration)
        case 11:
            return ease_quad_out(time, startValue, deltaValue, duration)
        case 12:
            return ease_quad_in_out(time, startValue, deltaValue, duration)

        # Ease Expo
        case 13:
            return ease_expo_in(time, startValue, deltaValue, duration)
        case 14:
            return ease_expo_out(time, startValue, deltaValue, duration)
        case 15:
            return ease_expo_in_out(time, startValue, deltaValue, duration)

        # Ease Back
        case 16:
            return ease_back_in(time, startValue, deltaValue, duration)
        case 17:
            return ease_back_out(time, startValue, deltaValue, duration)
        case 18:
            return ease_back_in_out(time, startValue, deltaValue, duration)

        # Ease Bounce
        case 19:
            return ease_bounce_in(time, startValue, deltaValue, duration)
        case 20:
            return ease_bounce_out(time, startValue, deltaValue, duration)
        case 21:
            return ease_bounce_in_out(time, startValue, deltaValue, duration)

        # Ease Elastic
        case 22:
            return ease_elastic_in(time, startValue, deltaValue, duration)
        case 23:
            return ease_elastic_out(time, startValue, deltaValue, duration)
        case 24:
            return ease_elastic_in_out(time, startValue, deltaValue, duration)
        case _:  # Can't actually reach here, but it silences a warning
            return 0.0

        # ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - 2d camera")

    easing_function_1 = 0
    easing_function_2 = 20
    current_time = 0.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # Update Time and wrap to the range 0..(TIMR_SPAN + 2 * SIT_STILL_TIME)
        current_time += get_frame_time()
        current_time = current_time % (TIMR_SPAN + 2.0 * SIT_STILL_TIME)

        # Calculate a fake time that sits still for a bit at the start and end
        fake_current_time = current_time
        if fake_current_time < SIT_STILL_TIME:
            fake_current_time = 0.0
        elif fake_current_time < SIT_STILL_TIME + TIMR_SPAN:
            fake_current_time -= SIT_STILL_TIME
        else:
            fake_current_time = TIMR_SPAN

        # Update Functions based on input
        if is_key_pressed(KeyboardKey.KEY_ONE):
            easing_function_1 = (easing_function_1 + 1) % 25
        elif is_key_pressed(KeyboardKey.KEY_TWO):
            easing_function_2 = (easing_function_2 + 1) % 25
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()
        clear_background(BLACK)

        # Fill in the graph
        # Easing from GRAPH_OFFSET_Y to GRAPH_OFFSET_Y + GRAPH_HEIGHT, current time is 0 out of GRAPH_WIDTH
        prev_position1 = calculate_easing(easing_function_1, 0.0, GRAPH_OFFSET_Y, GRAPH_HEIGHT, GRAPH_WIDTH)
        prev_position2 = calculate_easing(easing_function_2, 0.0, GRAPH_OFFSET_Y, GRAPH_HEIGHT, GRAPH_WIDTH)
        for ii in range(0, GRAPH_WIDTH, 5):
            # Easing from GRAPH_OFFSET_Y to GRAPH_OFFSET_Y + GRAPH_HEIGHT, current time is ii out of GRAPH_WIDTH
            next_position1 = calculate_easing(easing_function_1, ii + 5, GRAPH_OFFSET_Y, GRAPH_HEIGHT, GRAPH_WIDTH)
            next_position2 = calculate_easing(easing_function_2, ii + 5, GRAPH_OFFSET_Y, GRAPH_HEIGHT, GRAPH_WIDTH)

            draw_line(ii + GRAPH_OFFSET_X, int(prev_position1), ii + 5 + GRAPH_OFFSET_X, int(next_position1), RED)
            draw_line(ii + GRAPH_OFFSET_X, int(prev_position2), ii + 5 + GRAPH_OFFSET_X, int(next_position2), BLUE)

            prev_position1 = next_position1
            prev_position2 = next_position2

        # Draw instructions
        draw_text(b"Press 1 to change red easing, 2 to change blue easing", 0, 0, 20, WHITE)

        # Draw a graph box with labels
        text_time_width = measure_text(b"Time", 20)
        draw_text(b"Time", int(GRAPH_OFFSET_X + (GRAPH_WIDTH - text_time_width) / 2), GRAPH_OFFSET_Y - 20, 20, WHITE)
        text_position_width = measure_text(b"Position", 20)
        draw_text_pro(get_font_default(), b"Position",
                      Vector2(GRAPH_OFFSET_X - 20.0, GRAPH_OFFSET_Y + (GRAPH_HEIGHT + text_position_width) / 2.0),
                      Vector2(0.0, 0.0),
                      -90.0, 20.0, 2.0, WHITE)
        draw_rectangle_lines(GRAPH_OFFSET_X, GRAPH_OFFSET_Y, GRAPH_WIDTH, GRAPH_HEIGHT, WHITE)

        # Draw Legend
        draw_text(EASING_FUNCTION_NAMES[easing_function_1], GRAPH_OFFSET_X, GRAPH_OFFSET_Y + GRAPH_HEIGHT, 20, RED)
        draw_text(EASING_FUNCTION_NAMES[easing_function_2], GRAPH_OFFSET_X, GRAPH_OFFSET_Y + GRAPH_HEIGHT + 20, 20, BLUE)

        # Draw timeline on graph
        time_x = int(GRAPH_OFFSET_X + GRAPH_WIDTH * (fake_current_time / TIMR_SPAN))
        draw_line(time_x, GRAPH_OFFSET_X, time_x, GRAPH_OFFSET_Y + GRAPH_HEIGHT, GREEN)

        # Draw Boxes, easing from GRAPH_OFFSET_Y to GRAPH_OFFSET_Y + GRAPH_HEIGHT over TIMR_SPAN seconds
        box1_y = calculate_easing(easing_function_1, fake_current_time, GRAPH_OFFSET_Y, GRAPH_HEIGHT, TIMR_SPAN)
        box2_y = calculate_easing(easing_function_2, fake_current_time, GRAPH_OFFSET_Y, GRAPH_HEIGHT, TIMR_SPAN)
        draw_rectangle(GRAPH_OFFSET_X + GRAPH_WIDTH + 50, int(box1_y - 25), 50, 50, RED)
        draw_rectangle(GRAPH_OFFSET_X + GRAPH_WIDTH + 150, int(box2_y - 25), 50, 50, BLUE)

        # Draw outlines at start and end position
        draw_rectangle_lines(GRAPH_OFFSET_X + GRAPH_WIDTH + 50, GRAPH_OFFSET_Y - 25, 50, 50, RED)
        draw_rectangle_lines(GRAPH_OFFSET_X + GRAPH_WIDTH + 50, GRAPH_OFFSET_Y + GRAPH_HEIGHT - 25, 50, 50, RED)
        draw_rectangle_lines(GRAPH_OFFSET_X + GRAPH_WIDTH + 150, GRAPH_OFFSET_Y - 25, 50, 50, BLUE)
        draw_rectangle_lines(GRAPH_OFFSET_X + GRAPH_WIDTH + 150, GRAPH_OFFSET_Y + GRAPH_HEIGHT - 25, 50, 50, BLUE)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
