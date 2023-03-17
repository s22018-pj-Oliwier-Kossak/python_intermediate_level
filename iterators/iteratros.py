list1 = [x for x in range(500)]
list2 = [x for x in range(50)]
list3 = [x for x in range(500)]


for i in list1:
    for j in list2:
        for n in list3:
            print(f'{i} {j} {n}')

class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):

        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = f"{self.products[self.current_product],} - {self.promotions[self.current_promotion]} -" \
                         f"{self.customers[self.current_customer]}"

        self.current_customer += 1
        return item_to_return

    def __iter__(self):
        return self




comb = Combinations(list1, list2, list3)

for c in comb:
    print(c)