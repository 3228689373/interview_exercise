#id        unique-node-id
#pid       unique-parent-id
#lid       left-child-id
#rid       right-child-id
#clr       color
#val       value  

#nd        nodes
#rnd       root-node
#wfsnds    wfs-node-list
#lchild    left-child
#rchild    right-child
#pnd       parent-node
#chain     path
#branch    left-or-right
#minnd     min-node
#maxnd     max-node

#二叉树性质
#中序排列  唯一对应  从小到大
#但是一个序列 有不止一种二叉树表示 与插入顺序有关
#左叶子节点的 next 是parent
#右叶子节点的 next 是ances链上第一个大于node.val的
#左叶子节点的 next 是ances链上第一个小于node.val的
#右叶子节点的 prev 是parent



class Node():
    pid = None
    id = None
    lid = None
    rid = None
    clr = None
    val = None
    _visited = None
    _mdfs_prev_id = None
    def __repr__(self):
        s=  " id: "  + str(self.id)+"\n"
        s=s+"pid: "  + str(self.pid)   +"\n"
        s=s+"lid: "  + str(self.lid)   +"\n"
        s=s+"rid: "  + str(self.rid)   +"\n"
        s=s+"clr: "  + str(self.clr)  +"\n"
        s=s+"val: "  + str(self.val)  +"\n\n"
        return(s)

def is_leaf(nd):
    return((nd.lid == None) and (nd.rid == None))

def nds_clear_visited(nds):
    for nd in nds:
        nd._visited = None
    return(nds)

def nds_clear_mdfs_prev_id(nds):
    for nd in nds:
        nd._mdfs_prev_id = None
    return(nds)

def idgetnd(id,nds):
    for nd in nds:
        if(nd.id == id):
            return(nd)
        else:
            pass
    return(None)

def ndsgetroot(nds):
    for nd in nds:
        if(nd.pid == None):
            return(nd)
        else:
            pass
    return(None)

def ndgetlchild(nd,nds):
    if(nd.lid == None):
        return(None)
    else:
        return(idgetnd(nd.lid,nds))

def ndgetrchild(nd,nds):
    if(nd.rid == None):
        return(None)
    else:
        return(idgetnd(nd.rid,nds))

def ndgetpnd(nd,nds):
    if(nd.pid == None):
        return(None)
    else:
        return(idgetnd(nd.pid,nds))

def ndget_fst_open_ances_nd(nd,nds):
    '''
        沿着ancestors 寻找第一个状态是"open"的
    '''
    nd = ndgetpnd(nd,nds)
    visited = nd._visited
    while(visited!="open" and nd !=None):
        nd = ndgetpnd(nd,nds)
        visited = nd._visited
    return(nd)

def mdfs_next(nd,nds,mdfs_nds):
    visited = nd._visited
    # mdfs_prev_id = nd._mdfs_prev_id
    # mdfs_prev_nd = idgetnd(mdfs_prev_id,nds)
    if(visited == None):
        cond = is_leaf(nd)
        if(cond):
            #如果当前节点初次访问,并且是叶子
            #把这个节点假如访问序列 mdfs_nds
            #那么访问状态直接设为 "close"
            #下一个待访问节点是父节点(中序)
            #设置下一个待访问节点的prev_mdfs_id为当前节点id
            nd._visited = "close"
            mdfs_nds.append(nd)
            fst_open_ances_nd = ndget_fst_open_ances_nd(nd,nds)
            next_nd = fst_open_ances_nd
            next_nd._mdfs_prev_id = nd.id
        else:
            #如果当前节点初次访问,并且不是叶子
            #那么访问状态直接设为 "open"
            #下一个待访问节点是左儿子
            #设置下一个待访问节点的prev_mdfs_id为当前节点id
            nd._visited = "open"
            lchild = ndgetlchild(nd,nds)
            next_nd = lchild
            next_nd._mdfs_prev_id = nd.id
    elif(visited == "open"):
        cond = is_leaf(nd)
        if(cond):
            raise(ValueError("leaf node visited-state should NOT be open"))
        else:
            #如果当前节点再次访问
            #那么访问状态直接设为 "close"
            #把这个节点假如访问序列 mdfs_nds
            #下一个待访问节点是右儿子
            #设置下一个待访问节点的prev_mdfs_id为当前节点id
            nd._visited = "close"
            mdfs_nds.append(nd)
            rchild = ndgetrchild(nd,nds)
            next_nd = rchild
            next_nd._mdfs_prev_id = nd.id
    else:
        raise(ValueError("next mdfs node visited-state should NOT be close"))
    return((next_nd,nds,mdfs_nds))

def nds2mdfsnds(nds):
    '''
        中序遍历输出
    '''
    nds = nds_clear_visited(nds)
    lngth = len(nds)
    nd = ndsgetroot(nds)
    mdfs_nds = []
    while(len(mdfs_nds)<lngth-1):
        nd,nds,mdfs_nds = mdfs_next(nd,nds,mdfs_nds)
    mdfs_nds.append(nd)
    nds = nds_clear_visited(nds)
    mdfs_nds = nds_clear_visited(mdfs_nds)
    return(mdfs_nds)

def mdfs_prev(nd,nds)
    mdfs_prev_nd = nd_find_nearest_lt(nd,nds)
    return(mdfs_prev_nd)


#####

def get_rsib(nd,nds):
    if(is_rnd(nd)):
        return(None)
    elif(is_right(nd)):
        return(None)
    else:
        pnd = ndgetpnd(nd,nds)
        lchild,rchild = get_children(pnd,nds)
        return(rchild)

def get_fst_ances_rsib(nd,nds):
    '''
        获取第一个有rsib的ances的rsib
    '''
    while(not(is_rnd(nd))):
        rsib = get_rsib(nd,nds)
        if(rsib != None):
            return(rsib)
        else:
            nd = ndgetpnd(nd,nds)
    return(None)

def sdfs_next(nd,nds,sdfs_nds):
    '''
        sdfs 和先序遍历一样
        是层次化深度优先遍历
        sdfs: 左子树--右子树--当前节点
        先序: 当前节点-左子树-右子树
    '''
    lchild,rchild = get_children(nd,nds)
    if(lchild != None):
        #如果当前节点有左儿子
        next_nd = lchild
    elif(rchild != None):
        #如果当前节点有右儿子
        next_nd = rchild
    else:
        #否则沿着ances向上,直到找到第一个有rsib的ances
        fst_ances_rsib = get_fst_ances_rsib(nd,nds)
        next_nd = fst_ances_rsib
    sdfs_nds.append(next_nd)
    return((next_nd,nds,sdfs_nds))

def nds2sdfsnds(nds):
    '''
        sdfs 和先序遍历一样
        是层次化深度优先遍历
        sdfs: 当前节点-左子树--右子树
        先序: 当前节点-左子树-右子树
        sdfsnds = nds2sdfsnds(nds)
        elel.mapv(sdfsnds,lambda nd:nd.val)
        sdfs cmds性质: 从下到上,第一个小于当前路径长度的就是parent
    '''
    nds = nds_clear_visited(nds)
    lngth = len(nds)
    nd = ndsgetroot(nds)
    sdfs_nds = [nd]
    while(len(sdfs_nds)<lngth):
        nd,nds,sdfs_nds = sdfs_next(nd,nds,sdfs_nds)
    return(sdfs_nds)

def get_lsib(nd,nds):
    if(is_rnd(nd)):
        return(None)
    elif(is_left(nd)):
        return(None)
    else:
        pnd = ndgetpnd(nd,nds)
        lchild,rchild = get_children(pnd,nds)
        return(lchild)

def nd_get_fstbot_thenright_most_des(nd,nds):
    '''
        如果有子节点就走子节点
        如果有右子节点就走右子节点
    '''
    lchild,rchild = get_children(nd,nds)
    while(True):
        if(rchild != None):
            nd = rchild
        elif(lchild != None):
            nd = lchild
        else:
            break
        lchild,rchild = get_children(nd,nds)
    return(nd)

def sdfs_prev(nd,nds):
    lsib = get_lsib(nd,nds)
    if(lsib != None):
        nd = nd_get_fstbot_thenright_most_des(lsib,nds)
        return(nd)
    else:
        #没有左邻居,parent
        pnd = ndgetpnd(nd,nds)
        return(pnd)


#####

def get_lsib(nd,nds):
    if(is_rnd(nd)):
        return(None)
    elif(is_left(nd)):
        return(None)
    else:
        pnd = ndgetpnd(nd,nds)
        lchild,rchild = get_children(pnd,nds)
        return(lchild)

def nd_get_fstbot_thenleft_most_des(nd,nds):
    '''
        如果有子节点就走子节点
        如果有左子节点就走左子节点
    '''
    lchild,rchild = get_children(nd,nds)
    while(True):
        if(lchild != None):
            nd._visited = "open"
            nd = lchild
        elif(rchild != None):
            nd._visited = "open"
            nd = rchild
        else:
            break
        lchild,rchild = get_children(nd,nds)
    return(nd)


def nd_get_fstbot_thenleft_most_des_andthen_appending(nd,nds,sedfs_nds):
    '''
        如果有子节点就走子节点
        如果有左子节点就走左子节点
    '''
    lchild,rchild = get_children(nd,nds)
    while(True):
        if(lchild != None):
            nd._visited = "open"
            sedfs_nds.append(nd)
            nd = lchild
        elif(rchild != None):
            nd._visited = "open"
            sedfs_nds.append(nd)
            nd = rchild
        else:
            break
        lchild,rchild = get_children(nd,nds)
    return(nd)



def ndget_fstf_thenr_child(nd,nds):
    lchild,rchild = get_children(nd,nds)
    child = lchild if(lchild != None) else rchild
    return(child)


def ndget_fst_open_ances(nd,nds):
    while(not(is_rnd(nd))):
        nd = ndgetpnd(nd,nds)
        if(nd._visited == "open"):
            return(nd)
        else:
            pass
    return(None)

def edfs_next(nd,nds,edfs_nds):
    visited = nd._visited
    if(visited == None):
        cond = is_leaf(nd)
        if(cond):
            #如果当前节点初次访问,并且是叶子
            #把这个节点假如访问序列 edfs_nds
            #那么访问状态直接设为 "close"
            #下一个待访问节点是右邻居的最下最左,如果没有右邻居:parent
            #设置下一个待访问节点的prev_edfs_id为当前节点id
            nd._visited = "close"
            edfs_nds.append(nd)
            rsib = get_rsib(nd,nds)
            if(rsib == None):
                #如果没有右邻居,返回parent
                next_nd = ndgetpnd(nd,nds)
            else:
                #如果有右邻居,返回右邻居的最下最左
                fstbot_thenleft_most_des = nd_get_fstbot_thenleft_most_des(rsib,nds)
                next_nd = fstbot_thenleft_most_des
        else:
            #如果当前节点初次访问,并且不是叶子
            #那么访问状态直接设为 "open"
            #下一个待访问节点是儿子(左儿子优先)
            #设置下一个待访问节点的prev_edfs_id为当前节点id
            nd._visited = "open"
            fstl_thenr_child = ndget_fstf_thenr_child(nd,nds)
            next_nd = fstl_thenr_child
    elif(visited == "open"):
        cond = is_leaf(nd)
        if(cond):
            raise(ValueError("leaf node visited-state should NOT be open"))
        else:
            #如果当前节点再次访问
            #那么访问状态直接设为 "close"
            #把这个节点假如访问序列 edfs_nds
            # 下一个待访问节点是右邻居的最下最左，如果没有右邻居就是 parent
            # 也就是
            #设置下一个待访问节点的prev_edfs_id为当前节点id
            nd._visited = "close"
            edfs_nds.append(nd)
            ####
            rsib = get_rsib(nd,nds)
            if(rsib == None):
                #如果没有右邻居,返回parent
                next_nd = ndgetpnd(nd,nds)
            else:
                #如果有右邻居,返回右邻居的最下最左
                fstbot_thenleft_most_des = nd_get_fstbot_thenleft_most_des(rsib,nds)
                next_nd = fstbot_thenleft_most_des
            ####
    else:
        raise(ValueError("next edfs node visited-state should NOT be close"))
    return((next_nd,nds,edfs_nds))


def nds2edfsnds(nds):
    '''
        edfs 不是序后遍历
        是层次化深度优先遍历
        edfs: 左子树--右子树--当前节点
        后序: 左子树--右子树--当前节点
        edfs_nds = nds2edfsnds(nds)
        elel.mapv(edfs_nds,lambda nd:nd.val)
        edfs cmds性质: 从上到下,第一个小于当前路径长度的就是parent
    '''
    nds = nds_clear_visited(nds)
    lngth = len(nds)
    nd = ndsgetroot(nds)
    edfs_nds = []
    while(len(edfs_nds)<lngth):
        nd,nds,edfs_nds = edfs_next(nd,nds,edfs_nds)
    nds = nds_clear_visited(nds)
    edfs_nds = nds_clear_visited(edfs_nds)
    return(edfs_nds)


#####

def sedfs_next(nd,nds,sedfs_nds):
    '''
        open 加一次,close 加一次
        sdefs 是为了 输出有闭合的html
    '''
    visited = nd._visited
    if(visited == None):
        cond = is_leaf(nd)
        if(cond):
            #如果当前节点初次访问,并且是叶子
            #把这个节点假如访问序列 sedfs_nds,添加两次：叶子节点open->close
            #那么访问状态直接设为 "close"
            #下一个待访问节点是右邻居的最下最左,如果没有右邻居:parent
            #设置下一个待访问节点的prev_sedfs_id为当前节点id
            nd._visited = "close"
            sedfs_nds.append(nd)
            sedfs_nds.append(nd)
            rsib = get_rsib(nd,nds)
            if(rsib == None):
                #如果没有右邻居,返回parent
                next_nd = ndgetpnd(nd,nds)
            else:
                #如果有右邻居,返回右邻居的最下最左
                fstbot_thenleft_most_des = nd_get_fstbot_thenleft_most_des_andthen_appending(rsib,nds,sedfs_nds)
                next_nd = fstbot_thenleft_most_des
        else:
            #如果当前节点初次访问,并且不是叶子
            #那么访问状态直接设为 "open"
            ##把这个节点假如访问序列 sedfs_nds
            #下一个待访问节点是儿子(左儿子优先)
            #设置下一个待访问节点的prev_sedfs_id为当前节点id
            nd._visited = "open"
            sedfs_nds.append(nd)
            fstl_thenr_child = ndget_fstf_thenr_child(nd,nds)
            next_nd = fstl_thenr_child
    elif(visited == "open"):
        cond = is_leaf(nd)
        if(cond):
            raise(ValueError("leaf node visited-state should NOT be open"))
        else:
            #如果当前节点再次访问
            #那么访问状态直接设为 "close"
            #把这个节点假如访问序列 sedfs_nds
            # 下一个待访问节点是右邻居的最下最左，如果没有右邻居就是 parent
            # 也就是
            #设置下一个待访问节点的prev_sedfs_id为当前节点id
            nd._visited = "close"
            sedfs_nds.append(nd)
            ####
            rsib = get_rsib(nd,nds)
            if(rsib == None):
                #如果没有右邻居,返回parent
                next_nd = ndgetpnd(nd,nds)
            else:
                #如果有右邻居,返回右邻居的最下最左
                fstbot_thenleft_most_des = nd_get_fstbot_thenleft_most_des_andthen_appending(rsib,nds,sedfs_nds)
                next_nd = fstbot_thenleft_most_des
            ####
    else:
        #raise(ValueError("next sedfs node visited-state should NOT be close"))
        return("finished")
    return((next_nd,nds,sedfs_nds))

def nds2sedfsnds(nds):
    '''
        sedfs: 当前节点-左子树--右子树--当前节点
        sedfs_nds = nds2sedfsnds(nds)
        elel.mapv(sedfs_nds,lambda nd:nd.val)
        sedfs cmds性质: 成对出现,对应open,close
    '''
    nds = nds_clear_visited(nds)
    lngth = len(nds)
    nd = ndsgetroot(nds)
    sedfs_nds = []
    while(len(sedfs_nds)<lngth*2):
        nd,nds,sedfs_nds = sedfs_next(nd,nds,sedfs_nds)
    nds = nds_clear_visited(nds)
    sedfs_nds = nds_clear_visited(sedfs_nds)
    return(sedfs_nds)

#####

def nds_get_leaf_nds(nds):
    leaf_nds = []
    for nd in nds:
        cond = is_leaf(nd)
        if(cond):
            leaf_nds.append(nd)
        else:
            pass
    return(leaf_nds)

def nds_get_nonleaf_nds(nds):
    nonleaf_nds = []
    for nd in nds:
        cond = is_leaf(nd)
        if(cond):
            pass
        else:
            nonleaf_nds.append(nd)
    return(nonleaf_nds)

def nd_get_ances_nds(nd,nds):
    ances = [nd]
    nd = ndgetpnd(nd,nds)
    while(nd!=None):
        ances.append(nd)
        nd = ndgetpnd(nd,nds)
    return(ances)

def nds_get_all_chains(nds):
    '''
        获取所有路径
    '''
    leaf_nds = nds_get_leaf_nds(nds)
    chains= []
    for nd in leaf_nds:
        chain = nd_get_ances_nds(nd,nds)
        chains.append(chain)
    return(chains)


def chain_get_black_nd_num(chain):
    '''
        任意从根到叶子的路径的黑色节点总数相同
    '''
    c = 0
    for nd in chain:
        if(nd.clr == "black"):
            c = c + 1
        else:
            pass
    return(c)


def chain_not_contain_ge_two_continuous_red(chain):
    for i in range(0,len(chain)-1):
        nd = chain[i]
        next_nd = chain[i+1]
        cond = (nd.clr == "red") and (next_nd.clr == "red")
        return(False)
    return(True)


def rnd_match_rule_zero(rnd):
    '''
        根节点必须是黑色
    '''
    return(rnd.clr == "black")

def chains_match_rule_one(chains):
    '''
        任意从根到叶子的路径不包含连续的红色节点
    '''
    bool_array = list(map(chain_not_contain_ge_two_continuous_red,chains))
    for bl in bool_array:
        if(bl):
            return(False)
        else:
            pass
    return(True)


def chains_match_rule_two(chains):
    '''
        任意从根到叶子的路径的黑色节点总数相同
    '''
    num_array = list(map(chain_get_black_nd_num,chains))
    c = list(filter(lambda ele:ele!=num_array[0],num_array)).__len__()
    return(c==0)


def nds_is_rbtree(nds):
    '''
        规则1、根节点必须是黑色。
        规则2、任意从根到叶子的路径不包含连续的红色节点。
        规则3、任意从根到叶子的路径的黑色节点总数相同。
    '''
    rnd = ndsgetroot(nds)
    chains = nds_get_all_chains(nds)
    cond0 = rnd_match_rule_zero(rnd)
    cond1 = chains_match_rule_one(chains)
    cond2 = chains_match_rule_two(chains)
    return((cond0 and cond1 and cond2))

##########################

def new_black_nd(val,id):
    '''
    '''
    nd = Node()
    nd.clr = "black"
    nd.val = val
    nd.id = id
    return(nd)

def new_root_nd(val,id):
    '''
    '''
    nd = new_black_nd(val)
    nd.id = id
    return(nd)

def new_red_nd(val,id):
    '''
    '''
    nd = Node()
    nd.clr = "red"
    nd.val = val
    nd.id = id
    return(nd)

def get_children(nd,nds):
    children = [idgetnd(nd.lid,nds),idgetnd(nd.rid,nds)]
    return(children)


def rnd_find_insert_new_node(nnd,rnd,nds):
    '''
        找到新节点的插入位置
    '''
    nd = rnd
    while(True):
        lchild,rchild = get_children(nd,nds)
        if(nd.val<= nnd.val):
            if(rchild == None):
                nd.rid = nnd.id
                nnd.pid = nd.id
                nds.append(nnd)
                break
            else:
                nd = rchild
        else:
            if(lchild == None):
                nd.lid = nnd.id
                nnd.pid = nd.id
                nds.append(nnd)
                break
            else:
                nd = lchild
    return(nnd)


def nd_find_minnd(nd,nds):
    '''
        最左最下，有可能不是叶子节点 (例如只有右子树)
    '''
    if(is_leaf(nd)):
        return(nd)
    else:
        parent = nd
        lchild,rchild = get_children(nd,nds)
        while(lchild != None):
            parent = lchild
            lchild,rchild = get_children(lchild,nds)
        return(parent)


def nd_find_maxnd(nd,nds):
    '''
        最右最下，有可能不是叶子节点 (例如只有左子树)
    '''
    if(is_leaf(nd)):
        return(nd)
    else:
        parent = nd
        lchild,rchild = get_children(nd,nds)
        while(rchild != None):
            parent = rchild
            lchild,rchild = get_children(rchild,nds)
        return(parent)

def nd_get_left_child(nd):
    lnd = idgetnd(nd.lid,nds)
    return(lnd)

def nd_get_right_child(nd):
    rnd = idgetnd(nd.rid,nds)
    return(rnd)

def is_left(nd):
    pnd = ndgetpnd(nd,nds)
    if(pnd == None):
        return(None)
    else:
        cond = (pnd.lid == nd.id)
        return(cond)

def is_right(nd):
    pnd = ndgetpnd(nd,nds)
    if(pnd == None):
        return(None)
    else:
        cond = (pnd.rid == nd.id)
        return(cond)


def nd_find_fst_left_ances(nd,nds):
    '''
        找到祖先链上第一个左节点
    '''
    while(nd!=None):
        if(is_left(nd)):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)

def nd_find_fst_right_ances(nd,nds):
    '''
        找到祖先链上第一个右节点
    '''
    while(nd!=None):
        if(is_right(nd)):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)

def nd_find_fst_left_real_ances(nd,nds):
    '''
        找到祖先链上第一个左节点
    '''
    nd = ndgetpnd(nd,nds)
    while(nd!=None):
        if(is_left(nd)):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)

def nd_find_fst_right_real_ances(nd,nds):
    '''
        找到祖先链上第一个右节点
    '''
    nd = ndgetpnd(nd,nds)
    while(nd!=None):
        if(is_right(nd)):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)

def nd_find_fst_lt_real_ances(nd,nds):
    '''
    '''
    val =nd.val
    nd = ndgetpnd(nd,nds)
    while(nd!=None):
        if(nd.val<val):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)

def nd_find_fst_gt_real_ances(nd,nds):
    '''
    '''
    val =nd.val
    nd = ndgetpnd(nd,nds)
    while(nd!=None):
        if(nd.val>val):
            return(nd)
        else:
            pass
        nd = ndgetpnd(nd,nds)
    return(nd)


def is_rnd(nd):
    return(nd.pid==None)

def nd_find_nearest_lt(nd,nds):
    '''
        如果是根节点:
            首先排除右子树,右子树均大于当前节点
            如果有左子树:
                然后要找左子树最大的
            否则:
                返回None, 根节点没有左子树, 说明整个二叉树只有一个根节点
        否则:
            如果有左子树:
                然后要找左子树最大的
            否则一定是叶子节点:
                如果是右节点:
                    一定是parent
                        1.因为parent lt 当前节点,满足必要条件
                        2.因为任意一个节点 如果是左节点,那么这个节点的parent就会大于所有这个节点的 子树
                          所以，沿着 parent向上 直到根节点的 ances为p1,p2,p3,p4,.....pk,r 
                          对于任意一个不在ances链上的node,  这个node 和 parent的关系
                          首先这个node肯定可以和当前node 找到一个 共同的ances, 这个点不可能和curr在同一侧
                          要么在ances链上,要么和curr_node在ances的两侧
                          如果这个node 在 ances 的右子树  node.val > curr.val 不考虑
                          如果这个node 在 ances 的左子树  node.val < ances.val < curr.val , node.val <ances.val< parent.val,
                          curr.val-parent.val  + parent.val - ances.val + ances.val- node.val >= curr.val-parent.val
                          #
                          0<curr.val - parent.val +parent.val - node.val > curr.val - parent.val
                如果是左节点:
                    同上和curr.val 相差最小的一定在ances链上
                    设ances链为  curr p0,p1,p2....pk，pk+1....ances  假如pk是链上第一个右节点
                    curr<p0<p1<p2....<pk 
                    curr>pk+1 
                    curr 向上找到第一个是左节点的ancestor,画图很容易证明，沿着ances链往下,
                    如果某个节点的后代链是左子树，那这个节点val > curr.val ,不考虑
                    如果某个节点的后代链是右子树，那这个节点val < curr.val ,val< pk+1
                    0<curr.val - pk+1  + pk+1 - val  = curr.val  - val找到链上第一个小于curr的
                    
    '''
    if(is_rnd(nd)):
        lchild = nd_get_left_child(nd)
        if(lchild != None):
            nd = nd_find_maxnd(lchild,nds)
            return(nd)
        else:
            return(None)
    else:
        lchild = nd_get_left_child(nd)
        if(lchild != None):
            nd = nd_find_maxnd(lchild,nds)
            return(nd)
        else:
            if(is_right(nd)):
                pnd = ndgetpnd(nd,nds)
                return(pnd)
            else:
                fst_lt_ancesnd = nd_find_fst_lt_real_ances(nd,nds)
                return(fst_lt_ancesnd)

def nd_find_nearest_gt(nd,nds):
    '''
        如果是根节点:
            因为左子树均小于当前节点,首先排除左子树
            如果有右子树:
                然后要找右子树最小的
            否则:
                返回None, 根节点没有右子树, 说明整个二叉树只有一个根节点
        否则:
            如果有右子树:
                然后要找右子树最小的,(这个点不一定是叶子节点)
            否则一定是叶子节点:
                如果是左节点:
                    一定是parent
                如果是右节点:
                    同上和curr.val 相差最小的一定在ances链上
                    0<curr.val - pk+1  + pk+1 - val  = curr.val  - val找到链上第一个大于curr的
                    
    '''
    if(is_rnd(nd)):
        rchild = nd_get_right_child(nd)
        if(rchild != None):
            nd = nd_find_minnd(rchild,nds)
            return(nd)
        else:
            return(None)
    else:
        rchild = nd_get_right_child(nd)
        if(rchild != None):
            nd = nd_find_minnd(rchild,nds)
            return(nd)
        else:
            if(is_left(nd)):
                pnd = ndgetpnd(nd,nds)
                return(pnd)
            else:
                fst_gt_ancesnd = nd_find_fst_gt_real_ances(nd,nds)
                return(fst_gt_ancesnd)

def nd_find_nearest(nd,nds):
    '''
        找到相差最小的
    '''
    nearest_lt = nd_find_nearest_lt(nd,nds)
    nearest_gt = nd_find_nearest_gt(nd,nds)
    if(nearest_lt == None):
        return(nearest_gt)
    else:
        pass
    if(nearest_gt == None):
        return(nearest_lt)
    else:
        pass
    diff_lt = (nd.val - nearest_lt.val) 
    diff_gt = (nearest_gt.val - nd.val) 
    nd = nearest_lt if(diff_lt < diff_gt) else nearest_gt
    return(nd)

def is_has_only_lchild(nd,nds):
    lchild,rchild = get_children(nd,nds)
    condl = (lchild != None)
    condr = (rchild == None)
    return(condl and condr)

def is_has_only_rchild(nd,nds):
    lchild,rchild = get_children(nd,nds)
    condl = (lchild == None)
    condr = (rchild != None)
    return(condl and condr)

def is_has_only_one_child(nd,nds):
    lchild,rchild = get_children(nd,nds)
    condl = (lchild != None) and (rchild == None)
    condr = (lchild == None) and (rchild != None)
    return(condl or condr)


def id_del_nd_from_nds(id,nds):
    nnds = nds[:]
    for i in range(len(nds)):
        nd = nds[i]
        if(id == nd.id):
            nnds.pop(i)
            break
        else:
            pass
    return(nnds)

def bin_tree_delete(nd,nds):
    '''
        
    '''
    pnd = ndgetpnd(nd,nds)
    id = nd.id
    if(pnd == None):
        #根节点,删除根节点的话, nds变空
        nds = []
    else:
        pass
    if(is_leaf(nd)):
        #删除叶子节点
        if(is_left(nd,nds)):
            #如果是是左叶子
            #父节点lid置空
            #nds 删除当前节点
            nds = id_del_nd_from_nds(id,nds)
            pnd.lid = None
        if(is_right(nd,nds)):
            #如果是是右叶子
            #父节点rid置空
            #nds 删除当前节点
            nds = id_del_nd_from_nds(id,nds)
            pnd.rid = None
    elif(is_has_only_lchild(nd,nds)):
        # 只有左子树的节点
        nds = id_del_nd_from_nds(id,nds)
        lchild,rchild = get_children(nd,nds)
        if(is_left(nd,nds)):
            #如果是是左叶子
            #父节点lid 连接 左子树
            #更新左子树 父节点
            #nds 删除当前节点
            pnd.lid = lchild.id
            lchild.pid = pnd.id
        if(is_right(nd,nds)):
            #如果是是右叶子
            #父节点lid 连接 右子树
            #更新右子树 父节点
            #nds 删除当前节点
            pnd.rid = lchild.id
            lchild.pid = pnd.id
    elif(is_has_only_rchild(nd,nds)):
        # 只有右子树的节点
        nds = id_del_nd_from_nds(id,nds)
        lchild,rchild = get_children(nd,nds)
        if(is_left(nd,nds)):
            #如果是是左叶子
            #父节点lid 连接 左子树
            #更新左子树 父节点
            #nds 删除当前节点
            pnd.lid = rchild
            rchild.pid = pnd.id
        if(is_right(nd,nds)):
            #如果是是右叶子
            #父节点rid 连接 右子树
            #更新右子树 父节点
            #nds 删除当前节点
            pnd.rid = rchild
            rchild.pid = pnd.id
    else:
        #同时有左右子树
        lchild,rchild = get_children(nd,nds)
        #找到右子树中最小的节点作为后继节点
        #    可以证明,这个点要么是叶子节点,要么没有左子树
        succ_nd = nd_find_nearest_gt(nd,nds)
        #把当前节点的左子树 链到后继节点
        succ_nd.lid = lchild.id
        lchild.pid = succ_nd.id
        #把当前节点的右子树链到当前节点的父节点
        if(is_left(nd)):
            pnd.lid = rchild.id
            rchild.pid = pnd.id
        else:
            pnd.rid = rchild.id
            rchild.pid = pnd.id
        #nds 删除当前节点
        nds = id_del_nd_from_nds(id,nds)
    return(nds)

#######################

import elist.elist as elel
from nvhtml import struct_show
from nvhtml import rshtml
from lxml.etree import HTML as LXHTML


def nds_set_tag_clr_md(nds):
    struct_show.TAG_COLOR_MD['html'] = 0
    struct_show.TAG_COLOR_MD['body'] = 0
    for nd in nds:
        tag = "v"+str(nd.val)
        clr = 1 if(nd.clr=="red") else 15
        struct_show.TAG_COLOR_MD[tag] = clr
    return(struct_show.TAG_COLOR_MD)



def ndgetdepth(nd,nds):
    return(len(nd_get_ances_nds(nd,nds))-1)

def nds2rsh(nds):
    '''
        rsh = nds2rsh(nds)
    '''
    sdfsnds = nds2sdfsnds(nds)
    depths = elel.mapv(sdfsnds,lambda nd:ndgetdepth(nd,nds))
    lns = elel.mapiv(depths,lambda i,depth:"    "*depth+"v"+str(sdfsnds[i].val))
    rsh = elel.join(lns,"\n")
    return(rsh)

def display_rbtree(nds):
    struct_show.TAG_COLOR_MD = nds_set_tag_clr_md(nds)
    rsh = nds2rsh(nds)
    html_str = rshtml.rsh2html(rsh)
    root = LXHTML(html_str)
    wfs = engine.WFS(root)
    mat = wfs.mat
    mat = scan_s0(mat)
    disp_mat = creat_display_mat(mat)
    mat = elel.mat_mapv(mat,modi_width_s0)
    mat = scan_s1(mat)
    mat =  scan_s2(mat)
    mat =  scan_s3(mat)
    disp_mat = scan_disp_mat_s0(disp_mat,mat,color_enable=True)
    show_tag_tb(disp_mat[2:])

#######################

#第一个有rsib的先祖
#fst_ances_with_rsib
#fst_ances_with_rsib_get_rsib
#第一个有lsib的先祖
#fst_ances_with_lsib
#fst_ances_with_lsib_get_lsib

#next 右邻居子树最下最左
#rsib_get_fstbotmost_thenleftmost_des
#prev 左邻居子树最下最右
#lsib_get_fstbotmost_thenleftmost_des


###########################
#红黑树 左旋 与 右旋
###########################

def get_branch(nd):
    if(is_rnd(nd)):
        return(None)
    else:
        if(is_left(nd)):
            return("left")
        else:
            return("right")


def root_get_wfsnds(rnd,nds):
    # init nonleaf_unhandled
    cond = is_leaf(rnd)
    nonleaf_unhandled = [] if(cond) else [rnd]
    wfsnds = [rnd]
    #
    while(len(nonleaf_unhandled) > 0):
        childrens = elel.mapv(nonleaf_unhandled,get_children,[nds])
        lyr =  elel.concat_seqs(childrens)
        # get_children 函数叶子节点可以是None, 也可以是lid,rid 均为None的节点
        # 所以要过滤一次
        lyr =  elel.filter(lyr,lambda nd:(nd != None))
        wfsnds = wfsnds + lyr
        nonleaf_unhandled = elel.filter(lyr,lambda nd:not(is_leaf(nd)))
    return(wfsnds)

def tear(nd,nds):
    rnd = ndsgetroot(nds)
    pnd = ndgetpnd(nd,nds)
    if(pnd == None):
        # 从nds中移除tear的节点
        nds = []
        return((nd,nds))
    else:
        if(is_left(nd)):
            pnd.lid = None
        else:
            pnd.rid = None
        nd.pid = None
        # 从nds中移除tear的节点
        nds = root_get_wfsnds(rnd,nds)
        return((nd,nds))

#################
#################


def conn(branch,nd,npnd,nds):
    #从原父节点tear_down
    nd = tear(nd,nds)
    #链接新父节点
    if(npnd == None):
        nd.pid = None
        rplced = npnd
        return((nd,npnd,rplced))
    else:
        nd.pid = npnd.id
        lchild,rchild = get_children(npnd,nds)
        if(branch == "left"):
            if(lchild == None):
                rplced = None
            else:
                rplced = tear(lchild,nds)
            npnd.lid = nd.id
        else:
            if(rchild == None):
                rplced = None
            else:
                rplced = tear(rchild,nds)
            npnd.rid = nd.id
        return((nd,npnd,rplced))

def rot_left(nd,nds):
    pnd = ndgetpnd(nd,nds)
    lchild,rchild = get_children(nd,nds)
    rchild_left,rchild_right = get_children(rchild,nds)
    #把nd 从其父节点移除
    tear(nd,nds)
    #把rchild 连接到nd的父节点
    branch = get_branch(nd)
    conn(branch,rchild,pnd,nds)
    #把右儿子的左子 变为右儿子
    conn("right",rchild_left,nd,nds)
    return(nd)

def rot_right(nd,nds):
    '''
        -------------------
        |       v35       |
        -------------------
        | v27 |    v45    |
        -------------------
        |     | v40 | v48 |
        -------------------
        tstnds = copy.deepcopy(nds)
    '''
    pnd = ndgetpnd(nd,nds)
    lchild,rchild = get_children(nd,nds)
    rchild_left,rchild_right = get_children(rchild,nds)
    #把nd 从其父节点移除
    tear(nd,nds)
    #把lchild 连接到nd的父节点
    branch = get_branch(nd)
    conn(branch,lchild,pnd,nds)
    #把左儿子的右子 变为左儿子
    conn("left",rchild_right,nd,nds)
    return(nd)

