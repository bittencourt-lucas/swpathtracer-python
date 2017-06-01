# -*- coding: utf-8 -*-

import glm
import camera
import buffer
import scene
import ray
import intersection_record as ir
import sys
import math
import onb
import material
from random import random

class PathTracer(object):
	"""
	PathTracer ( camera (Camera), scene (Scene), bg_color (vec3), buffer(Buffer) )
	This is where the images will be rendered! This class will integrate everything
	that has been done by tracing the rays and detecting if there are objects on
	the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.camera = kwargs.get('camera', camera.Camera()) 
			self.scene = kwargs.get('scene', scene.Scene())
			self.background_color = kwargs.get('background_color', glm.vec3(.0, .0, .0))
			self.samples = kwargs.get('samples', 1)
			self.max_depth = kwargs.get('max_depth', 1)
			self.buffer = kwargs.get('buffer', buffer.Buffer())
		elif args:
			self.camera, self.scene, self.background_color, self.samples, self.max_depth, self.buffer = args
		else:
			self.camera = camera.Camera()
			self.scene = scene.Scene()
			self.background_color = glm.vec3(.0, .0, .0)
			self.samples = 1
			self.max_depth = 1
			self.buffer = buffer.Buffer()

	# Calculates the Radiance
	def L(self, my_ray, current_depth):
		Lo = glm.vec3(.0, .0, .0)
		inter_rec = ir.IntersectionRecord()
		if current_depth < self.max_depth:
			inter_rec.t = sys.float_info.max
			if self.scene.intersect(my_ray, inter_rec):

				if inter_rec.material.name == "Light":
					return inter_rec.material.getEmittance()

				tangent_to_universe_space = onb.ONB()
				tangent_to_universe_space.setFromV(inter_rec.normal)
				universe_to_tangent_space = onb.ONB()
				universe_to_tangent_space.setFromV(inter_rec.normal)
				universe_to_tangent_space.transpose()

				wi = universe_to_tangent_space.multMatrixVec3(-my_ray.direction)
				wo = inter_rec.material.bounce(wi)

				new_direction = tangent_to_universe_space.multMatrixVec3(wo)

				ref_ray = ray.Ray(inter_rec.position + (new_direction * 0.001), new_direction)

				current_depth += 1
				Lo = inter_rec.material.getEmittance() + inter_rec.material.getFr(wi, wo) * self.L(ref_ray, current_depth)

		return Lo


	# This will render the image
	def integrate(self):
		for y in range(self.buffer.v_resolution):

			# In order to watch the progress of the rendering, a percentage will be displayed
			# as the image is created
			progress = "Progress: {:0.1f}%".format(100.0 * y / (self.buffer.v_resolution - 1))
			sys.stdout.write(progress)
			backspace(len(progress))
			sys.stdout.flush()

			# Now rendering multiple samples per pixel (Antialiasing)
			for x in range(self.buffer.h_resolution):
				for sample in range(self.samples):
					my_ray = self.camera.getWorldSpaceRay(glm.vec2(x + random(), y + random()))
					self.buffer.buffer_data[x][y] = self.buffer.buffer_data[x][y] + self.L(my_ray, 0)
				self.buffer.buffer_data[x][y] = self.buffer.buffer_data[x][y] / self.samples
		print("\nDONE!", file=sys.stderr)

# This function is merely updating the progress text on the Terminal
def backspace(n):
    print('\r' * n, end='')