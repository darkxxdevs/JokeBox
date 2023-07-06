# JOKEBOX

## Description
This project is a Python script that fetches a random joke from an API and converts it into speech using the gTTS library. The joke's setup and punchline are saved as separate audio files and played using the default system player.

## Installation
To clone the repository to your local machine, follow the steps below:

1. Open your terminal or command prompt.
2. Change to the directory where you want to clone the project.
   ```
   cd /path/to/destination/directory
   ```
3. Copy the repository's URL. You can find it on the project's GitHub page.
4. Run the `git clone` command followed by the repository URL:
   ```
   git clone https://github.com/thedistroyer17/JokeBox.git
   `
5. Press Enter to execute the command.
6. Git will now download the project files and create a new directory with the project name in the destination directory.
7. Once the cloning process is complete, you can navigate into the project directory to access the files:
   ```
   cd JokeBox
   ```
   Replace `project-directory` with the actual name of the directory created during cloning.
8. Now you can proceed with the installation and usage instructions provided in the project's README.md file.
2. Install the required dependencies by running the following command:
   ```
   pip install gtts requests
   ```

## Usage
1. Open the terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   ```
   python script.py
   ```
4. The script will fetch a random joke from the API and convert it into speech.
5. Two audio files will be generated: `out.mp3` containing the joke's setup and `out2.mp3` containing the punchline.
6. The audio files will be played using the default system player.

## Configuration
You can modify the `api_url` variable in the `__main__` block of the script to change the API endpoint from which jokes are fetched.

## License
This project is licensed under the [MIT License](LICENSE).