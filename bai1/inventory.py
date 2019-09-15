import os

class Inventory:
  def __init__(self, cap):
    self.capacity = cap
    self.currentQuantity = 0
  
  def importG(self, quanity):
    if self.currentQuantity + quanity > self.capacity:
      print("Insufficent space")
    else:
      print("{} were (was) imported".format(quanity))
      self.currentQuantity += quanity
  
  def exportG(self, quantity):
    if self.currentQuantity < quantity:
      print("Insufficent goods")
    else:
      self.currentQuantity -= quantity
      print("{} of goods were exported, only {} left".format(quantity, self.currentQuantity))
  
  def currentInventoryStatus(self):
    print("Current quantity: {}, current capacity: {}".format(self.currentQuantity, self.capacity))


def clearScreen ():
  clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
  clear()

def printMenu():
  print("---------------------------")
  print("|1. Import good           |")
  print("|2. Export good           |")
  print("|3. Check current status  |")
  print("|0. Exit                  |")
  print("---------------------------")

choice = 99
inventory = Inventory(100)


while choice != 0:
  printMenu()
  choice = int(input("Your choice: "))
  if choice == 1: #Nhap kho
    clearScreen()
    amount = input("Enter quantity to import: ")
    inventory.importG(int(amount))
  elif choice == 2:
    clearScreen()
    amount = input("Enter quantity to export: ")
    inventory.exportG(int(amount))
  elif choice == 3:
    clearScreen()
    inventory.currentInventoryStatus()
    
print("Bye bye!")


