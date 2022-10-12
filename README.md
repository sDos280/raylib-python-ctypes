# raylib-python-ctypes

A python wrapper for the greatest graphic library **[raylib](https://github.com/raysan5/raylib)**.

### Prerequisites
_raypyc_ uses type [annotations](https://www.python.org/dev/peps/pep-3107/#id30) in its source, so a Python version that supports it is required.

### Installing
the fastest way to use raypyc is by using the pip install command:

```
pip install raypyc
```

or

```
python -m pip install raypyc
```

## Using raypyc 
using raypyc is really simple, make a look at an example[^1]:

```python
"""

raylib [core] example - Basic Window

"""

# Import
# ------------------------------------------------------------------------------------
from raypyc import *
# ------------------------------------------------------------------------------------

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
[^1]the example use a main function to run, you don't have to use that if you don't want to...

## _raylib_ vs _raypyc_

Below are the differences in usage between _raylib_ and _raypyc_.

### Enums

All C `typeof enum`s got translated to Python 'constants'. Enums got translated to
Python [enums](https://docs.python.org/3/library/enum.html).

### Structures

In general, all structures inherit from `ctypes.Structure` class. At the moment, all the structures have a setters & getter

### Contributing
firstly, Contributions of any kind welcome!.

secondly, here are some of the things that contributing on will help this wrapper the most:
 * porting examples from c to python(if you can, please follow along with the [conventions](https://github.com/sDos280/raylib-python-ctypes/blob/main/CONVENTIONS.md) when porting). ([_C_ examples](https://github.com/raysan5/raylib/tree/master/examples), [_Python_ examples](https://github.com/sDos280/raylib-python-ctypes))
 * fixing(refactoring) my [fileGeneration](https://github.com/sDos280/raylib-python-ctypes/blob/main/filesGeneration.py) code: so it will be able to accept arrays of pointer, so it will look neater...
 * making the wrapper able to port to more operating systems
 * adding support to sound with the library. (make the library wrap sound functions/structures) 
 * wrapping more [_c_ raylib header](https://github.com/raysan5/raylib/tree/master/src) to this library[^2]

[^2] NOTE: at least for now, all the non-functions wrapper stuff need be implemented in the [filesGeneration.py](https://github.com/sDos280/raylib-python-ctypes/blob/main/filesGeneration.py) file, and all the functions wrapper stuff need be implemented in the [raypyc/__init__.py](https://github.com/sDos280/raylib-python-ctypes/blob/main/raypyc/__init__.py)

## thanks
thanks to [raysun5](https://github.com/raysan5), [raylibpy](https://github.com/Ho011/pyraylib) and [pyray](https://github.com/sDos280/raylib-python-cffi) for their good work, I took all the inspiration (and some code ;) ) from them, so thanks you guys very much