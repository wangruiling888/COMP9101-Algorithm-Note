 #n single man and n single women are dating
 #each man list n women ranking and each woman list n man ranking
 #find a resonable match for all the people at present
import random
def copy (list1):
    result = [item for item in list1]
    return result

def Gale_Shapley(man_rank, women_rank, man):
    free = copy(man)
    propose_dict = {item:0 for item in free}
    women_propose = {}
    result = {}

    propose = []
    while (len(free) > 0):
        cur_man = free[0]
        # get hightest rank women in cur_man's list
        cur_woman = man_rank[cur_man][propose_dict[cur_man]]
        if cur_woman not in women_propose:
            # if current woman has not been proposed by anyone yet
            women_propose[cur_woman] = cur_man
            result[cur_man] = cur_woman
            free.pop(0)
        else:
            # get rank for mtached man and cur free man
            # remain the man as match for smaller rank
            original_rank = women_rank[cur_woman].index(women_propose[cur_woman])
            new_rank = women_rank[cur_woman].index(cur_man)
            if new_rank < original_rank:
                free.append(women_propose[cur_woman])
                women_propose[cur_woman] = cur_man
                result[cur_man] = cur_woman
                free.pop(0)
        propose_dict[cur_man] += 1
    return result

# generates man_rank and women_rank randomly
man = ['A', 'B', 'C', 'D', 'E']
women = ['a', 'b', 'c', 'd', 'e']
# generate man rank:
man_rank = {}
for item in man:
    random.shuffle(women)
    man_rank[item] = copy(women)
women_rank = {}
for item in women:
    random.shuffle(man)
    women_rank[item] = copy(man)
print("The rank list for each woman is:")
print(women_rank)
print("The rank list for each man is:")
print(man_rank)
print("--------------------------")
result = Gale_Shapley(man_rank, women_rank, man)
print("the perfect matching is:")
for item in result:
    print("{} < -- > {}".format(item, result[item]))

