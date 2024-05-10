from Library import ropeMakerUI
import pymel.core as pm
import maya.cmds as cmds

def makeRope():
    lastSel = cmds.ls(sl = True)
    firstSel = lastSel[0]
    secondSel = lastSel[1]
    
    if cmds.objExists(cmds.listRelatives(firstSel,ad=1,type='mesh')[0]):
        cmds.select(firstSel)
        
        faces = cmds.select(firstSel+'.f[*]',add=True)
        
        cmds.select(secondSel,tgl=True)
        
        # get booleans
        ch = cmds.checkBox(ropeMakerUI.constHist,q=1,v=1)
        kft = cmds.checkBox(ropeMakerUI.keepFacesTogether,q=1,v=1)
        div = cmds.intField(ropeMakerUI.divisions,q=1,v=1)
        twi = cmds.intField(ropeMakerUI.twist,q=1,v=1)
        
        cmds.polyExtrudeFacet(firstSel,ch=ch,kft=kft,d=div,twt=twi,inc=secondSel)
        
        pos = cmds.checkBox(ropeMakerUI.position,q=1,v=1)
        if pos == True:
            cmds.makeIdentity(firstSel, apply=True, t=True, r=True, s=True)
        else:
            for axi in 'xyz':
                for atr in 'tr':
                    cmds.setAttr(firstSel+'.%s%s' % (atr,axi),0)
    
    else:
        print("Please select geo first, then curve.")
    '''
    # get name
    name = cmds.textField(ropeMakerUI.tf1,q=1,tx=1)
    if name != '':
        cmds.rename(firstSel,name+'_crv')
        cmds.rename(secondSel,name+'_rope')'''