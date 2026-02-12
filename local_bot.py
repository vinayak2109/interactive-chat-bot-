from openai import OpenAI

# Point to LM Studio Local Server
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

print("---------------------------------------")
print(" LOCAL AI BOT IS ONLINE (No Streaming)")
print("---------------------------------------")

history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    history.append({"role": "user", "content": user_input})

    try:
        # turn stream=False to fix the empty response bug
        completion = client.chat.completions.create(
            model="local-model",
            messages=history,
            temperature=0.7,
            stream=False
        )

        # Get the full answer at once
        response_text = completion.choices[0].message.content

        print(f"Bot: {response_text}\n")

        # Remember the answer
        history.append({"role": "assistant", "content": response_text})

    except Exception as e:
        print(f"Error: {e}")
        print("Check: Is LM Studio running? Is a model loaded?")