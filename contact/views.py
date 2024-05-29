from django.forms import ValidationError
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from helpers import sendEmail
from helpers.sendEmail import sendConfirmEmail
from .models import Contact
from .forms import ContactForm, UserAplicationForm
from .serializers import ContactSerializer, UserAplicationSerializer
from helpers.sendEmail.sendConfirmEmail import send_confirm_email, send_email_to_user


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_status(request):
    return Response({"message": "API is runing!"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.data)
            if form.is_valid():
                serializer = ContactSerializer(data=form.cleaned_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Contact created successfully!"}, status=status.HTTP_201_CREATED)
                return Response({'error': 'error from serrializer'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            contacts = Contact.objects.all().order_by('-created_at')
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def apply(request):
    try:
        form = UserAplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # print("form is valid")
            pdf_path = form.cleaned_data['pdf_path']
            
            data = {
                'fullname': form.cleaned_data['fullname'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'current_location': form.cleaned_data['current_location'],
                'current_company': form.cleaned_data['current_company'],
                'notice_period': form.cleaned_data['notice_period'],
                'salary_expectation': form.cleaned_data['salary_expectation'],
                'gender': form.cleaned_data['gender'],
                'referral_source': form.cleaned_data['referral_source'],
                'years_of_experience': form.cleaned_data['years_of_experience'],
                'linkedin_profile': form.cleaned_data['linkedin_profile'],
                'github_profile': form.cleaned_data['github_profile'],
                'portfolio': form.cleaned_data['portfolio']
            }
            # print(data)
            sent_count = send_email_to_user(data, pdf_path)
            serializer = UserAplicationSerializer(data=form.cleaned_data)
            if serializer.is_valid() and sent_count > 0:
                print("serializer is valid")
                serializer.validated_data['cv'] = False if sent_count != 1 else True
                print(serializer.validated_data)
                serializer.save()
                return Response({"message": "Email sent successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                raise ValidationError("Invalid serializer data")
            
            return Response({"message": "Email not sent!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
