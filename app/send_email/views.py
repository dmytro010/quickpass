
from .models import Contact
from .service import generate_pass
from .tasks import hello, send_email_task
from .forms import SecretForm
from django.shortcuts import render
from django.http import HttpResponse


def send_secret_view(request):
    secret = generate_pass()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        form = SecretForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']

            send_email_task.delay(email, description, secret)
            hello.delay()

            if form.cleaned_data['subscribe_for_news'] == True:
                new_contact = Contact.objects.create(email=email)
                new_contact.save()
                
            return HttpResponse(
            '''
            <h4>The password was send!</h4>
            <p>Please, check you email!<p>
            <p> Have a nice time :-) </p>
            ''')
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SecretForm()

    context = {'form': form, 'secret': secret}
    return render(request, 'send_email/contact.html', context)
    