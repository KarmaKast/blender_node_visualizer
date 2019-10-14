import bpy

#import nodeLib
from .debug import Debug_Tools
from . import cleanup

class CreateViz_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.create_ot_viz"
    bl_label = "Create Viz Operator"
    bl_description = "Create Visualization"
    
    def execute(self, context):
        # do something
        print("----------------------------------------------------------------")
        print("SCRIPT STARTED")
        # single script


        DEBUG_GLOBAL = True

        """
        step 1: cleanup if true
        """

        if True:
            cleanup.run_cleanup()


            
        """
        step 2: create a new collection 'Node_data_Viz'.
        default parent: Scene Collection or active collection
        """
        # create new collection
        # Note: if the name already exists blender adds 001
        Node_data_Viz_Coll = bpy.data.collections.new('Node_data_Viz.000')

        if True:
            # add new collection as child to active collection
            bpy.context.collection.children.link(Node_data_Viz_Coll)
        else:
            # add new collection as child to scene main collection
            bpy.context.scene.collection.children.link(Node_data_Viz_Coll)
            
        """
        step 3: 
        """


        print("SCRIPT ENDED")
        print("----------------------------------------------------------------")
        return {'FINISHED'}