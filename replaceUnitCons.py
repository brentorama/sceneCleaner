import maya.cmds as cmd

nodes = cmd.ls(sl=True)
cmd.select(nodes)
def replaceUnitConNodesWithBlendRotation():
    for node in nodes:
        incoming = cmd.listConnections(node, scn= True, c=True, d=False, s=True, p=True )
        outgoing = cmd.listConnections(node, scn= True, c=True, d=True, s=False, p=True )
        reverse = cmd.createNode('reverse')
        print incoming
        print outgoing    
        rote = cmd.createNode('animBlendNodeAdditiveRotation', n = node.replace('_BlndRotate', '' ))
        cmd.connectAttr(incoming[1], rote+'.inputA')
        cmd.connectAttr(incoming[3], rote+'.inputB')
        cmd.connectAttr(incoming[5], rote+'.weightA')
        cmd.connectAttr(incoming[5], reverse+'.inputX')
        cmd.connectAttr(reverse+'.outputX', rote+'.weightB')
        cmd.connectAttr(rote+'.output', outgoing[1], f=True)
        cmd.delete(node)
    

