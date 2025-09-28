#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int cnt = 0;
        vector<int> ans;
        for(int num : nums) {
            if(num != 0) {
                ans.push_back(num);
                continue;
            }
            else cnt++;
        }
        while(cnt--) {
            ans.push_back(0);
        }
        nums = ans;
    }
};