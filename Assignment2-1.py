
inputlst=[]
lstmax=int(input("enter number of sets in list"))
for i in range(lstmax):
    print(f"enter details of {i+1} tuple")
    firstint=int(input ("Enter the first value "))
    secondint=int(input ("Enter the second value "))
    inputlst.append((firstint,secondint))
print(inputlst)

for i in range(1,len(inputlst)):
    curtuple=inputlst[i]
    j=i-1
    while curtuple[1]<inputlst[j][1] and j >=0:
        inputlst[j+1]=inputlst[j]
        j-=1
    inputlst[j+1]=curtuple
print(inputlst)

"""
expected output
enter number of sets in list3
enter details of 1 tuple
Enter the first value 1
Enter the second value 3
enter details of 2 tuple
Enter the first value 1
Enter the second value 2
enter details of 3 tuple
Enter the first value 1
Enter the second value 1
[(1, 3), (1, 2), (1, 1)]
[(1, 1), (1, 2), (1, 3)]
"""
