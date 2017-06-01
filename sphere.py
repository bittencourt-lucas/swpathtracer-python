# -*- coding: utf-8 -*-

import glm
import material
from random import random
from math import sqrt
from math import pi

class Sphere(object):
	"""
	Sphere ( center (vec3), radius )
	Creates spheres on the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.center = kwargs.get('center', glm.vec3(.0, .0, .0))
			self.radius = kwargs.get('radius', 0.0)
			self.material = kwargs.get('material', material.Material())
		elif args:
			self.center, self.radius, self.material = args
		else:
			self.center = glm.vec3(.0, .0, .0)
			self.radius = 1.0
			self.material = material.Material()

	# The intersection function can be found at Peter Shirley's Realistic Ray Tracing
	def intersect(self, my_ray, inter_rec):
		eo = self.center - my_ray.origin
		v = glm.dot(eo, my_ray.direction)
		disc = (self.radius * self.radius) - (glm.dot(eo, eo) - (v * v))

		if disc < 0.0:
			return False
		else:
			d = sqrt(disc)
			t1 = v - d
			t2 = v + d

		if t1 > 0.00001:
			inter_rec.t = t1
		else:
			inter_rec.t = t2

		inter_rec.position = my_ray.origin + inter_rec.t * my_ray.direction
		inter_rec.normal = glm.normalize(inter_rec.position - self.center)
		inter_rec.material = self.material

		return True
