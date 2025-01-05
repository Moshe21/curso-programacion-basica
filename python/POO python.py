"""class Person:
    def __init__(self,name, age):
        
        self.name = name
        self.age= age

    def greet (self):
        print(f"hola, mi nombre es {self.name} y tengo {self.age} años")

person1 = Person("ana",16)
person2 = Person("carlo ",20)

person1.greet()
person2.greet()
"""

class bank:
   
    def __init__ (self,nombre_cuenta, balance):
        self.nombre_cuenta= nombre_cuenta
        self.balance = balance
        self.is_active = True
        
        
    def deposito(self,monto):
        if self.is_active:
            self.balance+= monto
            print(f"se a depositado {monto}. saldo total es igual a {self.balance}")
        else:
            print("La  cuenta esta desactiva y no se depositar")

    def withdraw(self,monto):
        if self.active:
            if monto <= self.balance:
                self.balance -= monto 
                print(f"se ha retirado {monto}. saldo total es igual a {self.balance}")

    def desactivate_cuenta(self):
        self.is_active = False
        print(f"la cuenta {self.nombre_cuenta} esta desactivada")
    
    def activate_cuenta(self):
        self.is_active = True
        print(f"la cuenta {self.nombre_cuenta} esta activada")


cuenta1=bank("vale",20)
cuenta2=bank("javier",50)

cuenta1.deposito(50)
cuenta2.deposito(82)

cuenta1.desactivate_cuenta()
cuenta2.desactivate_cuenta()

cuenta1.deposito(200)

cuenta1.activate_cuenta()
cuenta1.deposito(200)