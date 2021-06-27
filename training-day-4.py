a=[7, 5, 8, 2]

a.sort()

print(a)

a=[7, 5, 8, 2]

print("sorted:", sorted(a), "\noriginal",a)

for var1 in a: #For each item (called var1) in iterable1, do teh following.
  print(var1)
  
  sum_of_nums = 0

for num in [1,3,4,5,8,10]:
  sum_of_nums +=num

print(sum_of_nums)

nums = [4,7,3,4,2,1,6,8,7,9,9]
nums = sorted(nums)
idx = 0
while nums[idx] <=6:
    print(nums[idx])
    idx += 1
    
    grid = [[1,2,3,4], [5,6,7,8]]

for row in grid:
  for cell in row:
    print(cell + 1, end=" ")
    print("")
    
    #if statement
num = 4

if num ==5:
  print("num is 5")
elif num == 4:
  print("num is 4")
else:
  print("num is not 5 or 4")
  
  import random
num = random.randint(1,6)

print(num)

if num ==1:
  print("number is 1")
elif num ==2:
  print("number is 2")
else:
  pass
