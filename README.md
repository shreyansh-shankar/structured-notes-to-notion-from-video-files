# structured-notes-to-notion-from-video-files

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

