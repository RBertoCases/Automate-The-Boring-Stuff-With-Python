

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory 

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print (str(v)+' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)