CXX  = g++

ROOTCFLAGS  = $(shell $(ROOTSYS)/bin/root-config --cflags)
ROOTLIBS    = $(shell $(ROOTSYS)/bin/root-config --libs)

CXXFLAGS  = -g -Wall -fPIC -Wno-deprecated -O3
CXXFLAGS += $(ROOTCFLAGS)
CXXFLAGS += $(ROOTLIBS)
CXXFLAGS += -std=c++14

all: log_gaussian_stack log_gaussian_heap log_gaussian_stack_float log_gaussian_cython_pyx

log_gaussian_stack: log_gaussian_stack.c
	$(CXX) -o $@ $< $(CXXFLAGS)

log_gaussian_heap: log_gaussian_heap.c
	$(CXX) -o $@ $< $(CXXFLAGS)

log_gaussian_stack_float: log_gaussian_stack_float.c
	$(CXX) -o $@ $< $(CXXFLAGS)

.PHONY : log_gaussian_cython_pyx
log_gaussian_cython_pyx: log_gaussian_cython.pyx
	python setup.py build_ext --inplace

.PHONY : showulimit
showulimit:
	ulimit -a

.PHONY : setuplimit
setuplimit:
	@echo "Please execute in treminal > ulimit -s unlimited"	

.PHONY : clean
clean:
	rm -f *~
	rm -f .*~
	rm -f log_gaussian_stack
	rm -f log_gaussian_heap
	rm -f initialize_reference_array
	rm -f log_gaussian_stack_float
	rm -f log_gaussian_numba_CC.cpython-37m-x86_64-linux-gnu.so
	rm -f log_gaussian_cython.cpython-37m-x86_64-linux-gnu.so
	rm -f log_gaussian_cython.c
	rm -rf build
