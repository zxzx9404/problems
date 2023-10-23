#include <vector>

class Solution {
public:
    bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
        if (flowerbed.size() == 1 && !flowerbed[0]&& n == 1) {
            return true;
        }

        if (flowerbed.size() >= 2 && !(flowerbed[0]+ flowerbed[1])) {
            flowerbed[0]= 1;
            n -= 1;
        }

        for (int i = 1; i < flowerbed.size() - 1; i++) {
            if (!(flowerbed[i-1]+ flowerbed[i]+ flowerbed[i+1])) {
                flowerbed[i]= 1;
                n -= 1;
                if (!n) {
                    break;
                }
            }
        }

        if (flowerbed.size() >= 2 && !(flowerbed[flowerbed.size() - 1]+ flowerbed[flowerbed.size() - 2])) {
            flowerbed[flowerbed.size() - 1]= 1;
            n -= 1;
        }

        return n <= 0;
    }
};
