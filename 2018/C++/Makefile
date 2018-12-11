CXX=g++
CXXFLAGS=-O3 --std=c++17

ifeq (run,$(firstword $(MAKECMDGOALS)))
  RUN_TARGET := $(word 2, $(MAKECMDGOALS))
endif

all: 1 11

run: $(RUN_TARGET)
	./$(RUN_TARGET) < ../$(RUN_TARGET).in

1: 1.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

11: 11.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

.PHONY: clean
clean:
	-rm 1 11
