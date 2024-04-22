from django.shortcuts import render,redirect
from .models import book
from .forms import mybook



def has(request):
    form=mybook()
    if request.method=='POST':
       form=mybook(request.POST)
       if form.is_valid():
          form.save()
          return redirect('/has1')
          
    else:
         form=mybook()
         whos=book.objects.all()
         return render(request,'index.html',{'form':form,'whos':whos})
    
def has1(request):
    whos=book.objects.all()
    return render(request,'index.html1',{'whos':whos})

    
