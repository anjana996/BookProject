from django import forms
from book.models import Book
from django.forms import ModelForm
# class BookCreateForm(forms.Form):
#      book_name=forms.CharField(max_length=120)
#      author=forms.CharField(max_length=120)
#      price=forms.IntegerField()
#      page=forms.IntegerField()
class BookCreateForm(ModelForm):
     class Meta:
          model = Book
          fields = "__all__"

     def clean(self):
          cleaned_data=super().clean()
          bookname=cleaned_data.get('book_name')
          price=cleaned_data.get('price')
          pages=cleaned_data.get('page')
          book=Book.objects.filter(book_name=bookname)

          if book:
               msg="book with same name already exist"
               self.add_error('book_name',msg)
          if price<100:
               msg="please put price greater than 100"
               self.add_error('price',msg)
          if pages<50:
               msg="pageNo should be greater than 50"
               self.add_error('page',msg)

