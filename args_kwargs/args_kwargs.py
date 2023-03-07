
def calculate_paint(efficency_ltr_per_m2,*surface_to_paint):
    sum_paint = sum(surface_to_paint)
    needed_paint = efficency_ltr_per_m2*sum_paint
    return needed_paint

print(calculate_paint(1,2,10))

list_of_rooms = [2,5,5]

print(calculate_paint(2,*list_of_rooms))

def sum_values(*args):
    sum_of_values = 0
    for i in args:
        sum_of_values += i
    return sum_of_values

print(sum_values(1,2,3))


def kwargs_function(**kwargs):
    return kwargs

dict = {'x':'1','y':'2'}

print(kwargs_function(**dict,z=2,j=3))


