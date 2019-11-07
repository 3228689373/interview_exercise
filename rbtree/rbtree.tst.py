################
################
import edict.edict as eded
import elwfsist.elwfsist as elel
#先实现查询
#
vl = [27, 35, 40, 45, 48, 50, 56, 78, 90]
kl = [0,   1,  2,  3,  4,  5,  6,  7,  8]
# d = eded.kvlwfsist2d(kl,vl)
ovl = [50, 35, 78, 27, 45, 56, 90, 40, 48]
# okl = eded.klviavl(d,ovl)
okl = [ 5,  1,  7,  0,  3,  6,  8,  2,  4]


#####
nds = []
for i in range(len(okl)):
    nd = Node()
    nd.wfsi = i
    nd.value = ovl[i]
    nd.oi = vl.index(nd.value)
    nds.append(nd)
######


nds[0].clr = "black"
nds[0].pwfsi = None
nds[0].lwfsi = nds[1].wfsi
nds[0].rwfsi = nds[2].wfsi

nds[1].clr = "red"
nds[1].pwfsi = nds[0].wfsi
nds[1].lwfsi = nds[3].wfsi
nds[1].rwfsi = nds[4].wfsi


nds[2].clr = "black"
nds[2].pwfsi = nds[0].wfsi
nds[2].lwfsi = nds[5].wfsi
nds[2].rwfsi = nds[6].wfsi


nds[3].clr = "black"
nds[3].pwfsi = nds[1].wfsi
nds[3].lwfsi = None
nds[3].rwfsi = None


nds[4].clr = "black"
nds[4].pwfsi = nds[1].wfsi
nds[4].lwfsi = nds[7].wfsi
nds[4].rwfsi = nds[8].wfsi

nds[5].clr = "red"
nds[5].pwfsi = nds[2].wfsi
nds[5].lwfsi = None
nds[5].rwfsi = None


nds[6].clr = "red"
nds[6].pwfsi = nds[2].wfsi
nds[6].lwfsi = None
nds[6].rwfsi = None


nds[7].clr = "red"
nds[7].pwfsi = nds[4].wfsi
nds[7].lwfsi = None
nds[7].rwfsi = None


nds[8].clr = "red"
nds[8].pwfsi = nds[4].wfsi
nds[8].lwfsi = None
nds[8].rwfsi = None

wfsnds = nds

def is_leaf(nd):
    return((nd.lwfsi == None) and (nd.rwfsi == None))


def mdfs_next(nd,nds,nnds=[]):
    '''
        中序遍历的下一个
    '''
    if(is_leaf(nd)):
        return([nd])
    else:
        lnd = nds[nd.lwfsi]
        rnd = nds[nd.rwfsi]
        ll = mdfs_next(lnd,nds,nnds)
        rl = mdfs_next(rnd,nds,nnds)
        nnds = ll + [nd] + rl
    return(nnds)



def wfsnds2mdfsnds(nds):
    rnd = nds[0]
    mdfs_nodes = mdfs_next(rnd,nds,[])
    return(mdfs_nodes)
    


mdfsnds = wfsnds2mdfsnds(nds)
mdfsvals = list(map(lambda nd:nd.value,mdfsnds))


