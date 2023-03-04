## Python API Coding Style Conventions

Here is a list with some code conventions used by raylib in python:

| Code element        |            Convention             | Example                                   |
|---------------------|:---------------------------------:|-------------------------------------------|
| Variables           |            lower_case             | `delta_time = 0`, `player_age = 18`       |
| Local variables     |            lower_case             | `player_position = Vector2(0, 0)`         |
| Global variables    |            lower_case             | `window_ready = False`                    |
| Constants variables |             ALL_CAPS              | `MAX_VALUE = 8`, `SCREEN_WIDTH = 800`     |
| Definitions values  |             ALL_CAPS              | `MAX_BUILDINGS = 5`[^1]                   |
| string values       |       always ' ' or " "[^2]       | `output = "Hello"`, `'welcome'`[^3]       |
| float values        |            always x.x             | `gravity = 10.0`                          |
| Operators           |          value1 * value2          | `product = value * 6`                     |
| Operators           |          value1 / value2          | `division = value / 4`                    |
| Operators           |          value1 + value2          | `sum = value + 10`                        |
| Operators           |          value1 - value2          | `res = value - 5`                         |
| Class               |             TitleCase             | `class TextureFormat`                     |
| Enum Class members  |             ALL_CAPS              | `PIXELFORMAT_UNCOMPRESSED_R8G8B8`         |
| Class members       |             lowerCase             | `texture.width`, `color.r`                |
| Functions           |   lowerCase & wordSeparationBy_   | `init_window()`, `update_camera_center()` |
| Functions params    |             lowerCase             | `width`, `height`                         |
| Ternary Operator    | result1 if condition else result2 | `print("yes" if value == 0 else "no")`    |

[^1] like `macro definitions` of value in C

[^2] most of the time we use "..." for string and ' ' to char

[^3] most of the time raypyc need you to use bytes object and not a string object to convert.
to convert string object to bytes object use or b"..." or "...".encode('uft-8')

Some other conventions to follow:

- **ALWAYS** initialize all defined variables.
- **Use Tabs**.
- Avoid trailing spaces, please, avoid them
- Avoid using **semicolon** as you can
- Control flow statements always are followed **by a space**:

```python
if condition : value = 0

while not window_should_close():
    #Do something here!

for i in range(NUM_VALUES): print(i)
```

```python
if value > 1 and value1 < 50 and valueActive:
    #Do something here!
```

**If proposing new functions, please try to use a clear naming for function-name and functions-parameters, in case of
doubt, open an issue for discussion.**

## Import libraries and Module

- import libraries with the form `from library import *`
- import modules/variables from libraries with the form `from library import (module1, ..., variable1, ...)`

```python
from raypyc import *
from raypyc.colors import (
    RAYWHITE,
    DARKGRAY,
    ...
)
```

## Files and Directories Naming Conventions

- Directories will be named using `snake_case`: `resources/models`, `resources/fonts`

- Files will be named using `snake_case`: `main_title.png`, `cubicmap.png`, `sound.wav`

_NOTE: Avoid any space or special character in the files/dir naming!_

## Games/Examples Directories Organization Conventions

- Data files should be organized by context and usage in the game, think about the loading requirements for data and put
  all the resources that need to be loaded at the same time together.
- Use descriptive names for the files, it would be perfect if just reading the name of the file, it was possible to know
  what is that file and where fits in the game.
- Here is an example, note that some resources require to be loaded all at once while other require to be loaded only at
  initialization (gui, font).

```
resources/audio/fx/long_jump.wav
resources/audio/music/main_theme.ogg
resources/screens/logo/logo.png
resources/screens/title/title.png
resources/screens/gameplay/background.png
resources/characters/player.png
resources/characters/enemy_slime.png
resources/common/font_arial.ttf
resources/common/gui.png
```

## Example Conventions For Python API

- examples ***should*** have the following structure

```python
"""

raylib [raylib module] example - example explanation

"""

# do all the import stuff here


# Definitions
# ------------------------------------------------------------------------------------
# Define you functions/global variables here
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    # Do something here!
    # ------------------------------------------------------------------------------------

    # Main game loop
    while ... :
        # Update
        # ----------------------------------------------------------------------------------
        # Do something here!
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        # Do something here!
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    # Do something here!
    # ----------------------------------------------------------------------------------

# Execute the main function
if __name__ == '__main__':
    main()
```

- temple (basic window example):

```python
"""

raylib [core] example - Basic Window

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - basic window")

    # TODO: Load resources / Initialize variables at this point

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

        clear_background(RAYWHITE)
        draw_text(b"Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------

    # TODO: Unload all loaded resources at this point

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
```

## Ctypes Classes

to use the raypyc function we will need to use the structs that provided with raylib, that why we need to learn to
convert c struct to python class.

- when we want to use c structs in python we create a ctypes class object
- here is an example of converting the c vector2 struct to a valid python class that can be used by raypyc
- the c struct:

```c
typedef struct Vector2 {
    float x;
    float y;
} Vector2;
```

-
    1. first we need to import all the stuff from ctypes for later use (you can also just include raypyc, ctypes already
       included in there...)

```python
"from ctypes import *"

# the rest of the code will go here
```

-
    2. create a class named Vector2 that inherits from "Structure"

```python
class Vector2(Structures):
```

-
    3. add the data of the structure(class), the \_fields_ list has pairs of `("name of variable", ctypes type)`( for
       example: x is a variable of Vector2 with the c_float type, to see the types and their usage look in
       here: [fundamental-data-types](https://docs.python.org/3/library/ctypes.html#fundamental-data-types) ), can you
       see how the c_float type match with the float type

```python
class Vector2(Structures):
    _fields_ = [
		('x', c_float),
		('y', c_float)
	]
```

-
    4. recommended: add setter and getter to structure(class)

```python
class Vector2(Structure):
	_fields_ = [
		('x', c_float),  
		('y', c_float)  
	]

	@property
	def x(self) -> float:
		return self.x

	@x.setter
	def x(self, i: float) -> None:
		self.x = i

	@property
	def y(self) -> float:
		return self.y

	@y.setter
	def y(self, i: float) -> None:
		self.y = i
```

- and here we finished 😃. to see more example of c struct to python classes look [here](raypyc/structures/__init__.py)
