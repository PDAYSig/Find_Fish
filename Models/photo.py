class Photo:
    '''A photo of a fish'''
    def __init__(self, file_path : str, fish_id : int | None = None):
        self.__file_path = file_path
        self.__fish_id = fish_id

    def set_fish_id(self, fish_id : int) -> None:
        '''Specifies the fish in the image'''
        self.__fish_id = fish_id

    def get_fish_id(self) -> int:
        '''Returns the id of the fish in the image'''
        return self.__fish_id

    def get_file_path(self) -> str:
        '''returns the filepath of the image'''
        return self.__file_path
