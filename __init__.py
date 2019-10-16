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

bl_info = {
    "name" : "Node_Viz",
    "author" : "Sree Chandan R",
    "description" : "visualization addon for nodeLib databases",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .create_viz import CreateViz_OT_Operator
from .main_panel import Main_PT_Panel, MyProperties

classes = (
    CreateViz_OT_Operator,
    Main_PT_Panel,
    MyProperties
    )

#register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    for cls_ in classes:
        bpy.utils.register_class(cls_)
    bpy.types.Scene.my_props = bpy.props.PointerProperty(type=MyProperties)
    
def unregister():
    for cls_ in classes:
        bpy.utils.unregister_class(cls_)
    del bpy.types.Scene.my_props
    
