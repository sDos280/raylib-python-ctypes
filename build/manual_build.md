## Windows build steps

* before we start make sure that you have `make` and `git` on your device.
* get raypyc and go to build folder
```cmd
git clone --depth 1https://github.com/sDos280/raylib-python-ctypes
cd ./raylib-python-ctypes/build
```
* get raudio, raylib and raygui 

```cmd
git clone --depth 1 https://github.com/raysan5/raylib
git clone --depth 1 https://github.com/raysan5/raudio
git clone --depth 1 https://github.com/raysan5/raygui
```

* compile raudio

```cmd
gcc -c raylib/src/raudio.c -std=c99 -Iraudio/src
ar rcs raudio.a raudio.o
```

* compile raypyc extra functions

```cmd
gcc -c raypyc_extra_functions.c -std=c99 -Iraudio/src -lraudio -DRAUDIO_STANDALONE
gcc -shared -o raypyc_extra_functions.dll raypyc_extra_functions.o
```

* compile raylib as dynamic library

```cmd
cd ./raylib/src
windres raylib.dll.rc -o raylib.dll.rc.data
make RAYLIB_LIBTYPE=SHARED RAYLIB_MODULE_RAYGUI=TRUE GRAPHICS=GRAPHICS_API_OPENGL_43
cd ../..
```

* compile raylib parser and API(s)

```cmd
copy raygui\src\raygui.h raylib
cd raylib/parser
make clean
make raylib_parser
make raylib_api.json FORMAT=JSON EXTENSION=json
make raymath_api.json FORMAT=JSON EXTENSION=json
make rlgl_api.json FORMAT=JSON EXTENSION=json
make raygui_api.json FORMAT=JSON EXTENSION=json
cd ../..
```