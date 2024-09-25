from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Document
from django.http import JsonResponse
from .models import Document
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'index.html')



def infinput(request):
    success_message = None
    if request.method == "POST":
        document_name = request.POST.get('document-name', '')
        owner_name = request.POST.get('owner-name', '')
        certificate_number = request.POST.get('certificate-number', '')
        completion_date = request.POST.get('completion-date', '')

        details = Document(
            document_name=document_name,
            owner_name=owner_name,
            certificate_number=certificate_number,
            completion_date=completion_date
        )
        details.save()
        success_message = 'The data has been saved to the db'
        
    return render(request, 'infinput.html', {'success_message': success_message})

def display(request):
    details = Document.objects.all()  # Fetch all records
    return render(request, 'display.html', {'details': details})

def document_info(request):
    if request.method == 'GET':
        owner_name = request.GET.get('owner-name', '')
        certificate_number = request.GET.get('certificate_number', '')

        # Query the database
        documents = Document.objects.filter(
            owner_name=owner_name,
            certificate_number=certificate_number
        )

        # Prepare the response
        if documents.exists():
            data = [{'document_name': doc.document_name,
                     'certificate_number': doc.certificate_number}
                    for doc in documents]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



def verify_document(request):
    print(f"Request method: {request.method}")
    
    if request.method == 'GET':
        try:
            # Retrieve query parameters
            owner_name = request.GET.get('owner-name')
            cert_number = request.GET.get('cert_number')
            
            print(f"Received parameters - owner_name: {owner_name}, cert_number: {cert_number}")
            
            # Process the parameters (e.g., verify the document)
            response_data = {
                "status": "success",
                "message": "Document verified successfully.",
                "owner-name": owner_name,
                "cert_number": cert_number,
                # Include any additional verification details
            }
            
            print(f"Response data: {response_data}")
        except Exception as e:
            response_data = {
                "status": "error",
                "message": str(e),
            }
            print(f"Exception occurred: {e}")
        
        return JsonResponse(response_data)
    else:
        print("Invalid request method")
        return JsonResponse({"status": "error", "message": "Invalid request method."})



