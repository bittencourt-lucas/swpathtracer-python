# -*- coding: utf-8 -*-

import glm
from random import random
from math import sqrt

class Sphere(object):
	"""
	Sphere ( center (vec3), radius )
	Creates spheres on the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.center = kwargs.get('center', glm.vec3(.0, .0, .0))
			self.radius = kwargs.get('radius', 0.0)
			self.color = kwargs.get('color', glm.vec3(.0, .0, .0))
		elif args:
			self.center, self.radius, self.color = args
		else:
			self.center = glm.vec3(.0, .0, .0)
			self.radius = 1.0
			self.color = glm.vec3(.0, .0, .0)

		# RANDOM COLOR GENERATOR
		# self.color = glm.vec3(((random() * 255) % 255) / 255.0, ((random() * 255) % 255) / 255.0, ((random() * 255) % 255) / 255.0)

	# The intersection function can be found at Peter Shirley's Realistic Ray Tracing
	def intersect(self, my_ray, inter_rec):
		eo = (my_ray.origin * (-1)) + self.center
		v = glm.dot(eo, my_ray.direction)
		disc = (self.radius ** 2) - (glm.dot(eo, eo) - (v ** 2))

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

		inter_rec.position = my_ray.direction * (my_ray.origin + inter_rec.t)
		inter_rec.normal = glm.normalize(inter_rec.position - self.center)
		inter_rec.color = self.color

		return True
