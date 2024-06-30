#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> map_idx;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map_idx.find(complement) != map_idx.end()) {
                return {map_idx[complement], i};
            }
            map_idx[nums[i]] = i;
        }
        return {};
    }
};

int main()
{
    vector<int> nums = {1, 2, 3};
    int target = 5;
    Solution s;
    auto result = s.twoSum(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}