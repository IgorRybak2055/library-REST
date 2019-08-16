from django.shortcuts import render


def main_page(request):
    return render(request, 'users.html', locals())


def subs(request, id):
    return render(request, 'subscriptions.html', {'id': id})


def edit_book(request, id):
    return render(request, 'book.html', {'id':  id})


def free_books(request):
    return render(request, 'free_books.html', locals())


