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
class Solution {
public:
    void inOrderTraversal(TreeNode* root, int& nodeNum, int& result) {
        if(!root || nodeNum == 0)   { //either node is null, or we already hit target
            return;
        }
        inOrderTraversal(root->left, nodeNum, result);
        //we check are we the Kth node, if not
        nodeNum--; 
        if(nodeNum == 0)    {
            result = root->val;
            return;
        }

        inOrderTraversal(root->right, nodeNum, result);
    }
    int kthSmallest(TreeNode* root, int k) {
        /*
        Do an in order traversal, LNR, and 
        the kth node we visit is the kth smallest
        */
        int result = -1;
        int nodeNum = k;
        inOrderTraversal(root, nodeNum, result);
        return result;


    }
};