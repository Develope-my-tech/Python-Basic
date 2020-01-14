'''
ImageMagick은 2D 비트맵 이미지를 표현, 변환, 수정하는 프로그램의 집합
'''

from wand.image import Image
# from wand.display import display


img = Image(filename='sim.png')
print(img.size)
print(img.format)
display(img)