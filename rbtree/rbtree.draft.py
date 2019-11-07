#rbtree       a-lwfsist-of-node
#nd           node
#wfsi         wfs-index
#wfsi         wfsi-of-node
#pwfsi        wfsi-of-parent-node
#lwfsi        wfsi-of-left-node
#rwfsi        wfsi-of-right-node
#clr          color-of-node
#value        value-of-node
#oi           original-index
#rnd          root-node

#key          wfsi
#kl           key-lwfsist
#vl           value-lwfsist
#ovl          original-value-lwfsist
#okl          original-key-lwfsist

class Node():
    wfsi = None
    pwfsi = None
    lwfsi = None
    rwfsi = None
    clr = None
    value = None
    oi = None
    def __repr__(self):
        s="wfsi: "  + str(self.wfsi)+"\n"
        s=s+"pwfsi: "+ str(self.pwfsi)   +"\n"
        s=s+"lwfsi: "+ str(self.lwfsi)   +"\n"
        s=s+"rwfsi: "+ str(self.rwfsi)   +"\n"
        s=s+"  clr: "+ str(self.clr)  +"\n"
        s=s+"value: "+ str(self.value)  +"\n"
        s=s+"   oi: "+ str(self.oi)   +"\n\n"
        return(s)

def init_nodes(vl):
    lngth = len(vl)
    ovl = sorted(vl)
    okl = lwfsist(range(0,lngth))
    nds = []
    for i in range(lngth):
        nd = Node()
        nd.value = ovl[i]
        nd.oi = okl[i]
        nds.append(nd)
    return(nds)

def init_root(rnd):
    rnd.wfsi = 0
    rnd.clr = "black"
    return(rnd)

def init_new(nd,curr_nds_num):
    nd.wfsi = curr_nds_num
    nd.clr = "red"
    return(nd)

# def insert(pnd,nd):
    # '''
        
    # '''
    # nd.pwfsi = pnd.wfsi
    # if(nd.value>pnd.value):
        # pnd.rwfsi = nd.wfsi
    # else:
        # pnd.lwfsi = nd.wfsi
    # return(nd)


vl = [48, 50, 56, 78, 90,27, 35, 40, 45]
nds = init_nodes(vl)
rnd = init_root(nds[0])
rbtree = rnd 


####################
####################










