# BDD Step Analyzer

**BDD Step Analyzer** is a Python tool designed to analyze BDD (Behavior-Driven Development) feature files, detect similar steps across scenarios, and identify potential redundancies. It leverages NLP and semantic similarity techniques to help streamline test steps, making tests more maintainable and easier to refactor.

## Features

- **Semantic Step Similarity Detection**: Uses a machine learning model to detect similarities in step wording and meaning, rather than just text-based matching.
- **Context-Aware Analysis**: Differentiates steps by their context (`Given`, `When`, `Then`) and uses thresholds to ensure meaningful results.
- **Report Generation**: Automatically generates a report with details on similar steps, including step type, similarity score, and file references.
- **Auto-Numbered Reports**: Automatically numbers report files if a report already exists, ensuring no overwriting.

## Project Structure

```bash
bdd-analyzer/
├── bdd_step_analyzer/
│   ├── __init__.py                 # Marks directory as a package
│   ├── step_analyzer.py            # Main analysis functions
├── data/                            # Folder to store .feature files for analysis
├── reports/                         # Folder where generated reports will be saved
├── requirements.txt                 # Dependencies for the project
├── README.md                        # Project documentation
└── main.py                          # Script to run the analysis
```

## Getting Started

### Prerequisites

- **Python 3.7+**: Ensure Python is installed and available in your PATH.
- **Dependencies**: Listed in `requirements.txt`, including `sentence-transformers` for NLP processing.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bdd-analyzer.git
   cd bdd-analyzer

## Usage

   1. Prepare Your Feature Files:
        - Place .feature files in the data/ directory. Each file should follow the BDD syntax with Given, When, Then, And, and But steps
   2. Run the Analysis:
   ```bash
   python main.py
   ```

   3. Check the Report:
   - After running, a report will be generated in the reports/ directory (e.g., reports/similar_steps_report.txt). If a report already exists, the tool will save the new report with an incremented filename (e.g., similar_steps_report_1.txt, similar_steps_report_2.txt).

## Example Output in the Report

The report will show similar steps with their type, similarity score, and file references. Example:

```bash
Similar Steps Found:

Step 1: the user is on the login page (Type: Given, File: data/login.feature)
Step 2: the user navigates to the login page (Type: Given, File: data/registration.feature)
Similarity Score: 92.5
Note: Based on semantic similarity and domain-specific adjustments.
```

## Customization

### Adjusting Similarity Thresholds

You can adjust similarity thresholds in step_analyzer.py:

    - Context-Specific Thresholds: The tool uses different thresholds for each step type (Given, When, Then). Modify these in the get_threshold_for_step_type function.

### Adding or Ignoring Keywords

    - Domain-Specific Keywords: You can update DOMAIN_KEYWORDS in step_analyzer.py to add keywords specific to your domain that affect similarity scoring.
    - Common Phrases Exclusion: Add frequently used phrases to COMMON_PHRASES to ignore them during comparisons.


