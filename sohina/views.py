# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_user_agents.utils import get_user_agent
from django.views.decorators.csrf import ensure_csrf_cookie
import time

def home(request):
	user_agent = get_user_agent(request)
	if user_agent.is_mobile:
		return render(request, "home_mobile_2.html")
	elif user_agent.is_tablet:
		return render(request, "home_mobile_2.html")
	else:
		return render(request, "home_pc_2.html")

def dev_mobile(request):
	user_agent = get_user_agent(request)
	if user_agent.is_mobile:
		return render(request, "home_mobile_2.html")
	elif user_agent.is_tablet:
		return render(request, "home_mobile_2.html")
	else:
		return render(request, "home_pc_2.html")
