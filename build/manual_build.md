## Windows build steps

* before we start make sure that you have `make` and `git` on your device.
* get raypyc and go to build folder.

```cmd
git clone --depth 1 https://github.com/sDos280/raylib-python-ctypes
cd ./raylib-python-ctypes/build
```

* get raudio, raylib and raygui.

```cmd
git clone --depth 1 https://github.com/raysan5/raylib
git clone --depth 1 https://github.com/raysan5/raudio
git clone --depth 1 https://github.com/raysan5/raygui
```

* compile raudio.

```cmd
gcc -c raylib/src/raudio.c -std=c99 -Iraudio/src
ar rcs raudio.a raudio.o
```

* compile raypyc extra functions.

```cmd
gcc -c raypyc_extra_functions.c -std=c99 -Iraudio/src -lraudio -DRAUDIO_STANDALONE
gcc -shared -o raypyc_extra_functions.dll raypyc_extra_functions.o
```

* compile raylib as dynamic library.

```cmd
cd ./raylib/src
windres raylib.dll.rc -o raylib.dll.rc.data
make RAYLIB_LIBTYPE=SHARED RAYLIB_MODULE_RAYGUI=TRUE GRAPHICS=GRAPHICS_API_OPENGL_43
cd ../..
```

* compile raylib parser and API(s).

```cmd
copy raygui\src\raygui.h raylib
copy raylib\src\config.h raylib\parser
cd raylib/parser
make raylib_parser
make raylib_api.json FORMAT=JSON EXTENSION=json
make raymath_api.json FORMAT=JSON EXTENSION=json
make rlgl_api.json FORMAT=JSON EXTENSION=json
make raygui_api.json FORMAT=JSON EXTENSION=json
raylib_parser --input config.h --output config_api.json --format JSON
cd ../..
```

So what exactly did we build here:

* `raypyc_extra_functions.dll` (in the "build" folder) used to help raypyc with some external stuff.
* `raylib.dll` (in the "build\raylib\src" folder) used to call raylib functions from python.
* `rlgl_api.json`, `raymath_api.json`, `raylib_api.json` and `raygui_api.json` (in the "build\raylib\parser" folder)
  used to tell raypyc some data about raylib stuff.

Some notes before used the generated files:

* we compiled raylib with the `GRAPHICS_API_OPENGL_43` (openGL 4.3) but some GPUs just doesn't support that, if your GPU
  doesn't support openGL 4.3 try to compile raylib with the `GRAPHICS_API_OPENGL_11` or `GRAPHICS_API_OPENGL_21`
  or `GRAPHICS_API_OPENGL_33` flags.
* some API(s) may be broken while using the raylib parser, so before using the API(s) make sure that they aren't broken.

what do we do with the generated files:

* replace all the `rlgl_api.json`, `raymath_api.json`, `raylib_api.json` and `raygui_api.json` files in the "raypyc"
  folder with the `rlgl_api.json`, `raymath_api.json`, `raylib_api.json` and `raygui_api.json` files in the "
  build\raylib\parser".
* replace the `raylib.dll` in the "raypyc/libs" folder with the `raylib.dll` in the "build\raylib\src" folder.
* replace the `raypyc_extra_functions.dll` in the "raypyc/libs" folder with the `raypyc_extra_functions.dll` in the "build" folder.
* run the [filesGeneration.py](../filesGeneration.py) file.

We are done 😀, if you got/find any errors along the way fill free to open an issue on git.
