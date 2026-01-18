from abc import ABC, abstractmethod

# Abstract class
class Pet(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self):
        pass

# Child class
class Dog(Pet):
    def play(self):
        print(self.name, "is playing 🐶")

# Game
pet = Dog("Adelade")  
pet.play() 