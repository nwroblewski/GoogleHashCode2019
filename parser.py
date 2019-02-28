import sys


class Photo:
    def __init__(self,id,orientation,tags_no,tags):
        self.id = id
        self.tags = tags
        self.o = orientation
        self.tags_no = tags_no

# class Slideshow:
    

def parse():
    photos = []
    dataset = open(sys.argv[1],'r')
    n = int(dataset.readline())
    for i in range(n):
        line = dataset.readline().split(" ")
        line[-1] = line[-1].rstrip()
        photos.append(Photo(i,line[0],line[1],line[2:len(line)]))
    return photos

def group_by_orientation(photos):
    horizontals = [] 
    verticals = []
    for photo in photos:
        if(photo.o == 'H'):
            horizontals.append(photo)
        else:
            verticals.append(photo)

if __name__== "__main__":
    photos = parse()
    