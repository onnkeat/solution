# Question 4/8
print("Question 4 / 8")

print('please input integers list:')  # 2 4 1 5 3
input_str = input() 

input_list = input_str.split(' ')

int_list = [int(x) for x in input_list]
size = len(int_list)

subset_dict = {}
def findAllSubset(n, currentSubset, int_list, size, unique):
    if n==size:
        return
    
    print(n, type(currentSubset), int_list[n])
    currentSubset_includeNextNum = currentSubset.copy()
    currentSubset_includeNextNum.append(int_list[n])
    findAllSubset(n+1, currentSubset_includeNextNum, int_list, size, True)
    
    findAllSubset(n+1, currentSubset, int_list, size, False)
    
    if unique:
        if currentSubset: #list not empty
            subset_sum = sum(currentSubset)
            if subset_sum not in subset_dict:
                subset_dict[subset_sum] = [currentSubset]
            else:
                subset_dict[subset_sum].append(currentSubset)
    

findAllSubset(0, [], int_list, size, False)
print(subset_dict)


    
