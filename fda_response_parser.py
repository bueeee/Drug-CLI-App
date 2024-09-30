from drug import Drug

class FDAResponseParser:
    """Class to parse OpenFDA API responses and create Drug objects."""
    @staticmethod
    def parse_response(response_json):
        """Parse the JSON response and create a Drug object."""
        try:
            drug_data = response_json['results'][0]
            name = drug_data['openfda']['brand_name'][0] if 'brand_name' in drug_data['openfda'] else "Unknown"
            active_ingredient = drug_data['active_ingredient'][0] if 'active_ingredient' in drug_data else "Unknown"
            purpose = drug_data['purpose'][0] if 'purpose' in drug_data else "N/A"

            return Drug(name, active_ingredient, purpose)
        except (KeyError, IndexError) as e:
            print(f"Error parsing response: {e}")
            return None
