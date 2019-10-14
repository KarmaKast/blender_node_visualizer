import bpy

#import nodeLib
from .debug import Debug_Tools
from . import cleanup
from . import node_dataLoader

class CreateViz_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.create_ot_viz"
    bl_label = "Create Viz Operator"
    bl_description = "Creates Visualization of Node data"
    
    
    def execute(self, context):
        # do something
        Debug_Tools.debug_msg("----------------------------------------------------------------")
        Debug_Tools.debug_msg("Create viz STARTED")
        # single script


        Debug_Tools.set_force_off(False)

        """
        step 1: cleanup if true
        """

        if True:
            cleanup.run_cleanup()


            
        """
        step 2: create a new collection 'Node_data_Viz'.
        default parent: Scene Collection or active collection
        """
        # create the main viz collection
        if 'Node_data_Viz' in bpy.data.collections:
            Node_data_Viz_Coll = bpy.data.collections['Node_data_Viz']
        else:
            Node_data_Viz_Coll = bpy.data.collections.new('Node_data_Viz')
        # create new collection
        # Note: if the name already exists blender adds 001
        Node_data_Viz_Coll_new = bpy.data.collections.new('Node_data_Viz.000')

        # link main viz collection to the scene main collection
        if 'Node_data_Viz' not in bpy.context.scene.collection.children:
            bpy.context.scene.collection.children.link(Node_data_Viz_Coll) 
        
        # link the new collection to the main viz collection
        Node_data_Viz_Coll.children.link(Node_data_Viz_Coll_new) 
            
        """
        step 3: load database to visualize
        Currently nodeLib cannot export database. So create a sample database and load that.
        """
        node_data = node_dataLoader.create_sample_database()
        

        Debug_Tools.debug_msg("Create viz ENDED")
        Debug_Tools.debug_msg("----------------------------------------------------------------")
        return {'FINISHED'}