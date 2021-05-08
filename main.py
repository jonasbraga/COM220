import os

def listFilesDirectory(filePath, tabs):
  localFiles = os.listdir(filePath)
  for i in range(len(localFiles)):
    if localFiles[i] in ['.upm', '.git', '__pycache__']: continue
    print('\t' * tabs, localFiles[i])

    if (os.path.isdir("{}/{}".format(filePath, localFiles[i]))):
      listFilesDirectory("{}/{}".format(filePath, localFiles[i]), tabs + 1)

print("Selecione o arquivo desejado (separando as pastas por '.'): \n")
listFilesDirectory('.', 0)

selectedFileName = input("\n")

mod = __import__(selectedFileName)