def add(*args):
    total = 0
    for n in args:
        total += n
    return total

sum = add(1,1,2,3,4,5,6,6,7,8,2)

print(sum)