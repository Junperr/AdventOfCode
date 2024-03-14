//
// Created by junper on 12/5/23.
//

#include "splitString.h"

vector<string> splitString(string s, const char *sep) {
    vector<string> v;
    string temp;
    for (char c: s) {
        if (c == sep ) {
            if (!temp.empty()) {
                v.push_back(temp);
                temp = "";
            }
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