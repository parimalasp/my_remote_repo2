from django.shortcuts import render
from testapp.forms import FeedbackForm

def feedback_view(request):
    submitted=False
    name=''
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('form validation is completed')
            print('*'*20)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']
    form=FeedbackForm()
    my_dict={'form':form,'submitted':submitted,'name':name}
    return render(request,'testapp/feedback.html',my_dict)


# Create your views here.
