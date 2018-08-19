from django.shortcuts import render, redirect
import requests
import petfinder
import petpy
import json

# Create your views here.
def cat_breeds(request):
    cat_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
    breed_list = Petfinder.breed_list('cat', outputformat='json', return_df=False)
    print breed_list
    breed = breed_list['petfinder']['breeds']['breed']
    print breed
    petfinder = breed_list['petfinder']
    print petfinder
    breeds = petfinder['breeds']
    print breeds
    breed_type = breeds['breed']
    print breed_type
    breed_name = breed_type
    print breed_name
    for breed in breed_name:
        print breed['$t']
        cat_breeds.append(str(breed['$t']))
    print cat_breeds
    context = {
        'breed_list': breed_list,
        'cat_breeds': cat_breeds,
    }
    return render(request, 'petfinder_api/cat_breeds.html', context)


def index(request):
    api = petfinder.PetFinderClient(api_key='a2a128f9fc017e107d12f400c579ba54', api_secret='5fb1ed325a37e2ce66c1a4600f652a70')
    pet_array = []
    for pet in api.pet_find(animal="dog", location="29678", output="basic",breed="Treeing Walker Coonhound", count=1):
        pet_array.append("%s - %s" % (pet['id'], pet['name']))
        # print("%s - %s" % (pet['id'], pet['name']))
    print("Pet Array: " + str(pet_array))
    context = {
        'pet_array': pet_array,
    }
    return render(request, 'petfinder_api/index.html',context)