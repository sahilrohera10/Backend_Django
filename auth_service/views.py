from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from django.http import HttpResponse

@api_view(['GET'])
def test_api(request):

    #register service will be there to registering the user
    return Response({"message" : "Testing Successfully DONE !!"})


