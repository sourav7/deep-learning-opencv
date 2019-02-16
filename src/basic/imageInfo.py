from os import path

__imageName = 'photography.jpg'
__output = 'output.jpg'

basepath = path.dirname(__file__)
photographyImage = path.abspath(path.join(basepath, "..", "resources","images",__imageName))

outputImage = path.abspath(path.join(basepath, "..", "resources","images",__output))