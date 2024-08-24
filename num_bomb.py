def minrob():
    earth = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    earth[0][0] = int(input('enter 0 or 1: '))
    earth[0][1] = int(input('enter 0 or 1: '))
    earth[0][2] = int(input('enter 0 or 1: '))
    earth[1][0] = int(input('enter 0 or 1: '))
    earth[1][1] = int(input('enter 0 or 1: '))
    earth[1][2] = int(input('enter 0 or 1: '))
    earth[2][0] = int(input('enter 0 or 1: '))
    earth[2][1] = int(input('enter 0 or 1: '))
    earth[2][2] = int(input('enter 0 or 1: '))
    earth_min = [[0,0,0],
                 [0,0,0],
                 [0,0,0]] 
    for i in range(0,3):
        for j in range(0,3):
            if i==0 and j==0:
                earth_min[i][j] = earth[i+1][j] + earth[i][j+1]
            elif i==0 and j==1:
                earth_min[i][j] = earth[i+1][j] + earth[i][j+1] + earth[i][j-1]
            elif i==0 and j==2:
                earth_min[i][j] = earth[i][j-1] + earth[i+1][j]
            elif i==1 and j==0:
                earth_min[i][j] = earth[i][j+1] + earth[i+1][j] + earth[i-1][j]
            elif i==1 and j==1:
                earth_min[i][j] = earth[i][j+1] + earth[i+1][j] + earth[i-1][j] + earth[i][j-1]
            elif i==1 and j==2:
                earth_min[i][j] = earth[i-1][j] + earth[i+1][j] + earth[i-1][j-1]
            elif i==2 and j==0:
                earth_min[i][j] = earth[i][j+1] + earth[i-1][j]  
            elif i==2 and j==1:
                earth_min[i][j] = earth[i][j+1] + earth[i][j-1] + earth[i-1][j]
            elif i==2 and j==2:
                earth_min[i][j] = earth[i][j-1] + earth[i-1][j]  

    return(earth_min)

print(minrob())