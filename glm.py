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

	# Handling Addition of vec3 Objects:
	def __add__(self, value):
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

	# Handling Multiplication of vec3 Objects:
	def __mul__(self, value):
		if isinstance(value, vec3):
			return vec3(self.x * value.x, self.y * value.y, self.z * value.z)
		else:
			return vec3(self.x * value, self.y * value, self.z * value)
		
# Cross Product of Two vec3 Objects
def cross(first, second):
	return vec3(
		first.y * second.z - second.y * first.z,
		first.z * second.x - second.z * first.x,
		first.x * second.y - second.y * first.x)

# Dot Product of Two vec3 Objects
def dot(first, second):
	if isinstance(first, float) and isinstance(second, float):
		return first * second
	elif isinstance(first, vec3) and isinstance(second, vec3):
		dotproduct = first * second
		return dotproduct.x + dotproduct.y + dotproduct.z

# Inverse Square Root (used on normalize())
def inversesqrt(value):
	if isinstance(value, float):
		return (1.0 / sqrt(value))
	elif isinstance(value, vec3):
		return vec3((1.0 / sqrt(value.x)), (1.0 / sqrt(value.y)), (1.0 / sqrt(value.z)))

# Normalization of a vec3 Object
def normalize(value):
	if isinstance(value, float):
		if value < 0.0:
			return -1.0
		return 1.0
	elif isinstance(value, vec3):
		result = value.x * value.x + value.y * value.y + value.z * value.z
		return value * inversesqrt(result)