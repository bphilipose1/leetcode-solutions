#include <algorithm>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        /*
        we know absolute best we can do is O(n^2),
        we need to check for dups in each grid, column, row.
            -Since we can easily iterate one row at a time, we can verify the row condition one by one
            - for columna dn grid we need to save the state
        */
        int N = board.size();
        vector<unordered_set<int>> column_counter(N);
        vector<unordered_set<int>> grid_counter(N);
        vector<unordered_set<int>> row_counter(N);
        
        for(int row_idx = 0; row_idx < board.size(); row_idx++)   {
            for(int col_idx = 0; col_idx < board[0].size(); col_idx++)    {
                //check row counter
                char char_val = board[row_idx][col_idx];
                if (char_val == '.')  {
                    continue;
                }
                int cur_val = int(char_val);
                int grid_idx = ((row_idx / 3) * 3 + (col_idx / 3));
                if (row_counter[row_idx].count(cur_val) || grid_counter[grid_idx].count(cur_val) || column_counter[col_idx].count(cur_val))    {
                    return false;
                }
                //update the counters
                row_counter[row_idx].insert(cur_val);
                grid_counter[grid_idx].insert(cur_val);
                column_counter[col_idx].insert(cur_val);
                
                //Even though sudoku is constant, lets assume we can get any grid from 0 to n
                //Time Complexity: O(n^2)
                //Space Complexity: O(n^2 + n^2 + n^2) = O(n^2)

            }
        }
        return true;

    }
};