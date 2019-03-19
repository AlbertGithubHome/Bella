from PIL import ImageDraw
from PIL import Image

img = Image.open('maze.png').getdata()
new = Image.new('RGBA',img.size,'black')
newimg = ImageDraw.Draw(new)
 
for i in range(img.size[1]):
    if img.getpixel((i,0))[0]==0:
        pos = (i,0)
    if img.getpixel((i,img.size[0]-1))[0]==0:
        endpos = (i,img.size[0]-1)
        
path = []
wholepath = []
dire = [(1,0),(0,1),(-1,0),(0,-1)]
wall = (255,)*4
 
while pos!=endpos:
    img.putpixel(pos, wall)
    flag = 0
    newpos = pos
    for i in dire:
        try:
            pp = (pos[0]+i[0],pos[1]+i[1])
            if img.getpixel(pp)!=wall:
                flag+=1
                newpos = pp
        except:
            pass
    if flag==0:
        if path == []:
            path = wholepath.pop()
            continue
        pos = path[0]
        path = []
    elif flag>1:
        #print(path)
        #break
        wholepath.append(path)
        path = [pos]
        pos = newpos
    else:
        path.append(pos)
        pos = newpos
else:       
     path.append(pos)
     wholepath.append(path)
 
img = Image.open('maze.png').getdata()
data = [(img.getpixel(k)[0],new.putpixel(k, wall)) for i in wholepath for k in i]
#out = open('out24.zip','w')
#for i in data[1::2]:
#    out.write(chr(i[0]))
#out.close()
new.save('out24.png')
print(wholepath, len(wholepath))