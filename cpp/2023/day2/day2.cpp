#include <string>
#include <vector>
#include "fstream"
#include "iostream"
#include "../../splitString.cpp"
#include "unordered_map"

using namespace std;
std::ifstream ifs;



string part1() {
    ifs.open("2023/day2/day2_input.txt");
    string line;
    int score = 0;
    int count = 0;
    getline(ifs,line);
    while (!line.empty()) {

        count ++;
//        cerr << count << line << endl;
        unordered_map <string, int> maxs;
        vector<string> v = splitString(line, ':');
        vector<string> v2 = splitString(v[1], ';');
        for (auto seg : v2) {
            vector<string> v3 = splitString(seg, ',');
            for (auto seg2 : v3) {
                vector<string> v4 = splitString(seg2, ' ');
//                cerr << v4[0] << " " << v4[1] << endl;
                int val = stoi(v4[0]);
                string name = v4[1];
                maxs[name] = max(maxs[name], val);
            }
        }
        if (maxs["red"] <= 12 and maxs["blue"] <= 14 and maxs["green"] <= 13 ) {
            score = score + count;
        }
//        cout << count << ' ' << maxs["red"] << " " << maxs["blue"] << " " << maxs["green"] << endl;
        getline(ifs,line);
    }
//    cout << score << endl;
    ifs.close();
    return to_string(score);
}

string part2() {
    ifs.open("2023/day2/day2_input.txt");
    string line;
    int score = 0;
    int count = 0;
    getline(ifs,line);
    while (!line.empty()) {

        count ++;
//        cerr << count << line << endl;
        unordered_map <string, int> maxs;
        vector<string> v = splitString(line, ':');
        vector<string> v2 = splitString(v[1], ';');
        for (auto seg : v2) {
            vector<string> v3 = splitString(seg, ',');
            for (auto seg2 : v3) {
                vector<string> v4 = splitString(seg2, ' ');
//                cerr << v4[0] << " " << v4[1] << endl;
                int val = stoi(v4[0]);
                string name = v4[1];
                maxs[name] = max(maxs[name], val);
            }
        }

        score = maxs["red"]*maxs["blue"]*maxs["green"] + score;

//        cout << count << ' ' << maxs["red"] << " " << maxs["blue"] << " " << maxs["green"] << endl;
        getline(ifs,line);
    }
//    cout << score << endl;
    ifs.close();
    return to_string(score);
}

#include <benchmark/benchmark.h>

void BM_part1(benchmark::State& state)
{
    while (state.KeepRunning()) {
        string part1_result = part1();
        benchmark::DoNotOptimize(part1_result);
    }
}

void BM_part2(benchmark::State& state)
{
    while (state.KeepRunning()) {
        string part2_result = part2();
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