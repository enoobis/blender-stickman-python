# blender-stickman-python

This script demonstrates how to create a new material in Blender and assign it to an object using Python.

## Requirements

- Blender 2.90 or higher

## Usage

1. Open the script in Blender's text editor and run it.
2. The script will create a new material and assign it to the active object.

## Customization

You can customize the material by modifying the `diffuse_color` property in the script. The `diffuse_color` property specifies the RGB color of the material. You can also adjust other material properties as needed.

## Example

```python
import bpy

# Create a new material
mat = bpy.data.materials.new(name="MyMaterial")

# Set the diffuse color of the material
mat.diffuse_color = (1, 0, 0, 1)  # Red color

# Assign the material to the object
obj = bpy.context.active_object
obj.data.materials.append(mat)
