# befor 
# class FormatDefine:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format

# class Editing:
#     def edit(self, file):
#         if file.format == 'pdf':
#             print(f'Editing pdf {file.name}....')
#         elif file.format == 'xml':
#             print(f'Editing Xml {file.name}...')
#         else:
#             raise ValueError('format not exist...')


# format = FormatDefine('myFile', 'pdf')
# editing = Editing()
# editing.edit(format)



# after
# Factory Design Pattern 
    # 1- creator
    # 2- client
    # 3- Product

class FormatDefine:
    def __init__(self, name, format):
        self.name = name
        self.format = format

class Editing:
    def edit(self, file):       # client
        edit = self._get_edit(file)
        return edit(file)
    
    def _get_edit(self,file):   # creator
        if file.format == 'pdf': # identifire
            return self.pdf_edit
        elif file.format == 'xml':
            return self.xml_edit
        else:
            raise ValueError('format not exist...')


    def pdf_edit(self,file): # product
        print(f'Editing pdf {file.name}....')

    def xml_edit(self,file):
        print(f'Editing Xml {file.name}...')

format = FormatDefine('myFile', 'pdf')
editing = Editing()
editing.edit(format)

