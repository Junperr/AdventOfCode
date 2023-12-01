#include <string>
#include <vector>
#include "fstream"
#include "iostream"
#include "filesystem"

using namespace std;
std::ifstream ifs;

//string path = filesystem::current_path();

string part1() {

    ifs.open("2023/day1/day1_input.txt");
    string line;

    int s = 0;

    while (ifs.good()) {

        int first = -1, last = -1;
        for (int x: line) {
            int sint = x;
            if (sint > 47 and sint < 58) {
                if (first == -1) {
                    first = x - 48;
                }
                last = x - 48;
            }
        }
        if (first != -1) {
            s += first * 10 + last;
        }
        ifs >> line;
    }
    ifs.close();
//    cout << s << endl;
    return to_string(s);
}

string part2() {
    ifs.open("2023/day1/day1_input.txt");
    string line;
    ifs >> line;
    int s = 0;

    vector<string> val{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five",
                       "six", "seven", "eight", "nine"};
    while (ifs.good()) {
        int first = -1, last = -1;
        int indf = line.size(), indl = -1;
        for (int i = 0; i < 20; i++) {
            string v = val[i];

            int f = line.find(v), l = line.rfind(v);
            if (f != -1) {
                if (f < indf) {
                    indf = f;
                    first = i % 10;
                }
                if (f > indl) {
                    indl = l;
                    last = i % 10;
                }
            }
            if (l != -1) {
                if (l < indf) {
                    indf = f;
                    first = i % 10;
                }
                if (l > indl) {
                    indl = l;
                    last = i % 10;
                }
            }
        }
        s += first * 10 + last;
        ifs >> line;
    }
    ifs.close();
//    cout << path << endl;
    return to_string(s);
}


#include <benchmark/benchmark.h>

void BM_part1(benchmark::State& state)
{
    while (state.KeepRunning()) {
        string part1_result = part1();
    }
}

void BM_part2(benchmark::State& state)
{
    while (state.KeepRunning()) {
        string part2_result = part2();
    }
}

BENCHMARK(BM_part1);
BENCHMARK(BM_part2);

BENCHMARK_MAIN();

//int main(){
//    ios::sync_with_stdio(false);
//    cout << part1() << endl;
//    cout << part2() << endl;
//}