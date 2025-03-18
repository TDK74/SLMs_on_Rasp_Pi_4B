import subprocess
#import os


def get_ollama_models():
    """
    Retrieves a list of available Olama models.

    Returns:
        list: A list of model names, or an empty list on error.
    """
    try:
        result = subprocess.run(['ollama', 'list'], capture_output = True,
                                text = True, check = True)
        # Skip header line
        models = [line.split()[0] for line in result.stdout.splitlines()[1 : ]]

        return models

    except subprocess.CalledProcessError as e:
        print(f"Error getting Ollama models: {e}")

        return []


def choose_model(models):
    """
    Allows the user to choose a model from the list.

    Args:
        models (list): A list of available models.

    Returns:
        str: The selected model, or None if no models are available
        or an error occurred.
    """
    if not models:
        print("No Ollama models found.")

        return None

    print("Available models:")

    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")

    while True:
        try:
            choice = int(input("Enter the number of the model you want to run: "))

            if 1 <= choice <= len(models):
                return models[choice - 1]

            else:
                print("Invalid choice. Please enter a valid number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def run_ollama_model(model):
    """
    Runs an Ollama model.

    Args:
        model (str): The name of the model to run.
    """
    try:
        subprocess.Popen(['ollama', 'run', model],
                         stdin = subprocess.PIPE,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE,
                         text = True)

    except subprocess.CalledProcessError as e:
        print(f"Error running Ollama model: {e}")


def stop_ollama(model):
    """
    Stops the specified Ollama model.

    Args:
        model (str): The name of the model to stop.

    Outputs:
        - A success message if the model was stopped successfully.
        - An error message if the stop process fails.
    """
    try:
        result = subprocess.run(["ollama", "stop", model],
                                capture_output = True, text = True)

        if result.returncode == 0:
            print(f"Ollama model '{model}' has been successfully stopped.")
        else:
            print(f"Failed to stop Ollama model '{model}': {result.stderr}")

    except Exception as e:
        print(f"An error occurred while stopping Ollama model '{model}': {e}")


if __name__ == "__main__":
    models = get_ollama_models()
    selected_model = choose_model(models)

    if selected_model:
        run_ollama_model(selected_model)

