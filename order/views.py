from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from profiles.models import Profile
from order.models import Order

# Create your views here.
