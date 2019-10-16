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
from .debug import Debug_Tools

def get_parent_collection():
    """
    gets the parent collection of Node_data_Viz
    assumes all Node_data_Viz collections are children to only one collection
    """
    parent_coll = None # if remains None 'Node_data_Viz collection does not exist
    
    for coll in bpy.data.collections:
        Debug_Tools.debug_msg('checking in {}'.format(coll.name),False)
        for child_coll in coll.children:
            Debug_Tools.debug_msg('child collection {}'.format(child_coll.name),False)
            if 'Node_data_Viz' in child_coll.name:
                parent_coll = coll
                break
    if parent_coll == None:
        Debug_Tools.debug_msg("Node_data_Viz.xxx collections does not exist in this file")
    else:
        Debug_Tools.debug_msg('parent collection for the Node_data_Viz.xxx collections: {}'.format(parent_coll))
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
    Debug_Tools.debug_msg("Running Cleanup")
    if True:
        Debug_Tools.debug_msg('deleting objects')
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
        if parent_coll != None:
            for coll in parent_coll.children:
                # delete collection objects
                delete_collection_objects(coll.name)
                # delete collection
                bpy.data.collections.remove(bpy.data.collections[coll.name])