from PIL import Image, ImageFile, ImageOps

class ImageWork:
    '''Preperation of image objects'''
    RATIO = 2048
    SCALE = (RATIO, RATIO)
    @staticmethod
    def resize_image(image_path : str) -> Image:
        '''resizes image objects to a universal scale'''
        image : ImageFile = Image.open(image_path, "r")
        padded_image : Image = ImageOps.pad(image, ImageWork.SCALE)
        return padded_image
