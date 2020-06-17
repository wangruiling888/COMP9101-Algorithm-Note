// edited by Ruiling Wang
# include "BST.h"
void find_number(int * nums, int count){
	assert(count > 2);
	TreeNode t;
	int sum = 0;
	for (int i = 0; i < count -1; i++){
		for (int j = i+1; j < count; j++){
			//printf("%d %d %d %d\n", nums[i], nums[j], i ,j);
			int a = nums[i], b = nums[j];
			sum = a * a + b*b;
			//printf("this is sum %d\n", sum);
			if (i == 0 && j == 1) {
				t = newNode(sum);
			}
			else if (SearchNode(t, sum) == 1) printf("%d\n", sum);
			else{
				InsertNode(t, sum);
			}
		}
	}
	DestroyTree(t);
	return ;
	
}
int main(){
	printf("please enter a series of positive number:\n");
	int num;
	int * nums = malloc(sizeof(int));
	int count = 0;
	while (scanf("%d", &num) != EOF){
		nums = realloc(nums, sizeof(count + 1) * sizeof(int));
		nums[count] = num;
		count ++;
	} 
	
	find_number(nums, count);
	printf("complete\n");
	return 0;
}
