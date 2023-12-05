//
// Created by junper on 12/5/23.
//

#include "splitString.h"

vector<string> splitString(string s, char sep) {
    vector<string> v;
    string temp;
    for (char c: s) {
        if (c == sep and !temp.empty()) {
            v.push_back(temp);
            temp = "";
        } else {
            temp += c;
        }
    }
    if (!temp.empty()) {
        v.push_back(temp);
    }
    return v;
};