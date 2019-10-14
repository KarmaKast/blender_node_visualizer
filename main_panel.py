import bpy
    
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )


class MyProperties(PropertyGroup):

    select_file_prop: StringProperty(
        name="",
        description="choose a node datafile",
        default = "",
        subtype = "FILE_PATH"
        )

class Main_PT_Panel(bpy.types.Panel):
    bl_label = "Main Panel"
    bl_idname = "Main_PT_Panel"
    bl_category = "Node_Viz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        sce= context.scene
        my_props = sce.my_props
        
        layout.prop(my_props, 'select_file_prop')
        #layout.prop(mytool, 'my_int', text='Integer Property')
        
        row = layout.row()
        row.operator('view3d.create_ot_viz', text = "Create Visialization")