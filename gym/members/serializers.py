from rest_framework import serializers

from .models import person, service, service_type, exercise, booking

class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = '__all__'

class service_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = service_type
        fields = '__all__'

class exercizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = exercise
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'