from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, required=True)
    address_line1 = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=50, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 
                 'user_type', 'address_line1', 'city', 'state', 'pincode', 'password1', 'password2')
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data