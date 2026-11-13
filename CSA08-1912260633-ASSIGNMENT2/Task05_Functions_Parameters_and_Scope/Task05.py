# Q5 - Functions, Parameters and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def bill_total(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst

# Demonstrate the mutable-default bug.
print("Buggy calls:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print("Correct calls:")
print(add_item("Tea"), add_item("Vada"))

print("Default object:", add_item_buggy.__defaults__)

# Three independent customers.
orders = [
    add_item("Tea"),
    add_item("Vada"),
    add_item("Coffee"),
]
print("Independent customer orders:", orders)

total, gst = bill_total(200, gst_rate=0.05)
print(f"Bill amount: 200.00, GST: {gst:.2f}, Total: {total:.2f}")

# Scope demonstration.
tax_rate = 0.05
def calculate_tax(amount):
    local_tax = amount * tax_rate
    return local_tax

print("Global tax rate:", tax_rate)
print("Calculated tax:", calculate_tax(100))
