from rest_framework import serializers

from userprofileapp.models import UserProfile
from usersapp.models import MainUser
from mainapp.serializers import MainUserSerializer




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'pk', 'username', 'email', 'is_staff'
#         )


class UserProfileSerializer(serializers.ModelSerializer):
    # nest the profile inside the user serializer
    user = MainUserSerializer()

    class Meta:
        model = UserProfile
        fields = (
            'first_name', 'middle_name', 'last_name', 'avatar',
            'phone', 'inn_field', 'address', 'user'
        )

    def update(self, instance, validated_data):
        nested_serializer = self.fields['user']
        nested_instance = instance.profile
        # note the data is `pop`ed
        nested_data = validated_data.pop('profile')
        nested_serializer.update(nested_instance, nested_data)
        # this will not throw an exception,
        # as `profile` is not part of `validated_data`
        return super(UserProfileSerializer, self).update(instance, validated_data)
