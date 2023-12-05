#!/bin/bash

# Clean previous build and clear terminal
make clean
clear

echo "--------------------"
echo "Compiling program..."
echo "--------------------"
if ! make; then
    echo "Compilation failed. Exiting."
    exit 1
fi

echo "Running program..."
echo "--------------------"

# Check if the executable exists
if [ ! -f "./2023/day1/day1" ]; then
    echo "Executable not found. Please ensure the compilation was successful."
    exit 1
fi

# Setting CPU to max performance mode (requires root permission)
#echo "Setting CPU to max performance mode..."
#echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor > /dev/null

# Running the process on an isolated CPU core
echo "Running on CPU core 1..."
taskset -c 1 ./2023/day1/day1

taskset -c 1 ./2023/day2/day2
# Different output formats
# taskset -c 1 ./2023/day1/day1 --benchmark_format=console  # default
# taskset -c 1 ./2023/day1/day1 --benchmark_format=json
# taskset -c 1 ./2023/day1/day1 --benchmark_format=csv

# Re-setting CPU performance mode (requires root permission)
#echo "Re-setting CPU to powersave mode..."
#echo powersave | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor > /dev/null

echo "================================================================================"
