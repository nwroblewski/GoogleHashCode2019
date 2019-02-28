import sys
import random
from random import shuffle

class Photo:
    def __init__(self,ids,orientation,tags_no,tags):
        self.ids = ids
        self.tags = tags
        self.o = orientation
        self.tags_no = tags_no

    def __str__(self):
        return str(self.ids)
    __repr__ = __str__

class Slide:
    def __init__(self,photos):
        self.photos = photos


def make_sets(photo1,photo2):
    
    intersection_list = list(set(photo1.tags).intersection(photo2.tags))
    photo1_ex = [i for i in photo1.tags if i not in intersection_list or intersection_list.remove(i)]
    photo2_ex = [i for i in photo2.tags if i not in intersection_list or intersection_list.remove(i)]
    
    return photo1_ex,intersection_list,photo2_ex


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
        if(photo.o == 'V'):
            verticals.append(photo)
    
    return horizontals,verticals

def randomize_slides(horizontals, verticals):
    slides = []
    for i in range(len(verticals)):
        if(len(verticals) == 0 or len(verticals) == 1):
            break
        rand1 = random.randint(0,len(verticals) - 1)
        photo1 = verticals[rand1]
        verticals.remove(verticals[rand1])
        rand2 = random.randint(0,len(verticals) - 1)
        photo2 = verticals[rand2]
        verticals.remove(verticals[rand2])
        slides.append(Slide([photo1,photo2]))
    

    for i in range(len(horizontals)):
        slides.append(Slide([horizontals[i]]))
    
    return slides


def make_output(slides):
    shuffle(slides)
    print(len(slides))
    for slide in slides:
        if(len(slide.photos) == 2):
            print(slide.photos[0],slide.photos[1])
        else:
            print(slide.photos[0])

if __name__== "__main__":
    photos = parse()
    horizontals,verticals = group_by_orientation(photos)
    # print(tuple8_of_photos)
    slides = randomize_slides(horizontals.copy(),verticals.copy())
    # print(photos)
    # print(horizontals)
    # print(verticals)
    make_output(slides)