# -*- coding: utf-8 -*-

import glm
import ray
import camera

class PerspectiveCamera(camera.Camera):
	"""
	PerspectiveCamera
	This inherits from the Camera class, and it'll create an Perspective
	Camera, which will render a scene with 3D perspective.
	"""
	def __init__(self, *args, **kwargs):
		if kwargs:
			self.min_x = kwargs.get('min_x', 0.0)
			self.max_x = kwargs.get('max_x', 0.0)
			self.min_y = kwargs.get('min_y', 0.0)
			self.max_y = kwargs.get('max_y', 0.0)
			self.distance = kwargs.get('distance', 0.0)
			self.camera = kwargs.get('camera', camera.Camera(glm.ivec2(0, 0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0)))	
		elif args:
			self.min_x, self.max_x, self.min_y, self.max_y, self.distance, self.camera = args
		else:
			self.min_x = 0.0
			self.max_x = 0.0
			self.min_y = 0.0
			self.max_y = 0.0
			self.distance = 0.0
			self.camera = camera.Camera(glm.ivec2(0, 0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0), glm.vec3(.0, .0, .0))

	def getWorldSpaceRay(self, pixel_coord):
		u = self.max_x - self.min_x
		v = -(self.max_y - self.min_y)
		w = -self.distance

		cam_x = (pixel_coord.x) / float(self.camera.resolution.x)
		cam_y = (pixel_coord.y) / float(self.camera.resolution.y)

		cam_vec = glm.vec3(cam_x * u + self.min_x, cam_y * v - self.min_y, w)

		return ray.Ray(self.camera.position, glm.normalize(self.camera.onb.multMatrixVec3(cam_vec)))