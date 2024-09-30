# Drug Information Python CLI App

## Project Overview
This Python CLI application allows users to search for drug information using the OpenFDA API. The app provides basic details about a drug, including its name, active ingredients, and purpose, displayed in a readable format. The project is structured to promote modular design, best coding practices, and ease of use for new developers.

## Requirements
The application requires the following files and dependencies:

### Required Files
1. **`drug.py`**: Contains the `Drug` class.
2. **`fda_response_parser.py`**: Handles parsing the API response to extract drug information.
3. **`drug_cli.py`**: Main CLI logic for user interaction and API calls.
4. **`main.py`**: Entry point to start the CLI application.
5. **`requirements.txt`**: Lists third-party dependencies.

### Required Packages
- **`requests`**: For making API calls to OpenFDA.
- **`json`**: To handle JSON responses from the API.

Install these packages using the following command:

```bash
pip install -r requirements.txt
```

### Legal and Ethical Impacts
The project uses the `requests` library, which is licensed under the Apache License 2.0, and the OpenFDA API, which adheres to the terms of service set by the FDA. The application should respect rate limits and ensure that data retrieved is used responsibly and ethically.

## Installation and Setup Guide
### Step 1: Clone or Download the Repository
Navigate to the folder where you want to store the project and run the following commands:

```bash
git clone https://github.com/bueeee/Drug-CLI-App.git
cd drug_lookup_cli
```

### Step 2: Create and Activate a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to keep dependencies isolated:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Run the application from the `main.py` file:

```bash
python main.py
```

## Application Structure
The project follows a modular structure to separate concerns and improve maintainability:

```
drug_lookup_cli/
├── drug.py               # Contains the Drug class
├── fda_response_parser.py # Contains the FDAResponseParser class
├── drug_cli.py            # Main logic for the CLI
├── requirements.txt      # Dependency management
└── main.py               # Entry point for the CLI
```

### Class Details
1. **`Drug` Class** (`drug.py`):
   - Represents a drug and stores information such as the name, active ingredient, and purpose.
   - Contains a method `display_info()` to print the drug details.

2. **`FDAResponseParser` Class** (`fda_response_parser.py`):
   - Parses the JSON response from the OpenFDA API.
   - Creates and returns a `Drug` object based on the parsed data.

3. **`DrugCLI` Class** (`drug_cli.py`):
   - Manages the main user interaction and API calls.
   - Handles input validation and provides feedback in case of invalid responses.

## Error Handling
The app implements error handling for the following scenarios:
- **API Connectivity Issues**: Catches `requests.RequestException` to manage API connection errors.
- **Invalid JSON Structure**: Handles `KeyError` and `IndexError` when parsing responses.
- **User Input Validation**: Ensures user inputs are valid and sanitizes them before making requests.

## Example Usage
1. **User Input**: Enter the name of a drug (e.g., `aspirin`).
2. **API Request**: The app calls the OpenFDA API to retrieve drug information.
3. **Output**:
   ```
   Welcome to the Drug Lookup CLI!
   Please enter a drug name to look up: aspirin

   Looking up information for 'aspirin'...

   Drug Name: Aspirin
   Active Ingredient: ASPIRIN
   Purpose: Pain reliever/fever reducer
   ```

## Development and Contribution Guidelines
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use meaningful variable and function names.
- Keep functions small and focused on a single task.
- Use classes to group related functionalities.
- Test changes in a local environment before pushing to the repository.

## License
This project is licensed under the MIT License. By using the OpenFDA API, you agree to adhere to its terms of service and ethical guidelines.

