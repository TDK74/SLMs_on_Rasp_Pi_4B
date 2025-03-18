import subprocess


commands = [
    "sudo apt-get update",
    "sudo apt-get upgrade -y",
    "dpkg -l | grep curl || sudo apt install curl -y",  # Check for curl before installation
    "systemctl is-active --quiet ollama",
    "sudo ollama run gemma2:2b"
]

def run_command(command):
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        print(result.stdout.decode())

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing command '{command}': {e.stderr.decode()}")


if __name__ == "__main__":
    for command in commands:
        # Check of status of Ollama (if installed)
        if command == "systemctl is-active --quiet ollama":
            try:
                subprocess.run("systemctl is-active --quiet ollama",
                                shell=True, check=True)
                print("Ollama already installed and running.")

            except subprocess.CalledProcessError:
                print("Ollama is not installed. Installing now...")
                run_command("curl -sSL https://ollama.ai/install.sh | sudo bash")

        else:
            run_command(command)

    # After executing the commands you can enter /set verbose manually
    print("Installation complete. Enter '/set verbose' manually if necessary.")
