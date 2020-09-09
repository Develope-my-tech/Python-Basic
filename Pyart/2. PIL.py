from PIL import Image
img = Image.open('sim.png')
print(img.format)   # PNG
print(img.size)     # (225, 224)
print(img.mode)     # P
img.show()  # 화면에 사진을 띄움

crop = (55, 70, 85, 100)    # 왼쪽 x,y 오른쪽 x, y
img2 = img.crop(crop)
img.show()

img2.save('cropped.gif', 'GIF') # 이미지 파일 저장
img3 = Image.open('cropped.gif')
print(img3.format)  # GIF
print(img3.size)    # (30, 30)

img4 = Image.open('mous.png')
tmp = img4.crop( (316, 282, 394, 310 ))
print(tmp.size)
img.paste(tmp, (45, 90))    # 원본에 콧수염 붙이기
img.show()