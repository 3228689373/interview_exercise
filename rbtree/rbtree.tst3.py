nds = copy.deepcopy(nds_bak)
tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[3],tstnds)
display_rbtree(tstnds)


-------------------------------
|             v50             |
-------------------------------
|       v35       |    v78    |
-------------------------------
| v27 |    v45    | v56 | v90 |
-------------------------------
|     | v40 | v48 |     |     |
-------------------------------

tstnds[3] 27


-------------------------
|          v50          |
-------------------------
|    v35    |    v78    |
-------------------------
|    v45    | v56 | v90 |
-------------------------
| v40 | v48 |     |     |
-------------------------



tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[1],tstnds)
display_rbtree(tstnds)

-------------------------------
|             v50             |
-------------------------------
|       v35       |    v78    |
-------------------------------
| v27 |    v45    | v56 | v90 |
-------------------------------
|     | v40 | v48 |     |     |
-------------------------------

tstnds[1] 35

-------------
|    v50    |
-------------
|    v78    |
-------------
| v56 | v90 |
-------------



tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[2],tstnds)
display_rbtree(tstnds)


-------------------------------
|             v50             |
-------------------------------
|       v35       |    v78    |
-------------------------------
| v27 |    v45    | v56 | v90 |
-------------------------------
|     | v40 | v48 |     |     |
-------------------------------

tstnds[2] 78

-------------------
|       v50       |
-------------------
|       v35       |
-------------------
| v27 |    v45    |
-------------------
|     | v40 | v48 |
-------------------



tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[4],tstnds)
display_rbtree(tstnds)


>>> tstnds = copy.deepcopy(nds)
>>> display_rbtree(tstnds)
-------------------------------
|             v50             |
-------------------------------
|       v35       |    v78    |
-------------------------------
| v27 |    v45    | v56 | v90 |
-------------------------------
|     | v40 | v48 |     |     |
-------------------------------
>>> elel.mapv(tstnds,lambda nd:nd.val)
[50, 35, 78, 27, 45, 56, 90, 40, 48]
>>> nd,tstnds= tear(tstnds[4],tstnds)
>>> display_rbtree(tstnds)
-------------------
|       v50       |
-------------------
| v35 |    v78    |
-------------------
| v27 | v56 | v90 |
-------------------
>>>


tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[5],tstnds)
display_rbtree(tstnds)



tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[6],tstnds)
display_rbtree(tstnds)


tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[7],tstnds)
display_rbtree(tstnds)


tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[8],tstnds)
display_rbtree(tstnds)


tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)
nd,tstnds= tear(tstnds[0],tstnds)
display_rbtree(tstnds)


###################
###################


nds = copy.deepcopy(nds_bak)
tstnds = copy.deepcopy(nds)
display_rbtree(tstnds)
elel.mapv(tstnds,lambda nd:nd.val)

