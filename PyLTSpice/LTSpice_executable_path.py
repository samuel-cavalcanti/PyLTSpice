import os
import sys


class LTSpiceExecutablePath:
    __LTspiceIV_exe = None
    __LTspiceXVII_exe = None
    __LTspice_IV_file_exe = "scad3.exe"
    __LTspiceXVII_file_exe = "XVIIx64.exe"
    # if need add Mac os support add "darwin"
    __supported_platforms = ["linux", "win32", "cygwin"]
    __possible_LTspiceIV_directories = []
    __possible_LTspiceXVII_directories = []

    def __init__(self):
        if sys.platform not in self.__supported_platforms:
            raise Exception(f'This Operational system is not supported {sys.platform}')

        self.__adding_possible_directories()

        self.__LTspiceXVII_exe = self.__search_for_executable(self.__possible_LTspiceXVII_directories,
                                                              self.__LTspiceXVII_file_exe)
        self.__LTspiceIV_exe = self.__search_for_executable(self.__possible_LTspiceIV_directories,
                                                            self.__LTspiceXVII_file_exe)

        pass

    def __adding_possible_directories(self):
        home_directory = os.path.expanduser('~')
        default_LTspiceXVII_wine_installation = os.path.join(home_directory,
                                                             '.wine/drive_c/Program Files/LTC/LTspiceXVII/')
        default_LTspiceIV_wine_installation = os.path.join(home_directory,
                                                           '.wine/drive_c/Program Files (x86)/LTC/LTspiceIV/')

        self.__possible_LTspiceIV_directories = [default_LTspiceIV_wine_installation,
                                                 r"C:\Program Files (x86)\LTC\LTspiceIV\\"]

        self.__possible_LTspiceXVII_directories = [default_LTspiceXVII_wine_installation,
                                                   r"C:\Program Files\LTC\LTspiceXVII\\"]

    @staticmethod
    def __search_for_executable(directories: list, executable_name: str) -> str or None:
        for directory in directories:
            path_to_executable = os.path.join(directory, executable_name)
            if os.path.isfile(path_to_executable):
                return path_to_executable
        return None

    pass

    def get(self):
        LTspiceXVII_exe = self.__search_for_executable(self.__possible_LTspiceXVII_directories,
                                                       self.__LTspiceXVII_file_exe)
        if LTspiceXVII_exe:
            return LTspiceXVII_exe

        LTspiceIV_exe = self.__search_for_executable(self.__possible_LTspiceIV_directories,
                                                     self.__LTspiceXVII_file_exe)
        if LTspiceIV_exe:
            return LTspiceIV_exe

        raise FileNotFoundError("Error: No LTSpice installation found")
