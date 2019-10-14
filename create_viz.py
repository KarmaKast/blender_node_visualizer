import bpy

class CreateViz_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.create_ot_viz"
    bl_label = "Create Viz Operator"
    bl_description = "Creates Visialization"
    
    def execute(self, context):
        # do something
        return {'FINISHED'}