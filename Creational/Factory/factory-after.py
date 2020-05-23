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
        edit = self._get_edit(file)
        return edit(file)
        

    def _get_edit(self,file):
        if file.format=='json':
            return self.edit_json
        elif file.format=='xml':
            return self.edit_xml
        else:
            raise ValueError(f'the format is not exist')


    def edit_json(self,file):
        print(f'the file format is {file.name}...')

    def edit_xml(self,file):
        print(f'the file format is {file.name} ')





g = A('myfiel','json')
b = B()
b.edit_file(g)