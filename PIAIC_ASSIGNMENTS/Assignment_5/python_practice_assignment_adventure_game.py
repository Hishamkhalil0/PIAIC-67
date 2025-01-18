
# introduction
print("Welcome to the Adventure Game!\n")

inventory = []

locations = {
    "forest": "You are in a dark forest. You hear strange noises.",
    "cave": "You have entered a damp cave. It's very cold here.",
    "river": "You are standing by a river. The water is flowing quickly."
}

items = {
    "forest": "wooden stick",
    "cave": "glowing crystal",
    "river": "shiny stone"
}
visited_locations = []

# game looop starts here

while True:
  available_keys = [loc for loc in locations if loc not in visited_locations]

  if not available_keys:
    print("You have visited all locations! Type 'inventory' to view your items or 'quit' to end the game.")
  else:
    available_locations = ", ".join(available_keys)
    print(f"Available locations : {available_locations}")

  destination = input(f"Where do you want to go?  : ").lower().strip()

# Check if the destination is valid
  if destination in locations :
    print(f"\nHeading towards {destination}")
    print(f"Welcome to the {destination}\n")
    print(locations[destination])

    visited_locations.append(destination)

 # Offer the item at the location
    question =input(f"You found a {items[destination]} . Do you want to collect it? (yes/no): ").lower().strip()

    if question == "yes":
      print("\nCollecting item.....")
      print(f"{items[destination]} Collected Successfully  \n")
      inventory.append(items[destination])

    elif question == "no"  :
      print(f"\nYou decided not to collect {items[destination]}... Heading towards next location....\n")

    else:
      print("Invalid input ... input again\n")

# accessing inventory

  elif destination == "inventory":
    if inventory == []:
      print(f"You have nothing in your inventory\n")
    else:
      print(f"\n{', '.join(inventory)}\n")

# endinh game
  elif destination == "quit":

    if inventory == []:
      print(f"Goood bye.. you have nothing in your inventory")
      break

    else:
      print(f"\nGoood bye.. you have collected {', '.join(inventory)}")
      break

# incase of invalid input
  else:
    print("Invalid input ... input again")

