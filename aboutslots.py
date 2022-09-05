class C:
    __slots__ = ["a", "b"]

X = C()
X.a = 1
print(X.a)
# 1
# print(X.__dict__)
# AttributeError: "C" object has no attribute "__dict__"

print(getattr(X, "a"))
setattr(X, "b", 2) # Но getattr() и setattr() работают по прежнему
print(X.b)
print(dir(X)) # И dir() тоже находит слотовые атрибуты 
print("a" in dir(X))
print("b" in dir(X))

class D:
    __slots__ = ["a", "b"]
    def __init__(self):
        self.d = 4 # В отсутвствие dict добавлять новые имена невозможно

# Y = D()
# AttributeError: 'D' object has no attribute 'd'

class E:
    __slots__ = ["a",  "b", "__dict__"] # Указание dict для его включения
    c = 3 # Атрибуты работают нормально
    
    def __init__(self):
        self.d = 4 # d хранится в __dict__, а является слотом

U = E()
print(U.d, U.c)
#print(U.a)
# AttributeError: "a"
U.a = 5
U.b = 7
print(U.a)
print(dir(U))
print(U.__dict__)
print(getattr(U, "a"), getattr(U, "d")) # getattr() работает для обоих форм хранения данных(с dict и без dict)

for attr in list(getattr(U, "__dict__", [])) + getattr(U, "__slots__", []):
    print(attr, "=>", getattr(U, attr)) # Неправильно, но не так ужасно..
