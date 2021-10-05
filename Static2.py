class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  @classmethod
  def franchise(cls, name):
    name2 = name + " - franchise"
    return cls(name2)

  @classmethod
  def store_details(store):
    return store.__repr__()

  def add_item(self, name, price):
    item = {"name": name, "price": price}
    self.items.append(item)
    
  def stock_price(self):
    return sum(item["price"] for item in self.items)

  def __str__(self):
    line = "=" * len(self.name)
    return f"{self.name}\n{line}\n{self.items}\n{line}\nstock price : {self.stock_price()}"


amazon = Store("Amazon")
amazon.add_item("Abba Gold", 12.99)
amazon.add_item("Mouse", 19.00)
mcd1 = Store.franchise("McDonalds 1")
mcd1.add_item("Big Mac", 3.24)
print(amazon)
print(mcd1)