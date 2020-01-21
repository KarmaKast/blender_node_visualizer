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

from . import nodeLib
#import nodeLib

def load_cluster():
    #path = "data/"+name+".node_cluster"
    path = bpy.context.scene.my_props.select_file_prop
    cluster_ = None
    cluster_ = nodeLib.files.load_cluster(path)
    # hopefully a import export feature is added to nodeLib.    
    #node_data = nodeLib.file.import(path) # probably a json file
    return cluster_

#cluster_ = load_cluster('FamilyCluster')

def create_sample_database():
    bill_pack = nodeLib.cluster.create_cluster('lol')
    return bill_pack

