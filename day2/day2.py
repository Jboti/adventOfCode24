#p1

# f = open("input.txt","r")
# safeCount = 0

# def IsValid(line):
#     asc = None
#     for i in range(len(line) - 1):
#         if(not(0 < abs(line[i]-line[i+1]) < 4)):
#             return False
#         else:
#             if(asc == None):
#                 if(line[i]<line[i+1]):
#                     asc = True
#                 else:
#                     asc = False
#             else:
#                 if((asc==True and line[i]>line[i+1]) or (asc == False and line[i]<line[i+1])):
#                     return False                
#     return True
                


# for line in f.readlines():
#     line = [int(x) for x in line.split(' ')]
#     if(IsValid(line)):
#         safeCount += 1

# print(safeCount)



#p2

f = open("input.txt","r")
safeCount = 0

def IsValid(line):
    asc = None
    for i in range(len(line) - 1):
        if(not(0 < abs(line[i]-line[i+1]) < 4)):
            return False
        else:
            if(asc == None):
                if(line[i]<line[i+1]):
                    asc = True
                else:
                    asc = False
            else:
                if((asc==True and line[i]>line[i+1]) or (asc == False and line[i]<line[i+1])):
                    return False                
    return True
                


for line in f.readlines():
    line = [int(x) for x in line.split(' ')]
    for i in range (len(line)):
        temp = line.copy()
        temp.pop(i)
        print(temp)
        if(IsValid(temp)):
            safeCount += 1
            break


print(safeCount)

