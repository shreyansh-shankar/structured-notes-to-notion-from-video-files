# **AI-Powered Transcription and Structured Note Automation Project**

This project automates the process of transcribing video content, extracting structured notes, and uploading them directly into Notion. The system uses **OpenAI's Whisper** for transcription, **Ollama’s LLaMA model** for structured note formatting, and **Notion API** for seamless integration into a Notion database.

---

## **Features**
- **Automated Transcription**: Processes video files from a folder and transcribes them into text using Whisper.
- **Structured Notes Extraction**: Uses AI to format transcriptions into structured notes with clear titles, subheadings, and paragraphs.
- **Notion Integration**: Automatically uploads structured notes into a specific Notion page or database, making the content easily accessible and organized.

---

## **Table of Contents**
- [Getting Started](#getting-started)
- [Project Setup](#project-setup)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

---

## **Getting Started**

Follow the instructions below to set up and run the project on your machine.

### **Prerequisites**

- **Python 3.7+**
- **Notion API key**
- **Ollama (LLaMA)** installed locally.
- **Google Cloud API credentials** (if you're using it for additional integrations)
- **FFmpeg** for handling audio processing.

### **Required Libraries**

Install the required libraries by running:

```bash
pip install whisper notion-client requests google-api-python-client
```

## **Project Setup**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/shreyansh-shankar/structured-notes-to-notion-from-video-files.git
cd ai-transcription-notion
```
### **Step 2: Set Up Your Notion API**

1. **Get your Notion API key**:
   - Go to [Notion Developers](https://www.notion.so/my-integrations).
   - Click **Create New Integration**.
   - Choose your workspace and generate the **API Key**.
   - Save the API key as `NOTION_API_KEY` for use in the Python script.

2. **Set up a Notion database** with the following properties:
   - **Objective**: A **Text** property for storing the titles of the transcriptions.
   - **Context**: A **Select** property for filtering, with values such as `"DM-BITS"`. You can customize these according to your needs.

3. **Find your Database ID**:
   - Open your database in Notion.
   - The URL will look something like this: `https://www.notion.so/workspace-name/7d9c18fd12ef4e30b56a41dbab4796cb`.
   - Copy the long string after the workspace name (in this case, `7d9c18fd12ef4e30b56a41dbab4796cb`) — this is your `DATABASE_ID`.

4. **Replace the following placeholders in the Python script** with your Notion API credentials:
   - Replace `NOTION_API_KEY` with your actual API key.
   - Replace `DATABASE_ID` with the ID of your Notion database.

Example of how to update the Python script:

```python
# Replace these with your actual values
NOTION_API_KEY = 'your-secret-api-key'
DATABASE_ID = 'your-database-id'
```

### **Step 3: Configure the Project**

1. **Organize Your Files**:
   - Create and Place your video files inside a folder named `BCV` (you can rename this folder, just make sure to update the script if you do).
   - Ensure you have an `Outputs` folder in your project directory where the transcription and structured notes will be saved.

   Your folder structure should look like this:

   ```bash
   📁 structured-notes-to-notion-from-video-files
   ├── 📁 BCV                # Folder where you place the video files
   ├── 📁 Outputs            # Folder where transcription and notes will be stored
   ├── notion.py              # Python script to update the notion database
   ├── transcribe.py         # Python script to transcribe the video files
   └── README.md             # Documentation
   ```
### **Step 4: Install Ollama and Whisper**

1. **Install Ollama** to run the LLaMA model locally on your machine:

   - For **macOS** users, install Ollama using Homebrew:

   ```bash
   brew install ollama

For other operating systems, refer to Ollama’s installation guide. Installation instructions for Linux or Windows can be found in their official documentation.

2. **Install FFmpeg for audio processing** (if not already installed):

   FFmpeg is essential for handling audio extraction from video files.

   - On **macOS**, install FFmpeg via Homebrew:

   ```bash
   brew install ffmpeg

On Windows, you can download the FFmpeg binaries from FFmpeg's official site and follow the installation instructions provided on the site. Make sure to add FFmpeg to your system's PATH to use it from the command line.

Feel free to submit issues or pull requests if you have suggestions for improving this project. Contributions are always welcome!
