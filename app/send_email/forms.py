from django import forms

class SecretForm(forms.Form):
    description = forms.CharField(label='Subject with desctiption', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    subscribe_for_news = forms.BooleanField(label='Would you like to subscribe for weekly news?', required=False)

