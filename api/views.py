
from api.models import mhs
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

from api.serialization import SerializationClass
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



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
       return JsonResponse({'message':'data berhasil di tambahkan'},status=status.HTTP_200_OK)
       return Response(saveserialize.data,Status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['DELETE'])
def delete(request):
    data = request.query_params.get('id')
    data.objects.all().delete()
    return JsonResponse({'message':'data berhasil di hapus.'},status=status.HTTP_200_OK)
 