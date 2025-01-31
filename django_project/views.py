from django.shortcuts import render

def custom_page_not_found(request, exception):  # Ensure both request and exception are included
    return render(request, "404.html", status=404)
