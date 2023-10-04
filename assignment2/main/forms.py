from django.forms import ModelForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User   

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "amount"]

# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(label='username')
#     password1 = forms.CharField(label='password1', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
    
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2
    
#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],    
#             self.cleaned_data['password1']  
#         )  
#         return user  

