'''Fish objects'''
from Models.image import Image
class Fish:
    '''Represents a fish object'''
    def __init__(self, fish_id : int, sex : str, sightings : int, caught : bool = True, images : list[Image] = None):
        self.fish_id = fish_id
        self.__sex = sex
        self.__sightings = sightings
        self.__caught = caught
        self.__images = images if images else []

    def get_sex(self) -> str:
        '''Returns the sex of the fish'''
        return self.__sex

    def add_sighting(self) -> None:
        '''Adds a sighting to the fish object'''
        self.__sightings += 1

    def get_sightings(self) -> int:
        '''Returns the number of sightings'''
        return self.__sightings

    def set_caught(self) -> None:
        '''Sets the caught flag to true'''
        self.__caught = True

    def get_caught(self) -> bool:
        '''Gets the caught status of a fish'''
        return self.__caught

    def get_images(self) -> list[Image]:
        '''returns a list of image objects related to the fish'''
        return self.__images

    def add_image(self, image : Image) -> None:
        '''Adds an image to the list of images'''
        self.__images.append(image)
