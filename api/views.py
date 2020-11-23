
from api.models import mhs, jurusan
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from api.serialization import SerializationClass,JurusanSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render


@api_view(['GET'])
def showmhs(request):
    if request.method == 'GET':
        results = mhs.objects.all()
        serialize = SerializationClass(results, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def savemhs(request):
    if request.method == 'POST':
        saveserialize = SerializationClass(data=request.data)
    if saveserialize.is_valid():
        saveserialize.save()
        return JsonResponse({'message': 'data berhasil di tambahkan'}, status=status.HTTP_200_OK)
        return Response(saveserialize.data, Status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request):
    data = request.query_params.get('id')
    data.objects.all().delete()
    return JsonResponse({'message': 'data berhasil di hapus.'}, status=status.HTTP_200_OK)


def halaman_depan(request):
    context = {'foo': 'bar',
               'mhs': mhs.objects.all()
               }
    return render(request, 'home.html', context)

def handler404(request):
    return render(request, '404.html', status=404)


# get of majoring data
@api_view(['GET'])
def showjurusan(request):
    if request.method == 'GET':
        results = jurusan.objects.all()
        karambia = SerializationClass(results, many=True)
        return Response(karambia.data)

@api_view(['POST'])
def savejurusan(request):
    if request.method == 'POST':
        savejurusan = SerializationClass(data=request.data)
    if savejurusan.is_valid():
        savejurusan.save()
        return JsonResponse({'message': 'data jurusan berhasil di tambahkan'}, status=status.HTTP_200_OK)
        # return Response(savejurusan.data, Status=status.HTTP_400_BAD_REQUEST)

 