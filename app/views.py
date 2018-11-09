from django.http import JsonResponse

def keyboard(request):
    
    return JsonResponse(
        {
        'type': 'buttons',
        'buttons': ['공식', 'E-강의동', '도서관']
        }
    )

# Create your views here.
