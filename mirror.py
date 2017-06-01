# -*- coding: utf-8 -*-

import material
import glm

class Mirror(material.Material):
	"""
	Mirror ( name (string), emittance (vec3), brdf (vec3) )
	The material is a mirror.
	"""
	def __init__(self):
		self.emittance = glm.vec3(.0, .0, .0)
		self.name = "Mirror"
		self.brdf = glm.vec3(.0, .0, .0)

	def getFr(self, wi, wo):
		return glm.vec3(1.0, 1.0, 1.0)

	def bounce(self, wi):
		return glm.vec3(-wi.x, wi.y, -wi.z)

	def getEmittance(self):
		return self.emittance