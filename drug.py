class Drug:
    """Class to represent a Drug with relevant properties."""
    def __init__(self, name, active_ingredient, purpose):
        self.name = name
        self.active_ingredient = active_ingredient
        self.purpose = purpose

    def display_info(self):
        """Display the drug information in a readable format."""
        print(f"Drug Name: {self.name}")
        print(f"Active Ingredient: {self.active_ingredient}")
        print(f"Purpose: {self.purpose}")
