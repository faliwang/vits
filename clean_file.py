import os

filePath = '/mnt/c/Users/fali1210/凡林/美國實習/Salient/vits/filelists/sal_audio_sid_text_train_filelist.txt.cleaned'
datasetPath = '/mnt/c/Users/fali1210/凡林/美國實習/Salient/VCTK-Corpus-0.92/wav48_silence_trimmed'

with open(filePath, 'r') as f:
    audioList = []
    for line in f.readlines():
        line = line.strip().rstrip()
        audioList.append(line.split('|'))

removeList = []
for audioInfo in audioList:
    audioFile = audioInfo[0].split('/')
    audioFile = os.path.join(datasetPath, audioFile[1], audioFile[2].replace('.wav', '_mic1.flac'))
    if (not os.path.isfile(audioFile)) and audioInfo[1] != '108':
        removeList.append(audioInfo)
print(len(removeList))

print(len(audioList))
for info in removeList:
    audioList.remove(info)
print(len(audioList)) 

with open(filePath, "w", encoding="utf-8") as f:
      f.writelines(["|".join(x) + "\n" for x in audioList])