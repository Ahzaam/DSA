
import openai

openai.api_key = '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'

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = ''
while True :
    prompt += '\nHuman:' + input('Human: ')

    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    
    prompt += response.choices[0].text
    print(response.choices[0].text)