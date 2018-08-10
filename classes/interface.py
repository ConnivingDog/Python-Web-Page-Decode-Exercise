import os

class Interface():

    def PrintMenu():
        print('[1]. Get HTML')
        print('[2]. Find')
        print('[3]. Set URL')
        print('[4]. Set File Name')
        print('[5]. --')
        print('[6]. Exit\n')

    def PrintFindMenu():
        os.system('cls')
        print('[1]. Tag')
        print('[2]. File Type (.***)')
        print('[3]. Back\n')