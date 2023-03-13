class NoDuplictes:

    def __init__(self):

        self.list = []

    def __call__(self, new_items):
        for i in new_items:
            if not i in self.list:
                self.list.append(i)


my_no_dup_list = NoDuplictes()

print(callable(my_no_dup_list))

my_no_dup_list([1,2,3,4,5,1,2])

print(my_no_dup_list.list)