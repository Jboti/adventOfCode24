import re
#p1


# f = open("input.txt","r")
# data = f.read().strip()
# ans = 0
# nums = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",data)
# for pair in nums:
#     x,y = pair
#     ans += int(x)*int(y)
# print(ans)



#p2

f = open("input.txt","r")
data = f.read().strip()
ans = 0
enabled = True

for i in range(len(data)):
    if data[i:i+4] == "do()":
        enabled = True
    if data[i:i+len("don't()")] == "don't()":
        enabled = False
    if data[i:i+4] == "mul(":
        j = i+4
        while data[j] != ")":
            j+=1
        try:
            x,y = map(int,re.findall(r'\d{1,3}',data[i:j+1]))
            if data[j-1] in ['1','2','3','4','5','6','7','8','9']:
                continue
            if enabled:
                ans += x*y
        except:
            pass

print(ans)