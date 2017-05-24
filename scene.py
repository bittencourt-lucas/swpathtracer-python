# -*- coding: utf-8 -*-

import glm
import sphere
import triangle
import models
import intersection_record as ir

class Scene(object):
	"""
	Scene
	This is where we'll create our scene. It's possible to hardcode some polygons in here.
	Some examples are provided on the load function.
	"""
	def __init__(self):
		self.primitives = []

	# Intersects all of the primitives on the scene
	def intersect(self, my_ray, inter_rec):
		intersection_result = False
		tmp_intersection_record = ir.IntersectionRecord()
		num_primitives = len(self.primitives)

		for primitive_id in range(num_primitives):
			if self.primitives[primitive_id].intersect(my_ray, tmp_intersection_record):
				if tmp_intersection_record.t < inter_rec.t and tmp_intersection_record.t > 0.0:
					inter_rec.t = tmp_intersection_record.t
					inter_rec.color = tmp_intersection_record.color
					intersection_result = True

		return intersection_result

	def create_model(self, model, position):
		if model.done:
			for index in range(len(model.triangles)):
				self.primitives.append(triangle.Triangle(position + model.triangles[index].vertex1, position + model.triangles[index].vertex2, position + model.triangles[index].vertex3))

	def load(self):
		# Blender Monkey
		# load_model = models.Models("CornellBox-Original.obj")
		# self.create_model(load_model, glm.vec3(0.0, 0.0, -2.0))

		# First Scene: FOUR SPHERE
		# self.primitives.append(sphere.Sphere(glm.vec3(0.0, 0.0, 0.0), 0.2))
		# self.primitives.append(sphere.Sphere(glm.vec3(-0.5, 0.0, -1.0), 0.2))
		# self.primitives.append(sphere.Sphere(glm.vec3(0.0, -0.5, -2.0), 0.2))
		# self.primitives.append(sphere.Sphere(glm.vec3(0.0, 0.5, -3.0), 0.2))

		# Second Scene: TRIFORCE
		# self.primitives.append(triangle.Triangle(glm.vec3(0.0, 0.6, -2.0), glm.vec3(-0.2, 0.3, -2.0), glm.vec3(0.2, 0.3, -2.0)))
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -2.0), glm.vec3(-0.4, 0.0, -2.0), glm.vec3(0.0, 0.0, -2.0)))
		# self.primitives.append(triangle.Triangle(glm.vec3(0.2, 0.3, -2.0), glm.vec3(0.0, 0.0, -2.0), glm.vec3(0.4, 0.0, -2.0)))

		# Third Scene: THE WIZARD
		# self.primitives.append(sphere.Sphere(glm.vec3(0.0, 0.5, -3.0), 0.2))
		# self.primitives.append(triangle.Triangle(glm.vec3(0.0, 1.0, -0.5), glm.vec3(-1.0, -2.0, -3.0), glm.vec3(1.0, -2.0, -3.0)))

		# Forth Scene: TRIANGLES
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -1.0), glm.vec3(-0.4, 0.0, -1.0), glm.vec3(0.0, 0.0, -1.0)))
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -1.5), glm.vec3(-0.4, 0.0, -1.5), glm.vec3(0.0, 0.0, -1.5)))
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -2.0), glm.vec3(-0.4, 0.0, -2.0), glm.vec3(0.0, 0.0, -2.0)))
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -2.5), glm.vec3(-0.4, 0.0, -2.5), glm.vec3(0.0, 0.0, -2.5)))
		# self.primitives.append(triangle.Triangle(glm.vec3(-0.2, 0.3, -3.0), glm.vec3(-0.4, 0.0, -3.0), glm.vec3(0.0, 0.0, -3.0)))

		# Pathtracer Scene: CORNELL BOX WITH SPHERES
		# BACK
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.2, -2.5), glm.vec3(1.3, -1.2, -2.5), glm.vec3(-1.2, 1.3, -2.5), glm.vec3(1.0, 1.0, 1.0)))
		self.primitives.append(triangle.Triangle(glm.vec3(1.3, 1.3, -2.5), glm.vec3(1.3, -1.2, -2.5), glm.vec3(-1.2, 1.3, -2.5), glm.vec3(1.0, 1.0, 1.0)))
		# FLOOR
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.2, -2.5), glm.vec3(1.3, -1.2, -2.5), glm.vec3(-1.2, -1.0, -1.0), glm.vec3(1.0, 1.0, 1.0)))
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.0, -1.0), glm.vec3(1.3, -1.2, -2.5), glm.vec3(1.3, -1.0, -1.0), glm.vec3(1.0, 1.0, 1.0)))
 		# LEFT WALL
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.2, -2.5), glm.vec3(-1.2, -1.0, -1.0), glm.vec3(-1.1999, 1.3, -2.5), glm.vec3(1.0, 0.0, 0.0)))
		self.primitives.append(triangle.Triangle(glm.vec3(-1.1999, 1.3, -2.5), glm.vec3(-1.2, -1.0, -1.0), glm.vec3(-1.2, 1.3, -1.0), glm.vec3(1.0, 0.0, 0.0)))
		# RIGHT WALL
		self.primitives.append(triangle.Triangle(glm.vec3(1.2999, 1.3, -2.5), glm.vec3(1.3, -1.0, -1.0), glm.vec3(1.3, -1.2, -2.5), glm.vec3(0.0, 1.0, 0.0)))
		self.primitives.append(triangle.Triangle(glm.vec3(1.2999, 1.3, -2.5), glm.vec3(1.3, -1.0, -1.0), glm.vec3(1.3, 1.3001, -1.0), glm.vec3(0.0, 1.0, 0.0)))
		# CEILING
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, 1.3001, -1.0), glm.vec3(-1.1999, 1.3, -2.5), glm.vec3(1.2999, 1.3, -2.5), glm.vec3(1.0, 1.0, 1.0)))
		self.primitives.append(triangle.Triangle(glm.vec3(1.2999, 1.3001, -2.5), glm.vec3(1.3, 1.2999, -1.0), glm.vec3(-1.2, 1.2999, -1.0), glm.vec3(1.0, 1.0, 1.0)))
		# SPHERES
		self.primitives.append(sphere.Sphere(glm.vec3(-0.5, -0.65, -1.5), 0.4, glm.vec3(1.0, 1.0, 1.0)))
		self.primitives.append(sphere.Sphere(glm.vec3(0.6, -0.65, -1.8), 0.4, glm.vec3(1.0, 1.0, 1.0)))
