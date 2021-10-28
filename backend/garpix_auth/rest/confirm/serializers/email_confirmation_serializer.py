from rest_framework import serializers


class EmailConfirmSendSerializer(serializers.Serializer):
    email = serializers.EmailField()


class EmailConfirmCheckCodeSerializer(serializers.Serializer):
    email_confirmation_code = serializers.models.CharField(max_length=15)


class EmailPreConfirmSendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class EmailPreConfirmCheckCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    email_confirmation_code = serializers.models.CharField(max_length=15)


class EmailPreConfirmCheckSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    token = serializers.models.CharField(max_length=40)