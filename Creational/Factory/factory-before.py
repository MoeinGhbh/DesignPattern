"""
    creational:
        Factory Design Pattern
"""

class A:
    def __init__(self,name,format):
        self.name=name
        self.format=format

class B:
    def edit_file(self, file):
        if file.format=='json':
            print(f'the file format is {file.name}...')
        elif file.format=='xml':
            print(f'the file format is {file.name} ')
        else:
            ValueError f'the format is not exist'

g = A('myfiel','json')
b = B()
b.edit_file(g)