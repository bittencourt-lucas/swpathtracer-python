# -*- coding: utf-8 -*-

import glm

class Triangle(object):
	"""
	Triangle ( vertex1 (vec3), vertex2 (vec3), vertex3 (vec3) )
	Creates triangles on the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.vertex1 = kwargs.get('vertex1', glm.vec3(.0, .0, .0))
			self.vertex2 = kwargs.get('vertex2', glm.vec3(.0, .0, .0))
			self.vertex3 = kwargs.get('vertex3', glm.vec3(.0, .0, .0))
		elif args:
			self.vertex1, self.vertex2, self.vertex3 = args
		else:
			self.vertex1 = glm.vec3(.0, .0, .0)
			self.vertex2 = glm.vec3(.0, .0, .0)
			self.vertex3 = glm.vec3(.0, .0, .0)

	# The intersection function can be found at Peter Shirley's Realistic Ray Tracing
	def intersect(self, my_ray, inter_rec):
		a = self.vertex1.x - self.vertex2.x
		b = self.vertex1.y - self.vertex2.y
		c = self.vertex1.z - self.vertex2.z
		d = self.vertex1.x - self.vertex3.x
		e = self.vertex1.y - self.vertex3.y
		f = self.vertex1.z - self.vertex3.z
		g = my_ray.direction.x
		h = my_ray.direction.y
		i = my_ray.direction.z
		j = self.vertex1.x - my_ray.origin.x
		k = self.vertex1.y - my_ray.origin.y
		l = self.vertex1.z - my_ray.origin.z

		M = a * (e * i - h * f) + b * (g * f - d * i) + c * (d * h - e * g)
		t = -(f * (a * k - j * b) + e * (j * c - a * l) + d * (b * l - k * c)) / M

		if t < 0.0:
			return False

		gamma = (i * (a * k - j * b) + h * (j * c - a * l) + g * (b * l - k * c)) / M

		if gamma < 0.0 or gamma > 1.0:
			return False

		beta = (j * (e * i - h * f) + k * (g * f - d * i) + l * (d * h - e * g)) / M

		if beta < 0.0 or beta > (1.0 - gamma):
			return False

		center = glm.vec3((self.vertex1.x + self.vertex2.x + self.vertex3.x) / 3.0,
			(self.vertex1.y + self.vertex2.y + self.vertex3.y) / 3.0,
			(self.vertex1.z + self.vertex2.z + self.vertex3.z) / 3.0)

		inter_rec.t = t
		inter_rec.position = my_ray.origin + my_ray.direction * inter_rec.t
		inter_rec.normal = glm.normalize(inter_rec.position - center)

		return True