EXAMPLE_NAME := core_basic_window_web
PYTHON_INCLUDE_PATH ?= $(shell python3 -c "from sysconfig import get_paths;print(get_paths()['include'])")
RAYPYC_PATH ?= ../../../raypyc
EMSCRIPTEN_HEADER_PATH ?= /home/dor/Documents/emsdk/upstream/emscripten/cache/sysroot/include/
CYTHON_FLAGS = --embed -3 -a -f --line-directives --warning-extra
CFLAGS := -pthread -fPIC -fwrapv -Wall -fno-strict-aliasing -Os
CLINKS := -l:weblibraylib.a -lpython3.10 -lm

$(EXAMPLE_NAME):$(EXAMPLE_NAME).pyx
	cython3 -I $(RAYPYC_PATH)/.. $(CYTHON_FLAGS) -o $(EXAMPLE_NAME).c $(EXAMPLE_NAME).pyx
	emcc -o game.html $(EXAMPLE_NAME).c $(CFLAGS) $(RAYPYC_PATH)/libs -I. -I$(PYTHON_INCLUDE_PATH) -I$(RAYPYC_PATH)/includes -L. -L$(RAYPYC_PATH)/libs -s USE_GLFW=3 $(CLINKS) --shell-file minshell.html

clean:
	rm -f $(EXAMPLE_NAME).c $(EXAMPLE_NAME).html $(EXAMPLE_NAME)