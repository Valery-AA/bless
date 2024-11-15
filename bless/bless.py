import bpy
import os
import json

# hooks found and implemented by michaeljared from this original gist:
# https://gist.github.com/bikemurt/0c36561a29527b98220230282ab11181


# https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_shape
class OMIPhysicsShape(bpy.types.PropertyGroup):
    # possibly needed for internal for gd3d
    is_collision: bpy.props.BoolProperty(default=False)  # type: ignore
    index: bpy.props.IntProperty(default=0, description="index of the physics shape")  # type: ignore
    shape_types: bpy.props.EnumProperty(
        name="",
        description="collider shape types",
        default="convex",
        items=[
            ("box", "Box", "", 1),
            ("sphere", "Sphere", "", 1 << 1),
            ("capsule", "Capsule", "", 1 << 2),
            ("cylinder", "Cylinder", "", 1 << 3),
            ("convex", "Convex", "", 1 << 4),
            ("trimesh", "Trimesh", "", 1 << 5)
        ])  # type: ignore
    size: bpy.props.FloatVectorProperty(subtype="XYZ_LENGTH", description="size of the shape in meters", default=[1.0, 1.0, 1.0])  # type: ignore
    radius: bpy.props.FloatProperty(subtype="DISTANCE", description="radius of the shape in meters", default=0.5)  # type: ignore
    height: bpy.props.FloatProperty(subtype="DISTANCE", description="height of the shape in meters", default=2.0)  # type: ignore
    # The index of the glTF mesh in the document to use as a mesh shape.
    mesh: bpy.props.IntProperty(default=-1)  # type: ignore


# https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body
class OMIPhysicsBody(bpy.types.PropertyGroup):
    shape_index: bpy.props.IntProperty(default=-1)  # type: ignore
    # https://github.com/omigroup/gltf-extensions/blob/main/extensions/2.0/OMI_physics_body/README.motion.md
    is_motion: bpy.props.BoolProperty(default=False)  # type: ignore
    # https://github.com/omigroup/gltf-extensions/blob/main/extensions/2.0/OMI_physics_body/README.trigger.md
    is_trigger: bpy.props.BoolProperty(default=False)  # type: ignore
    # https://github.com/omigroup/gltf-extensions/blob/main/extensions/2.0/OMI_physics_body/README.collider.md
    is_collision: bpy.props.BoolProperty(default=False)  # type: ignore

    motion_types: bpy.props.EnumProperty(
        name="Body Types",
        description="physics body types",
        default="static",
        items=[
            ("static", "Static", "", 1),
            ("dynamic", "Dynamic", "", 1 << 1),
            ("kinematic", "Kinematic", "", 1 << 2)
        ])  # type: ignore
    mass: bpy.props.FloatProperty(default=1.0)  # type: ignore
    linear_velocity: bpy.props.FloatVectorProperty(subtype="VELOCITY", default=[0.0, 0.0, 0.0])  # type: ignore
    angular_velocity: bpy.props.FloatVectorProperty(subtype="VELOCITY", default=[0.0, 0.0, 0.0])  # type: ignore
    center_of_mass: bpy.props.FloatVectorProperty(default=[0.0, 0.0, 0.0])  # type: ignore


# Default collision type for new objects.
class BlessDefaultCollisionType(bpy.types.PropertyGroup):
    collision_types: bpy.props.EnumProperty(
        name="Collision Type",
        description="Static level geometry.",
        default="trimesh",
        items=[
            ("trimesh", "Trimesh", "", 1),
            ("convex", "Convex", "", 1 << 1),
            ("custom", "Custom", "", 1 << 2),
            ("none", "None", "", 1 << 3),
        ])  # type: ignore


class BlessCollisionTypes(bpy.types.PropertyGroup):
    collision_types: bpy.props.EnumProperty(
        name="Collision Type",
        description="Static level geometry.",
        default="trimesh",
        items=[
            ("trimesh", "Trimesh", "", 1),
            ("convex", "Convex", "", 1 << 1),
            ("custom", "Custom", "", 1 << 2),
            ("none", "None", "", 1 << 3),
        ])  # type: ignore


# TODO, does this need to have so many lines? could be a factoryfunction to make each prop.
##

class BlessCollisionLayers(bpy.types.PropertyGroup):
    layer_1: bpy.props.BoolProperty(name="Layer 1", default=True)  # type: ignore
    layer_2: bpy.props.BoolProperty(name="Layer 2")  # type: ignore
    layer_3: bpy.props.BoolProperty(name="Layer 3")  # type: ignore
    layer_4: bpy.props.BoolProperty(name="Layer 4")  # type: ignore
    layer_5: bpy.props.BoolProperty(name="Layer 5")  # type: ignore
    layer_6: bpy.props.BoolProperty(name="Layer 6")  # type: ignore
    layer_7: bpy.props.BoolProperty(name="Layer 7")  # type: ignore
    layer_8: bpy.props.BoolProperty(name="Layer 8")  # type: ignore
    layer_9: bpy.props.BoolProperty(name="Layer 9")  # type: ignore
    layer_10: bpy.props.BoolProperty(name="Layer 10")  # type: ignore
    layer_11: bpy.props.BoolProperty(name="Layer 11")  # type: ignore
    layer_12: bpy.props.BoolProperty(name="Layer 12")  # type: ignore
    layer_13: bpy.props.BoolProperty(name="Layer 13")  # type: ignore
    layer_14: bpy.props.BoolProperty(name="Layer 14")  # type: ignore
    layer_15: bpy.props.BoolProperty(name="Layer 15")  # type: ignore
    layer_16: bpy.props.BoolProperty(name="Layer 16")  # type: ignore
    layer_17: bpy.props.BoolProperty(name="Layer 17")  # type: ignore
    layer_18: bpy.props.BoolProperty(name="Layer 18")  # type: ignore
    layer_19: bpy.props.BoolProperty(name="Layer 19")  # type: ignore
    layer_20: bpy.props.BoolProperty(name="Layer 20")  # type: ignore
    layer_21: bpy.props.BoolProperty(name="Layer 21")  # type: ignore
    layer_22: bpy.props.BoolProperty(name="Layer 22")  # type: ignore
    layer_23: bpy.props.BoolProperty(name="Layer 23")  # type: ignore
    layer_24: bpy.props.BoolProperty(name="Layer 24")  # type: ignore
    layer_25: bpy.props.BoolProperty(name="Layer 25")  # type: ignore
    layer_26: bpy.props.BoolProperty(name="Layer 26")  # type: ignore
    layer_27: bpy.props.BoolProperty(name="Layer 27")  # type: ignore
    layer_28: bpy.props.BoolProperty(name="Layer 28")  # type: ignore
    layer_29: bpy.props.BoolProperty(name="Layer 29")  # type: ignore
    layer_30: bpy.props.BoolProperty(name="Layer 30")  # type: ignore
    layer_31: bpy.props.BoolProperty(name="Layer 31")  # type: ignore
    layer_32: bpy.props.BoolProperty(name="Layer 32")  # type: ignore


class BlessCollisionMaskLayers(bpy.types.PropertyGroup):
    layer_1: bpy.props.BoolProperty(name="Layer 1", default=True)  # type: ignore
    layer_2: bpy.props.BoolProperty(name="Layer 2")  # type: ignore
    layer_3: bpy.props.BoolProperty(name="Layer 3")  # type: ignore
    layer_4: bpy.props.BoolProperty(name="Layer 4")  # type: ignore
    layer_5: bpy.props.BoolProperty(name="Layer 5")  # type: ignore
    layer_6: bpy.props.BoolProperty(name="Layer 6")  # type: ignore
    layer_7: bpy.props.BoolProperty(name="Layer 7")  # type: ignore
    layer_8: bpy.props.BoolProperty(name="Layer 8")  # type: ignore
    layer_9: bpy.props.BoolProperty(name="Layer 9")  # type: ignore
    layer_10: bpy.props.BoolProperty(name="Layer 10")  # type: ignore
    layer_11: bpy.props.BoolProperty(name="Layer 11")  # type: ignore
    layer_12: bpy.props.BoolProperty(name="Layer 12")  # type: ignore
    layer_13: bpy.props.BoolProperty(name="Layer 13")  # type: ignore
    layer_14: bpy.props.BoolProperty(name="Layer 14")  # type: ignore
    layer_15: bpy.props.BoolProperty(name="Layer 15")  # type: ignore
    layer_16: bpy.props.BoolProperty(name="Layer 16")  # type: ignore
    layer_17: bpy.props.BoolProperty(name="Layer 17")  # type: ignore
    layer_18: bpy.props.BoolProperty(name="Layer 18")  # type: ignore
    layer_19: bpy.props.BoolProperty(name="Layer 19")  # type: ignore
    layer_20: bpy.props.BoolProperty(name="Layer 20")  # type: ignore
    layer_21: bpy.props.BoolProperty(name="Layer 21")  # type: ignore
    layer_22: bpy.props.BoolProperty(name="Layer 22")  # type: ignore
    layer_23: bpy.props.BoolProperty(name="Layer 23")  # type: ignore
    layer_24: bpy.props.BoolProperty(name="Layer 24")  # type: ignore
    layer_25: bpy.props.BoolProperty(name="Layer 25")  # type: ignore
    layer_26: bpy.props.BoolProperty(name="Layer 26")  # type: ignore
    layer_27: bpy.props.BoolProperty(name="Layer 27")  # type: ignore
    layer_28: bpy.props.BoolProperty(name="Layer 28")  # type: ignore
    layer_29: bpy.props.BoolProperty(name="Layer 29")  # type: ignore
    layer_30: bpy.props.BoolProperty(name="Layer 30")  # type: ignore
    layer_31: bpy.props.BoolProperty(name="Layer 31")  # type: ignore
    layer_32: bpy.props.BoolProperty(name="Layer 32")  # type: ignore


# TODO rework this as an operator to call from the panel rather than ins

class BlessApplyCollisions(bpy.types.Operator):
    """Apply Props"""
    bl_idname = "object.gd3d_apply_collisions"
    bl_label = "Apply Multiple Collisions"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if not isinstance(context.selected_objects, list):
            self.report({'ERROR'}, "No objects selected or selection is invalid.")
            return {'CANCELLED'}

        collision_type = context.object.collision_types.collision_types
        tools = context.window_manager.bless_tools

        for obj in context.selected_objects:
            # set attribute, not custom property
            obj.collision_types.collision_types = collision_type

            # Set the visual feedback
            obj.display_type = 'SOLID'
            obj.show_wire = True  # Optional: show wireframe for better visibility
            if collision_type == "trimesh":
                obj.color = tools.trimesh_color
            elif collision_type == "convex":
                obj.color = tools.convex_color

        return {'FINISHED'}


class BlessTools(bpy.types.PropertyGroup):
    lock_camera: bpy.props.BoolProperty(default=False)  # type: ignore
    profile_filepath: bpy.props.StringProperty(
        name="Game Profile Path",
        description="Path to the game profile configuration",
        default="",
        subtype='FILE_PATH'
    )  # type: ignore
    trimesh_color: bpy.props.FloatVectorProperty(
        name="Trimesh Color",
        subtype='COLOR',
        default=(0.1, 0.8, 0.1, 1),  # green
        min=0.0, max=1.0,
        size=4
    )  # type: ignore
    convex_color: bpy.props.FloatVectorProperty(
        name="Convex Color",
        subtype='COLOR',
        default=(0.1, 0.1, 0.8, 1),  # blue
        min=0.0, max=1.0,
        size=4
    )  # type: ignore
    filter_glob: bpy.props.StringProperty(
        default="*.json",  # Change this to match your profile file type
        options={'HIDDEN'},
        maxlen=255,
    )  # type: ignore


class BlessPanel(bpy.types.Panel):
    bl_label = "Bless"
    bl_idname = "VIEW3D_PT_object_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bless'

    def draw(self, context):
        collision_types = context.object.collision_types
        collision_layers = context.object.collision_layers
        collision_mask = context.object.collision_mask
        layout = self.layout
        tools = context.window_manager.bless_tools

        ### GRID ###
        grid_box = layout.box()
        row = grid_box.row()
        row.label(text="Grid")
        row = grid_box.row()
        row.prop(context.window_manager, "unit_size", text="Unit Size (m)")
        row.operator("map_editor.double_unit_size", text="", icon="MESH_GRID")
        row.operator("map_editor.halve_unit_size", text="", icon="SNAP_GRID")

        # TODO, make this next part safer, and add a check for the object type.
        # TODO check what the object collision type enum is, and use that to determine the operator to use etc
        # FIXME something in this code is makign the GUI flicker. Probably constantly checking stuff.

        # TODO only show Apply (Batch) Collision button if there are MULTIPLE objects selected.
        # TODO add a check to see if the object is a mesh, and if not, don't show the collision type options.
        # TODO Put Layers and Mask options INSIDE the collision box on the panel.

        if context.object is not None:

            ### COLLISION ###
            collision_box = layout.box()
            row = collision_box.row()
            row.label(text="Collision")

            row = collision_box.row()
            row.prop(collision_types, "collision_types", text="")
            row.operator("object.gd3d_apply_collisions", text="Apply Collision", icon="CUBE")

            # Get collision type from the object's attribute
            collision_data = collision_types.collision_types
            # print(f"Collision data: {collision_data}, Type: {type(collision_data)}")

            collision_box.alignment = "CENTER"
            if collision_data:
                collision_box.label(text=f"Selected object has {str(collision_data).upper()} collision.", icon="ERROR")
                # Only show custom collision settings if collision type is "custom"
                if collision_data == "custom":
                    custom_collision_box = collision_box.box()
                    body_properties = context.scene.body_properties
                    shape_properties = context.scene.shape_properties

                    indented_layout = custom_collision_box.column()
                    indented_layout.label(text=f"CUSTOM COLLISION NOT SUPPORTED IN THIS VERSION", icon="ERROR")

            else:
                collision_box.label(text="No collision data available.")

            ### COLLISION LAYERS ###
            if collision_data and collision_data != "none":
                collision_layer_box = collision_box.box()
                row = collision_layer_box.row()
                row.label(text="Collision Layers")
                # Arrange buttons in two main rows of 16 buttons (4 blocks of 4 buttons per row)
                for main_row_index in range(2):  # Two main rows
                    main_row = collision_layer_box.row()
                    for block_index in range(4):
                        col = main_row.column()
                        row = col.row(align=True)
                        for button_index in range(4):
                            index = (main_row_index * 16) + (block_index * 4) + button_index
                            row.prop(collision_layers, f"layer_{index + 1}", text=str(index + 1), toggle=True)

            ### COLLISION MASK ###
                collision_mask_box = collision_box.box()
                row = collision_mask_box.row()
                row.label(text="Collision Mask")
                for main_row_index in range(2):  # Two main rows
                    main_row = collision_mask_box.row()
                    for block_index in range(4):
                        col = main_row.column()
                        row = col.row(align=True)
                        for button_index in range(4):
                            index = (main_row_index * 16) + (block_index * 4) + button_index
                            row.prop(collision_mask, f"layer_{index + 1}", text=str(index + 1), toggle=True)

            ### TOOLS ###
            tools_box = layout.box()
            row = tools_box.row()
            row.label(text="Tools")

            # Game Profile Path with file selector
            profile_box = tools_box.box()
            row = profile_box.row()
            row.label(text="Game Profile:")

            row = profile_box.row(align=True)
            row.prop(tools, "profile_filepath", text="")
            row.operator("object.load_game_profile", text="Load Profile", icon='IMPORT')

            # Camera Lock
            row = tools_box.row()
            row.prop(tools, "lock_camera", text="Lock Camera")
            if (hasattr(tools, "lock_camera")) and getattr(tools, "lock_camera") == True:
                bpy.context.space_data.lock_object = bpy.data.objects[context.object.name]
            else:
                bpy.context.space_data.lock_object = None

            # Color Settings
            colors_box = tools_box.box()
            row = colors_box.row()
            row.label(text="Colors:")
            row = colors_box.row()
            row.prop(tools, "trimesh_color", text="Trimesh")
            row = colors_box.row()
            row.prop(tools, "convex_color", text="Convex")

        else:
            row = layout.row()
            row.label(text="No object selected!")


class BlessLoadGameProfile(bpy.types.Operator):
    """Load Game Profile"""
    bl_idname = "object.load_game_profile"
    bl_label = "Load Game Profile"

    def load_textures(self, texture_paths):
        for path in texture_paths:
            try:
                # Load the image
                img = bpy.data.images.load(path, check_existing=True)

                # Mark as asset
                img.asset_mark()
                img.asset_generate_preview()

                # Set asset metadata
                if not img.asset_data:
                    continue

                img.asset_data.catalog_id = "textures"
                img.asset_data.description = f"Game texture: {os.path.basename(path)}"

            except Exception as e:
                self.report({'WARNING'}, f"Failed to load texture {path}: {str(e)}")

    def parse_color(self, color_str):
        """Parse a Godot Color string into RGBA values"""
        # Convert "Color(0.238422, 0.238422, 0.238422, 1)" to [0.238422, 0.238422, 0.238422, 1]
        color_str = color_str.replace('Color(', '').replace(')', '')
        return [float(x.strip()) for x in color_str.split(',')]

    def parse_vector3(self, vec_str):
        """Parse a Godot Vector3 string into XYZ values"""
        # Convert "Vector3(0, 0, 0)" to [0, 0, 0]
        vec_str = vec_str.replace('Vector3(', '').replace(')', '')
        return [float(x.strip()) for x in vec_str.split(',')]

    def load_materials(self, material_paths):
        for path in material_paths:
            try:
                # Parse the .tres file
                with open(path, 'r') as f:
                    lines = f.readlines()

                # Create new material
                mat_name = os.path.splitext(os.path.basename(path))[0]
                mat = bpy.data.materials.new(name=mat_name)
                mat.use_nodes = True

                # Get the node tree
                nodes = mat.node_tree.nodes
                links = mat.node_tree.links

                # Get the principled BSDF node (created by default)
                principled = nodes.get("Principled BSDF")

                # Parse material properties
                for line in lines:
                    line = line.strip()

                    # Handle albedo color
                    if line.startswith('albedo_color'):
                        color_value = line.split('=')[1].strip()
                        color = self.parse_color(color_value)
                        principled.inputs["Base Color"].default_value = color

                    # Handle metallic
                    elif line.startswith('metallic'):
                        value = float(line.split('=')[1].strip())
                        principled.inputs["Metallic"].default_value = value

                    # Handle roughness
                    elif line.startswith('roughness'):
                        value = float(line.split('=')[1].strip())
                        principled.inputs["Roughness"].default_value = value

                    # Handle emission
                    elif line.startswith('emission'):
                        if 'emission_energy_multiplier' in line:
                            value = float(line.split('=')[1].strip())
                            principled.inputs["Emission Strength"].default_value = value
                        elif line.startswith('emission ='):
                            color_value = line.split('=')[1].strip()
                            color = self.parse_color(color_value)
                            principled.inputs["Emission"].default_value = color

                    # Handle UV triplanar
                    elif line.startswith('uv1_triplanar'):
                        value = line.split('=')[1].strip()
                        if value == 'true':
                            # Create Texture Coordinate node
                            tex_coord = nodes.new('ShaderNodeTexCoord')
                            tex_coord.location = (principled.location.x - 600, principled.location.y)

                            # Create Mapping node
                            mapping = nodes.new('ShaderNodeMapping')
                            mapping.location = (principled.location.x - 450, principled.location.y)

                            # Link them together
                            links.new(tex_coord.outputs["Generated"], mapping.inputs["Vector"])

                # Mark as asset
                mat.asset_mark()
                mat.asset_generate_preview()

                # Set asset metadata
                if mat.asset_data:
                    mat.asset_data.catalog_id = "materials"
                    mat.asset_data.description = f"Game material: {mat_name}"

            except Exception as e:
                self.report({'WARNING'}, f"Failed to load material {path}: {str(e)}")

    def load_audio(self, music_paths, sfx_paths):
        # Load music
        for path in music_paths:
            try:
                sound = bpy.data.sounds.load(path, check_existing=True)

                # Mark as asset
                sound.asset_mark()
                sound.asset_generate_preview()

                # Set asset metadata
                if not sound.asset_data:
                    continue

                sound.asset_data.catalog_id = "audio_music"
                sound.asset_data.description = f"Game music: {os.path.basename(path)}"

            except Exception as e:
                self.report({'WARNING'}, f"Failed to load music {path}: {str(e)}")

        # Load SFX
        for path in sfx_paths:
            try:
                sound = bpy.data.sounds.load(path, check_existing=True)

                # Mark as asset
                sound.asset_mark()
                sound.asset_generate_preview()

                # Set asset metadata
                if not sound.asset_data:
                    continue

                sound.asset_data.catalog_id = "audio_sfx"
                sound.asset_data.description = f"Game SFX: {os.path.basename(path)}"

            except Exception as e:
                self.report({'WARNING'}, f"Failed to load SFX {path}: {str(e)}")

    def execute(self, context):
        tools = context.window_manager.bless_tools
        profile_path = tools.profile_filepath

        if not profile_path:
            self.report({'ERROR'}, "No game profile path specified")
            return {'CANCELLED'}

        try:
            # Convert the relative path to absolute if needed
            if profile_path.startswith("//"):
                profile_path = bpy.path.abspath(profile_path)

            with open(profile_path, 'r') as f:
                profile_data = json.load(f)

            # Load assets into Asset Browser
            self.load_textures(profile_data.get('textures', []))
            self.load_materials(profile_data.get('materials', []))
            self.load_audio(
                profile_data.get('audio_music', []),
                profile_data.get('audio_sfx', [])
            )

            self.report({'INFO'}, "Game profile loaded successfully")
            return {'FINISHED'}

        except Exception as e:
            self.report({'ERROR'}, f"Failed to load game profile: {str(e)}")
            return {'CANCELLED'}


class BlessSelectGameProfile(bpy.types.Operator):
    """Select Game Profile Path"""
    bl_idname = "object.select_game_profile"
    bl_label = "Select Game Profile"

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        tools = context.window_manager.bless_tools
        tools.profile_filepath = self.filepath
        return {'FINISHED'}
