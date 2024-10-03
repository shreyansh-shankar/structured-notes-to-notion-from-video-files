from googleapiclient.discovery import build
from notion_client import Client
import requests
import re
import os

NOTION_API_KEY = 'secret_D7RVCBs8uM5mH7WNHSwITv2ivE85cusCZhFHAEE7WbC'
DATABASE_ID = '7d9c18fd12ef4e30b56a41dbab4796cb'

# authorising notion client
notion = Client(auth = NOTION_API_KEY)

headers = {
    "Authorization": "Bearer " + NOTION_API_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def fetch_specific_page(database_id, title_to_find, context_value):
    try:
        # Define the filter for the context
        filter_query = {
            "and": [
                {
                    "property": "Objective",  # Ensure this matches your actual title property name
                    "title": {
                        "equals": title_to_find  # Filtering for the specific title
                    }
                },
                {
                    "property": "Context",  # Change to your actual context property name
                    "select": {
                        "equals": context_value  # Filtering for 'DM-BITS'
                    }
                }
            ]
        }

        # Query the database with the filter
        query_response = notion.databases.query(
            database_id=database_id,
            filter=filter_query  # Apply the filter here
        )

        # Check if any pages were returned
        if not query_response['results']:
            print(f"No pages found for title '{title_to_find}' with context '{context_value}'.")
            return None

        # Print the found page details
        for page in query_response['results']:
            print(f"Found page with title '{title_to_find}':")
            return page['id']

        print(f"Page with title '{title_to_find}' not found.")
        return None  # Return None if the page is not found
    except Exception as e:
        print(f"Error fetching page: {e}")

# Call the function to fetch the specific page
page_name_to_find = "Week 8: Writng Methods Section of an Academic Report"  # Replace with your specific title
context_to_filter = "WP-BITS"  # The context to filter
page_id = fetch_specific_page(DATABASE_ID, page_name_to_find, context_to_filter)

def add_content_to_page(file_path, pageID):
    # Load the content from the text file
    with open(file_path, 'r') as file:
        content = file.read()

    # Prepare blocks to be added to the Notion page
    blocks = []

    # Split the content into lines and process it
    lines = content.splitlines()
    for line in lines:
        if line.startswith("TITLE="):
            # Add title as heading 1
            title = line.replace("TITLE=", "").strip()
            blocks.append({
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            })
        elif line.startswith("SUBHEAD="):
            # Add subhead as heading 3
            subhead = line.replace("SUBHEAD=", "").strip()
            blocks.append({
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": subhead
                            }
                        }
                    ]
                }
            })
        elif line.strip():  # If the line is not empty
            if line.startswith("*"):
                # Remove leading '*' if present and strip whitespace
                line = line[1:].strip()
            
            # Process the line to handle bold text
            rich_text = []
            parts = re.split(r'(\*\*.*?\*\*)', line)  # Split on bold markers

            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    # It's a bold text, strip the '**' and make it bold
                    bold_text = part[2:-2].strip()
                    rich_text.append({
                        "type": "text",
                        "text": {
                            "content": bold_text
                        },
                        "annotations": {
                            "bold": True  # Set the text to bold
                        }
                    })
                else:
                    # Normal text
                    normal_text = part.strip()
                    if normal_text:  # Avoid adding empty strings
                        rich_text.append({
                            "type": "text",
                            "text": {
                                "content": normal_text
                            }
                        })

            # Add paragraph text
            blocks.append({
                "type": "paragraph",
                "paragraph": {
                    "rich_text": rich_text
                }
            })

    # Now add the blocks to the Notion page
    try:
        notion.blocks.children.append(
            block_id = pageID,
            children = blocks
        )
        print(f"Content added successfully to {pageID}")
    except Exception as e:
        print(f"Error adding content: {e}")

# Iterate through all text files in the Outputs directory and add their content to the Notion page
outputs_dir = "Outputs"

# Check if the Outputs directory exists
if os.path.exists(outputs_dir):
    for filename in os.listdir(outputs_dir):
        if filename.endswith('.txt'):  # Process only .txt files
            file_path = os.path.join(outputs_dir, filename)
            add_content_to_page(file_path, page_id)
else:
    print(f"The directory '{outputs_dir}' does not exist.")