class Student:
  def __init__(self, name, school, grades):
    self.name = name
    self.school = school
    self.grades = grades

  def average(self):
    if len(self.grades) == 0:
      return -1
    return sum(self.grades)/len(self.grades)

  def __str__(self):
    return f"{self.name} ({self.school}) : {self.grades}[{self.average()}]"


class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    item = {"name": name, "price": price}
    self.items.append(item)
    
  def stock_price(self):
    return sum(item["price"] for item in self.items)

  def __str__(self):
    line = "=" * len(self.name)
    return f"{self.name}\n{line}\n{self.items}\n{line}\nstock price : {self.stock_price()}"

students = [{ "name": "Martin", "school": "OU", "grades": (6.0, 7.0, 8.0, 9.0)},
            {"name": "Astrid", "school": "ACT", "grades": (8.0, 8.0, 9.0)},
           ]

def average_grade(data):
  grades = data["grades"]
  return sum(grades)/len(grades)

student1 = Student("Rolf", "Computers", (90, 60, 100, 80))
student2 = Student("Martin", "OU", (60, 70, 80, 70, 70))


#print(student1)
#print(student2)

hubo = Store("Hubo")
hubo.add_item("Zaag", 5.95)
hubo.add_item("Hamer", 4.45)

print(hubo)
