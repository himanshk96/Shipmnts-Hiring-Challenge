# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:58:01 2018

@author: himansh
"""
import io
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print("THis is it")
    file_f = open("testfile.txt","w") 
    for text in texts:
        try:
            print(text.description)
            #print('\n"{}"'.format(text.description))
            vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
            #print('bounds: {}'.format(','.join(vertices)))
        except: continue;
    file_f.close()
if __name__ == '__main__':
    detect_text("G:\shipmnts\Capture123.PNG")


