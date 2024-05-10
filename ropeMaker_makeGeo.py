from Library import ropeMakerUI
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mm
def makeGeo():
    if len(cmds.ls(sl=1)) != 0:
        if cmds.ls(type='nurbsCurve'):
            crv = cmds.ls(sl=1)[0]
            geo = cmds.polyCylinder(r=1,h=2,sx=20,sy=1,sz=1,ax=[0,1,0],rcp=0,cuv=3,ch=1)
            cmds.delete(geo[0]+'.f[0:39]')
            cmds.setAttr(geo[0]+'.ty',-1)
            cmds.xform(geo[0],cp=1)
            for axis in 'xyz':
                cmds.setAttr(geo[0]+'.s%s' % axis,5)
            #cmds.setAttr(geo[0]+'.rx',-90)
            pm.makeIdentity(geo[0], apply=True, t=True, r=True, s=True)
            
            cmds.select(geo[0],r=1)
            cmds.DeleteHistory()
            cmds.select(crv,r=1)
            cmds.select(geo[0],add=1)
            uvPin = cmds.UVPin()
            cmds.setAttr('uvPin1.coordinate[0].coordinateU',0)
            cmds.setAttr('uvPin1.coordinate[0].coordinateV',0)
            
            # get name
            name = cmds.textField(ropeMakerUI.tf1,q=1,tx=1)
            if name != '':
                pm.rename(crv,name+'_crv')
                pm.rename(geo[0],name+'_rope')
            
        else:
            geo = cmds.polyCylinder(r=1,h=2,sx=20,sy=1,sz=1,ax=[0,1,0],rcp=0,cuv=3,ch=1)
            cmds.delete(geo[0]+'.f[0:39]')
            cmds.setAttr(geo[0]+'.ty',-1)
            cmds.xform(geo[0],cp=1)
            
            for axis in 'xyz':
                cmds.setAttr(geo[0]+'.s%s' % axis,5)
            pm.makeIdentity(geo[0], apply=True, t=True, r=True, s=True)
            cmds.select(geo[0],r=1)
            cmds.DeleteHistory()
            
            # get name
            name = cmds.textField(ropeMakerUI.tf1,q=1,tx=1)
            if name != '':
                pm.rename(geo[0],name+'_rope')          
    else:
        geo = cmds.polyCylinder(r=1,h=2,sx=20,sy=1,sz=1,ax=[0,1,0],rcp=0,cuv=3,ch=1)
        cmds.delete(geo[0]+'.f[0:39]')
        cmds.setAttr(geo[0]+'.ty',-1)
        cmds.xform(geo[0],cp=1)
        
        for axis in 'xyz':
            cmds.setAttr(geo[0]+'.s%s' % axis,5)
        pm.makeIdentity(geo[0], apply=True, t=True, r=True, s=True)
        cmds.select(geo[0],r=1)
        cmds.DeleteHistory()
        
        # get name
        name = cmds.textField(ropeMakerUI.tf1,q=1,tx=1)
        if name != '':
            pm.rename(geo[0],name+'_rope')