def find_list(coin_list, denomination):
     i = 0
     while i < len(coin_list):
         if denomination < coin_list[i]:
             break
         i += 1
     return coin_list[:i]
result = []
result.append(0)
def get_result(coin_list, amount):
    if amount in coin_list:
        return 1
    coin_list_sub = find_list(coin_list, amount)
    coin_result = []
    for item in coin_list_sub:
        coin_result.append(result[amount - item]+1)
    return min(coin_result)

coin_list = [1,2,5,10,20,50,100]
amount = 101
for i in range(1, amount+1):
    result.append(get_result(coin_list, i))
print("the minimum number of notes is:", result[amount])
