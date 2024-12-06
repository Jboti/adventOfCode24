# p1
import math

f = open('input.txt','r')
dict = {}
nums = []
ans = 0

r = f.readline()
while r != '\n':
    r = [ int(x) for x in r.split('|')]
    if dict.get(r[0]) is None:
        dict[r[0]] = [r[1]]
    else:
        dict[r[0]].append(r[1])
    r = f.readline()

r = f.readline().strip()
while r:
    nums.append([int(x) for x in r.split(',')])
    r = f.readline().strip()


def ValidCheck(num,arr):
    for x in arr:
        if x in dict[num]:
           return False
    return True

for i in range(len(nums)):
    corr = True
    for j in range(len(nums[i])-1,0,-1):
        if not corr:
            break
        num = nums[i][j]
        arr = nums[i][j-1::-1]
        if not ValidCheck(num,arr):
            corr = False
            break
    if corr:
        ans+=nums[i][math.floor(len(nums[i])/2)]

print(ans)


