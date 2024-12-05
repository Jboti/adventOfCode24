import math

#p1

# f = open("input.txt","r")
# left,right = [],[]
# for line in f.readlines():
#     split = line.split('   ')
#     left.append(int(split[0]))
#     right.append(int(split[1].split('\n')[0]))
# left.sort()
# right.sort()
# ans = 0
# for i in range(len(left)):
#     ans += abs(left[i]-right[i])
# print(ans)

#p2

f = open("input.txt","r")
left,right = [],[]
for line in f.readlines():
    split = line.split('   ')
    left.append(int(split[0]))
    right.append(int(split[1].split('\n')[0]))
left.sort()
right.sort()
ans = 0
for i in range(len(left)):
    j = 0
    temp = 0
    while(right[j] <= left[i] and j!=998):
        if(right[j]==left[i]):
            temp+=1
        j+=1
    ans+=left[i]*temp
print(ans)