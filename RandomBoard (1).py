import random
n = 10
array = [[random.randint(0,9) for i in range(n)] for j in range(n)]

def print2DArray():
  for x in range(n):
    print(array[x],"\n")

def findSum(arraya):
  sum = 0
  for i in range (n):
    for j in range (n):
        sum += arraya[i][j]
  return sum

print2DArray()
print(findSum(array))