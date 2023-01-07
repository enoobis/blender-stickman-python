import bpy
import math


# Create a new material
red = bpy.data.materials.new(name="red")
green = bpy.data.materials.new(name="green")
blue = bpy.data.materials.new(name="blue")

# Set the diffuse color of the material
red.diffuse_color = (1, 0, 0, 1)  # red color
green.diffuse_color = (0, 1, 0, 1)  # green color
blue.diffuse_color = (0, 0, 1, 1)  # blue color

# Create the head
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 5))
head = bpy.context.active_object
head.data.materials.append(red)

# Create the torso
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 2))
torso = bpy.context.active_object
torso.scale = (1, 0.5, 2)
torso.data.materials.append(green)

# Create the legs
bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=3, location=(-0.5, 0, -1))
leg1 = bpy.context.active_object
leg1.scale = (0.5, 0.5, 1)
leg1.data.materials.append(blue)

bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=3, location=(0.5, 0, -1))
leg2 = bpy.context.active_object
leg2.scale = (0.5, 0.5, 1)
leg2.data.materials.append(blue)

# Create the arms
bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=2, location=(-1, 1, 2))
arm1 = bpy.context.active_object
arm1.scale = (1, 1, 1.5)
arm1.rotation_euler = (45 * (math.pi / 180), 0, 0)
arm1.data.materials.append(blue)

bpy.ops.mesh.primitive_cylinder_add(radius=0.25, depth=2, location=(1, 1, 2))
arm2 = bpy.context.active_object
arm2.scale = (1, 1, 1.5)
arm2.rotation_euler = (45 * (math.pi / 180), 0, 0)
arm2.data.materials.append(blue)