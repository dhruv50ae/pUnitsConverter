def add(*args):
    total = 0
    for n in args:
        total += n
    return total

sum = add(1,1,2,3,4,5,6,6,7,8,2)

# print(sum)

def calculator(n, **kwargs):
    # print(kwargs)
    # for key, values in kwargs.items():
    #     print(key)
    #     print(values)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    return n

total = calculator(1, add = 2, multiply = 5)
print(total)