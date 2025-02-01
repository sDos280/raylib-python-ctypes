"""

raygui - custom sliders

"""

"""

raylib [core] example - Basic Window

"""

import ctypes

from raypyc import *


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raygui - custom sliders")

    value = 0.5

    slider_edit_Mode = False
    vSlider_edit_Mode = False
    vSlider_bar_edit_Mode = False

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update variables / Implement example logic at this point
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(get_color(gui_get_state(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR)))

        if vSlider_edit_Mode or vSlider_bar_edit_Mode:
            gui_lock()
        else:
            gui_unlock()

        # raygui: controls drawing
        # ----------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------

    # TODO: Unload all loaded resources at this point

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
def gui_fade(color: Color, alpha: float) -> Color:
    # Clamp alpha value between 0.0 and 1.0
    if alpha < 0.0:
        alpha = 0.0
    elif alpha > 1.0:
        alpha = 1.0

    # Create a new Color with the adjusted alpha value
    result = Color(color.r, color.g, color.b, int(color.a * alpha))

    return result


def gui_draw_rectangle(rec: Rectangle, border_width: int, border_color: Color, color: Color):
    if color.a > 0:
        # Draw rectangle filled with color
        draw_rectangle(int(rec.x), int(rec.y), int(rec.width), int(rec.height), gui_fade(color, 1.0))

    if border_width > 0:
        # Draw rectangle borderlines with color
        draw_rectangle(int(rec.x), int(rec.y), int(rec.width), border_width, gui_fade(border_color, 1.0))
        draw_rectangle(int(rec.x), int(rec.y) + border_width, border_width, int(rec.height) - 2 * border_width, gui_fade(border_color, 1.0))
        draw_rectangle(int(rec.x) + int(rec.width) - border_width, int(rec.y) + border_width, border_width, int(rec.height) - 2 * border_width, gui_fade(border_color, gui_alpha))
        draw_rectangle(int(rec.x), int(rec.y) + int(rec.height) - border_width, int(rec.width), border_width, gui_fade(border_color, 1.0))


# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
def GuiVerticalSliderPro(bounds: Rectangle, textTop: ctypes.c_char_p, textBottom: ctypes.c_char_p, value: ctypes.c_float, minValue: ctypes.c_float, maxValue: ctypes.c_float, sliderHeight: ctypes.c_int) -> float:
    state = gui_get_state()

    sliderValue = int(((value - minValue) / (maxValue - minValue)) * (bounds.height - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)))

    slider = Rectangle(
        bounds.x + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH) + gui_get_style(GuiControl.SLIDER, GuiControlProperty.SLIDER_PADDING),
        bounds.y + bounds.height - sliderValue,
        bounds.width - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH) - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.SLIDER_PADDING),
        0.0,
    )

    if sliderHeight > 0:  # Slider
        slider.y -= sliderHeight / 2
        slider.height = float(sliderHeight)
    elif sliderHeight == 0:  # SliderBar
        slider.y -= gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
        slider.height = float(sliderValue)

    # Update control
    # ----------------------------------------------------------------------------------
    if state != GuiState.STATE_DISABLED and not gui_is_locked():
        mousePoint = get_mouse_position()

        if check_collision_point_rec(mousePoint, bounds):
            if is_mouse_button_down(MouseButton.MOUSE_LEFT_BUTTON):
                state = GuiState.STATE_PRESSED

                # Get equivalent value and slider position from mousePoint.x
                normalizedValue = (bounds.y + bounds.height - mousePoint.y - (sliderHeight / 2)) / (bounds.height - sliderHeight)
                value = (maxValue - minValue) * normalizedValue + minValue

                if sliderHeight > 0:
                    slider.y = mousePoint.y - slider.height / 2  # Slider
                elif sliderHeight == 0:  # SliderBar
                    slider.y = mousePoint.y
                    slider.height = bounds.y + bounds.height - slider.y - gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH);
            else:
                state = GuiState.STATE_FOCUSED

        if value > maxValue:
            value = maxValue
        elif value < minValue:
            value = minValue

    # Bar limits check
    if sliderHeight > 0:  # Slider
        if slider.y < (bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)):
            slider.y = bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
        elif (slider.y + slider.height) >= (bounds.y + bounds.height):
            slider.y = bounds.y + bounds.height - slider.height - gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
    elif sliderHeight == 0:  # SliderBar
        if slider.y < (bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)):
            slider.y = bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
            slider.height = bounds.height - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)

        # ----------------------------------------------------------------------------------
        # Draw control
        # ----------------------------------------------------------------------------------
        gui_draw_rectangle(
            bounds,  # Rectangle object
            gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH),  # Border width
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER + (state * 3))),
                1.0
            ),  # Border color (faded)
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, GuiControlProperty.BASE_COLOR_NORMAL if state != GuiState.STATE_DISABLED else GuiControlProperty.BASE_COLOR_DISABLED)),
                1.0
            )  # Base color (faded)
        )

    # Draw slider internal bar(depends on state)
    if (state == GuiState.STATE_NORMAL) or (state == GuiState.STATE_PRESSED):
        gui_draw_rectangle(
            slider,  # Rectangle object
            0,  # Border width
            BLANK,  # Border color (blank/transparent)
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, GuiControlProperty.BASE_COLOR_PRESSED)),
                1.0
            )  # Base color (faded)
        )
    elif state == GuiState.STATE_FOCUSED:
        draw_rectangle(
            slider,  # Rectangle object
            0,  # Border width
            BLANK,  # Border color (blank/transparent)
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, GuiControlProperty.TEXT_COLOR_FOCUSED)),
                1.0
            )  # Base color (faded)
        )

    # Draw top/bottom text if provided
    if textTop is not None:
        textBounds = Rectangle(0, 0, 0, 0)
        textBounds.width = float(get_text_width(textTop))  # Get width of the top text
        textBounds.height = float(gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_SIZE))  # Get text height
        textBounds.x = bounds.x + bounds.width / 2 - textBounds.width / 2  # Center horizontally
        textBounds.y = bounds.y - textBounds.height - gui_get_style(GuiControl.SLIDER, GuiControlProperty.TEXT_PADDING)  # Position above the bounds

        # Draw the top text
        GuiDrawText(
            textTop,
            textBounds,
            TEXT_ALIGN_RIGHT,
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, TEXT + (state * 3))),
                guiAlpha
            )
        )

    if textBottom is not None:
        textBounds = Rectangle(0, 0, 0, 0)
        textBounds.width = float(get_text_width(textBottom))  # Get width of the bottom text
        textBounds.height = float(gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_SIZE))  # Get text height
        textBounds.x = bounds.x + bounds.width / 2 - textBounds.width / 2  # Center horizontally
        textBounds.y = bounds.y + bounds.height + gui_get_style(GuiControl.SLIDER, GuiControlProperty.TEXT_PADDING)  # Position below the bounds

        # Draw the bottom text
        GuiDrawText(
            textBottom,
            textBounds,
            TEXT_ALIGN_LEFT,
            fade(
                get_color(gui_get_style(GuiControl.SLIDER, TEXT + (state * 3))),
                guiAlpha
            )
        )

    # Return the value (placeholder)
    return value

        # ----------------------------------------------------------------------------------

        # Execute the main function
        if __name__ == '__main__':
            main()
