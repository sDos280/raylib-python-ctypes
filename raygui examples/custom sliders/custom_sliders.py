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
def GuiVerticalSliderPro(bounds: Rectangle, textTop: ctypes.c_char_p, textBottom: ctypes.c_char_p, value: ctypes.c_float, minValue: ctypes.c_float, maxValue: ctypes.c_float, sliderHeight: ctypes.c_int) -> float:
    state = gui_get_state()

    sliderValue = int(((value - minValue)/(maxValue - minValue)) * (bounds.height - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)))

    slider = Rectangle(
        bounds.x + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH) + gui_get_style(GuiControl.SLIDER, GuiControlProperty.SLIDER_PADDING),
        bounds.y + bounds.height - sliderValue,
        bounds.width - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH) - 2 * gui_get_style(GuiControl.SLIDER, GuiControlProperty.SLIDER_PADDING),
        0.0,
    )

    if sliderHeight > 0:        # Slider
        slider.y -= sliderHeight/2
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
                elif sliderHeight == 0:                                          # SliderBar
                    slider.y = mousePoint.y
                    slider.height = bounds.y + bounds.height - slider.y - gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH);
            else:
                state = GuiState.STATE_FOCUSED

        if value > maxValue:
            value = maxValue
        elif value < minValue:
            value = minValue


    # Bar limits check
    if sliderHeight > 0:        # Slider
        if slider.y < (bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)):
            slider.y = bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
        elif (slider.y + slider.height) >= (bounds.y + bounds.height):
            slider.y = bounds.y + bounds.height - slider.height - gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
    elif sliderHeight == 0:  # SliderBar
        if slider.y < (bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)):
            slider.y = bounds.y + gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)
            slider.height = bounds.height - 2*gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH)

    # ----------------------------------------------------------------------------------
    # Draw control
    # ----------------------------------------------------------------------------------
    GuiDrawRectangle(bounds, gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER_WIDTH), Fade(GetColor(gui_get_style(GuiControl.SLIDER, GuiControlProperty.BORDER + (state*3))), guiAlpha), Fade(GetColor(gui_get_style(GuiControl.SLIDER, (state != STATE_DISABLED)?  BASE_COLOR_NORMAL : BASE_COLOR_DISABLED)), guiAlpha));

    // Draw slider internal bar (depends on state)
    if ((state == STATE_NORMAL) || (state == STATE_PRESSED)) GuiDrawRectangle(slider, 0, BLANK, Fade(GetColor(gui_get_style(SLIDER, GuiControlProperty.BASE_COLOR_PRESSED)), guiAlpha));
    else if (state == STATE_FOCUSED) GuiDrawRectangle(slider, 0, BLANK, Fade(GetColor(gui_get_style(SLIDER, GuiControlProperty.TEXT_COLOR_FOCUSED)), guiAlpha));

    // Draw top/bottom text if provided
    if (textTop != NULL)
    {
        Rectangle textBounds = { 0 };
        textBounds.width = (float)GetTextWidth(textTop);
        textBounds.height = (float)gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_SIZE);
        textBounds.x = bounds.x + bounds.width/2 - textBounds.width/2;
        textBounds.y = bounds.y - textBounds.height - gui_get_style(GuiControl.SLIDER, GuiControlProperty.TEXT_PADDING);

        GuiDrawText(textTop, textBounds, TEXT_ALIGN_RIGHT, Fade(GetColor(gui_get_style(GuiControl.SLIDER, TEXT + (state*3))), guiAlpha));
    }

    if (textBottom != NULL)
    {
        Rectangle textBounds = { 0 };
        textBounds.width = (float)GetTextWidth(textBottom);
        textBounds.height = (float)gui_get_style(GuiControl.DEFAULT, GuiControlProperty.TEXT_SIZE);
        textBounds.x = bounds.x + bounds.width/2 - textBounds.width/2;
        textBounds.y = bounds.y + bounds.height + gui_get_style(GuiControl.SLIDER, GuiControlProperty.TEXT_PADDING);

        GuiDrawText(textBottom, textBounds, TEXT_ALIGN_LEFT, Fade(GetColor(gui_get_style(GuiControl.SLIDER, TEXT + (state*3))), guiAlpha));
    }
    //--------------------------------------------------------------------

    return value;


# ----------------------------------------------------------------------------------

# Execute the main function
if __name__ == '__main__':
    main()
