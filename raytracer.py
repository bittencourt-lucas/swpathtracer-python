# -*- coding: utf-8 -*-

import glm
import camera
import buffer
import scene
import ray
import intersection_record as ir
import sys

class RayTracer(object):
	"""
	RayTracer ( camera (Camera), scene (Scene), bg_color (vec3), buffer(Buffer) )
	This is where the images will be rendered! This class will integrate everything
	that has been done by tracing the rays and detecting if there are objects on
	the scene.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.camera = kwargs.get('camera', camera.Camera()) 
			self.scene = kwargs.get('scene', scene.Scene())
			self.background_color = kwargs.get('background_color', glm.vec3(.0, .0, .0))
			self.buffer = kwargs.get('buffer', buffer.Buffer())
		elif args:
			self.camera, self.scene, self.background_color, self.buffer = args
		else:
			self.camera = camera.Camera()
			self.scene = scene.Scene()
			self.background_color = glm.vec3(.0, .0, .0)
			self.buffer = buffer.Buffer()

	# This will render the image
	def integrate(self):
		inter_rec = ir.IntersectionRecord()
		for y in range(self.buffer.v_resolution):

			# In order to watch the progress of the rendering, a percentage will be displayed
			# as the image is created
			progress = "Progress: {:0.1f}%".format(100.0 * y / (self.buffer.v_resolution - 1))
			sys.stdout.write(progress)
			backspace(len(progress))
			sys.stdout.flush()
			for x in range(self.buffer.h_resolution):
				inter_rec.t = sys.float_info.max
				my_ray = self.camera.getWorldSpaceRay(glm.vec2(x + 0.5, y + 0.5))
				if self.scene.intersect(my_ray, inter_rec):
					inter_rec = self.scene.color(my_ray, inter_rec)
					self.buffer.buffer_data[x][y] = glm.vec3(inter_rec.t * 0.2, inter_rec.t * 0.2, inter_rec.t * 0.2)
		print("\nDONE!", file=sys.stderr)

# This function is merely updating the progress text on the Terminal
def backspace(n):
    print('\r' * n, end='')