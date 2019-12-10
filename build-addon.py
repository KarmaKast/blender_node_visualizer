import os
import shutil
import zipfile
#import fnmatch
#import glob

"""
    Current Usage:
    python build-addon.py
"""

"""
    Aimed Usage:
    python build-addon.py addonPath
"""


# echo "running build"
print("running build")

cwd = os.getcwd()
print(cwd)

DEV = False  # for print statements meant for debugging purposes

if True:
    # TODO handle previous builds
    # mkdir -p build
    path = "build"

    try:
        os.mkdir(os.path.join(cwd, path))
    except OSError as error:
        print("%s folder exists" % path)
        if DEV:
            print(error)
    else:
        pass
        # print ("Successfully created the directory %s " % path)

    # TODO create build
    # TODO Step 1: create a seperate README.md file for the build

    # TODO Step 2: parse .buildignore

    #files = parseIgnoreFile('.buildignore')
    files = ["__init__.py", "cleanup.py", "debug.py", "LICENSE", "main_panel.py", "node_dataLoader.py", "create_viz.py", "nodeLib/debug.py", "nodeLib/LICENSE.txt",
             "nodeLib/node.py", "nodeLib/query.py", "nodeLib/__init__.py", "nodeLib/README.md", "nodeLib/structure/__init__.py", "nodeLib/structure/node_structs.py"]

    # TODO Step 2: copy needed files to /build/.zip

    defaultBuildName = str.split(cwd, os.path.sep)[-1]
    buildName = defaultBuildName
    newZip = zipfile.ZipFile(buildName+'.zip', mode='w')
    shutil.move(defaultBuildName+'.zip', os.path.join(cwd, path))

    #add_to_zip(newZip, files)

    for file in files:
        if os.path.isfile(os.path.join(cwd, file)):
            newZip.write(os.path.join(
                cwd, file), os.path.join(buildName, file), compress_type=zipfile.ZIP_DEFLATED)
        elif os.path.isdir(os.path.join(cwd, file)):
            pass
            #add_dir_to_zip(newZip, cwd, file)
    # newZip.write('__init__.py', compress_type=zipfile.ZIP_DEFLATED)

    # TODO Step 3: add


"""
print(os.listdir('.'))
files = []
with open(".buildignore", 'r') as buildignore:
    # print(patterns.read())
    patterns = []
    for line in buildignore.readlines():
        if not line.startswith("#"):
            # patterns.append(line)
            patterns.append(str.split(line, '\n')[0])
    if '.buildignore' not in patterns:
        patterns.append('.buildignore')
    if 'build-addon.py' not in patterns:
        patterns.append('build-addon.py')
    # print(str.split(patterns[0], '\n')[0])
    for pattern in patterns:
        print(glob.glob(pattern))
    for file in os.listdir('.'):
        ignore = False
        isFile = True if os.path.isfile(os.path.join(cwd, file)) else False
        for pattern in patterns:
            #pattern_  = pattern
            if pattern.endswith('/'):
                if os.path.isdir(os.path.join(cwd, file)):
                    if file == str.split(pattern, '/')[0]:
                        ignore = True
            else:
                if file == pattern:
                    ignore = True
        if not ignore:
            files.append(file)
print('have any files been ignored? {} > {}, {}'.format(
    len(os.listdir('.')), len(files), len(os.listdir('.')) > len(files)))
print(files)
"""
"""
files2 = []
for r, d, f in os.walk(cwd):
    #print(d)
    for file in f:
        path_ = str.join('', str.split(str.split(r, cwd)[-1], os.path.sep)[1:])
        files2.append(os.path.join(path_, file))
print(len(files2))
for file in files2[:]:
    print(file)
"""

# print(glob.glob('__pycache__'))
