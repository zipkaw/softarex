from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateNameForm

import io
import os 
import joblib

from .apps import WebRevenueConfig
from .models import RestaurantData, UploadedFile
from model.revenue_predictor import *
from .forms import CSVUploadForm, RegistryUser

def prediction(data_to_predict):

    ml_models = {
        'KNeighbors':joblib.load('./model1knn.pkl'),
        'RandomForest':joblib.load('./model1rf.pkl'), 
        'LightGBM': joblib.load('./model1lgb.pkl'),
        'Linear': joblib.load('./model2.pkl'),
    }
    data = prepare_test_data(data_to_predict)
    return predict_revenue(ml_models.pop('Linear'), ml_models, data)

def to_csv(self, filepath, data):
        save_to_csv(data, filename=filepath)

def read_file(file_path, content):
    try:
        with open(file_path, 'r') as file:
            file.write(content)
        return "File written successfully"
    except IOError:
        return "Error writing to the file"

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            uploaded_file = UploadedFile(file=csv_file)    
            uploaded_file.save()  
            # # write_file('/home/plantator/revenue_predict/web_app_files/content.csv', str(csv_file.read()))
            # revenue = WebRevenueConfig.prediction(os.path.join('./web_app_files', csv_file.name))
            file_path = './web_app_files/response_file.csv'

            revenue = prediction(os.path.join('./web_app_files', csv_file.name))
            save_to_csv(revenue, file_path)
            with open(file_path, 'r') as file:
                response = FileResponse(file.read(), as_attachment=True)
                response['Content-Type'] = 'application/csv'
                response['Contenta-Disposition'] = 'attachment; filename=revenue.csv'
                return response
    else:
        form = CSVUploadForm(request.FILES)

    return render(request, 'revenue.html', {'form': form})

def sign_in(request): 
    
    if request.method == 'POST':
        register_user = RegistryUser(request.POST)

        if register_user.is_valid():
            user = User.objects.create_user(
                username=register_user.cleaned_data['username'],
                password=register_user.cleaned_data['password'], 
            )                   
            user.save()

            return HttpResponseRedirect(reverse('revenue'))
    else: 
        register_user = RegistryUser()

    context = {
        'form':register_user,
    }

    return render(request, 'user_form.html', context) 

@login_required
def update_name(request):
    if request.method == 'POST':
        form = UpdateNameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']
            user = request.user
            user.username = new_name
            user.save()
            return redirect('profile')
    else:
        form = UpdateNameForm()
    return render(request, 'update_name.html', {'form': form})