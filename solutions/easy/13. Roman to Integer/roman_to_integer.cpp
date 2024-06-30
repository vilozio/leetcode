#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int romanToInt(const string& s) {
        unordered_map<char, int> nums = {
            {'I', 1}, 
            {'V', 5}, 
            {'X', 10},
            {'L', 50}, 
            {'C', 100}, 
            {'D', 500}, 
            {'M', 1000}
        };

        unordered_map<char, unordered_map<char, int>> subtractive_cases = {
            {'I', {{'V', 4}, {'X', 9}}},
            {'X', {{'L', 40}, {'C', 90}}},
            {'C', {{'D', 400}, {'M', 900}}}
        };

        int num = 0;
        for (size_t i = 0; i < s.length(); ++i) {
            int digit = nums[s[i]];
            if (subtractive_cases.count(s[i]) && i < s.length() - 1) {
                char next_char = s[i + 1];
                if (subtractive_cases[s[i]].count(next_char)) {
                    digit = subtractive_cases[s[i]][next_char];
                    ++i; // Skip the next character
                }
            }
            num += digit;
        }
        return num;
    }
};

int main() {
    Solution solution;
    string roman = "XIV";
    int result = solution.romanToInt(roman);
    cout << "The integer value of " << roman << " is: " << result << endl;
    return 0;
}