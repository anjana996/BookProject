from django.shortcuts import render, redirect
from book.models import Book
from book.forms import BookCreateForm,BookUpdate

# Create your views here.
def bookCreate(request):
    template_name="bookcreate.html"
    form=BookCreateForm()
    context={}
    books=Book.objects.all()
    context["books"]=books
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            qs=Book.objects.all()
            context={}
            context["books"]=qs
            return render(request, template_name, context)
        else:

            context["form"]=form
            return render(request, template_name, context)

    return render(request,template_name,context)
def listbook(request):
    template_name="list.html"
    qs=Book.objects.all()
    context={}
    context["books"]=qs
    return render(request,template_name,context)
def viewBook(request,pk):
    template_name="book.html"
    qs=Book.objects.get(id=pk)
    context={}
    context["book"]=qs
    return render(request,template_name,context)
def deleteBook(request,pk):
    qs = Book.objects.get(id=pk).delete()
    return redirect("list")

def updateBook(request,pk):
    book=Book.objects.get(id=pk)
    form = BookUpdate(instance=book)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BookUpdate(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    return render(request,"bookupdate.html",context)




