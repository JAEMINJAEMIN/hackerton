from django.shortcuts import render
import csv

# Create your views here.



def index(request):
    address_list = []
    latitude_list= []
    longitude_list = []
    name_list = []
    disposal_list = []
    violation_list = []
    location_list = []
    with open('./data/dataset.csv', encoding = 'ms949', newline="") as f:
        data = csv.reader(f)
        next(data)

        for line in data:
            location_list.append(line)
        f.close
        
        location = location_list[:11]


        for line in data:
            content= ({
                'address' : line[1],
                'latitude' : line[2],
                'longitude' : line[3],
                'name' : line[5],
                'disposal' : line[10],
                'violation' : line[12].split('.')[0],
                'test' : [line[2],line[3]],
        })
            address_list.append(content['address'])
            latitude_list.append(content['latitude'])
            longitude_list.append(content['longitude'])
            name_list.append(content['name'])
            disposal_list.append(content['disposal']) 
            violation_list.append(content['violation']) 
  
    
    context ={
        'address' :  address_list,
        'latitude' : latitude_list,
        'longitude' : longitude_list,
        'name' : name_list,
        'disposal' : disposal_list,
        'violation' :violation_list,
        'location' : location_list
    }
    
    f.close()
    return render(request,'index2.html',context)



def main(request):
    return render(request, 'main.html')

def intro(request):
    return render(request, 'intro.html')

def find(request):
    return render(request, 'find.html')

def help1(request):
    return render(request, 'help.html')






