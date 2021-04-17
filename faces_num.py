import face_recognition as fr
import PIL.Image
import PIL.ImageDraw
import sys

help_print = ("""
Установите необходимые модули:
pip install face_recognition

Передайте проверяемый файл:

faces_num photo.jpg

или

faces_num ../photo.jpg

""")

if(len(sys.argv)!=2) or ("-help" in sys.argv[1]):
        print(help_print)
else:
        (help_print)
        img_filename = sys.argv[1]
        img = fr.load_image_file(img_filename)
        face_len = len(fr.face_locations(img))

        print("Faces in the photo:",face_len)
