from rest_framework import serializers
from api.models import Sponsor, Student, SponsorForStudent


class SponsorSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField
    class Meta:
        model = Sponsor
        fields = ('first_name', 'last_name', 'middle_name', 'tel_number',
                  'sponsorship_sum', 'spent_sum', 'date', 'status', 'actions')


class SponsorRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('person_type', 'first_name', 'last_name', 'middle_name', 'tel_number',
                  'sponsorship_sum', 'payment_type', 'organization')


class AddSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorForStudent
        fields = ('sponsor', 'student', 'allocated_sum')


# class AddSponsorSerializer2(serializers.Serializer):
#     sponsor = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all())
#     student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
#     allocated_sum = serializers.CharField()
#
#     def create(self, validated_data):
#
#         print('\n\n')
#         print(validated_data)
#         print('\n\n')
#         return SponsorForStudent.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.sponsor = validated_data.get('sponsor', instance.sponsor)
#         instance.allocated_sum = validated_data.get('allocated_sum', instance.allocated_sum)
#         instance.save()
#         return instance





class SponsorFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('status', 'date', 'sponsorship_sum')


class StudentSponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('first_name', 'last_name', 'middle_name', 'spent_sum')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'student_type', 'hti',
                  'contract_amount', 'allocated_sum', 'actions')


class StudentRUDSerializer(serializers.ModelSerializer):
    hti = serializers.StringRelatedField(source="hti.name")

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'student_type', 'hti',
                  'contract_amount', 'allocated_sum')






