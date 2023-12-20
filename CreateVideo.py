import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
count = len(images)
print(count)
frame = cv2.imread(images[0])
height, width, channel = frame.shape
size = (width, height)
print(size)

out1 = cv2.VideoWriter('project_sunset.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
out2 = cv2.VideoWriter('project_sunrise.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
#Sun rise
for i in range(count - 1, 0, -1):
    frame = cv2.imread(images[i])
    out2.write(frame)

out2.release()
#sun set

for i in range(0, count - 1):
    frame = cv2.imread(images[i])
    out1.write(frame)

out1.release()
print("Done.")

