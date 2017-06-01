# -*- coding: utf-8 -*-

import glm
import onb
import ray

class Camera(object):
	"""
	Camera ( resolution(ivec2), position(vec3), up(vec3), look_at(vec3) )
	This is a general Camera, we'll be using the Ortographic
	(and later the Perspective) Camera classes to handle the
	camera.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.resolution = kwargs.get('resolution', glm.ivec2(0, 0))
			self.position = kwargs.get('position', glm.vec3(.0, .0, .0))
			self.up = kwargs.get('up', glm.vec3(.0, 1.0, .0))
			self.look_at = kwargs.get('look_at', glm.vec3(.0, .0, -1.0))
		elif args:
			self.resolution, self.position, self.up, self.look_at = args
		else:
			self.resolution = glm.ivec2(0, 0)
			self.position = glm.vec3(.0, .0, .0)
			self.up = glm.vec3(.0, 1.0, .0)
			self.look_at = glm.vec3(.0, .0, -1.0)

		# Camera direction
		self.direction = glm.normalize((self.look_at - self.position))

		# The camera uses an orthonormal basis
		self.onb = onb.ONB()
		self.onb.setFromUW(glm.normalize(glm.cross(self.up, -self.direction)), -self.direction)

	# "Virtual" method for the Camera class
	def getWorldSpaceRay(self, pixel_coord):
		pass