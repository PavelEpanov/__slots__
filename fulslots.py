class Slotful:
    __slots__ = ["a", "b", "__dict__"]
    def __init__(self, data):
        self.c = data

I = Slotful(3)
I.a, I.b = 1, 2
print(I.a, I.b, I.c) # Нормальное извлечение атрибутов
print(I.__dict__) # Присутствуют хранилища __dict__ и __slots__ 
print([x for x in dir(I) if not x.startswith("__")])
print(I.__dict__["c"]) # Единственным источником атрибутов является __dict__
print(getattr(I, "c"), getattr(I, "a")) # Сочетание dir+getattr обширнее, чем просто __dict__
# Применяется к слотам, свойствам, дескрипторам 
for a in (x for x in dir(I) if not x.startswith("__")):
    print(a, getattr(I, a))
