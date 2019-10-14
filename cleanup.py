import bpy
from .debug import Debug_Tools

def get_parent_collection():
    """
    gets the parent collection of Node_data_Viz
    assumes all Node_data_Viz collections are children to only one collection
    """
    parent_coll = None # if remains None 'Node_data_Viz collection does not exist
    for coll in bpy.data.collections:
        for child_coll in coll.children:
            if 'Node_data_Viz' in child_coll.name:
                parent_coll = coll
    return parent_coll

def delete_collection_objects(collection_name):
    """
    Arguments:
        collection_name {[type]} -- [description]
    """
    # deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    # select objects of this 
    for object_ in bpy.data.collections[collection_name].objects:
        object_.select_set(True)
    bpy.ops.object.delete() # deletes selected objects
    
def run_cleanup():
    """
    step 1: reset 
    """
    """
    step 1a: delete all objects if true
    """
    if True:
        Debug_Tools.debug_msg('deleting objects')
        # do something
        bpy.ops.object.select_all(action='SELECT') # select all objects
        Debug_Tools.debug_msg('List of names of deleted objects:')
        for object_ in bpy.data.objects:
            Debug_Tools.debug_msg(object_)
        bpy.ops.object.delete() # deletes selected objects
        
    """
    step 1b: remove collection 'Node_data_Viz' and everything in it if the collection already exists
    """
    coll_exists = False
    for coll in bpy.data.collections:
        if 'Node_data_Viz' in coll.name:
            coll_exists = True
            Debug_Tools.debug_msg('')
            break
    if coll_exists:
        parent_coll = get_parent_collection()
        for coll in parent_coll.children:
            # delete collection objects
            delete_collection_objects(coll.name)
            # delete collection
            bpy.data.collections.remove(bpy.data.collections[coll.name])