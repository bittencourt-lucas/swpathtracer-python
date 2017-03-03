# swpathtracer-python

The Template for this program was made by Prof. PhD. Christian Azambuja Pagot, and it can be found here:
https://github.com/capagot/RT-Template

glm.py is based on GLM (OpenGL Mathematics) library which can be found here:
http://glm.g-truc.net/0.9.8/index.html

UPDATE 1.0: Ortographic Camera capable of rendering spheres.

UPDATE 1.1: The Ortographic Camera can now render triangles.

UPDATE 2.0: Perspective Camera added.

UPDATE 3.0: Can now render 3D Models with gray scales based on depth.

BUG FIX 3.1: Fixed a bug on intersection (rays were intersecting the last primitive added, instead of the closest one).

UPDATE 3.1: Now renders with random colors on each primitive.


Using this program:

First, you need the following Python libs:

pyassimp

pygame

numpy


Clone all files and run the following command on a Terminal (or any Python3 interpreter):

python3 swpathtracer-python