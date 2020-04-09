class Room():
	"""docstring for Room"""
	"""Developing a constructor to initialize object"""
	def __init__(self, room_name):

		self.name = room_name
		self.description = None
		self.linked_rooms = {}

	# setters and getters for the attributes

	def get_description(self):
		return self.description

	def set_description(self, room_description):
		self.description = room_description
		
	def get_room_name(self):
		return self.name

	def set_room_name(self, room_name):
		self.name = room_name

	def describe(self):
		print (self.description)

	#Adding linking room method
	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link

	def get_details(self):
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print("The "+ room.get_room_name() +" is " + direction)