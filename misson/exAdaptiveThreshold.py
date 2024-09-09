import sys,cv2
import matplotlib.pyplot as plt
import myLib

# 이미지 불러오기
src = cv2.imread('misson/nato.png',cv2.IMREAD_GRAYSCALE)
if src is None:
    sys.exit("이미지 로딩 실패")
    
myLib.hist_gray(src)
    
# # src의 히스토그램을 가져오기
# hist = cv2.calcHist([src],[0],None,[256],[0,256])
# plt.plot(hist)
# plt.show()


# threshold 함수를 이용해서 흑과 백으로 나눈다
src_th = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51,7)
cv2.imshow("src",src)
cv2.imshow("src_th",src_th)
cv2.waitKey()
cv2.destroyAllWindows()