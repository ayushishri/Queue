class queue:
	def __init__(self):
		self.store=[]
	def enQ(self,val):
		self.store+=[val]
		return 0
	def deQ(self):
		rval=self.store[0]
		self.store=self.store[1:]
		return rval

