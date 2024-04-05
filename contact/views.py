from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Contact
from .forms import ContactForm, UserAplicationForm
from .serializers import ContactSerializer
from helpers.sendEmail.sendConfirmEmail import send_email_to_user


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
            pdf_path = form.cleaned_data['pdf_path']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
        
            sent_count = send_email_to_user(firstname, lastname, pdf_path)
            serializer = ContactSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.validated_data['cv'] = True if sent_count > 0 else False
                print(serializer.data)
                serializer.save()
            
            if sent_count > 0:
                return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
            return Response({"message": "Email not sent!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
