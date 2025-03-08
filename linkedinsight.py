import time
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from dateutil.relativedelta import relativedelta

class LinkedInsight:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_data = {}  # Dictionary to store employee headcount over time
        self.median_tenure = 0.0
        self.linkedin_token = None  # Placeholder for LinkedIn API token

    def simulate_data_collection(self, start_date, end_date):
        """Simulate collecting employee headcount data over time."""
        try:
            current_date = start_date
            headcount = 80  # Starting headcount based on the original graph
            while current_date <= end_date:
                if current_date >= datetime(2024, 9, 1):  # Start decrease from Sep 2024
                    headcount *= 0.9928  # Approximate 43% decrease over 6 months
                self.employee_data[current_date] = int(headcount)
                current_date += relativedelta(months=1)
        except Exception as e:
            print(f"Error in data collection: {e}")

    def calculate_trend(self):
        """Calculate the percentage change in headcount."""
        try:
            if not self.employee_data:
                raise ValueError("No employee data available to calculate trend.")
            start_count = list(self.employee_data.values())[0]
            end_count = list(self.employee_data.values())[-1]
            return ((end_count - start_count) / start_count) * 100
        except Exception as e:
            print(f"Error calculating trend: {e}")
            return 0

    def plot_insights(self):
        """Generate a detailed plot of employee headcount over time."""
        try:
            if not self.employee_data:
                raise ValueError("No employee data to plot.")
            dates = list(self.employee_data.keys())
            headcounts = list(self.employee_data.values())
            
            plt.figure(figsize=(12, 6))
            plt.plot(dates, headcounts, marker='o', linestyle='-', color='b', label='Headcount')
            plt.title(f"Employee Headcount Trend for {self.company_name}", fontsize=14)
            plt.xlabel("Date", fontsize=12)
            plt.ylabel("Number of Employees", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting insights: {e}")

    def set_median_tenure(self, tenure):
        """Set the median tenure."""
        try:
            if tenure < 0:
                raise ValueError("Median tenure cannot be negative.")
            self.median_tenure = tenure
        except Exception as e:
            print(f"Error setting median tenure: {e}")

    def display_insights(self):
        """Display the calculated insights."""
        try:
            trend_percentage = self.calculate_trend()
            print(f"Company: {self.company_name}")
            print(f"Total Headcount Growth: {trend_percentage:.1f}% over 6 months")
            print(f"Median Tenure: {self.median_tenure} years")
        except Exception as e:
            print(f"Error displaying insights: {e}")

    def save_data(self, filename="employee_data.json"):
        """Save employee data to a JSON file."""
        try:
            data_to_save = {
                "company_name": self.company_name,
                "employee_data": {date.strftime("%Y-%m-%d"): count for date, count in self.employee_data.items()},
                "median_tenure": self.median_tenure
            }
            with open(filename, 'w') as f:
                json.dump(data_to_save, f, indent=4)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename="employee_data.json"):
        """Load employee data from a JSON file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    data = json.load(f)
                    self.company_name = data["company_name"]
                    self.employee_data = {datetime.strptime(date, "%Y-%m-%d"): count for date, count in data["employee_data"].items()}
                    self.median_tenure = data["median_tenure"]
                print(f"Data loaded from {filename}")
            else:
                raise FileNotFoundError(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def set_linkedin_token(self, token):
        """Set the LinkedIn API access token (to be obtained via OAuth 2.0)."""
        try:
            if not token:
                raise ValueError("Token cannot be empty.")
            self.linkedin_token = token
            print("LinkedIn API token set. Ensure it has 'w_member_social' scope for sharing.")
        except Exception as e:
            print(f"Error setting LinkedIn token: {e}")

    def share_on_linkedin(self, message):
        """Simulate sharing insights on LinkedIn using the Share API."""
        try:
            if not self.linkedin_token:
                raise ValueError("LinkedIn API token not set. Please set a valid token using set_linkedin_token().")

            share_data = {
                "author": "urn:li:person:YOUR_PERSON_URN",  # Replace with actual URN
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": f"{message}\nHeadcount Trend: {self.calculate_trend():.1f}%"},
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {"com.linkedin.ugc.Visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}}
            }

            print("Simulating LinkedIn Share API request...")
            print(f"Sharing: {json.dumps(share_data, indent=2)}")
            print("Note: Replace the author URN and use a real LinkedIn API endpoint with authentication.")
            print("Endpoint example: POST https://api.linkedin.com/v2/ugcPosts")
            print("Requires OAuth 2.0 token with 'w_member_social' scope.")
        except Exception as e:
            print(f"Error sharing on LinkedIn: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize LinkedInsight
    insight = LinkedInsight("AcmeCorp")
    
    # Set start and end dates
    start_date = datetime(2023, 3, 1)
    end_date = datetime(2025, 3, 1)
    
    # Simulate data collection
    insight.simulate_data_collection(start_date, end_date)
    
    # Set median tenure
    insight.set_median_tenure(3.1)
    
    # Display insights
    insight.display_insights()
    
    # Plot insights
    insight.plot_insights()
    
    # Save data to file
    insight.save_data()
    
    # Load data from file (optional)
    # insight.load_data()
    
    # Set a mock LinkedIn token (replace with real token from LinkedIn Developer Portal)
    insight.set_linkedin_token("mock_token_12345")
    
    # Share insights on LinkedIn
    insight.share_on_linkedin("Check out the latest employee trend analysis for AcmeCorp!")
