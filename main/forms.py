from django.forms import ModelForm
from main import models

class CommentForm(ModelForm):
    class Meta:
        model=models.Comments
        fields=['text']
