
from api.models import mhs
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
       return Response(saveserialize.data,status=status.HTTP_200_OK)
       return Response(saveserialize.data,Status=status.HTTP_400_BAD_REQUEST)
