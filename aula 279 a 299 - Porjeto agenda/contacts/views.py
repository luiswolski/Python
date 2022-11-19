from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def views_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.show:
        raise Http404()

    return render(request, 'contacts/views_contact.html', {
        'contact': contact
    })


def search(request):
    word = request.GET.get('word')

    if word is None or not word:
        messages.add_message(
            request,
            messages.ERROR,
            'Search field cannot be empty.'
        )
        return redirect('index')

    tags = Concat('name', Value(' '), 'last_name')

    contacts = Contact.objects.annotate(
        full_name=tags
    ).filter(
        Q(full_name__icontains=word) | Q(phone_number__icontains=word)
    )

    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })
