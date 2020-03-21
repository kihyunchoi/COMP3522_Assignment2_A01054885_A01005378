import os


class FileHandler:
    """
    FileHandler Class which handling file reading and writing from a file
    """
    @staticmethod
    def load_data(file_name):
        """
        Loading File and print
        :param file_name:
        :return:
        """
        if os.path.exists(file_name):
            with open(file_name, mode='r', encoding='utf-8') as loading:
                data = loading.read()
                print(data)
        else:
            raise FileNotFoundError(f"File not exists : {file_name}")

    @staticmethod
    def write_lines(file_name, lines):
        """
        Write file
        :param file_name:
        :param lines:
        :return:
        """
        try:
            with open(file_name, mode='a') as adding_lines:
                for x in lines:
                    adding_lines.write(x + "\n")
        except Exception as e:
            print(e)

