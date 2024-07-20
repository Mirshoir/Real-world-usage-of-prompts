import pandas as pd

# Assuming the datasets are loaded from CSV files
pharmacies_df = pd.read_csv("C:/Users/dtfygu876/Downloads/pharmacies_uzbekistan.csv")
drugs_df = pd.read_csv("C:/Users/dtfygu876/Downloads/drugs_uzbekistan.csv")

# Define the PharmacyChatbot class
class PharmacyChatbot:
    def __init__(self, pharmacies_df, drugs_df):
        self.pharmacies_df = pharmacies_df
        self.drugs_df = drugs_df

    def get_drug_info(self, drug_name, pharmacy_name=None):
        drug_info = self.drugs_df[self.drugs_df["Drug Name"].str.lower() == drug_name.lower()]
        if not drug_info.empty:
            drug = drug_info.iloc[0]
            pharmacy_info = self.pharmacies_df[self.pharmacies_df["Pharmacy Name"].str.lower() == pharmacy_name.lower()]
            if not pharmacy_info.empty:
                return pd.merge(drug_info, pharmacy_info, how='cross')
            else:
                return "It is not available"
        else:
            return "It is not available"

    def calculate_total_price(self, drug_names):
        total_price = 0
        for name in drug_names:
            drug_info = self.drugs_df[self.drugs_df["Drug Name"].str.lower() == name.lower()]
            if not drug_info.empty:
                total_price += drug_info.iloc[0]["Price"]
            else:
                return "It is not available"
        return f"Total price for the requested drugs is {total_price} UZS."

    def handle_request(self, request):
        words = request.lower().split()
        if "price" in words:
            drug_names = [word for word in words if word in self.drugs_df["Drug Name"].str.lower().tolist()]
            return self.calculate_total_price(drug_names)
        elif "instruction" in words:
            drug_name = next((word for word in words if word in self.drugs_df["Drug Name"].str.lower().tolist()), None)
            pharmacy_name = next((word for word in words if word in self.pharmacies_df["Pharmacy Name"].str.lower().tolist()), None)
            if drug_name and pharmacy_name:
                drug_info = self.get_drug_info(drug_name, pharmacy_name)
                if isinstance(drug_info, pd.DataFrame):
                    return drug_info
                else:
                    return drug_info
            else:
                return "Please specify both the drug and pharmacy name."
        else:
            return "Sorry, I didn't understand your request. Please ask for drug instructions or prices."

# Example usage
chatbot = PharmacyChatbot(pharmacies_df, drugs_df)
response = chatbot.handle_request("What is the price and instruction for Paracetamol at A Pharmacy ?")
print(response)
