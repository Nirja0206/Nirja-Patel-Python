file=open("Text File.txt","w")
file.write("This File is For Writing")
print("Hello How are you?")
print("******************************************************************************")
file.close()

print("Data is succesfully Written")
print("******************************************************************************")
file=open("Text File.txt","r")
print(file.read())
file.close()


file=open("Text File.txt","a")
file.write("\nJanvi is file")
print("******************************************************************************")
file.close()

print("Data is succesfully Written")
print("******************************************************************************")
file=open("Text File.txt","r")
print(file.read())
print("******************************************************************************")
file.close()


file=open("Text File.txt2","w+")
file.write("This File is For Writing and reading")
print(file.tell())
file.seek(0)
#print("Hello I am Nirja")
print("******************************************************************************")
print(file.read())
file.close()
