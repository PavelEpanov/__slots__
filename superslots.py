class E:
    __slots__ = ["c", "d"] # Суперкласс имеет слоты
class D(E):
    __slots__ = ["a", "__dict__"] # Но его подкласс тоже

X = D()
X.a = 1; X.b = 2; X.c = 3 # Экземпляр получает объединение (слоты: a, c)
print(X.a, X.c)
print(E.__slots__)
print(D.__slots__) # Однако слоты не объединяются
print(X.__slots__) # Экземпляр наследует "самый нижний" список  __slots__
print(X.__dict__) # И имеет собсвтенный словарь атрибутов
for attr in list(getattr(X, "__dict__", [])) + getattr(X, "__slots__", []):
    print(attr, "=>", getattr(X, attr))
    # Слоты остальных суперклассов отсутствуют!
print(dir(X)) # Но dir() включает все слотовые имена
