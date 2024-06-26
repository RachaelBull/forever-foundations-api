from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2: #2MB file size limit
            raise serializers.ValidationError(
                'Image file size too large. Please select an image that is 2MB or smaller.'
            )
        if value.image.width > 4069:
            raise serializers.ValidationError(
                'Image file width too large. Please select an image with a width of 4069px or smaller.'
            )
        if value.image.height > 4069:
            raise serializers.ValidationError(
                'Image file height too large. Please select an image with a height of 4069px or smaller.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'created_on', 
            'updated_on', 'title', 'content', 'location', 'theme', 'image', 'is_owner'
        ]