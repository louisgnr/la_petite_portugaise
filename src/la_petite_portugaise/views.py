from django.shortcuts import redirect
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from .forms import EmailPostForm
from django.utils.translation import ugettext_lazy as _

# def handler503(request, exception):
#     return render(request, '503.html', locals())

def page_redirect(request):
	if request.LANGUAGE_CODE == 'en':
		return redirect('en/')
	elif request.LANGUAGE_CODE == 'fr':
		return redirect('fr/')
	elif request.LANGUAGE_CODE == 'de':
		return redirect('de/')
	elif request.LANGUAGE_CODE == 'pt':
		return redirect('pt/')

def index(request):
    """
    Posts method: list all objects on the database + hide draft versions to non-staff users

    """
    return render(request, "posts/index.html") #queryset

def contact(request):
    sent = False 
 
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = 'New mail from {}'.format(cd['email'])
            message = 'Name {} \nSubject  {} \nMessage  {} \nEmail {} \n'.format(cd['name'], cd['subject'], cd['message'], cd['email'])
            send_mail(subject, message, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_RECIPIENT])
            sent = True
            messages.success(request,"Your message was successfully sent to: "+settings.EMAIL_HOST_RECIPIENT)
            return HttpResponseRedirect('')
        else:
            messages.error(request,"Your message could not be sent")
            return HttpResponseRedirect('')
    else:
        form = EmailPostForm()
    return render(request, "posts/contact.html", {'form': form,'Name_placeholder': _('Name')})


def aboutus(request):
    return render(request, "posts/about-us.html")