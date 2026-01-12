from PIL import Image, ImageOps

class ImageWork:
    '''Preperation of image objects'''
    RATIO = 2048
    SCALE = (RATIO, RATIO)
    @staticmethod
    def resize_image(image_path : str) -> Image:
        '''resizes image objects to a universal scale'''
        image : Image = Image.open(image_path, "r")
        padded_image : Image = ImageOps.pad(image, ImageWork.SCALE)
        return padded_image

    @staticmethod
    def crop_image(image_path : str, bbox_coordinates : tuple[int]) -> Image:
        '''Crops an image at given coordinates'''
        image : Image = Image.open(image_path) #TODO Possibly better to use Image object?
        new_image : Image = image.crop(bbox_coordinates)

        return new_image
