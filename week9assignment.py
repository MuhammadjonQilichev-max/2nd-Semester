from dataclasses import dataclass, field
@dataclass
class Product:
    name: str
    price: float
    quantity: int
    def value(self):
        return self.price * self.quantity
@dataclass
class Warehouse:
    name: str
    products: list = field(default_factory=list)
    total_value: float = field(init=False)
    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        total = 0
        for p in self.products:
            total += p.value()
        self.total_value = total
    def add_product(self, product):
        self.products.append(product)
        self._refresh()
    def sell(self, product_name, qty):
        for p in self.products:
            if p.name == product_name:
                if p.quantity >= qty:
                    p.quantity -= qty
                    self._refresh()
                    return True
                else:
                    return False
        return False
    def restock(self, product_name, qty):
        for p in self.products:
            if p.name == product_name:
                p.quantity += qty
                self._refresh()
    def report(self):
        result = self.name + " Inventory:\n"
        for p in self.products:
            result += f"  {p.name}: {p.quantity} units @ ${p.price} each\n"
        result += f"Total value: ${round(self.total_value, 2)}"
        return result

p1 = Product("Laptop", 999.99, 10)
p2 = Product("Mouse", 29.99, 50)
p3 = Product("Keyboard", 79.99, 30)
w = Warehouse("TechDepot")
w.add_product(p1)
w.add_product(p2)
w.add_product(p3)
print(w.total_value)
print(w.sell("Laptop", 3))
print(w.sell("Laptop", 20))
w.restock("Mouse", 25)
print(w.report())