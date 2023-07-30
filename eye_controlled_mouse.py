import cv2                 #lot of image processing
import mediapipe as mp     #detect the face
import pyautogui
cam=cv2.VideoCapture(0)    #first part is to read the camera
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) #  # type: ignore
#refine ,after passing true it gives 478 landmarks and every landmarks identifies diff partbof face.
screen_w,screen_h=pyautogui.size()
while True:
    _,frame=cam.read()     #to read every frame of video
    frame=cv2.flip(frame,1) # to fix the fliping of img. 1 means to flip vertically
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #detect the face in greyscale as detection in grey scale is easier.
    output=face_mesh.process(rgb_frame)#create an output from this rgb frame
    landmark_points=output.multi_face_landmarks   #to detects points on face
    frame_h,frame_w,_=frame.shape
    #print(landmarks_points)
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]): #e will give index or id and the landmark
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0)) #draw circle on frame on center with a radius of and colour(rgb).it detect landmark on whole face.

            #print(x,y)
            if id==1:  # id is selected so as to move the cursor by the help of 1 landmark as 4 landmark will make it janky
                screen_x=screen_w/screen_w*x
                screen_y=screen_w/screen_w*y
                pyautogui.moveTo(screen_x,screen_y)
            
            left=[landmarks[145],landmarks[159]]
            for landmark in left:
                x=int(landmark.x*frame_w)
                y=int(landmark.y*frame_h)
                cv2.circle(frame,(x,y),3,(0,255,255))
            
            if(left[0].y-left[1].y) < 0.004: #to get the co-ordinate for left
                #print('click')
                pyautogui.click()
                #pyautogui.sleep(1)
            
        cv2.imshow('Eye controlled Mouse',frame)     #to show some image
        cv2.waitKey(1)             #wait for a key

    





