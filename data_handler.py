import json
import os

DATA_FILE = "candidates_data.json"

def save_candidate_info(candidate_data):
    """
    Save candidate information to a JSON file.
    """
    if not os.path.exists(DATA_FILE):
        # If file doesn't exist, create it with an empty list
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    
    try:
        # Read existing data
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        
        # Append new candidate data
        data.append(candidate_data)
        
        # Write updated data back to the file
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Candidate information saved successfully.")
    except Exception as e:
        print(f"Error saving candidate information: {e}")

def get_all_candidates():
    """
    Retrieve all saved candidate information.
    """
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error retrieving candidates: {e}")
        return []

def delete_candidate(name):
    """
    Delete a candidate's information by name.
    """
    if not os.path.exists(DATA_FILE):
        print("No data file found.")
        return
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        
        # Filter out the candidate by name
        updated_data = [candidate for candidate in data if candidate['name'] != name]
        
        with open(DATA_FILE, 'w') as f:
            json.dump(updated_data, f, indent=4)
        
        print(f"Candidate '{name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting candidate: {e}")

