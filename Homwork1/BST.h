// BST ADT
// edited by RUILING WANG 12/02/2020
# include <stdio.h>
# include <stdlib.h>
# include <assert.h>
 typedef struct BSTreeNode* TreeNode;
 
 TreeNode newNode(int);
 int SearchNode (TreeNode, int);
 void InsertNode(TreeNode, int);
 void DeleteNode(TreeNode, int);
 void ShowInorder(TreeNode);
 void ShowPreorder(TreeNode);
 void ShowPostOrder(TreeNode);
 void DestroyTree(TreeNode);
 
