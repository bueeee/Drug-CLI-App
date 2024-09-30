# drug_cli.py

import requests
import json
from fda_response_parser import FDAResponseParser

class DrugCLI:
    """Main CLI class to handle user interaction and API requests."""
    API_ENDPOINT = "https://api.fda.gov/drug/label.json"

    @staticmethod
    def get_drug_info(drug_name):
        """Make API request to OpenFDA to retrieve drug information."""
        try:
            response = requests.get(f"{DrugCLI.API_ENDPOINT}?search=openfda.brand_name:{drug_name}&limit=1")
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error connecting to API: {e}")
            return None

    def run(self):
        """Run the main CLI loop."""
        print("Welcome to the Drug Lookup CLI!")

        while True:
            # Get user input and show example input prompt
            drug_name = input("Please enter a drug name to look up (e.g., 'aspirin') or type 'exit' to quit: ").strip()
            
            if drug_name.lower() == "exit":
                print("Exiting the Drug Lookup CLI. Goodbye!")
                break  # Exit the loop if the user types "exit"

            print(f"\nLooking up information for '{drug_name}'...\n")

            # Fetch drug data from OpenFDA API
            response = self.get_drug_info(drug_name)

            if response:
                # Parse the response and create a Drug object
                drug = FDAResponseParser.parse_response(response)
                if drug:
                    # Display the drug information
                    drug.display_info()
                else:
                    print("No valid drug information found.")
            else:
                print("Unable to retrieve drug information at this time.")