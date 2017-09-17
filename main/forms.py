from django import forms
from django.forms import ModelForm, Textarea
from .models import Profile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first = forms.CharField(help_text='Required')
    last = forms.CharField()
    birth_date = forms.DateField(help_text="Please use the following format: YYYY-MM-DD.")
    # fields_of_expertise = HStoreField(null=True)
    # account_value = forms.DecimalField()
    # hours_taught = models.IntegerField()
    # ratingsArray = ArrayField(models.IntegerField(default=0),null=True)
    # avg_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, null=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'first', 'last', 'birth_date','password1', 'password2' )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'first', 'last', 'birth_date' ]
