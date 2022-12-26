cdef extern from "emscripten.h":
	ctypedef void (*em_callback_func)();
	ctypedef void (*em_arg_callback_func)(void *);
	ctypedef void (*em_str_callback_func)(const char *);

	void emscripten_set_main_loop(em_callback_func func, int fps, int simulate_infinite_loop);