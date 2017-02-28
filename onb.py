# -*- coding: utf-8 -*-

import glm

class ONB(object):
	"""
	Orthonormal Basis
	This class creates an identity 3x3 matrix, and it'll handle
	some matrix calculations.
	"""
	def __init__(self):
		# Default ONB is the standard orthonormal basis.
		self.u = glm.vec3(1.0, 0.0, 0.0)
		self.v = glm.vec3(0.0, 1.0, 0.0)
		self.w = glm.vec3(0.0, 0.0, 1.0)
		self.setBasisMatrix()

	def setFromV(self, v):
		# Set up an ONB from an normalized input vector 'v' that will be assumed to be aligned to 
		# the 'v' (up) vector of the ONB to be created.
		self.v = v;
		if abs(self.v.x) > abs(self.v.y):
			self.w = glm.normalize(glm.vec3(self.v.z, 0.0, -self.v.x))
		else:
			self.w = glm.normalize(glm.vec3(0.0, -self.v.z, self.v.y))
		self.u = glm.cross(self.v, self.w)
		self.setBasisMatrix()

	def setFromUW(self, u, w):
		# Set up an ONB from the normalized input vectors 'u' and 'w', that will be assumed to be aligned to
		# the vectors 'u' (right) and 'w' vectors of the ONB to be created.
		self.u = u
		self.w = w
		self.v = glm.cross(self.w, self.u)
		self.setBasisMatrix()

	# Returns the 3x3 matrix
	def getBasisMatrix(self):
		return self.mat3x3

	# Builds a 3x3 matrix from vectors u, v and w.
	def setBasisMatrix(self):
		self.mat3x3 = [[self.u.x, self.u.y, self.u.z], [self.v.x, self.v.y, self.v.z], [self.w.x, self.w.y, self.w.z]]

	# Multiply a 3x3 matrix and a 3x1 vector
	def multMatrixVec3(self, value):
		if isinstance(value, glm.vec3):
			return glm.vec3((self.mat3x3[0][0] * value.x + self.mat3x3[0][1] * value.y + self.mat3x3[0][2] * value.z),
				(self.mat3x3[1][0] * value.x + self.mat3x3[1][1] * value.y + self.mat3x3[1][2] * value.z),
				(self.mat3x3[2][0] * value.x + self.mat3x3[2][1] * value.y + self.mat3x3[2][2] * value.z))
