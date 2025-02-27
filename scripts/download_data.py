import os
import zipfile
import subprocess

# Define paths
DATA_DIR = "data"
ZIP_FILE = "nlp-getting-started.zip"
COMPETITION_NAME = "nlp-getting-started"

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def download_data():
    """Downloads the dataset from Kaggle competition."""
    print("Checking Kaggle API installation...")
    
    # Verify if kaggle CLI is installed
    try:
        subprocess.run(["kaggle", "--version"], check=True)
    except FileNotFoundError:
        print("Error: Kaggle CLI is not installed. Install it via 'pip install kaggle'.")
        return

    # Download dataset
    print(f"Downloading dataset: {COMPETITION_NAME}...")
    subprocess.run(["kaggle", "competitions", "download", "-c", COMPETITION_NAME, "-p", DATA_DIR], check=True)
    
    # Extract files
    zip_path = os.path.join(DATA_DIR, ZIP_FILE)
    if os.path.exists(zip_path):
        print("Extracting dataset...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(DATA_DIR)
        os.remove(zip_path)  # Remove zip after extraction
    else:
        print("Download failed or zip file missing.")

    print(f"Dataset downloaded and extracted to '{DATA_DIR}/'")

if __name__ == "__main__":
    download_data()
