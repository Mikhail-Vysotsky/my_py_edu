def mean(*args):
    print(f"args: {args}, type of args: {type(args)}")
    
    for a in args:
        print(f"Значение: {a}, тип: {type(a)}")
        
def kwargs_mean(**kwargs):
    kwargs.pop("a", 0)
    return sum(kwargs.values()) / len(kwargs)

def mixed_mean(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    length = len(args) + len(kwargs)
    return total / length
     
arguments = tuple(iter(input, ''))    
#arguments = list(iter(input, ''))    

print("hardcode params: ")
mean({1, 2, 3}, 33, 44, 55, "qwerty")

print("params from user input: ")
mean(*arguments)

print("mixed set params: ")
mean("first", *arguments, "last")

print(kwargs_mean(a=1, b=2, c=3, d=4))

print(mixed_mean(1, 1, new=4))