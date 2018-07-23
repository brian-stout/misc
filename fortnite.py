import random

default_poi_list = ['Junk Junction', 'Lazy Links', 'Risky Reels', 'Haunted Hills',
                    'Pleasant Park', 'Tomato Town', 'Wailing Woods',
                    'Snobby Shores', 'Loot Lake', 'Dusty Divot', 'Retail Row',
                    'Lonely Lodge', 'Salty Springs', 'Titled Towers',
                    'Titled Towers', 'Titled Towers', 'Greasy Grove',
                    'Shifty Shafts', 'Fatal Fields', 'Paradise Palms',
                    'Flush Factory', 'Lucky Landing', 'Unnamed: Motel',
                    'Unnamed: Villain Lair', 'Unnamed: Old Faithful',
                    'Unnamed: Race Track', 'Unnamed: RV Park', 'Unnamed: Mansion',
                    'Unnamed: Viking Outpost', 'Unnamed: Flush Warehouses', 
                    'Unnamed: Adobe Villages (South of Paradise)',
                    'Unnamed: Indoor Soccer Stadium', 'Unnamed: Spires'
                    ]

class Locations():
  def __init__(self):
    self.perm_coordinate_list = self.gen_coordinate_list()
    self.perm_poi_list = default_poi_list
    self.running_coordinate_list = []
    self.running_poi_list = []
    self.gen_running_coordinate_list()
    self.gen_running_poi_list()

  def gen_coordinate_list(self):
    coordinate_list = []
    for base in range(0,10):
      letter = str(chr(base + ord('A')))
      for number in range(1,11):
        coordinate_list.append(letter + str(number))
    
    return coordinate_list

  def gen_running_coordinate_list(self):
    self.running_coordinate_list = self.perm_coordinate_list.copy()
  
  def gen_running_poi_list(self):
    self.running_poi_list = self.perm_poi_list.copy()

  def print_coordinates(self):
    print(random.choice(self.perm_coordinate_list))

  def print_poi(self):
    print(random.choice(self.perm_poi_list))

  def print_running_coordinate(self):
    if len(self.running_coordinate_list) == 0:
      self.gen_running_coordinate_list()

    choice = random.choice(self.running_coordinate_list)
    self.running_coordinate_list.remove(choice)
    print(choice)

  def print_running_poi(self):
    if len(self.running_poi_list) == 0:
      self.gen_running_poi_list()

    choice = random.choice(self.running_poi_list)
    self.running_poi_list.remove(choice)
    print(choice)

list_obj = Locations()

if __name__ == "__main__":
  while True:
    print("\nSelect an option")
    print("A: Print POI")
    print("B: Print random coordinates")
    print("C: Print non-repeating random POI")
    print("D: Print non-repeating random coordinates")
    option = input(":")
    option = option.upper()
    print("")

    if option == 'A' or '1':
      list_obj.print_poi()
    elif option == 'B' or '2':
      list_obj.print_coordinates()
    elif option == 'C' or '3':
      list_obj.print_running_poi()
    elif option == 'D' or '4':
      list_obj.print_running_coordinate()
    else:
      print("Not a valid option")
