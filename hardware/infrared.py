#此模块为红外模块,分为两个模块,1、红外接收模块;2、红外发送模块

#红外接收模块
class infraredread(object):
	"""docstring for infrared"""
	def __init__(self, arg):
		super(infrared, self).__init__()
		self.arg = arg

#红外发送模块
class infraredsend(object):
	"""docstring for infraredread"""
	def __init__(self, arg):
			super(infraredread, self).__init__()
		self.arg = arg
