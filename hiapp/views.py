from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import random


num = random.random()
def home_view(*args, **kwargs):
	return HttpResponse(num)
