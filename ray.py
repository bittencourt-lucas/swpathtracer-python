# -*- coding: utf-8 -*-

import glm

class Ray(object):
	"""
	Ray (origin = vec3, direction = vec3 )
	Determines the origin and direction of the rays.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.origin = kwargs.get('origin', glm.vec3(.0, .0, .0))
			self.direction = kwargs.get('direction', glm.vec3(.0, .0, .0))
		elif args:
			self.origin, self.direction = args
		else:
			self.origin = glm.vec3(.0, .0, .0)
			self.direction = (.0, .0, .0)