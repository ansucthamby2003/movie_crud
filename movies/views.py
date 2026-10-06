from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from json import loads

from movies.models import Movie
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class MovieListCreateView(View):
    def get(self,request):
        qs=Movie.objects.all().values()
        movie_list=list(qs)
        return JsonResponse(movie_list,safe=False)

    def post(self,request):
        form_data=loads(request.body)
        Movie.objects.create(
            name=form_data.get("name"),
            language=form_data.get("language"),
            duration=form_data.get("duration"),
            director=form_data.get("director"),
            release_date=form_data.get("release_date")
        )
        response_data=({"message":"movie created..."})
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class MovieRetrieveUpdateDeleteView(View):
    def get(self,request,pk):
        qs=Movie.objects.filter(id=pk).values()
        movie_list=list(qs)
        return JsonResponse(movie_list,safe=False)

    def put(self,request,pk):
        form_data=loads(request.body)
        Movie.objects.filter(id=pk).update(**form_data)
        response_data={"message":"movie updated..."}
        return JsonResponse(response_data)

    def delete(self,request,pk):
        qs=Movie.objects.filter(id=pk).delete()
        return JsonResponse({"message":"movie deleted"})