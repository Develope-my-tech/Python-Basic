'''
imghdr : 몇몇 이미지 파일의 파일 형식을 검출한다.
colorsys : 여러 가지 시스템(RGB, YIQ, HSV, HLS) 사이의 색상을 변환
'''

import imghdr
print(imghdr.what('sim.png'))