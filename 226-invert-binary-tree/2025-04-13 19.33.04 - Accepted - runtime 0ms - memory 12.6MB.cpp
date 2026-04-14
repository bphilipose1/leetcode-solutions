/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 #include <queue>
class Solution {
public:

    TreeNode* invertTree(TreeNode* root) {
        invertTreeHelp(root);
        return root;
    }
    void invertTreeHelp(TreeNode* root) {
        if(!root) return;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())   {
            int level_size = q.size();
            for(int i = 0; i < level_size; i++) {
                //get the current node to evaluate
                TreeNode* cur_node = q.front(); 
                q.pop();
                //Process node
                TreeNode* temp = cur_node->left;
                cur_node->left=cur_node->right;
                cur_node->right = temp;
                //add left, right children into the queue
                if(cur_node->left)  {
                    q.push(cur_node->left);
                }
                if(cur_node->right) {
                    q.push(cur_node->right);
                }

            }
        }

    }
};