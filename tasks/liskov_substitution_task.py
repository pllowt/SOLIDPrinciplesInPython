class Rectangle:
	def __init__(self, width: int, height: int):
		self._width = width
		self._height = height

	def set_width(self, width: int):
		self._width = width

	def set_height(self, height: int):
		self._height = height

	def calculate_area(self):
		return self._width * self._height


class Square(Rectangle):
	def set_width(self, width: int):
		self._width = width
		self._height = width

	def set_height(self, height: int):
		self._height = height
		self._width = height
