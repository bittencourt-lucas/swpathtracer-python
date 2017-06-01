# -*- coding: utf-8 -*-

import glm
import material
from random import random
from math import pi

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
			self.material = kwargs.get('material', material.Material())
		elif args:
			self.vertex1, self.vertex2, self.vertex3, self.material = args
		else:
			self.vertex1 = glm.vec3(.0, .0, .0)
			self.vertex2 = glm.vec3(.0, .0, .0)
			self.vertex3 = glm.vec3(.0, .0, .0)
			self.material = material.Material()

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

		ei_minus_hf = float(e * i - h * f)
		gf_minus_di = float(g * f - d * i)
		dh_minus_eg = float(d * h - e * g)
		ak_minus_jb = float(a * k - j * b)
		jc_minus_al = float(j * c - a * l)
		bl_minus_kc = float(b * l - k * c)


		M = a * (ei_minus_hf) + b * (gf_minus_di) + c * (dh_minus_eg)

		t = -(f * (ak_minus_jb) + e * (jc_minus_al) + d * (bl_minus_kc)) / M

		if t < 0.0:
			return False

		gamma = (i * (ak_minus_jb) + h * (jc_minus_al) + g * (bl_minus_kc)) / M

		if gamma < 0.0 or gamma > 1.0:
			return False

		beta = (j * (ei_minus_hf) + k * (gf_minus_di) + l * (dh_minus_eg)) / M

		if beta < 0.0 or beta > 1.0 - gamma:
			return False

		inter_rec.t = t
		inter_rec.position = my_ray.origin + inter_rec.t * my_ray.direction
		inter_rec.normal = glm.normalize(glm.cross(self.vertex2 - self.vertex1, self.vertex3 - self.vertex1))
		if glm.dot(inter_rec.normal, my_ray.direction) > 0:
			inter_rec.normal = -inter_rec.normal
		inter_rec.material = self.material

		return True