# **Mail Merge Invitation Script**

## **Overview**
This is the Day 24 project from the 100 Days of Code: The Complete Python Pro Bootcamp. This Python script automates the creation of personalized invitation letters. By merging a list of names with a template letter, the script generates individual letters for each invitee, saving them as separate text files. This is particularly useful for sending custom invitations, announcements, or formal communications.

## **How It Works**
- **Input Files**: The script requires two input files:
  1. `invited_names.txt`: A text file containing the names of the invitees, each name on a new line.
  2. `starting_letter.txt`: A template letter with a placeholder (`[name]`) where each invitee's name will be inserted.

- **Processing**:
  - The script reads the names from the `invited_names.txt` file.
  - It loads the content of the `starting_letter.txt` template.
  - For each name in the list, the script replaces the `[name]` placeholder in the template with the actual invitee's name.
  - Each personalized letter is saved as a new text file in the `Output/ReadyToSend` directory, with filenames formatted as `letter_for_<name>.txt`.


## **Customization**

This script is highly adaptable to different use cases, not just for invitations. You can customize it by modifying the input files and the placeholder in the template letter. Here are some examples of different scenarios where it can be used:

### 1. **Job Offer Letters**
- **Placeholder**: Replace `[name]` with the candidate's name, and add other placeholders for job title, salary, etc.
- **Template**:
   ```
   Dear [name],

   We are excited to offer you the position of [position] with a starting salary of [salary].

   Best regards,
   HR Team
   ```
- **Customization**: Modify the script to handle multiple placeholders like `[position]` and `[salary]`.

### 2. **Certificate Generation**
- **Placeholder**: Replace `[name]` with the recipient’s name.
- **Template**:
   ```
   This certificate is awarded to [name] for outstanding performance in [subject].

   Signed,
   [Instructor]
   ```
- **Customization**: You can adjust the script to handle multiple placeholders like `[subject]` and `[Instructor]`, allowing the script to generate certificates automatically.

### 3. **Personalized Thank You Notes**
- **Placeholder**: Replace `[name]` with the person’s name.
- **Template**:
   ```
   Dear [name],

   Thank you for your generous contribution to our fundraiser.

   Sincerely,
   The Event Team
   ```

### How to Add Multiple Placeholders:
1. In your `starting_letter.txt`, add additional placeholders (e.g., `[position]`, `[date]`, `[event]`).
2. Update the script to handle multiple replacements. Example:
   ```python
   new_letter = old_letter.replace("[name]", name).replace("[position]", position).replace("[date]", event_date)
   ```
3. The placeholders can be replaced with values from an additional file or hardcoded into the script.


## **Requirements**
- **Python Version**: Python 3.x
- **Modules**: No external modules are required; the script uses Python's built-in `open()` and `read()` methods for file handling.
