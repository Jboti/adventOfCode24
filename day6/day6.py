#p1

f = open('input.txt','r')
m = f.read().split('\n')
i = 0
while m[i].find('^') == -1:
    i+=1
g = (i,m[i].find('^'))
dir = 0
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

while True:
    if(dirs[dir][0]+g[0]<0 or dirs[dir][0]+g[0]>=len(m) or dirs[dir][1]+g[1] < 0 or dirs[dir][1]+g[1] >= len(m[0])):
        m[g[0]] = m[g[0]][:g[1]]+'X'+m[g[0]][g[1]+1:]
        break
    else:
        if(m[dirs[dir][0]+g[0]][dirs[dir][1]+g[1]]=='#'):
            if(dir==3):
                dir = 0
            else:
                dir+=1
        else:
            m[g[0]] = m[g[0]][:g[1]]+'X'+m[g[0]][g[1]+1:]
            g  = (dirs[dir][0]+g[0],dirs[dir][1]+g[1])

ans = 0
for x in m:
    ans += x.count('X')
print(ans)