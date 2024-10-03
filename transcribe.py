import whisper
import warnings
import subprocess
import os

def run_ollama_model(prompt, output_file):
    # Prepare the command to run the model
    command = ['ollama', 'run', 'llama3.2:3b']

    # Start the subprocess
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    try:
        # Send the prompt to the process and get the output
        output, error = process.communicate(input=prompt, timeout=300)

        # Write output to the specified file
        with open(output_file, 'w', encoding='utf-8') as file:
            if output:
                file.write(output)
            if error:
                file.write("Error:\n")
                file.write(error)
    except subprocess.TimeoutExpired:
        process.kill()
        print("The process timed out.")
    except UnicodeDecodeError:
        pass  # Suppress UnicodeDecodeError silently

def extract_structured_notes(transcription, output_file):
    # Prepare a prompt for generating structured notes
    prompt = f"Please summarize the following transcription into structured notes, also before the title write TITLE= , before any subheadings write SUBHEAD= \n\n{transcription}"

    # Run the model to get structured notes
    run_ollama_model(prompt, output_file)

# Suppress FutureWarnings and UserWarnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

model = whisper.load_model("base")

# Create the Outputs directory if it doesn't exist
output_dir = "Outputs"
os.makedirs(output_dir, exist_ok=True)

# Path to the BCV directory containing video files
video_dir = "BCV"

# Iterate through all video files in the BCV directory
for filename in os.listdir(video_dir):
    if filename.endswith(('.mp4', '.mkv', '.avi', '.mov')):  # Add other video formats if needed
        video_path = os.path.join(video_dir, filename)

        # Transcribe the video
        result = model.transcribe(video_path)

        # Create the output file path
        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_output.txt")

        # Extract structured notes
        extract_structured_notes(result['text'], output_file)

        print(f"Executed successfully for {filename}")

# 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