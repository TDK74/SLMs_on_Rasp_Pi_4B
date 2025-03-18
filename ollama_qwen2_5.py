from ollama import Client


input_prompt = input("Please, enter your prompt (in the terminal): \n")
# for instance -> Hi, can you tell me more about you?

print("Waiting for SLM's response... \n")

# If Ollama is on the local host.
client = Client(host = 'http://localhost:11434')
response = client.generate(model = 'qwen2.5:0.5b', prompt = input_prompt)

print(f"Qwen's message: \n{response['response']} \n")

