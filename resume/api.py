from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, FileResponse
from django.core.files import File
from rest_framework.parsers import MultiPartParser, FormParser
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
from weasyprint import HTML, CSS
import json

from users.models import User
from .models import ResumeProfile, EmploymentHistory, Education, Website, Skills
from .serializers import ResumeProfileSerializer, EmploymentHistorySerializer, EducationSerializer, WebsiteSerializer, SkillsSerializer
# weasyprint resume/templates/resume/wu.html tmp/sad.pdf

class ResumeModelViewSet(ModelViewSet):
    queryset = ResumeProfile.objects.all()
    serializer_class = ResumeProfileSerializer
    permission_classes = [IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'])
    def generate_resume(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        data = request.POST
        data = data.dict()
        file = request.FILES
        employment_history_string = data.get('employment_history')
        employment_history = json.loads(employment_history_string)
        education_string = data.get('education')
        education = json.loads(education_string)
        website_string = data.get('website')
        website = json.loads(website_string)
        skills_string = data.get('skills')
        skills = json.loads(skills_string)
        resume = ResumeProfile.objects.create(
            user=user,
            profile_pic=file["image"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data['last_name'],
            title=data["title"],
            phone=data["phone"],
            city=data["city"],
            country=data["country"],
            profile=data["profile"]
        )

        if len(employment_history) != 0:
            for data_list in employment_history:
                EmploymentHistory.objects.create(
                    role=data_list["role"],
                    company=data_list["company"],
                    city=data_list["city"],
                    start_date=data_list["start_date"],
                    end_date=data_list["end_date"],
                    description=data_list["description"],
                    employment_resume=resume
                )

        if len(education) != 0:
            for data_list in education:
                Education.objects.create(
                    school=data_list["school"],
                    degree=data_list["degree"],
                    city=data_list["city"],
                    start_date=data_list["start_date"],
                    end_date=data_list["end_date"],
                    education_resume=resume
                )

        if len(website) != 0:
            for data_list in website:
                Website.objects.create(
                    label=data_list["label"],
                    link=data_list["link"],
                    website_resume=resume
                )

        if len(skills) != 0:
            for data_list in skills:
                Skills.objects.create(
                    label=data_list["skill"],
                    skills_resume=resume
                )

        resume = ResumeProfile.objects.filter(user=user).last()
        employment_history = None
        education_resume = None
        website_resume = None
        skills_resume = None
        if EmploymentHistory.objects.filter(employment_resume=resume).exists():
            employment_history =  EmploymentHistory.objects.filter(employment_resume=resume)
        if Education.objects.filter(education_resume=resume).exists():
            education_resume =  Education.objects.filter(education_resume=resume)
        if Website.objects.filter(website_resume=resume).exists():
            website_resume =  Website.objects.filter(website_resume=resume)
        if Skills.objects.filter(skills_resume=resume).exists():
            skills_resume =  Skills.objects.filter(skills_resume=resume)
        html_string = render_to_string('resume/toronto.html', 
            { 
                "user" : resume,
                "employment_history": employment_history,
                "education_resume": education_resume,
                "website_resume": website_resume,
                "skills_resume": skills_resume,
            }
        )

        # Write the HTML string to a temporary file.
        with open('tmp/resume.html', 'w') as f:
            f.write(html_string)
        
        # Generate the PDF from the temporary file.
        HTML(filename='tmp/resume.html', base_url=request.build_absolute_uri()).write_pdf('tmp/mypdf.pdf', presentational_hints=True, optimize_size=('fonts', 'images'))

        # Delete the temporary HTML file after use (optional).
        os.remove('tmp/resume.html')
        return FileResponse(open('tmp/mypdf.pdf', 'rb'), content_type='application/pdf')
