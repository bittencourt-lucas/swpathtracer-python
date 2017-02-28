# -*- coding: utf-8 -*-

import camera
import ortographic_camera as oc
import scene
import buffer
import raytracer
import glm

# Setting image resolution
x_res = 512
y_res = 512

# Creating the Ortographic Camera
cam_parameters = camera.Camera(glm.ivec2(x_res, y_res), glm.vec3(0.0, 0.0, 1.0), glm.vec3(0.0, 1.0, 0.0), glm.vec3(0.0, 0.0, -1.0))
my_camera = oc.OrtographicCamera(-1.25, 1.25, -1.25, 1.25, cam_parameters)

# Creating and loading hardcoded Scene
my_scene = scene.Scene()
my_scene.load()

# Starting to render the image will the objects
rendering_buffer = buffer.Buffer(x_res, y_res)
bg_color = glm.vec3(.0, .0, .0)
rt = raytracer.RayTracer(my_camera, my_scene, bg_color, rendering_buffer)
rt.integrate()

# Output file
rendering_buffer.save("output_image.ppm")