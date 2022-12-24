EXAMPLE_NAME := core_basic_window
PYTHON_INCLUDE_PATH ?= $(shell python3 -c "from sysconfig import get_paths;print(get_paths()['include'])")
RAYPYC_PATH ?= ../../../raypyc
CYTHON_FLAGS = --embed -3 -a -f
CFLAGS := -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing
CLINKS := -l:libraylib.a -lpython3.10 -lm

main:
	cython3 -I $(RAYPYC_PATH)/.. $(CYTHON_FLAGS) -o $(EXAMPLE_NAME).c $(EXAMPLE_NAME).pyx
	gcc $(CFLAGS) -I $(PYTHON_INCLUDE_PATH) -I $(RAYPYC_PATH)/.. -I $(RAYPYC_PATH)/includes -L $(RAYPYC_PATH)/libs $(EXAMPLE_NAME).c $(CLINKS) -o $(EXAMPLE_NAME)

clean:
	rm $(EXAMPLE_NAME).c $(EXAMPLE_NAME).html $(EXAMPLE_NAME)