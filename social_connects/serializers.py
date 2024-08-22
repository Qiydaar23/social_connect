from rest_framework.serializers import ModelSerializer
from users.models import Profile
from blog.models import Post

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'      