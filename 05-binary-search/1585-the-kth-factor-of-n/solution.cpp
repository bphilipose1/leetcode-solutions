class Solution {
public:
    int kthFactor(int n, int k) {
        int count = 0;
        int temp = 1;
        while(count != k)   {
            if(n % temp == 0)   {//factor is found
                count++;
            }
            if(temp > n)   {
                return -1;
            }
            temp++;
        }
        return temp-1;
    }
};