"""
A Processing implementation of a Lindenmayer System with added animation and rainbow trees *-*. 
Author: Carina Karner 
"""

# Variables for timer
interval = 100
lastRecordedTime = 0
lastRecordedTime2 = 1700
max_depth = 14
theta0 = 20*PI/180
depth=1 
it=0

def recursion(max_depth, theta0, xs,ys,xe,ye,ls, theta,depth,rlist,sigma):
   
    if depth < max_depth:
        xn = 0
        yn = ls
        
        xorient = xn*cos(theta) - yn*sin(theta)
        yorient = yn*cos(theta) + xn*sin(theta)
    
        xs = xe 
        ys = ye 
        xe = xs - xorient
        ye = ys - yorient 
        theta = theta + sigma*theta0 
    
        depth = depth+1 
        rlist.append([xs,ys,xe,ye,depth])
        ls = ls*0.8
        exit_code = recursion(max_depth, theta0, xs,ys,xe,ye,ls, theta,depth,rlist,-1)
        exit_code = recursion(max_depth, theta0, xs,ys,xe,ye,ls, theta,depth,rlist,1)
    
    return False
    
def setup():
    global xs
    global ys
    global xe
    global ye
    global rlist
    global theta
    global max_depth 
    global theta0
    global ls 
    global A 
    global depth_list
    global font
    global textx 
    
    textx = width/2 - 100
    
    A=height*0.99
    colorMode(HSB, 360, 360, 360)
    size(600,600)    
    font = createFont("SignPainter-HouseScriptSemibold",40)
    
    ls = 40
    theta = 0
    depth = 0 
    
    xs=width/2
    ys=height/2
    xe = width/2
    ye = height/2 - ls
    
    background(0)
   
    rlist=[]
    exit_code = recursion(max_depth, theta0, xs,ys,xe,ye,ls,theta,depth,rlist,1)
    exit_code = recursion(max_depth, theta0, xs,ys,xe,ye,ls, theta,depth,rlist,-1)

    depth_list=[]
    for depth in range(0,16):
         sublist = [x for x in rlist if x[4]==depth]
         depth_list.append(sublist)

def draw():
    
    global lastRecordedTime
    global rlist 
    global max_depth 
    global depth 
    global depth_list
    global font 
    h=0
    global textx 
    global it

    if millis()<2500 and millis()-lastRecordedTime > interval:
    
        lst = depth_list[depth]
        depth=depth+1
        
        for i,l in enumerate(lst):
            if (h > 360):
                h = 0
            h += 2
    
            if l[4]<6:
                stroke(62,360,360)
                strokeWeight(5)
    
            if l[4]>5:
                stroke(h, 360, 360)
                strokeWeight(2)
        
            line(l[0],l[1],l[2],l[3])
            line(l[0],-l[1]+A,l[2],-l[3]+A)
            lastRecordedTime = millis()
    

   
    if millis()>1500:
        message="Welcome to GT_"
        textFont(font)            
        fill(62,360,360)
        print("hallo")
        print("texttx",textx)
        if millis()-lastRecordedTime > interval and it<len(message):
            text(message[it],textx,height/2)
            textx = textx+textWidth(message[it]) 
            it=it+1
            print(millis())
            lastRecordedTime = millis()
