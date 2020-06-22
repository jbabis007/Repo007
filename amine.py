import os

#listfile = os.listdir('data/VOC2007/JPEGImages/')


listfile=[x.split('.')[0] for x in os.listdir('data/VOC2007/JPEGImages/')]

print(len(listfile))
with open("file.txt", "w") as output:
    for row in listfile:
        output.write(str(row) + '\n')


print('Over')