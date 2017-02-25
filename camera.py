# -*- coding: utf-8 -*-

import glm
import onb
import ray

class Camera(object):
	"""docstring for Camera"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.resolution = kwargs.get('resolution', glm.ivec2(0, 0))
			self.position = kwargs.get('position', glm.vec3(.0, .0, .0))
			self.up = kwargs.get('up', glm.vec3(.0, .0, .0))
			self.look_at = kwargs.get('look_at', glm.vec3(.0, .0, .0))
		elif args:
			self.resolution, self.position, self.up, self.look_at = args
		else:
			self.resolution = glm.ivec2(0, 0)
			self.position = glm.vec3(.0, .0, .0)
			self.up = glm.vec3(.0, .0, .0)
			self.look_at = glm.vec3(.0, .0, .0)
		self.direction = glm.normalize((self.look_at - self.position))
		self.onb_cam = onb.ONB()
		self.onb_cam.setFromUW(glm.normalize(glm.cross(self.up, self.direction * (-1))), self.direction * (-1))