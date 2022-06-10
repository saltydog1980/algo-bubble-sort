sequence = [4, 3, 5, 5, 0, 1]
swaps = 0
# def sort(unsort):
#     ans = []
#     i = 0
#     a = 0
#     while unsort:
#         if len(unsort) == 1:
#             ans.append(unsort.pop(i))
#         elif unsort[i] == a:
#             ans.append(unsort.pop(i))
#             i = 0
#         elif i == len(unsort) - 1 and unsort[i] > a:
#             i = 0
#             a += 1
#         else:
#             i +=1
        
#     return ans

# print(sort(sequence))
# # Your Code Here

# print(f"Final result: {result}")
# print(f"Swaps: {swaps}")

def sort(unsort):
    i = 0
    unsorted = True
    while unsorted == True:
        if i == len(unsort) - 2:
            if unsort[i] > unsort[i+1]:
                temp = unsort[i+1]
                unsort[i+1] = unsort[i]
                unsort[i] = temp
                i = 0
            else:
                unsorted = False
        elif unsort[i] > unsort[i+1]:
            temp = unsort[i+1]
            unsort[i+1] = unsort[i]
            unsort[i] = temp
            i = 0
        else:
            i +=1
        
    return unsort

print(sort(sequence))







