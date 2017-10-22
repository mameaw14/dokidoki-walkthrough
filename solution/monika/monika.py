import cv2

img = cv2.imread('data.png')
s = ""
for i in range(140):
	for j in range(140):
		px = img[i,j,0]
		if px == 255:
			s += "1"
		else:
			s += "0"

print(s)
