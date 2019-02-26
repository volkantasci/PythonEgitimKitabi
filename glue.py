#!/usr/bin/python

from os.path import isfile, exists
from sys import argv


class Glue:
    @staticmethod
    def help_page():
        msg = """
        Glue, birden çok dosyayı birleştirip tek dosya haline getirmek için kullanılan programdır.
        Python ile yazılmıştır.
        
        [EXAMPLE]:
        --glue file1 file2 file3 result
        """

        return msg

    @staticmethod
    def check_files(files):
        for i in files:
            if exists(i):
                return isfile(i)
            else:
                return False

        return True

    @staticmethod
    def write_result_file(files, result):
        x = ""
        for i in files:
            with open(i) as f:
                x += f.read()

        with open(result, 'w') as rf:
            rf.write(x)


def main():
    if len(argv) >= 3:
        files = argv[1:-1]
        if Glue.check_files(files):
            Glue.write_result_file(files, argv[-1])

        else:
            print("Dosyaları kontrol edin!")

    else:
        print(Glue.help_page())


if __name__ == "__main__":
    main()


