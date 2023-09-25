# numbers=(1,2,3,4,5,6,7)

total =int(input("enter total numbers"))
numbers=[]
for i in range(total):
    numbers.append(int(input(f'enter {i+1} value ')))
print(numbers)
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print (f"no of even no are {even} \nno of odd  no are {odd} ")
"""
enter total numbers7 
enter1 value 1 
enter2 value 2 
enter3 value 3 
enter4 value 4 
enter5 value 5 
enter6 value 6 
enter7 value 7
[1, 2, 3, 4, 5, 6, 7]
no of even no are 3
no of odd  no are 4
"""
