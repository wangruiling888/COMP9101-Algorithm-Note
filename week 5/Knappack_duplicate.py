
weight_value = {1:3,2:5,3:10,4:9,10:2}
weight_list = list(weight_value.keys())
# find all available weight for weight C
def find_sub(weight_list, C):
    for i in range(len(weight_list)):
        if C < weight_list[i]:
            return weight_list[:i]
    return weight_list

result = []
result.append(0) # for weight = 0, there must be no value
def get_result(weight_value, C):
    if C == 0:
        return 0
    if C == 1:
        return weight_value[C]
    weight_list_sub = find_sub(weight_list, C)
    result_list = []
    for item in weight_list_sub:
        result_list.append(result[C-item]+weight_value[item])
    return max(result_list)

C = 6
for i in range(1, C+1):
    result.append(get_result(weight_value, i))
print("the max value contained in the knappack should be:", result[-1])





