import os

class Path:
    def package_path(self, file_path:str):
        return os.path.dirname(os.path.abspath(file_path))

    def final_path(self, file_path:str, file_name:str):
        __package_path = self.package_path(file_path)

        return os.path.join(__package_path, file_name)