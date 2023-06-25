# chatbot/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ChatForm
from .models import ChatMessage
from .chatbot import generate_bot_response

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            bot_response = generate_bot_response(user_input)
            chat_message = ChatMessage(user_input=user_input, response=bot_response)
            chat_message.save()
    else:
        form = ChatForm()
    
    chat_messages = ChatMessage.objects.all()
    
    return render(request, 'chatbot/chat.html', {'form': form, 'chat_messages': chat_messages})
