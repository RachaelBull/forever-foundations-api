from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review, Profile

class ReviewSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    owner_username = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    natural_created_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_natural_created_on(self, obj):
        return naturaltime(obj.created_on)

    class Meta:
        model = Review
        fields = [
            'id', 'profile', 'owner_username', 'is_owner', 'profile_image',
            'natural_created_on', 'content', 'title'
        ]

class ReviewDetailSerializer(ReviewSerializer):
    profile = serializers.ReadOnlyField(source='profile.id')