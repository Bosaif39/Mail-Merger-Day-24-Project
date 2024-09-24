# **Mail Merge Invitation Script**

## **Overview**
This Python script automates the creation of personalized invitation letters. By merging a list of names with a template letter, the script generates individual letters for each invitee, saving them as separate text files. This is particularly useful for sending custom invitations, announcements, or formal communications.

## **How It Works**
- **Input Files**: The script requires two input files:
  1. `invited_names.txt`: A text file containing the names of the invitees, each name on a new line.
  2. `starting_letter.txt`: A template letter with a placeholder (`[name]`) where each invitee's name will be inserted.

- **Processing**:
  - The script reads the names from the `invited_names.txt` file.
  - It loads the content of the `starting_letter.txt` template.
  - For each name in the list, the script replaces the `[name]` placeholder in the template with the actual invitee's name.
  - Each personalized letter is saved as a new text file in the `Output/ReadyToSend` directory, with filenames formatted as `letter_for_<name>.txt`.


## **Requirements**
- **Python Version**: Python 3.x
- **Modules**: No external modules are required; the script uses Python's built-in `open()` and `read()` methods for file handling.
