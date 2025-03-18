from ollama import Client
from ollama_run_stop import *


def handle_prompt(client, selected_model, input_prompt):
    """
    Sent the user's prompt to the chosen model and processing its response.
    """
    try:
        response = client.generate(model = selected_model, prompt = input_prompt)
        print(f"{selected_model}'s response: \n{response['response']} \n")

    except RuntimeError as e:
        print(f"Runtime Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Send user request to the chosen Ollama model.
    """
    client = Client(host = 'http://localhost:11434') # Create the client
    models = get_ollama_models()
    selected_model = choose_model(models)

    if selected_model:
        run_ollama_model(selected_model) # Start of the chosen model

        while True:
            input_prompt = input("Please, enter your prompt (in the terminal) \n"
                                 "or '/bye' if you want to exit the model: \n").strip()

            if input_prompt.lower() == "/bye":
                print("Waiting for SLM's response... \n")
                handle_prompt(client, selected_model, input_prompt)
                stop_ollama(selected_model)  # Stop Ollama model after sending /bye command
                break
            else:
                # Send the user's prompt to the model
                print("Waiting for SLM's response... \n")
                handle_prompt(client, selected_model, input_prompt)


if __name__ == "__main__":
    main()

