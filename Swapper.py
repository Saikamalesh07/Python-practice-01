print('Hello')
print("Welcome to the Swapper")

def get_items(who):
    print("Enter items for " + who + " (Type 'DONE' to finish):")
    items = []
    while True:
        item = input()
        if item.upper() == "DONE":
            break
        items.append(item)
    return items
items_a = get_items("A")
items_b = get_items("B")

if not items_a:
    print('Error You must enter anything for A, Cannot Proceed')
    exit()

elif not items_b:
    print(' Error You must enter anything for B, Cannot Proceed')
    exit()

common_items = set(items_a).intersection(set(items_b))
if common_items:

    print('Common items found between A and B')
    print("Common items:",list(common_items))

print('Before Swapping')
print("A has:", items_a)
print('B has:', items_b)

items_a, items_b = items_b, items_a

print("After Swapping")
print("A has:", items_a)
print("B has:", items_b)
