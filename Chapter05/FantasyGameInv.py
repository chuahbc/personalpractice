# You are creating a fantasy video game. The data structure to model the player’s inventory
# will be a dictionary where the keys are string values describing the item in the inventory
# and the value is an integer value detailing how many of that item the player has. For 
# example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible “inventory” and display it 
# like the following:

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    numItems = 0
    print('Inventory :')
    print('')
    for n in inventory:
        numItems = numItems + inventory[n]
        print(inv[n], end=" ")
        print(n)
    
    print('')
    print('Total number of items: ' + str(numItems))

# displayInventory(inv)

# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary 
# representing the player’s inventory (like in the previous project) and the addedItems parameter is a list 
# like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. 
# Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def addToInventory(inventory, addedItems):
    for n in addedItems:
        inventory.setdefault(n, 0) 
        inventory[n] = inventory[n] + 1
    
    return inventory
    # your code goes here


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)