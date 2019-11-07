####################################################
class Node():
    pid = None
    id = None
    lid = None
    rid = None
    clr = None
    val = None
    def __repr__(self):
        s=  " id: "  + str(self.id)+"\n"
        s=s+"pid: "  + str(self.pid)   +"\n"
        s=s+"lid: "  + str(self.lid)   +"\n"
        s=s+"rid: "  + str(self.rid)   +"\n"
        s=s+"clr: "  + str(self.clr)  +"\n"
        s=s+"val: "  + str(self.val)  +"\n\n"
        return(s)
####################################################


import edict.edict as eded
import elidst.elidst as elel
#先实现查询
#
vl = [27, 35, 40, 45, 48, 50, 56, 78, 90]
kl = [0,   1,  2,  3,  4,  5,  6,  7,  8]
# d = eded.kvlidst2d(kl,vl)
ovl = [50, 35, 78, 27, 45, 56, 90, 40, 48]
# okl = eded.klviavl(d,ovl)
okl = [ 5,  1,  7,  0,  3,  6,  8,  2,  4]


#####
nds = []
for i in range(len(okl)):
    nd = Node()
    nd.val = ovl[i]
    nd.id = vl.index(nd.val)
    nds.append(nd)
######



nds[0].clr = "black"
nds[0].pid = None
nds[0].lid = nds[1].id
nds[0].rid = nds[2].id

nds[1].clr = "red"
nds[1].pid = nds[0].id
nds[1].lid = nds[3].id
nds[1].rid = nds[4].id


nds[2].clr = "black"
nds[2].pid = nds[0].id
nds[2].lid = nds[5].id
nds[2].rid = nds[6].id


nds[3].clr = "black"
nds[3].pid = nds[1].id
nds[3].lid = None
nds[3].rid = None


nds[4].clr = "black"
nds[4].pid = nds[1].id
nds[4].lid = nds[7].id
nds[4].rid = nds[8].id

nds[5].clr = "red"
nds[5].pid = nds[2].id
nds[5].lid = None
nds[5].rid = None


nds[6].clr = "red"
nds[6].pid = nds[2].id
nds[6].lid = None
nds[6].rid = None


nds[7].clr = "red"
nds[7].pid = nds[4].id
nds[7].lid = None
nds[7].rid = None


nds[8].clr = "red"
nds[8].pid = nds[4].id
nds[8].lid = None
nds[8].rid = None


###################
###################

wfsnds = nds

mdfsnds = nds2mdfsnds(wfsnds)
elel.mapv(mdfsnds,lambda nd:nd.val)

leaf_nds = nds_get_leaf_nds(nds)
nonleaf_nds = nds_get_nonleaf_nds(nds)
chains = nds_get_all_chains(nds)

id = len(wfsnds)
nnd = new_red_nd(80,id)


#二叉树的删除
#https://blog.csdn.net/Future_LL/article/details/79968437
#有两个结点
#    A找到左子树的最右最下的元素
#    B找到右子树的最左最下的元素
#    找出 abs(A - V) 和 abs(B - V) 最小的那个nd
#    
