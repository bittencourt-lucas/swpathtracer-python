# -*- coding: utf-8 -*-

import glm

class Buffer(object):
	"""docstring for Buffer"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.h_resolution = kwargs.get('h_resolution', 512)
			self.v_resolution = kwargs.get('v_resolution', 512)
		elif args:
			self.h_resolution, self.v_resolution = args
		else:
			self.h_resolution = 512
			self.v_resolution = 512
		self.buffer_data = [[glm.vec3(.0, .0, .0) for i in range(self.h_resolution)] for j in range(self.v_resolution)]

	def save(self, filename):
		rendering_file = open(filename, "w")

		with open(filename, "a") as rendering_file:
			rendering_file.write("P3\n")
			rendering_file.write("{} {}\n".format(self.h_resolution, self.v_resolution))
			rendering_file.write("255\n")

			for i in range(self.h_resolution):
				for j in range(self.v_resolution):
					rendering_file.write("{} ".format(int(clamp(self.buffer_data[i][j].x) * 255.0 + 0.5)))
					rendering_file.write("{} ".format(int(clamp(self.buffer_data[i][j].y) * 255.0 + 0.5)))
					rendering_file.write("{} ".format(int(clamp(self.buffer_data[i][j].z) * 255.0 + 0.5)))

		rendering_file.close()

def clamp(x):
	if x < 0.0:
		return 0.0
	elif x > 1.0:
		return 1.0
	else:
		return x