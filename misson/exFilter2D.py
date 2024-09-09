import sys, cv2
import numpy as np

#src = cv2.imread('misson/rose.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('misson/cat3.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    sys.exit('Image load failed')
    
# 사용자 커널(=필터)을 생성
# kernel = np.array([[0, -1, 0],
#                    [-1, 5, -1],
#                    [0, -1, 0]], dtype=np.float32)
kernel = np.ones((3, 3), dtype=np.float32)/9
mask1 = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
dst = cv2.filter2D(src, -1, kernel)

# 2. blur kernel을 사용해서
dst2= cv2.blur(src, (3, 3))

cv2.imshow('src_th', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()