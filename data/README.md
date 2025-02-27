### Data Directory
This folder is meant to store the dataset for the **NLP Disaster Tweets** classification project.

---

### How to Get the Dataset
Since the dataset is too large for direct inclusion in this repository, you will need to download it manually.

#### **Option 1: Download from Kaggle (Manual)**
1. Visit the [Kaggle NLP Disaster Tweets Competition](https://www.kaggle.com/competitions/nlp-getting-started).
2. Download the following files:
   - \`train.csv\`
   - \`test.csv\`
   - \`sample_submission.csv\`
3. Place these files in the **\`data/\`** directory.

#### **Option 2: Use the Kaggle API (Recommended)**
1. Ensure you have the Kaggle API installed and authenticated:
   \`\`\`bash
   pip install kaggle
   kaggle competitions download -c nlp-getting-started
   \`\`\`
2. Alternatively, run the provided script:
   \`\`\`bash
   python scripts/data_download.py
   \`\`\`
   This will automatically download and extract the dataset into the **\`data/\`** directory.

---

### Expected Directory Structure
After downloading, the folder should be structured as follows:
\`\`\`
data/
├── train.csv             # Training data with labels
├── test.csv              # Test data for predictions
├── sample_submission.csv # Sample submission file for Kaggle
\`\`\`

---

### Note
- This folder is included in **\`.gitignore\`**, meaning dataset files will **not** be uploaded to GitHub.
- Make sure you have downloaded the dataset before running any scripts.

---

### Next Steps
Once the dataset is downloaded, you're ready to run the preprocessing and training scripts.
