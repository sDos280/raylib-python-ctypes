:: clone raylibs repositories
git clone --depth 1 https://github.com/raysan5/raylib
git clone --depth 1 https://github.com/raysan5/raudio
git clone --depth 1 https://github.com/raysan5/raygui

:: compile raudio
gcc -c raylib/src/raudio.c -std=c99 -Iraudio/src
ar rcs raudio.a raudio.o

:: compile raypyc extra functions
gcc -c raypyc_extra_functions.c -std=c99 -Iraudio/src -lraudio -DRAUDIO_STANDALONE
gcc -shared -o raypyc_extra_functions.dll raypyc_extra_functions.o
move raypyc_extra_functions.dll all
rm *.a *.o

:: compile raylib as dynamic library
cd "./raylib/src"
windres raylib.dll.rc -o raylib.dll.rc.data
make RAYLIB_LIBTYPE=SHARED RAYLIB_MODULE_RAYGUI=TRUE GRAPHICS=GRAPHICS_API_OPENGL_43
cp raylib.dll ../../all
make clean
cd ../..

:: preprocess raylib headers
python .\rlhpp.py raylib/src/raylib.h RLAPI
python .\rlhpp.py raylib/src/raymath.h RMAPI
python .\rlhpp.py raylib/src/rlgl.h RLAPI
python .\rlhpp.py raygui/src/raygui.h RAYGUIAPI

:: parse raylib headers
cp "./raylib/src/config.h" "./tmp/config.h.preprocessed"
cd raylib/parser
make raylib_parser
.\raylib_parser --input "../../tmp/raylib.h.preprocessed" --output "../../all/raylib_api.json" --define RLAPI --format JSON
.\raylib_parser --input "../../tmp/raymath.h.preprocessed" --output "../../all/raymath_api.json" --define RMAPI --format JSON
.\raylib_parser --input "../../tmp/rlgl.h.preprocessed" --output "../../all/rlgl_api.json" --define RLAPI --format JSON
.\raylib_parser --input "../../tmp/raygui.h.preprocessed" --output "../../all/raygui_api.json" --define RAYGUIAPI --format JSON
.\raylib_parser --input "../../tmp/config.h.preprocessed" --output "../../all/config_api.json" --format JSON
cd ../..
rm -rf tmp