from room import Room

#instatntiating (creating) an object

kitchen = Room("Kitchen")

#finding out what we learnt up to now
kitchen.set_description("A dank and dirty room buzzing with flies.")
#kitchen.get_description()
#kitchen.describe()

dining_hall = Room("Dining_hall")
dining_hall.set_description("Where gosts have their meals")

ballroom = Room("Ballroom")
ballroom.set_description("Where zombies have their parties")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# dining_hall.get_details()
# kitchen.get_details()
# ballroom.get_details()

current_room = kitchen

while True:
	print("\n")
	current_room.get_details()
	command = input("> ")
	current_room = current_room.move(command)