class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakkery_offer = []

    def __init__(self, name, kind, tase, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.tase = tase
        self.additives = additives
        self.filling = filling
        self.bakkery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == 'cake' and text == '':
            self.__text = text
        else:
            print("cannot add text")

    def show_info(self):
        print(f'''
        name: {self.name}
        kind: {self.kind}
        taste: {self.tase}
        additives: {self.additives}
        filling: {self.filling}
        gluten free: {self.__gluten_free}
        
        ''')

    def set_filling(self, filing):
        self.filing = filing

    def add_additives(self, addivites):
        self.additives.extend(addivites)

    @property
    def get_text(self):
        return self.__text

    @get_text.setter
    def set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print("can not change text")


cake1 = Cake("Vanilla cake", "cake", "vanilla", ['chocolade', 'nuts'], 'cream',True,'')
cake2 = Cake("Chocolade Muffin", "muffin", "chocolade", ['chocolade'], "Super Sweet Maringue",True,'')

cake1.Text = "write somethin"
cake1.show_info()


cake2.set_filling('mango')
cake2.add_additives(["banana", 'water'])
cake2.show_info()

print(isinstance(cake1, Cake))
print(vars(cake1))
print(vars(Cake))

for i in Cake.bakkery_offer:
    i.show_info()

cake1.set_text = 'cake cake'
print(cake1.get_text)
print(len(Cake.bakkery_offer))


