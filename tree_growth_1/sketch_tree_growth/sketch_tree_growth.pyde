"""
A Processing implementation of XXX
"""

# Variables for timer
interval = 100
lastRecordedTime = 0
max_depth = 15
theta0 = 25*PI/180

def recursion(max_depth, theta0, xs,ys,xe,ye,ls, theta,depth,rlist,sigma):
   
    if depth < max_depth:
        ls = ls*0.8
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
    print("hallo")
    colorMode(HSB, 360, 360, 360)
    size(600,600)    
    
    ls = 50
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
    print(rlist)
    

def draw():
    global lastRecordedTime
    global rlist 
    global max_depth 
    h=0
    for i,l in enumerate(rlist):
        if (h > 360):
            h = 0
            
        h += 2
        strokeWeight(2)
      
        if l[4]<6:
            stroke(62,360,360)
    
        if l[4]>5:
            stroke(h, 360, 360)
        
        a=3*width/4
        
        line(l[0],l[1],l[2],l[3])
        #line(l[0],-l[1]+a,l[2],-l[3]+a)
        #line(-l[0]+a,l[1],-l[2]+a,l[3])
        
    #if millis()-lastRecordedTime > interval:
        #xs,ys,xe,ye,ls,theta = iteration(xs,ys,xe,ye,ls,theta)    
        #lastRecordedTime = millis()
    
