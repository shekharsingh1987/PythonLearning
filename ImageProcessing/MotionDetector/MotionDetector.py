import cv2
cam=cv2.VideoCapture(0)

#Get the difference of image
def diffImage(a,b,c):
    t0=cv2.absdiff(a,b)
    t1=cv2.absdiff(b,c)
    t3=cv2.bitwise_and(t0,t1)
    return t3
    
#Initialize different frames
t=cam.read()[1]
tp=cam.read()[1]
tpp=cam.read()[1]

t=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
tp=cv2.cvtColor(tp,cv2.COLOR_BGR2GRAY)
tpp=cv2.cvtColor(tpp,cv2.COLOR_BGR2GRAY)

while True:
    imgMotion=diffImage(t,tp,tpp)
    cv2.imshow('Motion Detection in gray',imgMotion)
    res,img=cam.read()
    t=tp
    tp=tpp
    tpp=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
    #cv2.imshow('Motion Detection',img)
    k=cv2.waitKey(10)
    if k==27:
        cv2.destroyAllWindows()
        break
    
print 'Good Byee'
