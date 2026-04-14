#include <map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
          -
        2,7,11,15

        2 : 0
        9 - 7 = 2
        lookup in the hashmap does 2 exist


                \
        11, 7, 15, 2


        Hashmap: 
            7 : 1

            [1, 3]



        For each element in nums:
            1. At each new number if the values is greater than target, skip fully
            2. Find compliment value target - current = compliment_value
            3. Check if compliment value exists in the hashmap
        */

        map<int, int> prevIndexMap;

        int current_val;
        int compliment_val;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++)    {
            current_val = nums[i];
            compliment_val = target - current_val;

            //Check if compliment value exists in the hashmap if so return result.
            if(prevIndexMap.count(compliment_val))   {
                result.push_back(prevIndexMap[compliment_val]);
                result.push_back(i);
                return result;
            }

            prevIndexMap[current_val] = i;


        }
        return result;
        /*
        3 : 0
        2 : 1
        */

    }
};