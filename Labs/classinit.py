class person:

  max_energy = 100 #Constant | Once initial value is assigned, does not change
  #initialiser (special instance method)
  def __init__(self):
    self.name = "Gawr Gura"
    self.age = "22"
    self.weight = "Light"

#The object
Gura = person("Gura", 18, 75)

#-------------------------------------------------------------------------------------#

class person:

  max_energy = 100
  #initialiser
  def __init__(self, name, age=0, weight=0):
    self.name = name
    self.age = age
    self.weight = weight
    self.energy = person.max_energy
   def grow():
  self.age += 1

def display(self):
  print(f"My name is {self.name}) and i am {self.age} years old")

baby_gura = person("Gura")
adult_gura = person("Gura", 18)
adult_gura_with_weight = person("Gura", 18, 75)


#-----#

def generate_people(Self):
  name = input("Enter your name")
  the_person = person(name)
