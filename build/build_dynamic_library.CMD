cd ./raylib/src
:: compile dynamic library
make clean
make RAYLIB_LIBTYPE=SHARED RAYLIB_MODULE_RAYGUI=TRUE GRAPHICS=GRAPHICS_API_OPENGL_43
cd ../..

:: compile raypyc extras functions
:: compile raudio
gcc -c raylib/src/raudio.c -std=c99 -Iraudio/src
ar rcs raudio.a raudio.o
:: compile raypyc extra functions
gcc -c raypyc_extra_functions.c -std=c99 -Iraudio/src -lraudio -DRAUDIO_STANDALONE
gcc -shared -o raypyc_extra_functions.dll raypyc_extra_functions.o
rm raypyc_extra_functions.o raudio.o raudio.a

:: compile API(s)
:: fix rlgl.h
python fix_files.py
:: compile parser
copy raygui\src\raygui.h raylib
cd raylib/parser
make clean
make raylib_parser
make raylib_api.json FORMAT=JSON EXTENSION=json
make raymath_api.json FORMAT=JSON EXTENSION=json
:: note that the rlgl_api struct rlVertexBuffer need to be fixed because the parser can't parse it properly
make rlgl_api.json FORMAT=JSON EXTENSION=json
make raygui_api.json FORMAT=JSON EXTENSION=json
rm raylib_parser.exe
cd ../..
rm raylib/raygui.h