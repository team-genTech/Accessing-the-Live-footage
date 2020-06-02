import cv2
import os
name=str(input("Enter name of the person : "))
cap=cv2.VideoCapture(0)
count=0
train_dir='E:\\face_identification\\Data'
train_name_dir=os.path.join(train_dir,name)
os.makedirs(train_name_dir)
while True:
    ret,frame=cap.read()
    cv2.imshow(f'Collecting pictures of {name}',frame)
    k=cv2.waitKey(1)
    if k==ord('m'):
       count=count+1
       cv2.imwrite(f'{train_name_dir}\\{name}_{count}.jpg',frame)       
    elif k == ord('q'):
        break
    elif k== None:
        continue
    

cap.release()
cv2.destroyAllWindows()
        
    