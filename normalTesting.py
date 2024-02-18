import os
from os import path
# folder_name = "blob_videos"
# cwd = os.getcwd()
# print(cwd)
# print(cwd+folder_name)
# if os.path.exists(cwd+folder_name):
#     k = os.mkdir(folder_name)
#     os.path.join(cwd,)


# rootdir = os.getcwd()
# print(rootdir)
# for file in os.walk(rootdir):
#     if "videos" in file[0]:
#         print(file[0])

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print(os.path.join(subdir, file))



directory = os.getcwd()

for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isdir(f) and "videos" in f:
		print(f)
folder_name = "blob_videos"
cwd = os.getcwd()
dir = cwd+folder_name

if not os.path.exists(folder_name):
    os.mkdir(folder_name)