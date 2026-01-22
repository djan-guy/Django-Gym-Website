from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'email', 'duration', 'pricing', 'payment', 'membership']
