from rest_framework import serializers

from Accounts.models import User

class AcountSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","role","password","phone"]

        read_only_fields=["id","role"]