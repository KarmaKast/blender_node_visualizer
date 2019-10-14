import bpy

class Main_PT_Panel(bpy.types.Panel):
    bl_idname = "Main_PT_Panel"
    bl_label = "Main Panel"
    bl_category = "Node_Viz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator('view3d.create_ot_viz', text = "Creates Visialization")