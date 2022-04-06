from django.shortcuts import render

from .models import FileUpload


def upload_file(request):      
    file_name = 'price.odt'
    file_cart = FileUpload.objects.create(
        name=file_name,
        size=12123,
        path='files/'
    )
    file_cart.refresh_from_db()
    print('file.cart name refreshed = ', file_cart.name)
    return render(request, 'storage/upload.html', {'file_name': f'{file_name} -> {file_cart.name}'})


