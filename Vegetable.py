class Tomato:
    def type(self):
        print ("Tomato is a Vegetable")

    def color(self):
        print("The colour is Red")

class Mango:
    def type(self):
        print ("Mango is a Fruit")

    def color(self):
        print("The colour is Yellow")

def myfunc(obj):
    obj.type()
    obj.color()

tom= Tomato()
go = Mango()
myfunc(tom)
myfunc(go)
