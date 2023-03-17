try:
    x = int(input("Enter 1 number: "))
    y = int(input("Enter 2 number: "))
    division = x / y

except Exception as e:
    print(f"error... {e}")
except ValueError as  e:
    print(f"error... {e}")
else:
    print("x/y:",division)


def division(x,y):
    if y < -1:
        raise Exception("value error")
    else:
        return x/y

print(division(1,-3))


