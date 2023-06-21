import os
def trash_creator(mb,file_name:str):
    """ create random file with fixed size
        :param mb = file size in megabites
        :param file_name = file name
    """
    os.system(f"head -c {mb}MB /dev/urandom > {file_name}")
    print(f"File {file_name} was created successfully. File path {os.path.abspath(file_name)}")
