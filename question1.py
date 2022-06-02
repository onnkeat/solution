#Question 1/8
print("Question 1")

print('please input N:')  # 3
n = int(input()) 
print('please input matrix:') # 1 2 1 2 3 5 8 7 6
matrix_str = input()
matrix_list = matrix_str.split(' ')
# 1 2 1
# 2 3 5
# 8 7 6

diagonol_sum = 0
inverse_diagonol_sum = 0
for i in range(n): #row
    diagonol_sum += int(matrix_list[i*n+i])
    inverse_diagonol_sum += int(matrix_list[(i+1)*n-(i+1)])
    

output = diagonol_sum*inverse_diagonol_sum
print('output:', output) #120
