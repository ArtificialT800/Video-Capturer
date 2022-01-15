#press esc to save the file

import cv2
filename= input("What do you want to save the file as?: ")
cap= cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer= cv2.VideoWriter(filename+'.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
while True:
    ret,frame= cap.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()
