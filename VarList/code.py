class List:
	a0 = None
	a1 = None
	a2 = None
	a3 = None
	a4 = None
	
	def get(self, index):
		if index == 0: return self.a0
		elif index == 1: return self.a1
		elif index == 2: return self.a2
		elif index == 3: return self.a3
		elif index == 4: return self.a4
		else: raise ValueError('List index is out of range')

	def set(self, index, value):
		if index == 0: self.a0 = value
		elif index == 1: self.a1 = value
		elif index == 2: self.a2 = value
		elif index == 3: self.a3 = value
		elif index == 4: self.a4 = value
		else: raise ValueError('List index is out of range')


if __name__ == '__main__':
	my_list = List()
	my_list.set(1, 314)
	print(my_list.get(1))
