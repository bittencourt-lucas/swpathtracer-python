# -*- coding: utf-8 -*-

import triangle
import glm
import pyassimp
import pyassimp.postprocess

class Models(object):
	"""
	Models
	"""
	def __init__(self, filename):
		self.filename = filename
		self.done = False

		self.triangles = []
		scene = pyassimp.load(self.filename, pyassimp.postprocess.aiProcess_Triangulate)

		if scene:
			for index, mesh in enumerate(scene.meshes):
				for num in range(len(mesh.faces)):
					face = mesh.faces[num]
					if face.size == 3:
						vertex = [glm.vec3(), glm.vec3(), glm.vec3()]
						vertex[0].x = mesh.vertices[face[0], 0]
						vertex[0].y = mesh.vertices[face[0], 1]
						vertex[0].z = mesh.vertices[face[0], 2]
						vertex[1].x = mesh.vertices[face[1], 0]
						vertex[1].y = mesh.vertices[face[1], 1]
						vertex[1].z = mesh.vertices[face[1], 2]
						vertex[2].x = mesh.vertices[face[2], 0]
						vertex[2].y = mesh.vertices[face[2], 1]
						vertex[2].z = mesh.vertices[face[2], 2]
						self.triangles.append(triangle.Triangle(glm.vec3(vertex[0].x, vertex[0].y, vertex[0].z), glm.vec3(vertex[1].x, vertex[1].y, vertex[1].z), glm.vec3(vertex[2].x, vertex[2].y, vertex[2].z)))

			self.done = True