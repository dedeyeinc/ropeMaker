import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mm

## Function
def cvCurve():
    mm.eval("CVCurveTool")
def epCurve():
    mm.eval("EPCurveTool")
def bezierCurve():
    mm.eval("CreateBezierCurveTool")
def drawCurve():
    mm.eval("PencilCurveTool")

def makeRope():
    from ropeMaker import ropeMaker
    import imp
    imp.reload(ropeMaker)
    ropeMaker.makeRope()

def makeGeo():
    from ropeMaker import ropeMaker_makeGeo
    import imp
    imp.reload(ropeMaker_makeGeo)
    ropeMaker_makeGeo.makeGeo()

def attachGeoToCurve():
    from ropeMaker import ropeMakerUI_addCenterCurve
    import imp
    imp.reload(ropeMakerUI_addCenterCurve)
    ropeMakerUI_addCenterCurve.makeCenterCurve( cmds.checkBox(centerCurve,q=1,v=1),
                                                cmds.checkBox(centerJoints,q=1,v=1),
                                                cmds.checkBox(addSkinning,q=1,v=1),
                                                cmds.checkBox(addDynamics,q=1,v=1),
                                                )
    #ropeMakerUI_addCenterCurve.makeCenterCurve(1,1)
def makeRibbon():
    from ropeMaker import ropeMaker_ribbonizer
    import imp
    imp.reload(ropeMaker_ribbonizer)
    ropeMaker_ribbonizer.UI()

def changeAddCenterJoints():
    if cmds.checkBox(centerJoints,q=1,v=1):
        cmds.checkBox(addSkinning,e=1,ed=1)
        cmds.checkBox(addDynamics,e=1,ed=1)
    else:
        cmds.checkBox(addSkinning,e=1,ed=0,v=0)
        cmds.checkBox(addDynamics,e=1,ed=0,v=0)

def deleteUVPin():
    if cmds.objExists('uvPin1'):
        cmds.select('uvPin1',r=1)
        mm.eval("doDelete")
        print("UV Pin deleted!")
    else:
        print("No UV Pin exists")

def rebuildCurve():
    s=cmds.intField(spans,q=1,v=1)
    for shp in cmds.ls(sl=1):
        if len(cmds.listRelatives(shp,ad=1,s=1)) > 0:
            for c in cmds.listRelatives(shp,ad=1,s=1):
                cmds.rebuildCurve(c,ch=1,rpo=1,rt=0,end=1,kr=0,kep=1,kt=0,s=s,d=3,tol=1e-08)
                print("rebuilt "+c+" with "+str(s)+" spans, as requested!")
        else:
            print("Select a curve, bro!")
            
## UI

def ropeMakerUI():
    global rmUI
    title='Rope Maker'
    rmUI = cmds.window('Rope Maker',t=title,w=100,h=100,rtf=1)
    cl1 = cmds.columnLayout(adj=1,p=rmUI)
    fl1= cmds.frameLayout(l='Output Settings',cll=1,p=cl1)
    
    cl10 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=150,p=fl1)
    global btn7
    btn7 = cmds.button(l='CV Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.cvCurve()',w=80,p=cl10)
    cmds.separator(hr=0,width=10,p=cl10)
    global btn8
    btn8 = cmds.button(l='EP Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.epCurve()',w=80,p=cl10)
    cmds.separator(hr=0,width=10,p=cl10)
    global btn9
    btn9 = cmds.button(l='Bezier Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.bezierCurve()',w=80,p=cl10)
    global btn6
    btn6 = cmds.button(l='Draw Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.drawCurve()',p=fl1)
    cmds.separator(hr=1,height=1,p=fl1)
    
    cl3 = cmds.rowColumnLayout(nc=2,nch=2,h=25,w=270,p=fl1)
    global tx1
    tx1 = cmds.text('Name:',w=40,p=cl3)
    global tf1
    tf1 = cmds.textField(it='',pht='Insert name here',w=200,p=cl3)
    
    cl9 = cmds.rowColumnLayout(nc=4,nch=4,h=25,w=150,p=fl1)
    global tx4
    tx4 = cmds.text('Spans:',width=40,p=cl9)
    global spans
    spans = cmds.intField(min=2,v=100,step=1,width=50,p=cl9)
    cmds.separator(hr=0,width=10,p=cl9)
    global btn5
    btn5 = cmds.button(l='Rebuild Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.rebuildCurve()',p=cl9)
    
    global btn1
    btn1 = cmds.button(l='Create Geo Base',c='from ropeMaker import ropeMakerUI; ropeMakerUI.makeGeo()',p=fl1)
    
    global btn2
    btn2 = cmds.button(l='Delete UV Pin',c='from ropeMaker import ropeMakerUI; ropeMakerUI.deleteUVPin()',p=fl1)
    
    cl2 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=150,p=fl1)
    
    global tx2
    tx2 = cmds.text('Twist:',width=35,p=cl2)
    global twist
    twist = cmds.intField(min=0,v=0,step=1,width=40,p=cl2)
    cmds.separator(hr=0,width=10,p=cl2)
    global tx3
    tx3 = cmds.text('Divisions:',width=50,p=cl2)
    global divisions
    divisions = cmds.intField(min=0,v=100,step=1,width=40,p=cl2)
    
    cl4 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=250,p=fl1)
    global keepFacesTogether
    keepFacesTogether = cmds.checkBox(l='Keep Faces Together',v=1,p=cl4)
    cmds.separator(hr=0,width=10,p=cl4)
    global constHist
    constHist = cmds.checkBox(l='Construction History',v=0,p=cl4)
    
    cl5 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=150,p=fl1)
    global position
    position = cmds.checkBox(l='Position at Origin',v=0,p=cl5)
    
    global btn0
    btn0 = cmds.button(l='Extrude Geo (Make Rope)',c='from ropeMaker import ropeMakerUI; ropeMakerUI.makeRope()',p=fl1)
    
    cmds.separator(hr=1,height=1,p=fl1)
    cl6 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=150,p=fl1)
    global centerJoints
    centerJoints = cmds.checkBox(l='Add Center Joints',v=1,cc='from ropeMaker import ropeMakerUI; ropeMakerUI.changeAddCenterJoints()',p=cl6)
    global centerCurve
    centerCurve = cmds.checkBox(l='Add Center Curve',v=1,p=cl6)
    
    cl7 = cmds.rowColumnLayout(nc=5,nch=5,h=25,w=150,p=fl1)
    global addSkinning
    addSkinning = cmds.checkBox(l='Add Clusters',v=0,p=cl7)
    global addDynamics
    addDynamics = cmds.checkBox(l='Add Dynamics',v=0,p=cl7)
    
    cl8 = cmds.rowColumnLayout(nc=3,nch=3,h=25,w=250,p=fl1)
    global btn3
    btn3 = cmds.button(l='Attach Geo to Curve',c='from ropeMaker import ropeMakerUI; ropeMakerUI.attachGeoToCurve()',w=130,p=cl8)
    cmds.separator(hr=0,width=10,p=cl8)
    global btn4
    btn4 = cmds.button(l='Make Ribbon',c='from ropeMaker import ropeMakerUI; ropeMakerUI.makeRibbon()',w=130,p=cl8)
    
    pm.showWindow(rmUI)


## DELETE WINDOW IF IT EXISTS ##
try:
    if pm.window(rmUI,q=1,ex=1):
        pm.deleteUI(rmUI)
except:
    pass