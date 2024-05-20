class Variaveis:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c
    
func1 = Variaveis(13, 15, 12)
func2 = Variaveis(9, 17, 11)
func3 = Variaveis(11, 13, 14)

print(func1.volume())
print(func2.volume())
print(func3.volume())

