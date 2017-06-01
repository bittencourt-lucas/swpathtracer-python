# -*- coding: utf-8 -*-

import glm

class Material(object):
	"""
	Material ( name (string), emittance (vec3), brdf (vec3) )
	An abstract material type.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.name = kwargs.get('name', "Unknown")
			self.brdf = kwargs.get('brdf', glm.vec3(.0, .0, .0))
			self.emittance = kwargs.get('emittance', glm.vec3(.0, .0, .0))
		elif args:
			self.name, self.brdf, self.emittance = args
		else:
			self.name = "Unknown"
			self.brdf = glm.vec3(.0, .0, .0)
			self.emittance = glm.vec3(.0, .0, .0)

	def getFr(self, wi, wo):
		pass

	def bounce(self, wi):
		pass

	def getEmittance(self):
		pass