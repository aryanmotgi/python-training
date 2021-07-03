def count_vowels(in_string, include_y=False):
    """Returns teh number of vowels contained in `in_string`"""
    vowels = "aeiouAEIOU"
    if include_y:
        vowels += "yY" #add "y" to vowels
    #add 1 for each charecter in the string if tha charecter is in "vowels"
    return sum(1 for char in in_string if char in vowels)

print(count_vowels("hello worldy"))


#this is ok
def f(x, y, z, count=1, upper=2):
    pass

#this will raise a syntax error
def f(x, y, count=1, upper=2, z):
    pass
  
  
  def max_or_min(x, y, mode="max"):
    if mode == "max":
        return max(x, y)
    elif mode == "min":
        return min(x, y)
    else:
        return None
      
      
      #rertuning a sum
def sum(a, b):
    return a + b

print(sum(2, 3))
print(sum(a=2, b=3))

#you must type "sep" to use it
print("hello", "world", sep="_")


def f(*args):
    return args
print(f(1, 2, 3))
print(f(4, 5, 6, 7, 8))


def f(*args, a, b):
    return args, a, b
print(f(1, 2, 3, a=4, b=5))


def mean(*seq):
    """ Returns the mean of the function's a arguments """
if len(seq) == 0:
    return 0

total = 0
for num in seq:
    total += num
return total / len(seq)

print(mean(4, 10))


def f(**args):
    return args

print(f(x = 5, y = 10, z = "hi"))


def func1(*args):
    sum = 0 
    for i in args:
        if i >= 10 and i < 100:
            sum += i 
    return sum
