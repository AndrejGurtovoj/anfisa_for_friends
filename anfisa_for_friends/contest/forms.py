from django import forms
from .models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['title', 'description', 'price', 'comment', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
        }