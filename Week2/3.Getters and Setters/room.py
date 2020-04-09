class Room():
	"""docstring for Room"""
	"""Developing a constructor to initialize object"""
	def __init__(self, room_name):

		self.name = room_name
		self.description = None

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