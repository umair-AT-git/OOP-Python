class Item():
	"""docstring for Item"""
	def __init__(self, item_name):
		# super(Item, self).__init__()
		self.name = item_name
		self.description = None

	def set_name(self, item_name):
		self.name = item_name

	def get_name(self):
		return self.name

	def set_description(self, item_description):
		self.description = item_description

	def get_description(self):	
		return self.description

	def get_details(self):
		print(self.name)
		print(self.get_description())