from Models.fish import Fish
from Models.image import Image


lax = Fish(1, 'm', 2, True)

print(lax.get_sex())

pic = Image("https://github.com/PDAYSig/image_recognition_python.git", 1)
lax.add_image(pic)

print(lax.get_images())
