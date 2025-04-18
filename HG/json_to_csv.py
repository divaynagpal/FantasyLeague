import os
import json
import glob

def load_json_files(folder_path):
    """
    Load all JSON files from a folder into a dictionary.
    
    Args:
        folder_path (str): Path to the folder containing JSON files.
        
    Returns:
        dict: Dictionary where keys are filenames and values are the loaded JSON data.
    """
    # Dictionary to store the loaded JSON data
    json_data_dict = {}
    
    # Make sure to handle spaces in folder names
    folder_path = os.path.normpath(folder_path)
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        return json_data_dict
    
    # Print all files in the directory to help with debugging
    print(f"Contents of '{folder_path}':")
    for item in os.listdir(folder_path):
        print(f"  - {item}")
    
    # Find all JSON files in the folder
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    
    if not json_files:
        print(f"No JSON files found in '{folder_path}'")
        return json_data_dict
    
    print(f"Found {len(json_files)} JSON files")
    
    # Load each JSON file
    for json_file in json_files:
        filename = os.path.basename(json_file)
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                json_data_dict[filename] = data
                print(f"Successfully loaded: {filename}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    
    print(f"Successfully loaded {len(json_data_dict)} out of {len(json_files)} JSON files")
    return json_data_dict

# Example usage
if __name__ == "__main__":
    # Replace with your folder path
    folder_path = "ipl_json abridged"
    
    # Load all JSON files
    json_data = load_json_files(folder_path)
    
    # Print some basic info about each loaded file
    for filename, data in json_data.items():
        data_type = type(data).__name__
        if isinstance(data, dict):
            print(f"{filename}: Dictionary with {len(data)} keys: {list(data.keys())}")
        elif isinstance(data, list):
            print(f"{filename}: List with {len(data)} items")
        else:
            print(f"{filename}: {data_type}")