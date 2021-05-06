from django.forms import ModelForm
from .models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']