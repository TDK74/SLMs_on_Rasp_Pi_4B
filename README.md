# SLMs on Raspberry Pi 4B
Run Small Language Models (Gemma2 2b, phi 3.5 3.8b, Qwen2.5 0.5b) on Raspberry Pi 4B.

* Based on the guide from this site:

<https://www.dfrobot.com/blog-14068.html>

There were no Python script examples, but I created several, so that I could download and run different SLMs with scripts rather than manually from the command line in the terminal.

## 

# Setup Environment
* Raspberry Pi 4B (2 GB RAM + 2 GB swap)
* Operating System: Raspbian GNU/Linux 11 (bullseye)
* Distribution: raspberrypi 6.1.21-v8+
* OS type: 64-bit
* Software: Python 3.9.2 (same in the workspace)
* Environment: slmpy39 (virtual env)
* SLModels: only qwen2.5-0.5b-q4 (small enough). Unfortunately, I was not able to download, run and utilize gemma2-2b-q4, mistral-7B-q4, phi3.5-3.8b-q4. :(

See **_commands.txt_** and **_pip_freeze.txt_** for more details if interested.

## Notes
The Python file **install model_name** for automated update and upgrade of the system as well as for installing Ollama seems to me rather slower than pasting and running the corresponding commands manually. I'd recommend especially this one **sudo ollama run 'model_name'** to be run manually so that you can see and track the progress of downloading, instaliing and running the chosen model.

There are Pyton script files with different levels of complexity as I improved and developed my code.

Basic examples branch - first step should be to run **ollama_run_stop.py** and then the selected model file.

Improved examples branch - added a function and "try... except" in it, but it is also valid to run **ollama_run_stop.py** first and then the selected model fte file.

The master branch has the final version.

The branches are left unmerged into the master, so that the files of these different levels can be easily distinguished.
