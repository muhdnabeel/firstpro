from django.shortcuts import render

# Create your views here.

def demo(request):
   return render(request,'index.html')

#def about(request):
  # return render(request,"about.html")

#def contact(request):
   #return render(request,"contact.html")# views.py
#def addition(request):
   #x=int(request.GET['num1'])
   #sub=x-y
   #mul=x*y
   #div=x/y
   
  
   #return render(request,"result.html",{'result':res,'subc':sub,'multi':mul,'divi':div}



