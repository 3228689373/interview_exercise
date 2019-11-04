



def get_left_loc(loc):
    x,y=loc
    if(y==0):
        return(None)
    else:
        return((x,y-1))

def get_right_loc(loc,columns):
    x,y=loc
    if(y>=columns-1):
        return(None)
    else:
        return((x,y+1))

def get_up_loc(loc):
    x,y=loc
    if(x==0):
        return(None)
    else:
        return((x-1,y))

def get_down_loc(loc,rows):
    x,y=loc
    if(x>=rows-1):
        return(None)
    else:
        return((x+1,y))


def get_adjacent_locs(loc,rows,columns):
    x,y=loc
    left = get_left_loc(loc)
    right = get_right_loc(loc,columns)
    up = get_up_loc(loc)
    down = get_down_loc(loc,rows)
    locs = [left,right,up,down]
    locs = list(filter(lambda loc:loc!=None,locs))
    return(locs)


def loc_get_value(loc,grid):
    x,y = loc
    return(grid[x][y])

def get_adjacent_values(loc,grid):
    rows = len(grid)
    columns = len(grid[0])
    locs = get_adjacent_locs(loc,rows,columns)
    values = list(map(lambda loc:loc_get_value(loc,grid),locs))
    return(values)





def is_finished(grid):
    rows = len(grid)
    columns = len(grid[0])
    should_be = rows * columns
    sm = 0
    for lyr in grid:
        sm = sm + sum(lyr) 
    if(sm == should_be):
        return(True)
    else:
        return(False)


def get_zero_locs(grid):
    rows = len(grid)
    columns = len(grid[0])
    rslt = []
    for i in range(rows):
        lyr = grid[i]
        for j in range(columns):
            ele = lyr[j]
            if(ele == 0):
                rslt.append((i,j))
            else:
                pass
    return(rslt)


def get_one_locs(grid):
    rows = len(grid)
    columns = len(grid[0])
    rslt = []
    for i in range(rows):
        lyr = grid[i]
        for j in range(columns):
            ele = lyr[j]
            if(ele == 1):
                rslt.append((i,j))
            else:
                pass
    return(rslt)

import copy


def round(zero_locs,grid):
    nlocs = zero_locs[:]
    ngrid = copy.deepcopy(grid)
    for loc in zero_locs:
        tmp_values = get_adjacent_values(loc,grid)
        if(1 in tmp_values):
            x,y = loc
            ngrid[x][y] = 1
            nlocs.remove(loc)
        else:
            pass
    return((nlocs,ngrid))



def final(grid):
    zero_locs = get_zero_locs(grid)
    finished = is_finished(grid)
    hours = 0
    while(not(finished)):
        zero_locs,grid = round(zero_locs,grid)
        hours = hours + 1
        finished = is_finished(grid)
    return(hours)



# rows= 4
# columns = 5
# grid = [
   # [0,1,1,0,1],
   # [0,1,0,1,0],
   # [0,0,0,0,1],
   # [0,1,0,0,0]
# ]


# zero_locs = get_zero_locs(grid)
# grid = [
   # [0,1,1,0,1],
   # [0,1,0,1,0],
   # [0,0,0,0,1],
   # [0,1,0,0,0]
# ]

# zero_locs,ngrid = round(zero_locs,grid)

# ngrid = [
   # [1,1,1,1,1],
   # [1,1,1,1,1],
   # [0,1,0,1,1],
   # [1,1,1,0,1]
# ]

# zero_locs,ngrid = round(zero_locs,ngrid)
