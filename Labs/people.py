from person import person

class RecordSystem:
  def __init__(self):
    self.people = []
  def add_person(self, person):
    self.people.append(person)
  def display(self):
    print(self.people)

record_system = RecordSystem()

Gura = person("Gura")