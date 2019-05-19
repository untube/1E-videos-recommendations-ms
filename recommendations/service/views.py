from django.shortcuts import render
from django.http import HttpResponse
from service.models import UserPreferences
from service.models import VideoStatistics

# Create your views here.
def feedDbUser(request):
    response = ""
    user_id = 0
    category_id = 1
    temp = UserPreferences.objects.filter(id_user = user_id).filter(id_category = category_id)
    if len(temp) == 0:
        user = UserPreferences(id_user = user_id, id_category = category_id)
        user.save()
        response = "nuevo usuario"
    else:
        count = temp[0].counter
        count += 1
        temp[0].counter = count
        temp[0].save()
        response = "usuario existente"
    
    return HttpResponse(response)

def feedDbVideo(request):
    response = ""
    video_id = 0
    category_id = 1
    score = 1

    temp = VideoStatistics.objects.filter(id_video = video_id).filter(id_category = category_id)
    if len(temp) == 0:
        user = VideoStatistics(id_video = video_id, id_category = category_id, sumCalification = score)
        user.save()
        response = "usuario nuevo"
    else:
        suma = temp[0].sumCalification
        suma += score
        temp[0].sumCalification = suma
        count = temp[0].num_views
        count += 1
        temp[0].num_views = count
        cali_count = temp[0].calicationsCount
        cali_count += 1
        temp[0].calicationsCount = cali_count
        temp[0].save()
        response = "usuario antiguo"

    return HttpResponse(response)

def searchRecommendations(request):
    response = ""
    user_id = 0
    temp = UserPreferences.objects.filter(id_user = user_id)
    if len(temp == 0):
        response = "no hay recomendaciones"
    else:
        categories = []
        for i in range(len(temp)):
            categories.append((temp[i].id_category, temp[i].counter))
        if len(categories) > 0:
            recomendations = []
            for j in range(categories):
                temp = VideoStatistics.objects.filter(categories[i])
                if len(temp) != 0:
                    promedio = temp[j].calicationsCount / temp[j].num_views
                    recomendations.append((temp[j].id_video, temp[j].num_views, promedio))


    return HttpResponse(response)