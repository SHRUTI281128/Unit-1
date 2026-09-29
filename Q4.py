class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def categorize(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: ₹", self.price)
        print("Category:", self.categorize())
        print("------------------------")


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_mobiles(self):
        print("\nMobile Store Details")
        print("========================")

        for mobile in self.mobiles:
            mobile.display()


# Creating Store object
store = Store()

# Creating Mobile objects
m1 = Mobile("Apple", "iPhone 15", 60000)
m2 = Mobile("Samsung", "Galaxy A55", 30000)
m3 = Mobile("Redmi", "Note 13", 15000)

# Adding mobiles to store
store.add_mobile(m1)
store.add_mobile(m2)
store.add_mobile(m3)

# Displaying all mobiles
store.display_mobiles()