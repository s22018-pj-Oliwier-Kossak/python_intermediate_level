def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

def result(fun,x):
    print(fun(x))

result(div2,6)

list_of_functions = [double, div2, negative, square]

values = [1,2,3]
for i in list_of_functions:
    for j in  values:
        result(i, j)



