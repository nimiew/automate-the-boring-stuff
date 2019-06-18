stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print("Inventory: ")
    total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        total += v

    print("Total no. of items: " + str(total))

displayInventory(stuff)

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inv, loot):
    for i in loot:
        inv.setdefault(i, 0)
        inv[i] += 1

    return inv

new_stuff = addToInventory(stuff, loot)
displayInventory(new_stuff)
        
