import os
import random

uttPath = "/mnt/c/Users/fali1210/凡林/美國實習/Salient/dataset/Utterances (wav)/p400"
txtPath = "/mnt/c/Users/fali1210/凡林/美國實習/Salient/dataset/4000000001_4000000300_CustomerService.txt"

files = os.listdir(uttPath)
files.sort()
for i in range(len(files)):
    os.rename(os.path.join(uttPath, files[i]), os.path.join(uttPath, f"p400_{(i+1):03}.flac"))
    
with open(txtPath, 'r') as f:
    uttList = []
    for line in f.readlines():
        uttList.append(line.strip().split("	", 2))
random.shuffle(uttList)
# print(uttList[0])
# with open('./filelists/sal_audio_sid_text_train_filelist.txt', "a", encoding="utf-8") as f:
#     for i in range(290):
#         fid = int(uttList[i][0]) - 4000000000
#         uttInfos = [f"DUMMY2/p400/p400_{fid:03}.wav","108", uttList[i][-1]]
#         f.writelines(["|".join(uttInfos) + "\n"])

# with open('./filelists/sal_audio_sid_text_val_filelist.txt', "a", encoding="utf-8") as f:
#     for i in range(290, 295):
#         fid = int(uttList[i][0]) - 4000000000
#         uttInfos = [f"DUMMY2/p400/p400_{fid:03}.wav","108", uttList[i][-1]]
#         f.writelines(["|".join(uttInfos) + "\n"])

# with open('./filelists/sal_audio_sid_text_test_filelist.txt', "a", encoding="utf-8") as f:
#     for i in range(295, 300):
#         fid = int(uttList[i][0]) - 4000000000
#         uttInfos = [f"DUMMY2/p400/p400_{fid:03}.wav","108", uttList[i][-1]]
#         f.writelines(["|".join(uttInfos) + "\n"])