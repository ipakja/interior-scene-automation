"""
Blender Script: Interior Scene Generator
Creates complete photorealistic scene automatically.
Usage: Scripting → Open → Run Script → F12
"""

import bpy

# Reset scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Material helper
def mat(name, color, metallic=0, roughness=0.5, transmission=0):
    m = bpy.data.materials.new(name=name)
    m.use_nodes = True
    # Ensure Principled BSDF exists
    if 'Principled BSDF' not in m.node_tree.nodes:
        bsdf = m.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
    else:
        bsdf = m.node_tree.nodes['Principled BSDF']
    bsdf.inputs['Base Color'].default_value = (*color, 1)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = roughness
    # Transmission - use correct input name for Blender 4.x
    if 'Transmission Weight' in bsdf.inputs:
        bsdf.inputs['Transmission Weight'].default_value = transmission
    elif 'Transmission' in bsdf.inputs:
        bsdf.inputs['Transmission'].default_value = transmission
    return m

# Create materials
wood = mat('Wood', (0.25, 0.15, 0.1), 0, 0.7)
fabric = mat('Fabric', (0.9, 0.85, 0.75), 0, 0.9)
metal = mat('Metal', (0.7, 0.7, 0.75), 1, 0.1)
glass = mat('Glass', (0.9, 0.95, 1.0), 0, 0, 1)
wall = mat('Wall', (0.95, 0.95, 0.95), 0, 0.8)

# Room
bpy.ops.mesh.primitive_plane_add(size=10, location=(0,0,0))
bpy.context.active_object.name = 'Floor'
bpy.context.active_object.data.materials.append(wood)

for pos, rot, name in [
    ((0,-5,2.5), (1.5708,0,0), 'Back'),
    ((-5,0,2.5), (1.5708,0,1.5708), 'Left'),
    ((5,0,2.5), (1.5708,0,1.5708), 'Right'),
    ((0,0,5), (3.14159,0,0), 'Ceiling')
]:
    bpy.ops.mesh.primitive_plane_add(size=10, location=pos)
    obj = bpy.context.active_object
    obj.name = name + '_Wall'
    obj.rotation_euler = rot
    obj.data.materials.append(wall)

# Sofa
for scale, loc, name in [
    ((1.5,0.8,0.4), (0,-2,0.4), 'Base'),
    ((1.5,0.2,0.6), (0,-2.2,1.0), 'Back'),
    ((0.2,0.8,0.5), (-1.5,-2,0.6), 'Arm_L'),
    ((0.2,0.8,0.5), (1.5,-2,0.6), 'Arm_R')
]:
    bpy.ops.mesh.primitive_cube_add(size=2, location=loc)
    obj = bpy.context.active_object
    obj.name = 'Sofa_' + name
    obj.scale = scale
    obj.data.materials.append(fabric)

# Table
bpy.ops.mesh.primitive_cube_add(size=2, location=(0,-3.5,0.8))
bpy.context.active_object.name = 'Table_Top'
bpy.context.active_object.scale = (1, 0.6, 0.05)
bpy.context.active_object.data.materials.append(glass)

for x, y in [(-0.8,-3.7), (0.8,-3.7), (-0.8,-3.3), (0.8,-3.3)]:
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.8, location=(x,y,0.4))
    bpy.context.active_object.data.materials.append(metal)

# Lighting
bpy.ops.object.light_add(type='AREA', location=(0,2,4))
bpy.context.active_object.data.energy = 100
bpy.context.active_object.data.size = 3
bpy.context.active_object.rotation_euler = (-0.785, 0, 0)

bpy.ops.object.light_add(type='AREA', location=(-3,1,3))
bpy.context.active_object.data.energy = 50
bpy.context.active_object.data.size = 2

# World
world = bpy.context.scene.world
world.use_nodes = True
bg = world.node_tree.nodes.new('ShaderNodeBackground')
bg.inputs['Color'].default_value = (0.8, 0.85, 0.9, 1)
bg.inputs['Strength'].default_value = 0.5
# Ensure World Output exists
if 'World Output' not in world.node_tree.nodes:
    output = world.node_tree.nodes.new('ShaderNodeOutputWorld')
else:
    output = world.node_tree.nodes['World Output']
world.node_tree.links.new(bg.outputs['Background'], output.inputs['Surface'])

# Camera
bpy.ops.object.camera_add(location=(3,-6,1.6))
camera = bpy.context.active_object
camera.rotation_euler = (1.4, 0, 0.785)
bpy.context.scene.camera = camera
camera.data.lens = 35

# Render setup - 4K Quality
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.render.resolution_x, scene.render.resolution_y = 3840, 2160  # 4K UHD
scene.render.resolution_percentage = 100
scene.cycles.samples = 512  # Higher quality for 4K
scene.cycles.use_denoising = True
scene.cycles.denoiser = 'OPENIMAGEDENOISE'
scene.cycles.use_adaptive_sampling = True  # Optimize render time
scene.cycles.adaptive_threshold = 0.01
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGBA'
scene.render.image_settings.color_depth = '16'  # 16-bit for better quality

print('=' * 50)
print('✓ Scene created successfully!')
print('Press F12 to render.')
print('=' * 50)

