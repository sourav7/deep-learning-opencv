from os import path

__IMAGE_NAME = 'photography.jpg'
__OUTPUT = 'output.jpg'

basepath = path.dirname(__file__)
photographyImage = path.abspath(path.join(basepath, "..", "resources","images",__IMAGE_NAME))

outputImage = path.abspath(path.join(basepath, "..", "resources","images",__OUTPUT))