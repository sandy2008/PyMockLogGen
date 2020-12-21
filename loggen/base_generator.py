import abc


class log_gen(metaclass=abc.ABCMeta):
	"""
	Abstract Base Log Generator
	"""

	@abc.abstractproperty
	def lines(self):
		pass

	@abc.abstractproperty
	def methods(self):
		pass

	@abc.abstractproperty
	def methods_p(self):
		pass

	@abc.abstractproperty
	def mode(self):
		pass

	@abc.abstractproperty
	def out_format(self):
		pass

	@abc.abstractmethod
	def run(self):
		pass




