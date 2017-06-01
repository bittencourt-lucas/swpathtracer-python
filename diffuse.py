# -*- coding: utf-8 -*-

import material
import glm
import math
from random import random

class Diffuse(material.Material):
	"""
	Diffuse ( name (string), emittance (vec3), brdf (vec3) )
	The material is diffuse.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.brdf = kwargs.get('brdf', glm.vec3(.0, .0, .0))
		elif args:
			self.brdf = args
		else:
			self.brdf = glm.vec3(.0, .0, .0)
		self.brdf = self.brdf / math.pi
		self.name = "Diffuse"
		self.emittance = glm.vec3(.0, .0, .0)

	def getFr(self, wi, wo):
		return self.brdf * wo.y * 2.0 * math.pi

	def bounce(self, wi):
		theta = math.acos(1 - random())
		phi = 2 * math.pi * random()
		r = 1
		direction = glm.vec3(r * math.sin(theta) * math.cos(phi), r * math.cos(theta), r * math.sin(theta) * math.sin(phi))
		return direction

	def getEmittance(self):
		return self.emittance