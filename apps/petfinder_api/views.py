from django.shortcuts import render, redirect
# from forms import dogform
import wikipedia
import requests
import petfinder
import petpy
import json
from api_key import api_key

# Create your views here.
def barnyard_breeds(request):
    barnyard_breeds = []
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    breed_list = Petfinder.breed_list('barnyard', outputformat='json', return_df=False)
    print (breed_list)
    breed = breed_list['petfinder']['breeds']['breed']
    print (breed)
    petfinder = breed_list['petfinder']
    print (petfinder)
    breeds = petfinder['breeds']
    print (breeds)
    breed_type = breeds['breed']
    print (breed_type)
    breed_name = breed_type
    print (breed_name)
    for breed in breed_name:
        print (breed['$t'])
        barnyard_breeds.append(str(breed['$t']))
    print (barnyard_breeds)
    context = {
        'barnyard_breeds': barnyard_breeds,
        'breed_list': breed_list,
    }
    return render(request, 'petfinder_api/barnyard_breeds.html', context)

def bird_breeds(request):
    bird_breeds = []
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    breed_list = Petfinder.breed_list('bird', outputformat='json', return_df=False)
    print (breed_list)
    breed = breed_list['petfinder']['breeds']['breed']
    print (breed)
    petfinder = breed_list['petfinder']
    print (petfinder)
    breeds = petfinder['breeds']
    print (breeds)
    breed_type = breeds['breed']
    print (breed_type)
    breed_name = breed_type
    print (breed_name)
    for breed in breed_name:
        print (breed['$t'])
        bird_breeds.append(str(breed['$t']))
    print (bird_breeds)
    context = {
        'breed_list': breed_list,
        'bird_breeds': bird_breeds,
    }
    return render(request, 'petfinder_api/bird_breeds.html', context)

def cat_breeds(request):
    cat_breeds = []
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    breed_list = Petfinder.breed_list('cat', outputformat='json', return_df=False)
    print (breed_list)
    breed = breed_list['petfinder']['breeds']['breed']
    print (breed)
    petfinder = breed_list['petfinder']
    print (petfinder)
    breeds = petfinder['breeds']
    print (breeds)
    breed_type = breeds['breed']
    print (breed_type)
    breed_name = breed_type
    print (breed_name)
    for breed in breed_name:
        print (breed['$t'])
        cat_breeds.append(str(breed['$t']))
    print (cat_breeds)
    context = {
        'breed_list': breed_list,
        'cat_breeds': cat_breeds,
    }
    return render(request, 'petfinder_api/cat_breeds.html', context)

def dog_breeds(request):
    dog_breeds = []
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    breed_list = Petfinder.breed_list('dog', outputformat='json', return_df=False)
    print (breed_list)
    breed = breed_list['petfinder']['breeds']['breed']
    print (breed)
    petfinder = breed_list['petfinder']
    print (petfinder)
    breeds = petfinder['breeds']
    print (breeds)
    breed_type = breeds['breed']
    print (breed_type)
    breed_name = breed_type
    print (breed_name)
    for breed in breed_name:
        print (breed['$t'])
        dog_breeds.append(str(breed['$t']))
    print (dog_breeds)
    context = {
        'breed_list': breed_list,
        'dog_breeds': dog_breeds,
    }
    return render(request, 'petfinder_api/dog_breeds.html', context)

def find_pet(request):
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    find_pet = Petfinder.pet_find(95112, animal="cat", outputformat='json', return_df=False)
    petfinder_results = find_pet['petfinder']
    pets = petfinder_results['pets']
    pet = pets['pet']
    header = petfinder_results['header']
    status = header['status']
    context = {
        'header': header,
        'find_pet': find_pet,
        'petfinder_results': petfinder_results,
        'pet': pet,
        'pets': pets,
        'status': status,
    }
    return render(request, 'petfinder_api/find_pet.html', context)

def find_dog(request):
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    find_pet = Petfinder.pet_find(95112, animal="dog", outputformat='json', return_df=False)
    # print (find_pet)
    petfinder_results = find_pet['petfinder']
    # print (petfinder_results)
    pets = petfinder_results['pets']
    # print(pets)
    pet = pets['pet']
    header = petfinder_results['header']
    # print (header)
    status = header['status']
    # print (status)
    i = 0
    context = {
        'header': header,
        'find_pet': find_pet,
        'petfinder_results': petfinder_results,
        'pet': pet,
        'pets': pets,
        'status': status,
    }
    return render(request, 'petfinder_api/find_dog.html', context)

def index(request):
    context = {
    }
    return render(request, 'petfinder_api/index.html',context)


def reptile_breeds(request):
    reptile_breeds = []
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    breed_list = Petfinder.breed_list('reptile', outputformat='json', return_df=False)
    print (breed_list)
    breed = breed_list['petfinder']['breeds']['breed']
    print (breed)
    petfinder = breed_list['petfinder']
    print (petfinder)
    breeds = petfinder['breeds']
    print (breeds)
    breed_type = breeds['breed']
    print (breed_type)
    breed_name = breed_type
    print breed_name
    for breed in breed_name:
        print (breed['$t'])
        reptile_breeds.append(str(breed['$t']))
    print (reptile_breeds)
    context = {
        'breed_list': breed_list,
        'reptile_breeds': reptile_breeds,
    }
    return render(request, 'petfinder_api/reptile_breeds.html', context)

def pet_search(request):
    if request.method == 'POST':
        animal_type = request.POST['animal_type']
        print (animal_type)
        if animal_type == 'barnyard':
            context = {
                'animal_type': animal_type,
            }
            return render(request, 'petfinder_api/dog_search.html',context)
        if animal_type == 'bird':
            context = {
                'animal_type': animal_type,
            }
            return render(request, 'petfinder_api/bird_search.html',context)
        if animal_type == 'cat':
            context = {
                'animal_type': animal_type,
            }
            return redirect("/cat_search", context)
            return render(request, 'petfinder_api/cat_search.html',context)
        if animal_type == 'dog':
            context = {
                'animal_type': animal_type,
            }
            return render(request, 'petfinder_api/dog_search.html',context)
        if animal_type == 'reptile':
            context = {
                'animal_type': animal_type,
            }
            return render(request, 'petfinder_api/reptile_search.html',context)
    else:
        # form = dogform
        context = {
        # 'form': form,
        }
        return render(request, 'petfinder_api/pet_search.html',context)

def bird_search(request):
    if request.method == 'POST':
        animal = 'bird'
        print(animal)
        bird_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list(animal=animal, outputformat='json', return_df=False)
        print (breed_list)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            bird_breeds.append(str(breed['$t']))
        print (bird_breeds)
        # POST REQUEST
        bird_breed = request.POST['bird_breed']
        print(bird_breed)
        request.session['bird_breed'] = bird_breed
        session_bird_breed = request.session['bird_breed']
        print ("Session Bird Breed: " + str(session_bird_breed))
        zip_code = request.POST['zip_code']
        print(zip_code)
        request.session['zip_code'] = zip_code
        session_zip_code = request.session['zip_code']
        request.session['animal_type'] = animal
        session_animal = request.session['animal']
        print("Session Animal: " + str(session_animal))
        context = {
            'animal': animal,
            'session_animal': session_animal,
            'bird_breed': bird_breed,
            'bird_breeds': bird_breeds,
            'session_bird_breed': session_bird_breed,
            'breed_list': breed_list,
            'zip_code': zip_code,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        bird_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('bird', outputformat='json', return_df=False)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            bird_breeds.append(str(breed['$t']))
        print (bird_breeds)
        context = {
            'breed_list': breed_list,
            'bird_breeds': bird_breeds,
        }
        return render(request, 'petfinder_api/bird_search.html',context)

def barnyard_search(request):
    if request.method == 'POST':
        animal = 'barnyard'
        print(animal)
        barnyard_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list(animal=animal, outputformat='json', return_df=False)
        print (breed_list)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            barnyard_breeds.append(str(breed['$t']))
        print(barnyard_breeds)
        # POST REQUEST
        barnyard_breed = request.POST['barnyard_breed']
        print(barnyard_breed)
        request.session['barnyard_breed'] = barnyard_breed
        session_barnyard_breed = request.session['barnyard_breed']
        print ("Session Barnyard Breed: " + str(session_barnyard_breed))
        zip_code = request.POST['zip_code']
        print(zip_code)
        request.session['zip_code'] = zip_code
        session_zip_code = request.session['zip_code']
        request.session['animal_type'] = animal
        session_animal = request.session['animal']
        print("Session Animal: " + str(session_animal))
        context = {
            'animal': animal,
            'session_animal': session_animal,
            'barnyard_breed': barnyard_breed,
            'barnyard_breeds': barnyard_breeds,
            'session_barnyard_breed': session_barnyard_breed,
            'breed_list': breed_list,
            'zip_code': zip_code,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        barnyard_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('barnyard', outputformat='json', return_df=False)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            barnyard_breeds.append(str(breed['$t']))
        print (barnyard_breeds)
        context = {
            'barnyard_breeds': barnyard_breeds,
            'breed_list': breed_list,
        }
        return render(request, 'petfinder_api/barnyard_search.html',context)

def cat_search(request):
    if request.method == 'POST':
        animal = 'cat'
        print(animal)
        cat_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list(animal=animal, outputformat='json', return_df=False)
        print (breed_list)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            cat_breeds.append(str(breed['$t']))
        print (cat_breeds)
        # POST REQUEST
        cat_breed = request.POST['cat_breed']
        print(cat_breed)
        request.session['cat_breed'] = cat_breed
        session_cat_breed = request.session['cat_breed']
        print ("Session Cat Breed: " + str(session_cat_breed))
        zip_code = request.POST['zip_code']
        print(zip_code)
        request.session['zip_code'] = zip_code
        session_zip_code = request.session['zip_code']
        request.session['animal_type'] = animal
        session_animal = request.session['animal']
        print("Session Animal: " + str(session_animal))
        context = {
            'animal': animal,
            'session_animal': session_animal,
            'cat_breed': cat_breed,
            'cat_breeds': cat_breeds,
            'session_cat_breed': session_cat_breed,
            'breed_list': breed_list,
            'zip_code': zip_code,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        request.session['animal'] = 'cat'
        cat_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('cat', outputformat='json', return_df=False)
        print (breed_list)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            cat_breeds.append(str(breed['$t']))
        print (cat_breeds)
        context = {
            'cat_breeds': cat_breeds,
            'breed_list': breed_list,
        }
        return render(request, 'petfinder_api/cat_search.html',context)

def dog_search(request):
    if request.method == 'POST':
        dog_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('dog', outputformat='json', return_df=False)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            dog_breeds.append(str(breed['$t']))
        print (dog_breeds)
        animal_type = "dog"
        request.session['animal_type'] = animal_type
        print(animal_type)
        print(request.POST)
        #Below Line of Code Doesn't transmit dog_breed request.POST
        dog_breed = request.POST['dog_breed']
        request.session['dog_breed'] = dog_breed
        session_dog_breed = request.session['dog_breed']
        print("Dog Breed: " + str(session_dog_breed))
        zip_code = request.POST['zip_code']
        request.session['zip_code'] = zip_code
        session_zip_code = request.session['zip_code']
        print("Session Zip Code: " + str(session_zip_code))
        context = {
            'animal_type': animal_type,
            'breed_list': breed_list,
            'dog_breed': dog_breed,
            'dog_breeds': dog_breeds,
            'session_dog_breed': session_dog_breed,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        request.session['animal'] = 'dog'
        dog_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('dog', outputformat='json', return_df=False)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            dog_breeds.append(str(breed['$t']))
        print (dog_breeds)
        animal_type = "dog"
        request.session['animal_type'] = animal_type
        print (animal_type)
        context = {
            'animal_type': animal_type,
            'breed_list': breed_list,
            'dog_breeds': dog_breeds,
        }
        return render(request, 'petfinder_api/dog_search.html',context)

def reptile_search(request):
    if request.method == 'POST':
        animal = 'reptile'
        print(animal)
        reptile_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list(animal=animal, outputformat='json', return_df=False)
        print (breed_list)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print (breed_name)
        for breed in breed_name:
            print (breed['$t'])
            reptile_breeds.append(str(breed['$t']))
        print (reptile_breeds)
        # POST REQUEST
        reptile_breed = request.POST['reptile_breed']
        print(reptile_breed)
        request.session['reptile_breed'] = reptile_breed
        session_reptile_breed = request.session['reptile_breed']
        print ("Session Reptile Breed: " + str(session_reptile_breed))
        zip_code = request.POST['zip_code']
        print(zip_code)
        request.session['zip_code'] = zip_code
        session_zip_code = request.session['zip_code']
        request.session['animal_type'] = animal
        session_animal = request.session['animal']
        print("Session Animal: " + str(session_animal))
        context = {
            'animal': animal,
            'session_animal': session_animal,
            'reptile_breed': reptile_breed,
            'reptile_breeds': reptile_breeds,
            'session_reptile_breed': session_reptile_breed,
            'breed_list': breed_list,
            'zip_code': zip_code,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        reptile_breeds = []
        Petfinder = petpy.api.Petfinder(api_key['api_key'])
        breed_list = Petfinder.breed_list('reptile', outputformat='json', return_df=False)
        print (breed_list)
        breed = breed_list['petfinder']['breeds']['breed']
        print (breed)
        petfinder = breed_list['petfinder']
        print (petfinder)
        breeds = petfinder['breeds']
        print (breeds)
        breed_type = breeds['breed']
        print (breed_type)
        breed_name = breed_type
        print breed_name
        for breed in breed_name:
            print (breed['$t'])
            reptile_breeds.append(str(breed['$t']))
        print (reptile_breeds)
        context = {
            'breed_list': breed_list,
            'reptile_breeds': reptile_breeds,
        }
        return render(request, 'petfinder_api/reptile_search.html',context)


def result(request):
    animal = request.session['animal_type']
    print(animal)
    session_cat_breed = request.session['cat_breed']
    print(session_cat_breed)
    cat_breed = session_cat_breed
    session_zip_code = request.session['zip_code']
    print(session_zip_code)
    zip_code = session_zip_code
    zip_code = request.session['zip_code']
    Petfinder = petpy.api.Petfinder(api_key['api_key'])
    find_pet = Petfinder.pet_find(location=zip_code, animal=animal, outputformat='json', return_df=False)
    petfinder_results = find_pet['petfinder']
    pets = petfinder_results['pets']
    pet = pets['pet']
    header = petfinder_results['header']
    status = header['status']
    context = {
        'header': header,
        'find_pet': find_pet,
        'petfinder_results': petfinder_results,
        'pet': pet,
        'pets': pets,
        'session_cat_breed': session_cat_breed,
        'session_zip_code': session_zip_code,
        'status': status,
    }
    return render(request, 'petfinder_api/result.html',context)
