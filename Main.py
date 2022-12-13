import cv2
import numpy as np
video = cv2.VideoCapture('Test4k_2.mov')
video1 = cv2.VideoCapture('Test4k_2.mov')
#lower = [50, 0, 130] #[165, 241, 232] #[18, 50, 50]
#upper = [255, 255, 255] #[35, 255, 255]

# дым

lower = [50, 0, 130]#[0, 120, 100] 
upper = [255, 255, 255] #[120, 255, 255] 

lower = np.array(lower, dtype = 'uint8')
upper = np.array(upper, dtype = 'uint8')

# огонь
lower1 = [0, 120, 100] 
upper1 = [120, 255, 255]

lower1 = np.array(lower1, dtype = 'uint8')
upper1 = np.array(upper1, dtype = 'uint8')

while True:									
	ret, frame = video.read()
	ret1, frame1 = video.read()
	#обработка изображений
	try:
		frame1 = cv2.resize(frame1, (800, 600))
		frame = cv2.resize(frame, (800, 600)) #changed the size of picture
		blur = cv2.GaussianBlur(frame, (15, 15), 0) #add blur (15, 15)
		hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV) #change color format

	except:
		print("End of video")
		break



	mask = cv2.inRange(hsv, lower, upper)
	mask1 = cv2.inRange(hsv, lower1, upper1)
	mask_union = mask + mask1
	
	output = cv2.bitwise_and(frame, hsv, mask = mask_union)

	number_of_total = cv2.countNonZero(mask)

	if int(number_of_total) > 300:
		print('Fire Detection')

	if ret == False:
		break

	cv2.imshow('Output', output)
	cv2.imshow('Input', frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
cv2.destroyAllWindows()
video.release()
