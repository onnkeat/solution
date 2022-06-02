# Question 2/8
print("Question 2")

print('please input N:')  # 11
n = int(input()) 


factorial = 1
for i in range(n):
    factorial *= (i+1)

sum_digits = 0    
while(factorial > 0):
    sum_digits += factorial % 10
    factorial //= 10
    
    
output = sum_digits
print('sum for the number:', output) # 36

