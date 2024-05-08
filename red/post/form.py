from django.forms import ModelForm
from .models import Post, Topic
class createPost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
class createTopics(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'