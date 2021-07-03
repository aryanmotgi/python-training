class MyClass:
    # atrribute or methods go here
    pass

myObj = MyClass()


class Person:
    def __init__(self, name, age):
        """ This methods is executed every time we created a new `person` instance
        `self` is the object instanve being created."""

        self.name = name
        self.name = age

        self.num_arms = 2
        self.nums_legs = 2

        self.num_limbs = self.num_arms + self.nums_legs

    def print_name_and_age(self): 
        print("Name:", self.name, "\nAge:", self.age)
        
    person1 = Person("Bob", 15)
    
    
    class Dog:
  def __init__(self,name):
    self.name=name
  def speak(message):
    print("*woof* "+ message+" *woof")
dog1=Dog("Rocco")
print(dog1.name,dog1.speak("hello"))
