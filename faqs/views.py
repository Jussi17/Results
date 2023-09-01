from django.shortcuts import render


def faqindex(request):
    return render(request, 'faqs/faqs.html')