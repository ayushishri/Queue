class queue:
	def __init__(self):
		self.store=[]
		self.count=0

	def enQ(self,val):
		self.store+=[val]
		self.count+=1
		return 0

	def deQ(self):
		rval=self.store[0]
		self.store=self.store[1:]
		self.count-=1
		return [True,rval]
		
	def isEmpty(self):
		if (self.count==0):
			return True
		return False

