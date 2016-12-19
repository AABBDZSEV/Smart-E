#此模块为按键模块，分为两个模块：1、触摸开关；2、触摸开关16合一

#此类为触摸开关模块，主动式，不可关闭
class button(object):
	"""docstring for button"""
	def __init__(self, arg):
		super(button, self).__init__()
		self.arg = arg

#此类为触摸开关16合一模块，主动式，可关闭
class button16(object):
	"""docstring for button16"""
	def __init__(self, arg):
		super(button16, self).__init__()
		self.arg = arg

