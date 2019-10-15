import bpy

from . import nodeLib

def load_data():
    node_data = None
    path = bpy.context.scene.my_props.select_file_prop
    # hopefully a import export feature is added to nodeLib.    
    #node_data = nodeLib.file.import(path) # probably a json file
    if node_data == None:
        node_data = create_sample_database()
        
    return node_data

def create_sample_database():
    bill = nodeLib.node.Node_Manager.create_node(node_ID = {'ID':'01','node_name':'bill'})
    bill.data.update(
        {
            "invoice_NO":"001966",
            "date":"16/09/2019",
            "time":"12:05 PM",
            "seller":"Prestige",
            "seller address":"vodafone store somewhere",
            "shipping address":None,
            "buyer":"me",
            "total cost": 0,
            "total tax":{
                "cgst":0,
                "sgst":0
                },
            "discounts":{
                "voucher":"",
                "gift card":""
                },
            "net price": 0
        }
    )
    
    nodeLib.node.Node_Manager.create_related_node(
        from_node = bill, 
        node_ID = {'ID':'02','node_name':'entries'}, 
        rel_from_to_to = "group", 
        rel_to_to_from = "member")
    
    #entries = Node.Node(node_ID = {'ID':'02','node_name':'entries'})
    #entry1 = Node.Node(node_ID = {'ID':'03','node_name':'entry'})
    
    node_ = nodeLib.node.Node_Manager.get_rel_node(bill, [0]) # entries
    nodeLib.node.Node_Manager.create_related_node(
        from_node = node_,
        node_ID = {'ID':'03','node_name':'entry'}, 
        data = {
            'SNo':1, 
            'item':{
                "ID":{
                    "product":60006,
                    "HSN COde":40169340
                },
                'name':'gasket pop junior',
                'list price':'80.00 INR', 
                'tax percents':{
                    'cgst':9.0,
                    'sgst':9.0
                }
            },
            'quantity':2
            }, 
        rel_from_to_to = "group", 
        rel_to_to_from = "member"
        )
    nodeLib.node.Node_Manager.create_related_node(
        from_node = node_,
        node_ID = {'ID':'04','node_name':'entry'}, 
        data = {
            'SNo':2, 
            'item':{
                "ID":{
                    "product":60002,
                    "HSN COde":40169340
                },
                'name':'gasket senior ALU',
                'list price':'95.00 INR', 
                'tax percents':{
                    'cgst':9.0,
                    'sgst':9.0
                }
            },
            'quantity':2
            }, 
        rel_from_to_to = "group", 
        rel_to_to_from = "member"
        )    
    bill_pack = nodeLib.node.Node_Pack.create_pack(bill)
    nodeLib.node.Node_Pack.describe(bill_pack, 'compact')
    #nodeLib.debug.Debug_Node.describe(bill,'compact')
    
    return bill_pack
