import pygame
import os



main_dir = os.path.split(os.path.abspath(__file__))[0] 
image_dir = os.path.join(main_dir, "images") 


def load_image(name):
    '''Purpose:to load an image 
    :param name: name of the image 
    :note:must be in images directory in order to load
    :return:image a Suface object that represents the image
    :return:image.get_rect() a Rect object that represents image as Rect
    '''
    abs_path = os.path.join(image_dir,name)
    image = pygame.image.load(abs_path)
    return image,image.get_rect()
