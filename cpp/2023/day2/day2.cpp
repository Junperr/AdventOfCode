#include <string>
#include <vector>
#include "fstream"
#include "iostream"


using namespace std;
std::ifstream ifs;


string part1() {

    ifs.open("2023/day2/day2_input.txt");
    ifs.close();
    return "None";
}

string part2() {
    ifs.open("2023/day2/day2_input.txt");
    ifs.close();
    return "None";
}

//#include <benchmark/benchmark.h>

//void BM_part1(benchmark::State& state)
//{
//    while (state.KeepRunning()) {
//        string part1_result = part1();
//        benchmark::DoNotOptimize(part1_result);
//    }
//}
//
//void BM_part2(benchmark::State& state)
//{
//    while (state.KeepRunning()) {
//        string part2_result = part2();
//        benchmark::DoNotOptimize(part2_result);
//    }
//}
//
//BENCHMARK(BM_part1);
//BENCHMARK(BM_part2);
//
//BENCHMARK_MAIN();

int main() {
    cout << part1() << endl;
    cout << part2() << endl;
}