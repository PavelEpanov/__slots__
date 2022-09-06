class Operators:
    def __getattr__(self, name):
        if name == "age":
            return 40
        else:
            raise AttributeError(name)

X = Operators()
print(X.age) # Запускается __getattr__
#print(X.name) # Зпускается __getattr_

class Propirties:
    def getage(self):
        return 40
    age = property(getage, None, None, None) # Получение,  установка, удаление, строка документации; либо использовать @

Y = Propirties()
print(Y.age) # Запускается getage
# print(Y.name) # Нормальное извлечение
# AttributeError: ’properties' object has no attribute 'name'

class PropertiesTwo:
    def getage(self):
        return 40
    def setage(self, value):
        print(f"Set age: {value}")
        self._age = value
    age = property(getage, setage, None, None)

H = PropertiesTwo()
H.age # Запускается getage
print(H.age)
H.age = 42 # Запускается setage
print(H._age) # Нормальное извлечение getage не вызывается
print(H.age) # Запускается getage
H.job = "trainer" # Нормальное присваивание: setage не вызывается
print(H.job) # Нормальное извлечение: getage не вызывается

class OperatorsTwo:
    def __getattr__(self, name): # При ссылке на неопределенный атрибут
        if name == "age":
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value): # При всех операциях присваивания 
        print(f"set: {name} {value}")
        if name == "age":
            self.__dict__["_age"] = value # или object.__setattr__()
        else:
            self.__dict__[name] = value

M = OperatorsTwo()
print(M.age) # Запускается __getattr__
M.age = 41 # Запускается __setattr__
print(M._age) # Определен: __getattr__ не вызывается 
print(M.age) # Запускается __getattr__
M.job = "trainer" # Снова запускается __setattr__
print(M.job) # Определен: __getattr__ не вызывается
