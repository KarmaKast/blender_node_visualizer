print("----------------------------------------------------------------")
print("SCRIPT STARTED")
# single script
import bpy

#import nodeLib

DEBUG_GLOBAL = 1
"""
step 1: reset 
"""
"""
step 1a: delete all objects if true
"""
def debug_msg(msg, local_debug=0):
    if DEBUG_GLOBAL or local_debug:
        print(msg)
        
def del_all_objs(DEBUG=0):
    debug_msg('deleting objects', DEBUG)
    # do something
    bpy.ops.object.select_all(action='SELECT')
    debug_msg('List of names of deleted objects:', DEBUG)
    for object_ in bpy.data.objects:
        print(object)
    bpy.ops.object.delete() # deletes selected objects
    
if True:
    del_all_objs()
"""
step 1b: remove collection 'Node_data_Viz' and everything in it if True
"""
def delete_collection_objects(collection_name):
    # deselect all objects
    
    # select objects of this collection
    for object_ in bpy.data.collections[collection_name].objects:
        object_.select_set(True)
      
if 'Node_data_Viz' in bpy.data.collections:
    delete_collection_objects('Node_data_Viz')

"""
step 2: create a new collection 'Node_data_Viz'.
default parent: Scene Collection or active collection
"""
# create new collection
# Note: if the name already exists blender adds 001
Node_data_Viz_Coll = bpy.data.collections.new('Node_data_Viz')

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
