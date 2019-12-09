def won(lst):
    count=0                    #initialises the count of blasted ships to zero
    for i in range(5):
        for j in range(5):
            if lst[i][j]=='Bl':#checks whether the box in grid is occupied by ship
                count+=1       #incrments the count of blasted ships
    if count==6:             
        return True
