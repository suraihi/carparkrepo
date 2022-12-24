from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import random
import time

num = "temp = 10"

def home_view(*args, **kwargs):



	return HttpResponse(num)
	
	

