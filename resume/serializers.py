from .models import ResumeProfile, EmploymentHistory, Education, Website, Skills
from rest_framework.serializers import ModelSerializer

class ResumeProfileSerializer(ModelSerializer):
    class Meta:
        model = ResumeProfile
        fields = '__all__'


class EmploymentHistorySerializer(ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class WebsiteSerializer(ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'