//#include <string>
//#include <vector>
//#include "fstream"
//#include "iostream"
#include "../../splitString.cpp"
//#include "unordered_map"
//#include "cmath"
//
//using namespace std;
//std::ifstream ifs;


#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <cmath>


using namespace std;

// Define a struct to hold the input data
struct InputData {
    vector<string> t;
    vector<string> d;
};

// Function to read input data from the file
InputData readInputData() {
    ifstream ifs("2023/day8/day8_input.txt");

    ifs.close();
    return {};
}

// Function to compute part 1
string part1(const InputData& inputData) {
    const auto& t = inputData.t;
    const auto& d = inputData.d;
    int s = 1;


    return to_string(s);
}

// Function to compute part 2
string part2(const InputData& inputData) {
    const auto& t = inputData.t;
    const auto& d = inputData.d;

    return to_string();
}

//#include <benchmark/benchmark.h>

// Benchmark functions

//static void BM_part1(benchmark::State& state) {
//    InputData inputData = readInputData();
//
//    while (state.KeepRunning()) {
//        string part1_result = part1(inputData);
//        assert(part1_result == "2756160");
//        benchmark::DoNotOptimize(part1_result);
//    }
//}
//
//static void BM_part2(benchmark::State& state) {
//    InputData inputData = readInputData();
//
//    while (state.KeepRunning()) {
//        string part2_result = part2(inputData);
//        assert(part2_result == "34788142");
//        benchmark::DoNotOptimize(part2_result);
//    }
//}
//
//
//BENCHMARK(BM_part1);
//BENCHMARK(BM_part2);
//
//BENCHMARK_MAIN();


int main() {
    cout << part1() << endl;
    cout << part2() << endl;
}