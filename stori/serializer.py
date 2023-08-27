from rest_framework import serializers


class RequestDataSerializer(serializers.Serializer):
    email_recipient = serializers.EmailField(required=True)

    def validate_email_recipient(self, value):
        if value == '':
            raise serializers.ValidationError("Email can't be empty")
        return value
