import glob

ext_filenames = glob.glob("bot/**/*.py")
extension_names = []

for filename in ext_filenames:
    extension_names.append(filename.replace(".py", "").replace("\\", "."))
    
print(extension_names)