from zipfile import ZipFile

def extract(zipfile:str, outfolder: str):
    with ZipFile(zipfile, 'r') as z:
        z.testzip()
        z.extractall(outfolder)
    print()
    print('Extraction complete.')
    return zipfile.replace('.zip', '')
