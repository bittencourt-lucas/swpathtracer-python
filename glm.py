# -*- coding: utf-8 -*-

# These classes and functions were implemented following the DOCs from the original glm (OpenGL Mathematics) lib.
# You can find it here: http://glm.g-truc.net/0.9.8/index.html
# Also, some parts of it were implemented following the Mack Stone's glm Python code in GitHub.
# His code can be found here: https://github.com/mackst/glm

from math import sqrt

class ivec2(object):
	"""
	ivec2 ( x = 0, y = 0 )
	Creates a vector of two integers.
	DEFAULT is (0, 0)
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.x = kwargs.get('x', 0)
			self.y = kwargs.get('y', 0)
		elif args:
			self.x, self.y = args
		else:
			self.x = 0
			self.y = 0

class vec2(object):
	"""
	vec2 ( x = 0.0, y = 0.0 )
	Creates a vector of two floats.
	DEFAULT is (0.0, 0.0)
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.x = kwargs.get('x', .0)
			self.y = kwargs.get('y', .0)
		elif args:
			self.x, self.y = args
		else:
			self.x = .0
			self.y = .0
		
class vec3(object):
	"""
	vec3 ( x = 0.0, y = 0.0, z = 0.0 )
	Creates a vector of three floats.
	Has some vector operations.
	DEFAULT is (0.0, 0.0, 0.0)
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.x = kwargs.get('x', .0)
			self.y = kwargs.get('y', .0)
			self.z = kwargs.get('z', .0)
		elif args:
			self.x, self.y, self.z = args
		else:
			self.x = .0
			self.y = .0
			self.z = .0

	# Handling Negative Unary of vec3 Objects:
	def __neg__(self):
		return vec3(self.x * (-1), self.y * (-1), self.z * (-1))

	# Handling Addition of vec3 Objects:
	def __add__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x + value.x, self.y + value.y, self.z + value.z)
		else:
			return vec3(self.x + value, self.y + value, self.z + value)

	# Handling Reverse Addition of vec3 Objects:
	def __radd__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x + value.x, self.y + value.y, self.z + value.z)
		else:
			return vec3(self.x + value, self.y + value, self.z + value)

	# Handling Subtraction of vec3 Objects:
	def __sub__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x - value.x, self.y - value.y, self.z - value.z)
		else:
			return vec3(self.x - value, self.y - value, self.z - value)

	# Handling Reverse Subtraction of vec3 Objects:
	def __rsub__(self, value):
		if isinstance(value, vec3):
			return vec3(value.x - self.x, value.y - self.y, value.z - self.z)
		else:
			return vec3(value - self.x, value - self.y, value - self.z)

	# Handling Multiplication of vec3 Objects:
	def __mul__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x * value.x, self.y * value.y, self.z * value.z)
		else:
			return vec3(self.x * value, self.y * value, self.z * value)

	# Handling Reverse Multiplication of vec3 Objects:
	def __rmul__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x * value.x, self.y * value.y, self.z * value.z)
		else:
			return vec3(self.x * value, self.y * value, self.z * value)

	# Handling Division of vec3 Objects:
	def __truediv__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x / value.x, self.y / value.y, self.z / value.z)
		else:
			return vec3(self.x / value, self.y / value, self.z / value)

	# Handling Reverse Division of vec3 Objects:
	def __rtruediv__(self, value):
		if isinstance(value, vec3):
			return vec3(value.x / self.x, value.y / self.y, value.z / self.z)
		else:
			return vec3(value / self.x, value / self.y, value / self.z)

# Cross Product of Two vec3 Objects
def cross(first, second):
	return vec3(
		first.y * second.z - first.z * second.y,
		first.z * second.x - first.x * second.z,
		first.x * second.y - first.y * second.x)

# Dot Product of Two vec3 Objects
def dot(first, second):
	if isinstance(first, float) and isinstance(second, float):
		return first * second
	elif isinstance(first, vec3) and isinstance(second, vec3):
		return first.x * second.x + first.y * second.y + first.z * second.z

# Normalization of a vec3 Object
def normalize(value):
	if isinstance(value, float):
		if value < 0.0:
			return -1.0
		return 1.0
	elif isinstance(value, vec3):
		magnitude = sqrt(value.x ** 2 + value.y ** 2 + value.z ** 2)
		return value / magnitude