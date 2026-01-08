def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    mats.sort(reverse=True)

    for mat in mats:
        for i in range(rows):
            for j in range(cols):
                if i + mat <= rows and j + mat <= cols:
                   
                    is_ok = True

                    
                    for k in range(i, i + mat):
                        for z in range(j, j + mat):
                            
                            if park[k][z] != "-1":
                                is_ok = False 
                                break         

                        
                        if is_ok == False:
                            break

                    if is_ok == True:
                        return mat 

    return -1
