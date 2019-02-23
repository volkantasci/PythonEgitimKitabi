#!/usr/bin/python


from os.path import isdir, isfile, islink, exists
from sys import argv, exit

class WordCounter:
    @staticmethod
    def check_arguments(option):
        allowed_args = '-l','-w','-c','--help'
        if option in allowed_args:
            return True
        else:
            return False
    
    
    @staticmethod
    def help_page():
        msg = """
        Word Counter -- Help Page
        
    Word Counter, dosyalarınızda kaç satır, kelime ve karakter olduğunu gösteren, Python ile kodlanmış bir programdır.

        
        -- wdc [OPTION] [FILE]
        
        Examples:
        wdc -l example.txt
        wdc -w example.txt
        wdc -c example.txt
        wdc example.txt
        
        
        -l:\t Dosyadaki satır sayısını göster
        -w:\t Dosyadaki kelime sayısını göster
        -c:\t Dosyadaki karakter sayısını göster
        
    Herhangi bir parametre kullanılmadığında tüm bilgiler gösterilir.
        
        """
        return msg
    
    
    @staticmethod
    def check_file(file):
        if not exists(file):
            return 4
        
        if isfile(file):
            return 1
        
        if isdir(file):
            return 2
        
        if islink(file):
            return 3
        

        
    
    @staticmethod
    def line_count(file=None, data=None):
        if not data:
            # Eğer ki verilmiş bir data yoksa
            with open(file) as f:
                data = f.read()
        
        l = data.count('\n') + 1
        
        if data[-1] == '\n':
            l -= 1
        
        return l
    
    
    @staticmethod
    def word_count(file=None, data=None):
        if not data:
            # Eğer ki verilmiş bir data yoksa
            with open(file) as f:
                data = f.read()
        
        data = data.replace('\n', ' ')
        w = len(data.split(' '))
        
        return w
    
    
    @staticmethod
    def char_count(file=None, data=None):
        if not data:
            # Eğer ki verilmiş bir data yoksa
            with open(file) as f:
                data = f.read()
        
        c = len(data)
        
        return c
    
    

def main():
    if len(argv) == 2:
        # No Arguments
        file_or_arg = argv[1]
        if file_or_arg == '--help':
            print(WordCounter.help_page())
            exit()
            
        
        if WordCounter.check_file(file_or_arg) == 1:
            # Print All Options
            with open(file) as f:
                data = f.read()
                
            result = " {} {} {}  :'{}'".format(WordCounter.line_count(data=data),
                                              WordCounter.word_count(data=data),
                                              WordCounter.char_count(data=data),
                                              file_or_arg)
            
            print(result)
        
        elif WordCounter.check_file(file_or_arg) == 2:
            print("Bu bir dizin!")
            exit()
        
        elif WordCounter.check_file(file_or_arg) == 3:
            print("Bu bir link!")
            exit()
            
        else: # file_or_arg = 4
            print("Dosya mevcut değil!")
            exit()
            
    
    elif len(argv) == 3:
        # Have One Argument
        file = argv[2]
        option = argv[1]
        if WordCounter.check_arguments(option) and WordCounter.check_file(file):
            if option == '-l':
                result = " {}  :'{}'".format(WordCounter.line_count(file=file),
                                            file)
                
                print(result)
            
            elif option == '-w':
                result = " {}  :{}".format(WordCounter.word_count(file=file),
                                          file)
                
                print(result)
            
            elif option == '-c':
                result = " {}  :{}".format(WordCounter.char_count(file=file),
                                          file)
                
                print(result)
            
            else:
                print(WordCounter.help_page())
        
        else:
            print(WordCounter.help_page())
    
    else:
        print(WordCounter.help_page())
            
            

if __name__ == '__main__':
    main()
    
else:
    pass