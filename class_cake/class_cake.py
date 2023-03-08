
class Cake:
    def __init__(self, name, kind, tase, additives, filling):
        self.name = name
        self.kind =kind
        self.tase = tase
        self.additives  = additives
        self.filling = filling

    def show_info(self):
        print(f'''
        name: {self.name}
        kind: {self.kind}
        taste: {self.tase}
        additives: {self.additives}
        filling: {self.filling}
        ''')

    def set_filling(self,filing):
        self.filing = filing

    def add_additives(self,addivites):
        self.additives.extend(addivites)

cake1 = Cake("Vanilla cake","cake","vanilla",['chocolade', 'nuts'],'cream')
cake2 = Cake("Chocolade Muffin", "muffin", "chocolade", ['chocolade'], "Super Sweet Maringue")


bakkery_offer = [cake1,cake2]


cake1.show_info()

cake2.set_filling('mango')
cake2.add_additives(["banana",'water'])
cake2.show_info()

for i in bakkery_offer:
    print(f'{i.name} {i.kind} {i.tase} {i.additives} {i.filling}')