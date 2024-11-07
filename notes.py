# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n = "no name", a = 0):
        self.name = n
        self.age = a
        self.fetch_count = 0
    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch
    def fetch_rest(self):
        self.fetch_count = 0
logan = Dog("logan", 8)
becker = Dog("Becker", 4)
kepa = Dog("Kepa", 4) 

logan.play_fetch(100)
print (logan.fetch_count)