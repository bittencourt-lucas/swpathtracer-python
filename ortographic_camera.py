# -*- coding: utf-8 -*-

import glm
import ray
import camera

class OrtographicCamera(camera.Camera):
	"""
	OrtographicCamera
	This inherits from the Camera class, and it'll create an Ortographic
	Camera, which will render a scene without depth or 3D perspective.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.min_x = kwargs.get('min_x', 0.0)
			self.max_x = kwargs.get('max_x', 0.0)
			self.min_y = kwargs.get('min_y', 0.0)
			self.max_y = kwargs.get('max_y', 0.0)
			self.camera = kwargs.get('camera', camera.Camera(glm.ivec2(0, 0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0)))	
		elif args:
			self.min_x, self.max_x, self.min_y, self.max_y, self.camera = args
		else:
			self.min_x = 0.0
			self.max_x = 0.0
			self.min_y = 0.0
			self.max_y = 0.0
			self.camera = camera.Camera(glm.ivec2(0, 0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0))

	# This will send "rays" from the scene to the camera
	def getWorldSpaceRay(self, pixel_coord):
		width = self.max_x - self.min_x
		height = self.max_y - self.min_y
		origin = glm.vec3(pixel_coord.x / float(self.camera.resolution.x) * width + self.min_x, (pixel_coord.y / float(self.camera.resolution.y) * height + self.min_y) * (-1), 0.0)

		return ray.Ray(self.camera.onb.multMatrixVec3(origin) + self.camera.position, glm.normalize(self.camera.onb.multMatrixVec3(glm.vec3(0.0, 0.0, -1.0))))