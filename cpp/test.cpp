//
// Created by junper on 12/6/23.
//

class Solution {
public:
    int totalMoney(int n) {
        int nbM = n/7-1;
        int sM = ((1+nbM)/2)*nbM;
        int s = sM*7 + 6*fact(nbM);
        return s
    }
};