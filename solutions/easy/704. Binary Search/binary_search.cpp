#include <vector>
#include <iostream> // Include this for testing purposes (optional)

using namespace std; // Add this line to avoid writing 'std::' before 'vector'

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid;
        while (left <= right) {
            mid = (right + left) / 2;
            if (target < nums[mid]) {
                right = mid - 1;
            } else if (target > nums[mid]) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};

int main()
{
    vector<int> nums = {-1,0,3,5,9,12};
    int target = 9;
    Solution s;
    int result = s.search(nums, target);
    cout << "Index of target: " << result << endl;
    return 0;
}