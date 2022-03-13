natije = int (input())
points = 0
bords = 0
games = 0
for games in range (1, 31):
    if natije == 3:
        bords +=1
        games +=1
        points = points + 3
        natije = int (input())
    elif natije == 1:
        games +=1
        points +=1
        natije = int (input())
    else:
        games +=1
        natije = int (input())
    if games == 30:
        break
print (points, bords)
