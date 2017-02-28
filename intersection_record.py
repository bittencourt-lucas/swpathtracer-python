# -*- coding: utf-8 -*-

import glm

class IntersectionRecord(object):
	"""
	IntersectionRecord ( t, position(vec3), normal(vec3) )
	This class will be used when the rays intersect an object
	on the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.t = kwargs.get('t', 0.0)
			self.position = kwargs.get('position', glm.vec3(.0, .0, .0))
			self.normal = kwargs.get('normal', glm.vec3(.0, .0, .0))
		elif args:
			self.t, self.position, self.normal = args
		else:
			self.t = 0.0
			self.position = glm.vec3(.0, .0, .0)
			self.normal = glm.vec3(.0, .0, .0)