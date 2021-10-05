class Classtest:

  def instance_method(self):
    print(f"Called instance_method of {self}")

  @classmethod
  def class_method(cls):
    print(f"Called class_method of {cls}")

  @staticmethod
  def static_method():
    print("Called ststic method")

test = Classtest()

test.instance_method()
test.class_method()

Classtest.class_method()

test.static_method()