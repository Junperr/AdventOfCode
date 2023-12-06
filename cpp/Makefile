CC=g++

# Compiler flags
CC_FLAGS=-g -O2 -Wall -Wextra -pedantic -Wno-unused-variable -std=c++20



# Google Benchmark paths
GOOGLE_BENCHMARK_INSTALL_PATH="/home/junper/Info/benchmark"
GOOGLE_BENCHMARK_INCLUDE_PATH=$(GOOGLE_BENCHMARK_INSTALL_PATH)/include
GOOGLE_BENCHMARK_LIBRARY_PATH=$(GOOGLE_BENCHMARK_INSTALL_PATH)/lib

all: 2023
2023 : 2023/day1/day1 2023/day2/day2 2023/day6/day6

2023/day6/day6: 2023/day6/day6.o
	$(CC) $(CC_FLAGS) -o $@ $^ -L$(GOOGLE_BENCHMARK_LIBRARY_PATH) -lbenchmark -lpthread
	@echo "--------------------"

2023/day6/day6.o: 2023/day6/day6.cpp
	$(CC) $(CC_FLAGS) -c -I$(GOOGLE_BENCHMARK_INCLUDE_PATH) -o $@ $^

2023/day2/day2: 2023/day2/day2.o
	$(CC) $(CC_FLAGS) -o $@ $^ -L$(GOOGLE_BENCHMARK_LIBRARY_PATH) -lbenchmark -lpthread
	@echo "--------------------"

2023/day2/day2.o: 2023/day2/day2.cpp
	$(CC) $(CC_FLAGS) -c -I$(GOOGLE_BENCHMARK_INCLUDE_PATH) -o $@ $^

2023/day1/day1: 2023/day1/day1.o
	$(CC) $(CC_FLAGS) -o $@ $^ -L$(GOOGLE_BENCHMARK_LIBRARY_PATH) -lbenchmark -lpthread
	@echo "--------------------"

2023/day1/day1.o: 2023/day1/day1.cpp
	$(CC) $(CC_FLAGS) -c -I$(GOOGLE_BENCHMARK_INCLUDE_PATH) -o $@ $^

clean:
	rm -vf 2023/day1/day1 2023/day1/day1.o 2023/day2/day2 2023/day2/day2.o 2023/day6/day6 2023/day6/day6.o

.PHONY: clean
