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
#include <benchmark/benchmark.h>

using namespace std;

// Define a struct to hold the input data
struct InputData {
    vector<string> t;
    vector<string> d;
};

// Function to read input data from the file
InputData readInputData() {
    ifstream ifs("2023/day6/day6_input.txt");
    string line;
    getline(ifs, line);
    vector<string> t = splitString(line, ' ');
    getline(ifs, line);
    vector<string> d = splitString(line, ' ');
    ifs.close();
    return {t, d};
}

// Function to compute part 1
string part1(const InputData& inputData) {
    const auto& t = inputData.t;
    const auto& d = inputData.d;
    int s = 1;

    for (int i = 1; i < t.size(); i++) {
        int b = stoi(t[i]);
        int c = -stoi(d[i]);
        int a = -1;
        int det = (b * b) + (4 * c);
        int sol1 = ceil((-b + sqrt(det)) / -2 + 0.00000001);
        s *= (b - sol1) - sol1 + 1;
    }

    return to_string(s);
}

// Function to compute part 2
string part2(const InputData& inputData) {
    const auto& t = inputData.t;
    const auto& d = inputData.d;
    string tt = t[1] + t[2] + t[3] + t[4];
    string dd = d[1] + d[2] + d[3] + d[4];

    long long b = stoll(tt);
    long long c = -stoll(dd);
    long long a = -1;
    long long det = (b * b) + (4 * c);
    long long sol1 = ceil((-b + sqrt(det)) / -2 + 0.00000001);

    return to_string((b - sol1) - sol1 + 1);
}

// Benchmark functions

static void BM_part1(benchmark::State& state) {
    InputData inputData = readInputData();

    while (state.KeepRunning()) {
        string part1_result = part1(inputData);
        assert(part1_result == "2756160");
        benchmark::DoNotOptimize(part1_result);
    }
}

static void BM_part2(benchmark::State& state) {
    InputData inputData = readInputData();

    while (state.KeepRunning()) {
        string part2_result = part2(inputData);
        assert(part2_result == "34788142");
        benchmark::DoNotOptimize(part2_result);
    }
}


BENCHMARK(BM_part1);
BENCHMARK(BM_part2);

BENCHMARK_MAIN();


//int main() {
//    cout << part1() << endl;
//    cout << part2() << endl;
//}