
class Scope(object):
	def __init__(self, upper_scope, base_path = None):
		self.upper_scope = upper_scope
		self.variables = {}
		self.base_path = base_path

	def __repr__(self):
		return str(self.__dict__) + "\n" 

	def __str__(self):
		return self.__repr__()
