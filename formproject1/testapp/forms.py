from django import forms
class FeedbackForm(forms.Form):
    rno=forms.IntegerField()
    name=forms.CharField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
