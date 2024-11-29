from django import forms
from .models import Member
from .models import BlogPost

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'second_name', 'phone_number', 'email', 'date_of_birth', 'home_address', 'state_of_origin']  # Changed 'second_name' to 'last_name'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']