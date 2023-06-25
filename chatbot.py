import openai

openai.api_key = "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"



def generate_bot_response(user_input) :

    dataNew = user_input + ". The following information should be given with respective headings, Give me similar startup ideas, Market Research, Financial aspect, legal and regulatory knowledge, technology and development, problems that they mught face, solutions to resolve these problems, how is this idea better than the existing ideas. Also give me a list of similar msmes that I can collaborate with in bullets"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": dataNew}])
    
    
        
    return completion.choices[0].message.content
    