class C: # Пункт 1: слоты в подклассе, но не в суперклассе
    pass
class D(C):
    __slots__ = ["a"] # Создает словарь экземпляра для неслотовых имен
X = D() # Но слотовое имя по - прежнему поддерживается в классе
X.a = 1; X.b = 2
print(X.__dict__)
print(D.__dict__.keys())

class E: # Пункт 2: слоты в суперклассе, но в в подклассе
    __slots__ = ["a"]
class F(E):
    pass
Y = F()
Y.a = 1; Y.b = 2
print(Y.__dict__)
print(Y.__dict__.keys())

class K: # Пункт 3: доступен только самый нижний слот
    __slots__ = ["a"]
class L(K):
    __slots__ = ["a"]

class P: # Стандартные имена уровня класса отсутсвуют
    __slots__ = [a]
    a = 99
#ValueError: 'a' in __ slots__ conflicts with class variable

class M:
    __slots__ = ["a"]
class R(M):
    __slots__ = ["b"]

L = R()
L.a = 1; L.b = 2
print(L.__dict__)
# AttributeError: 'D' object has no attribute '__ diet__ '
print(R.__dict__.keys(),M.__dict__.keys())
