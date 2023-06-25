from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label='User Input', max_length=100)