from rest_framework import serializers
from .models import Images

#Validator
def file_size(value): 
    limit = 0.5 * 1024 * 1024
    if value.size > limit:
        raise serializers.ValidationError('File too large. Size should not exceed 500KB.')

class ImageSerializer(serializers.ModelSerializer):    
    image = serializers.ImageField(validators=[file_size])
    class Meta:
        model = Images
        fields = ('image','name')
    
