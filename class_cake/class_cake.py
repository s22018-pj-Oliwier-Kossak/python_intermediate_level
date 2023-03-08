
class Cake:
    def __init__(self, name, kind, tase, additives, filling):
        self.name = name
        self.kind =kind
        self.tase = tase
        self.additives  = additives
        self.filling = filling


cake1 = Cake("Vanilla cake","cake","vanilla",['chocolade', 'nuts'],'cream')
cake2 = Cake("Chocolade Muffin", "muffin", "chocolade", ['chocolade'], "Super Sweet Maringue")
bakkery_offer = [cake1,cake2]

for i in bakkery_offer:
    print(f'{i.name} {i.kind} {i.tase} {i.additives} {i.filling}')