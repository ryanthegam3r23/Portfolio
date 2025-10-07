from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about_me.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body = (
                f'You have a new email from your portolio \n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}\n'
            )

            try:
                send_mail(
                    "Email from portfolio",
                    message_body,
                    email,
                    ['rypop04@gmail.com']
                )
                form = ContactForm()
                return render(request, 'portfolio/contact.html',{'form':form})
            except Exception as e:
                print(f'Error sending email: {e}')

                return render(request,'portfolio/contact.html',{'form':form})
        else:
            print("data" + name, email, message)
    else:            
        form = ContactForm()
        return render(request, 'portfolio/contact.html',{'form':form})