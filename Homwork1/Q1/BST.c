// BST.c
// edited by RUILING WANG 12/02/2020
# include "BST.h"
struct BSTreeNode{
	int val;
	struct BSTreeNode* left;
	struct BSTreeNode* right;
};
TreeNode newNode(int val){
	TreeNode root = malloc(sizeof(struct BSTreeNode));
	if (root == NULL){
		fprintf(stderr, "node failed to initialize\n");
		exit(1);
	}
	root -> val = val;
	root -> left = NULL;
	root -> right = NULL;
	return root;
}
int SearchNode (TreeNode root, int val){
	assert(root != NULL);
	TreeNode curr = root;
	while (curr != NULL){
		if (val == curr -> val) return 1;
		else if (val < curr -> val) curr = curr -> left;
		else curr = curr -> right;
	}
	
	return 0;
}
TreeNode findMin(TreeNode root){
	assert(root != NULL);
	TreeNode curr = root;
	while (curr -> left != NULL){
		curr = curr -> left;
	}
	return curr;
}
void (TreeNode root, int val){
	assert(root != NULL);
	TreeNode curr = root;
	while (1){
		if (val > curr -> val){
			if (curr -> right == NULL){
				curr -> right = newNode(val);
				//printf("insert successful %d\n", val);
				return;
			}
			else curr = curr -> right;
		}
		else{
			if (curr -> left == NULL){
				curr -> left = newNode(val);
				//printf("insert successful %d\n", val);
				return;
			}
			else curr = curr -> left;
		}
	}
	
	return;
}
void DeleteNode(TreeNode root, int val){
	assert(root != NULL);
	TreeNode curr = root;
	while(1){
		if (val > curr -> val){
			TreeNode right = curr -> right;
			if (right == NULL) break;
			if (val == right -> val){
				// condition 1: leaf node
				if (right -> left == NULL && right -> right == NULL){
					curr -> right = NULL;
					free(right);
				}
				// condition 2: only have right child
				else if (right -> left == NULL){
					curr -> right = right -> right;
					free(right);
				}
				// condition 3: only have left child
				else if (right -> right == NULL){
					curr -> right = right -> left;
					free(right);
				}
				// condition 4: have both children
				else{
					TreeNode min = findMin(right -> right);
					int min_value = min -> val;
					DeleteNode(right, min_value);
					right -> val = min_value;
				}
				//printf("remove successful %d\n", val);
				return;
				
			}
			else curr = right;
		}
		else if (val < curr -> val){
			TreeNode left = curr -> left;
			if (left == NULL) break;
			if (val == left -> val){
				// condition 1: leaf node
				if (left -> right == NULL && left -> left == NULL){
					curr -> left = NULL;
					free(left);
				}
				// condition 2: only have left child
				else if (left -> right == NULL){
					curr -> left = left -> left;
					free(left);
				}
				// condition 3: only has right child
				else if (left -> left == NULL){
					curr -> left = left -> right;
					free(left);
				}
				// condition 4: have both children
				else{
					TreeNode min = findMin(left -> right);
					int min_value = min -> val;
					DeleteNode(left, min -> val);
					left -> val = min_value;
				}
				//printf("remove successful %d\n", val);
				return;
			}
			else curr = left;
		}
		else{
			TreeNode min = findMin(curr -> right);
			int min_value = min -> val;
			DeleteNode(curr -> right, min -> val);
			curr -> val = min_value;
			//printf("remove successful %d\n", val);
			return;
		}
	}
	printf("node %d is not in BStree\n", val);
	return;
}
void ShowInorder(TreeNode root){
	if (root == NULL) return;
	ShowInorder(root -> left);
	printf("%d ", root -> val);
	ShowInorder(root -> right);
}
void ShowPreorder(TreeNode root){
	if (root == NULL) return;
	printf("%d ", root -> val);
	ShowPreorder(root -> left);
	ShowPreorder(root -> right);
}
void ShowPostOrder(TreeNode root){
	if (root == NULL) return;
	ShowPostOrder(root -> left);
	ShowPostOrder(root -> right);
	printf("%d ", root -> val);
	printf("\n");
}
void DestroyTree(TreeNode root){
	if (root == NULL)
        return;
    DestroyTree(root->left);
	root -> left = NULL;
    DestroyTree(root->right);
	root -> right =NULL;
    printf("Deleting %d node.\n", root->val);
    free(root);
	return;
}
