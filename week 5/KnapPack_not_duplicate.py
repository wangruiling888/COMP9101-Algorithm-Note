
weight_value = {1:3,2:5,3:10,4:9,10:2}
used = {0:[]}
# find all available weight for weight C
def find_available(C, weight_value):
    weight_list = list(weight_value.keys())
    for i in range(len(weight_list)):
        if (weight_list[i] > C):
            return weight_list[:i]
    return weight_list
result = []
result.append(0)
def find_result(weight_value, C):
    if C == 0:
        return 0
    weight_list = find_available(C, weight_value)
    if len(weight_list) == 0:
        return 0
    max_value = 0
    max_list = []
    for item in weight_list:
        if item not in used[C-item]:
            cur_list =  used[C-item] + [item]
            cur_value = result[C-item] + weight_value[item]
        else:
            cur_list = used[C-item]
            cur_value = result[C-item]
        max_list = cur_list if cur_value > max_value else max_list
        max_value = cur_value if cur_value > max_value else max_value
    used[C] = max_list
    return max_value
C = 21
for i in range(1, C+1):
    result.append(find_result(weight_value, i))
print("for backpack that weight", C, " the max value is ", result[C])
print("the max value combination is ", used[C])



