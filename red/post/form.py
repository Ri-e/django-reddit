from django.forms import ModelForm
from .models import Post, Topic, Comment
class createPost(ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'heading', 'desc']
class createTopics(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
class editComment(ModelForm):
    class Meta:
        model=Comment
        fields = ['message']