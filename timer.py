import time
class timer:
	def __init__(self):
		self.ms = 0
		self.stx = None
		self.running = False
		self.endtime = 0.00

	def start(self):
		self.running = True
		self.stx = round(time.time()*1000.00)


	def end(self):
		self.running = False
		self.endtime = round(time.time() * 1000.00) - self.stx

	def convert(self):
		if not self.endtime:
			return None
		self.seconds = self.endtime / 1000
		return self.seconds

	def gettime(self):
		if not self.stx:
			return None
		if self.endtime:
			return self.endtime
		self.current = round(time.time() * 1000.00) - self.stx 
		self.seconds = self.current / 1000
		return self.seconds
