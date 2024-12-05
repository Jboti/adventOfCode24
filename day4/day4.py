#p1

# f = open("input.txt","r")
# M = []
# xmasCount = 0
# word = "XMAS"
# for line in f.readlines():
#     M.append(line.strip())
# DIRS = [
#     (-1,0),(1,0), #függöleges
#     (0,-1),(0,1), #vízszint
#     (-1,-1),(1,1), #bal átló
#     (-1,1),(1,-1) #jobb átló
# ]
                    
# def Valid(i, j):    
#     return 0 <= i < len(M) and 0 <= j < len(M[0])

                       
# for i in range(len(M)):
#     for j in range(len(M[i])):
#         if M[i][j] == word[0]:
#             for x,y in DIRS:
#                 found = True
#                 for k in range(1,4):
#                     newi = i+k*x
#                     newj = j+k*y
#                     if not Valid(newi,newj) or M[newi][newj] != word[k]:
#                         found = False
#                         break
#                 if found:
#                     xmasCount+=1
# print(xmasCount)


#p2

f = open("input.txt","r")
M = []
for line in f.readlines():
    M.append(line.strip())

ans = 0

for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == "A":
            if i-1>=0 and i+1<len(M) and j-1>=0 and j+1<len(M[0]):
                if M[i-1][j-1] == "M" and M[i+1][j-1] == "M" and M[i-1][j+1] == "S" and M[i+1][j+1]=="S":
                    ans+=1
                if M[i-1][j-1] == "S" and M[i+1][j-1] == "M" and M[i-1][j+1] == "S" and M[i+1][j+1]=="M":
                    ans+=1
                if M[i-1][j-1] == "S" and M[i+1][j-1] == "S" and M[i-1][j+1] == "M" and M[i+1][j+1]=="M":
                    ans+=1
                if M[i-1][j-1] == "M" and M[i+1][j-1] == "S" and M[i-1][j+1] == "M" and M[i+1][j+1]=="S":
                    ans+=1
print(ans)