import maya.cmds as cmds
import maya.mel as mm
import re
from ropeMaker import ropeMakerUI

def makeCenterCurve(c=1, j=1, s=1, d=1):
    #track select order must be turned ON for this to work
    points = 'curve -d 3 '
    sel = cmds.ls(os=1,fl=1)
    obj = cmds.ls(o=1,sl=1)
    num=[]
    out=[]
    edges=[]
    joints=[]
    clusters=[]
    name = cmds.textField(ropeMakerUI.tf1,q=1,tx=1)
    int1=0
    int2=0
    int3=0
    crv_int=0
    mPath_int1=0
    mPath_int2=0
    mPath_int3=0
    for one in sel:
        strip = re.search(r"\[([0-9]+)\]", one)
        num.append(strip.group(1))
    size=len(num)
    if(size):
        if size == 1:
            edges = cmds.polySelect(edgeRing=(int(num[0])), ns=1)
        if size == 2:
            edges = cmds.polySelect(edgeRingPath=(int(num[0]),int(num[1])),ns=1)
        if size > 2:
            edges = num
        clust_int1=0
        clust_int2=0
        clust_int3=0
        for one in edges:
            cmds.select(obj)
            cmds.polySelect(elb=int(one))
            clust=cmds.cluster(n='clusterPoo_%s%s%s' % (clust_int1,clust_int2,clust_int3))
            clust_int3+=1
            if clust_int3 > 9:
                clust_int3 = 0
                clust_int2+=1
            if clust_int2 > 9:
                clust_int2 = 0
                clust_int1+=1
            cmds.select(cl=1)
            posi=cmds.getAttr(clust[0]+'HandleShape.origin')
            if c:
                if name != '':
                    points=points+('-p %s %s %s ' %(posi[0][0],posi[0][1],posi[0][2]))
            if j:
                if name != '':
                    jnt_name = name+'_{0}{1}{2}_jnt'.format(int1,int2,int3)
                    jnt = cmds.joint(n=jnt_name,p=(posi[0][0],posi[0][1],posi[0][2]))
                    int3+=1
                    if int3 > 9:
                        int3 = 0
                        int2+=1
                    if int2 > 9:
                        int2 = 0
                        int1+=1
                else:
                    jnt_name = n='poo_{0}{1}{2}_jnt'.format(int1,int2,int3)
                    jnt = cmds.joint(n=jnt_name,p=(posi[0][0],posi[0][1],posi[0][2]))
                    int3+=1
                    if int3 > 9:
                        int3 = 0
                        int2+=1
                    if int2 > 9:
                        int2 = 0
                        int1+=1
                joints.append(jnt_name)
                cmds.delete([clust[0],clust[1]])
                
        if c:
            out.append(mm.eval(points))
        if j:
            # for i in reversed(range(1, len(edges))):
            #     cmds.parent(joints[i],joints[i-1])  
            # cmds.joint(joints[0],e=1,oj='xyz',sao='yup',ch=1,zso=1)
            # cmds.joint(joints[-1],e=1,o=(0,0,0))
            out.append(joints[0])
            if s:
                crv = '%s_crv'%(name)
                
                if d:
                    crv_name1 = '%s_%s_crv'%(name,crv_int)
                    cmds.rename('curve1',crv_name1)
                    
                    # make curve dynamic
                    cmds.select(crv_name1,r=1)
                    mm.eval('makeCurvesDynamic 2 { "1", "0", "1", "1", "0"}')
                    
                    crv = '%s_%s_dynaCrv'%(name,crv_int)
                    cmds.rename('curve1',crv)
                
                # attach to curve
                if name != '':
                    for i, (jnt) in enumerate(joints):
                        cmds.select(jnt,r=1)
                        cmds.select(crv+'Shape',add=1)
                        mm.eval('AttachToPath')
                        mPath = name+'_mPath_%s%s%s' %(mPath_int1,mPath_int2,mPath_int3)
                        cmds.select('motionPath*_uValue',r=1)
                        mp_old = cmds.ls(sl=1)[0]
                        cmds.rename(mp_old,mPath+'_uValue')
                        cmds.select('motionPath*',r=1)
                        mp_old = cmds.ls(sl=1)[0]
                        cmds.rename(mp_old,mPath)
                        mPath_int3+=1
                        if mPath_int3>9:
                            mPath_int3=0
                            mPath_int2+=1
                        if mPath_int2>9:
                            mPath_int2=0
                            mPath_int1+=1
                        
                        #minu = cmds.getAttr('%s_%s_crvShape'%(name,crv_int)+'.minValue')
                        #maxu = cmds.getAttr('%s_%s_crvShape'%(name,crv_int)+'.maxValue')
                        inc = 1/len(joints)
                        u = inc * i
                        
                        # set joints positions on curve
                        cmds.setAttr(mPath+'.uValue', u)
                # Add clusters
                
                clust_int1=0
                clust_int2=0
                clust_int3=0
                for one in edges:
                    cmds.select(obj)
                    cmds.polySelect(elb=int(one))
                    if name != '':
                        clust=cmds.cluster(n=name+'_cluster_%s%s%s' % (clust_int1,clust_int2,clust_int3))
                        clust_int3+=1
                        if clust_int3 > 9:
                            clust_int3 = 0
                            clust_int2+=1
                        if clust_int2 > 9:
                            clust_int2 = 0
                            clust_int1+=1
                    else:
                        clust=cmds.cluster(n='clusterPoo_%s%s%s' % (clust_int1,clust_int2,clust_int3))
                        clust_int3+=1
                        if clust_int3 > 9:
                            clust_int3 = 0
                            clust_int2+=1
                        if clust_int2 > 9:
                            clust_int2 = 0
                            clust_int1+=1
                
                    clusters.append(clust[0]+'Handle')
                for i, (jnt,clust) in enumerate(zip(joints,clusters)):
                    cmds.parentConstraint(jnt,clust,mo=1)
                
                cmds.select(joints,r=1)
                cmds.group(n='joints_grp',r=1)
                cmds.select(clusters,r=1)
                cmds.group(n='clusters_grp',r=1)
        cmds.select(cl=1)
        cmds.delete('curve1')
    else:
        print("Nothing is selected")