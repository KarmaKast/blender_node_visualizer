# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

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
        
        row = layout.row()
        row.operator_context = 'EXEC_DEFAULT'
        row.operator('view3d.create_ot_viz', text = "Create Visialization")