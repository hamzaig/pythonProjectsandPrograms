# D:\D\Songs
import os,shutil

dict_extentions={
    "audio_extentions" :     ('.mp3','.m4a','.wav','.flac'),
    "video_extentions":     (".mp4",".mkv",".MKV",".flv",".mpeg",'.3gp'),
    "Picture_extentions": (".jpg")
}

# print(type(os.listdir("D:\D\Songs")))
# a=os.listdir("D:\D\Songs")
# print(a[0].endswith(".mp4"))
folderpath=input("Please Enter Folder Path")

def file_finder(folder_path,file_extentions):
    files=[]
    for file in os.listdir(folder_path):
        for extentions in file_extentions:
            if file.endswith(extentions):
                files.append(file)
    return files

# print(file_finder("D:\D\Songs",video_extentions))

for extention_type,extention_tuple in dict_extentions.items():
    folder_name=extention_type.split("_")[0]+" Files"
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extention_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)


