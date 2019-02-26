#!/usr/bin/python


from os.path import exists, isfile
from sys import argv, exit


class Splitter:
    @staticmethod
    def check_arguments(args):
        if len(args) != 4:
            return False

        allowed_args = '-l', '-w', '-c'
        option = args[1]
        value = args[2]

        if option not in allowed_args:
            return False

        elif type(value) is int:
            if value > 0:
                return True
            else:
                return False

        else:
            return False


    @staticmethod
    def check_file(args):
        file = args[3]

        if exists(file):
            if isfile(file):
                return True

            else:
                return False

        else:
            return False


    @staticmethod
    def create_files(piece):
        l = []

        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in 'abcdefghijklmnopqrstuvwxyz':
                l.append(f"x{i}{j}")
                if len(l) == piece:
                    return l
    
    
    @staticmethod
    def help_page():
        msg = """
        Splitter; dosyaları satır sayısına, kelime sayısına ya da karakter sayısına göre bölen programdır.
        Python dili ile yazılmıştır.

        EXAMPLES:

        -- splitter -l 200 file.txt
        -- splitter -w 1000 file.txt
        -- splitter -c 1500 file.txt


        OPTIONS:

        -l     :  Satır sayısına göre bölme işlemi
        -w     :  Kelime sayısına göre bölme işlemi
        -c     :  Karakter sayısına göre bölme işlemi
        --help :  Bu mesajı görüntüler
        """

        return msg



    @staticmethod
    def split_by_line(file, line_count):
        with open(file) as f:
            lines = f.readlines()

        n = len(lines)
        if n % line_count == 0:
            files = Splitter.create_files(int(n/line_count))

        else:
            files = Splitter.create_files(int(n/line_count) + 1)

        d = dict()

        for i, j in enumerate(files):
            try:
                d[j] = ''.join(lines[i*line_count:(i+1)*line_count])

            except IndexError:
                d[j] = ''.join(lines[i * line_count:])

        return d

    @staticmethod
    def split_by_word(file, word_count):
        with open(file) as f:
            words = f.read().split(' ')

        w_copy = words.copy()
        n = 0

        for j, i in enumerate(w_copy):
            if '\n' in i:
                words.insert(j+1+n, i[i.rindex('\n') + 1:])
                words[j + n] = i[:i.rindex('\n')+1]

                n += 1

        for a in range(len(words)-2):
            if words[a]:
                if words[a][-1] != '\n':
                    if words[a+1]:
                        words[a+1] = ' ' + words[a+1]

            else:
                words[a] = ' '

        del w_copy
        d = dict()

        if len(words) % word_count == 0:
            files = Splitter.create_files(int(len(words)/word_count))

        else:
            files = Splitter.create_files(int(len(words)/word_count)+1)

        for k,l in enumerate(files):
            try:
                d[l] = ''.join(words[k*word_count:(k+1)*word_count])
            except IndexError:
                d[l] = ''.join(words[k*word_count:])

        return d

    @staticmethod
    def split_by_char(file,char_count):
        with open(file) as f:
            chars = tuple([i for i in f.read()])

        if len(chars) % char_count == 0:
            files = Splitter.create_files(int(len(chars)/char_count))

        else:
            files = Splitter.create_files(int(len(chars)/char_count) + 1)

        d = dict()

        for i, j in enumerate(files):
            try:
                d[j] = ''.join(chars[i*char_count:(i+1)*char_count])

            except IndexError:
                d[j] = ''.join(chars[i * char_count:])

        return d


def main():
    try:
        argv[2] = int(argv[2])
    except ValueError:
        print(Splitter.help_page())
        
    if Splitter.check_arguments(argv):
        if Splitter.check_file(argv):
            option = argv[1]
            value = argv[2]
            file = argv[3]

            if option == '-l':
                d = Splitter.split_by_line(file,value)
                for i in d:
                    with open(i, 'w')as f:
                        f.write(d.get(i))
            elif option == '-w':
                d = Splitter.split_by_word(file,value)
                for i in d:
                    with open(i, 'w')as f:
                        f.write(d.get(i))
            
            else: # option is -c
                d = Splitter.split_by_char(file,value)
                for i in d:
                    with open(i, 'w')as f:
                        f.write(d.get(i))
        
        else:
            print("Dosya Hatası")
    
    else:
        print(Splitter.help_page())


if __name__ == '__main__':
    main()