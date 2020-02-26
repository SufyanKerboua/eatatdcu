from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus
import json,requests

#from django.core.exceptions import ObjectDoesNotExist

def index(request):
   # print(Campus.objects.all())
   context = {}
   campus_json = serializers.serialize("json", Campus.objects.all())
   print(campus_json)
   context["campus_json"] = campus_json
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   # get the campus name from the request
   campus_name = request.GET.get('campus').lower()
   try:
      # retrieve the campus id from the db given this campus name
      campus_obj = Campus.objects.get(name = campus_name)
      campus_data = {'id': campus_obj.campus_id, 'name': campus_obj.name.title()}
      # find all restaurants for that campus 
      restaurants_obj = Restaurant.objects.filter(campus_id = campus_obj.campus_id)
      # put the information returned from the db in the context dictionary
      context = {'restaurants':restaurants_obj, 'campus_data':campus_data}
   except Campus.DoesNotExist:
      # handles the case where an invalid campus name is entered
      context = {'error':'No such campus'}
   return render(request, 'eatatdcu/restaurants.html', context)

def specials(request,restaurant):

   webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant
   response = requests.get(webservice_url)
   data = response.json()
   if ('error_num' in data):
      context = {
         'error_msg' : data['error_msg']
         }
   else:
      try:
         # print("here1|"+ data['restaurant_name'] + "|")
         obj_restau = Restaurant.objects.get(name = data['restaurant_name'])
         context = {
            'name' : data['restaurant_name'],
            'daily_special' : data['daily_special'],
            'time' : data['date'],
            'id_restaurant': obj_restau.restaurant_id
            }
      except Restaurant.DoesNotExist:
         context = {
            'name' : data['restaurant_name'],
            'daily_special' : data['daily_special'],
            'time' : data['date']
            }
      
   return render(request,'eatatdcu/specials.html', context)

def find_restaurants(request):
   context = {}
   restaurants_obj = Restaurant.objects.all()
   for restaurant in restaurants_obj:
      # print("Data of rest : Name:", restaurant.name, ", id campus: ", restaurant.campus_id)
      webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant.name
      data = requests.get(webservice_url).json()
      if ('daily_special' in data):
         restaurant.specials = data['daily_special']
      else:
         restaurant.specials = "No specials"
      restaurant.name = restaurant.name.title()
      restaurant.campus_name = str(restaurant.campus_id).title()

   campus_name_requiered = request.GET.get('form_campus_name')
   staff_requiered = request.GET.get('form_staff')
   special_dishes_requiered = request.GET.get('form_select_special_dishes')


   need_to_check_name = False
   need_to_check_staff = False
   need_to_check_special = False

   if ((campus_name_requiered != None) and (campus_name_requiered != "indifferent")):
      need_to_check_name = True
   if ((staff_requiered != None) and (staff_requiered != "anyone")):
      need_to_check_staff = True
   if ((special_dishes_requiered != None) and (special_dishes_requiered != "")):
      need_to_check_special = True

   # print("Value, name : ", campus_name_requiered, ", staff :", staff_requiered, ", special :", special_dishes_requiered)
   # print("Config, name : ", need_to_check_name, ", staff :", need_to_check_staff, ", special :", need_to_check_special)
   new_restaurants_list = []
   try:
      for r in restaurants_obj:
         push_current_obj = True
         
         if ((need_to_check_name) and (campus_name_requiered != r.campus_name.lower())):
            push_current_obj = False
         
         if ((need_to_check_staff) and (not r.staff_only)):
            push_current_obj = False
         
         if ((need_to_check_special) and (special_dishes_requiered not in r.specials)):
            push_current_obj = False

         if (push_current_obj):
            new_restaurants_list.append(r)

   except:
      print("ok")
   
   context["restaurant_obj"] = new_restaurants_list
   return render(request,'eatatdcu/find_restaurants.html',context)