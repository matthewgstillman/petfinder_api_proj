from django.shortcuts import render, redirect
# from forms import dogform
import wikipedia
import requests
import petfinder
import petpy
import json

# Create your views here.
def barnyard_breeds(request):
    barnyard_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    bird_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    barnyard_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
        cat_breeds = []
        Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
        context = {
            'cat_breed': cat_breed,
            'cat_breeds': cat_breeds,
            'session_cat_breed': session_cat_breed,
            'breed_list': breed_list,
            'zip_code': zip_code,
            'session_zip_code': session_zip_code,
        }
        return redirect("/result", context)
    if request.method == 'GET':
        cat_breeds = []
        Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    dog_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    return render(request, 'petfinder_api/dog_search.html',context)

def reptile_search(request):
    reptile_breeds = []
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
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
    session_cat_breed = request.session['cat_breed']
    print(session_cat_breed)
    cat_breed = session_cat_breed
    session_zip_code = request.session['zip_code']
    print(session_zip_code)
    zip_code = session_zip_code
    zip_code = request.session['zip_code']
    Petfinder = petpy.api.Petfinder('a2a128f9fc017e107d12f400c579ba54')
    find_pet = Petfinder.pet_find(location=zip_code, animal="cat", outputformat='json', return_df=False)
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
