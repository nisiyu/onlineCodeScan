from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views import generic
from .models import user,plan,item
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import csrf

# Create your views here.
def index(request):
    return HttpResponse("Hello,world!")

def userview(request, user_id):
    # return HttpResponse(str(user_id))
    try:
        # uobj = user.objects.get(pk=user_id)
        objs = plan.objects.filter(owner=user_id)[:]
    except plan.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'usertemplate.html', {'user_plan': objs, 'user_id': user_id, 'request': request})


def planview(request, user_id, plan_id):
    try:
        # uobj = user.objects.get(pk=user_id)
        objs = item.objects.filter(owner=plan_id)[:]
    except plan.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'usertemplate.html', {'user_plan': objs, 'user_id': user_id})

class DetailView(generic.DetailView):
    model = plan
    template_name = 'usertemplate.html'


def uploadview(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        print request.FILES
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            ## handle uploading
            pass
    else:
        form = UploadFileForm()
    c.update({'form':form})
    return render_to_response('uploadtemplate.html', c)

def handle_uploaded_file(f):
    with open('dest.zip', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
