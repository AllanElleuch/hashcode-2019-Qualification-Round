from photo import Photo

def parser(file):
    photos = []
    id=0
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == 0: nbRow = line.split(' ')
            else:
                
                line = line.rstrip('\r\n')
                #print(line.split(' '))
                orientation,numberTag, *tags =  line.split(' ') #orientation = V/H
                isvertical = True if orientation=="V" else False
                photo = Photo(id,isvertical,numberTag,tags)
                id+=1
                #print(photo)
                photos.append(photo) #replace with constructor of a photo
    return photos #rides, int(rows), int(cols), int(n_vehicles), int(bonus), int(t)

#to test
#parser("./a_example.txt")

