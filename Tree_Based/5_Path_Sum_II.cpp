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
    vector<int> path;
    vector<vector<int>> ans;
    
    vector<vector<int>> pathSum(TreeNode* root, int sum){
        helper(root,sum);
        return ans;
    }
    
    void helper(TreeNode* root, int sum){
        if(!root)
            return;
        
        sum -= root->val;
        path.push_back(root->val);
        
        if(!root->left && !root->right && sum==0)
            ans.push_back(path);
        
        helper(root->left, sum);
        helper(root->right, sum);
        path.pop_back();
    }
};