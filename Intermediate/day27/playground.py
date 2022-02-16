class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        self.make = kw.get("make")
        self.model = kw.get("model")  # <---- .get pula a key e vai direto para o value respectivo.
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)