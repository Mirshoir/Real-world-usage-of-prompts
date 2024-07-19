from langchain_community.llms import Ollama

llms = Ollama(model="phi")


def generate_response(llms, role_inputs):
    prompt = "Teach me 는 and 은 grammar"
    for role, text in role_inputs:
        prompt += f"{role}: {text}\n"

    response = llms.invoke(prompt)

    return response


role_inputs = [
    ("system", "You are a korean language teacher. ,"
               "if students ask for some help first you explain it in English secondly in Uzbek"
               "And compare them to each other"),
]


response = generate_response(llms, role_inputs)

# Print the conversation with roles
for role, text in role_inputs:
    print(f"{role.capitalize()}: {text.strip()}")
print(f"Assistant: {response.strip()}")
