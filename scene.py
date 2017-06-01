# -*- coding: utf-8 -*-

import glm
import sphere
import triangle
import models
import material
import light
import diffuse
import mirror
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
					inter_rec.position = tmp_intersection_record.position
					inter_rec.normal = tmp_intersection_record.normal
					inter_rec.material = tmp_intersection_record.material
					intersection_result = True

		return intersection_result

	def create_model(self, model, position):
		if model.done:
			for index in range(len(model.triangles)):
				self.primitives.append(triangle.Triangle(position + model.triangles[index].vertex1, position + model.triangles[index].vertex2, position + model.triangles[index].vertex3, diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))

	def load(self):
		# 3D Model Loader
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
		self.primitives.append(triangle.Triangle(glm.vec3(1.2, -1.2, -2.5), glm.vec3(-1.2, 1.2, -2.5), glm.vec3(-1.2, -1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
		self.primitives.append(triangle.Triangle(glm.vec3(1.2, -1.2, -2.5), glm.vec3(1.2, 1.2, -2.5), glm.vec3(-1.2, 1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
		# FLOOR
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.2, -2.5), glm.vec3(1.2, -1.2, -2.5), glm.vec3(-1.2, -1.0, -1.0), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.0, -1.0), glm.vec3(1.2, -1.2, -2.5), glm.vec3(1.2, -1.0, -1.0), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
 		# LEFT WALL
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, -1.2, -2.5), glm.vec3(-1.2, -1.0, -1.0), glm.vec3(-1.2, 1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.14, 0.45, 0.091))))
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, 1.2, -2.5), glm.vec3(-1.2, -1.0, -1.0), glm.vec3(-1.2, 1.2, -1.0), diffuse.Diffuse(brdf=glm.vec3(0.14, 0.45, 0.091))))
		# RIGHT WALL
		self.primitives.append(triangle.Triangle(glm.vec3(1.2, 1.2, -1.0), glm.vec3(1.2, -1.0, -1.0), glm.vec3(1.2, 1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.63, 0.065, 0.05))))
		self.primitives.append(triangle.Triangle(glm.vec3(1.2, 1.2, -2.5), glm.vec3(1.2, -1.0, -1.0), glm.vec3(1.2, -1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.63, 0.065, 0.05))))
		# CEILING
		self.primitives.append(triangle.Triangle(glm.vec3(-1.2, 1.2, -1.0), glm.vec3(-1.2, 1.2, -2.5), glm.vec3(1.2, 1.2, -2.5), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
		self.primitives.append(triangle.Triangle(glm.vec3(1.2, 1.2, -2.5), glm.vec3(1.2, 1.2, -1.0), glm.vec3(-1.2, 1.2, -1.0), diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))
		# LIGHT
		self.primitives.append(triangle.Triangle(glm.vec3(-0.5, 1.19, -1.5), glm.vec3(-0.5, 1.19, -2.0), glm.vec3(0.5, 1.19, -2.0), light.Light(emittance=glm.vec3(30.0, 30.0, 30.0))))
		self.primitives.append(triangle.Triangle(glm.vec3(0.5, 1.19, -2.0), glm.vec3(0.5, 1.19, -1.5), glm.vec3(-0.5, 1.19, -1.5), light.Light(emittance=glm.vec3(30.0, 30.0, 30.0))))
		# SPHERES
		self.primitives.append(sphere.Sphere(glm.vec3(-0.5, -0.65, -1.5), 0.4, mirror.Mirror()))
		self.primitives.append(sphere.Sphere(glm.vec3(0.6, -0.65, -1.8), 0.4, diffuse.Diffuse(brdf=glm.vec3(0.725, 0.71, 0.68))))