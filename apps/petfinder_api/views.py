from django.shortcuts import render, redirect
import requests
import petfinder

# Create your views here.
def index(request):
    api = petfinder.PetFinderClient(api_key='a2a128f9fc017e107d12f400c579ba54', api_secret='5fb1ed325a37e2ce66c1a4600f652a70')
    pet_array = []
    for pet in api.pet_find(animal="dog", location="29678", output="basic",breed="Treeing Walker Coonhound", count=1):
        pet_array.append("%s - %s" % (pet['id'], pet['name']))
        print("%s - %s" % (pet['id'], pet['name']))
    print("Pet Array: " + str(pet_array))
    context = {
        'pet_array': pet_array,
    }
    return render(request, 'petfinder_api/index.html',context)