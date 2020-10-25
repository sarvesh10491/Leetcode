/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int min(int a, int b){
    return a<b?a:b;
}

int minDepth(struct TreeNode* root){
    if(root==NULL) 
        return 0;
    else if(root->left==NULL && root->right==NULL) 
        return 1;
    else if(root->left!=NULL && root->right==NULL) 
        return 1+minDepth(root->left);
    else if(root->left==NULL && root->right!=NULL) 
        return 1+minDepth(root->right);
    else 
        return min(minDepth(root->left), minDepth(root->right)) + 1;
}