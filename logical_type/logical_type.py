list = ['load data', 'export data', 'analyze & predict']


while True:
    count = 1
    for i in  list:
        print(count, i)
        count +=1
    choice = input("choose number: ")

    if choice == '1':
        print(list[0])
    elif choice == '2':
        print(list[1])
    elif choice == '3':
        print(list[2])
    elif choice == '':
        break
    else:
        print("inccorect choice")
    print()