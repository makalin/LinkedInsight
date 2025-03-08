# LinkedInsight

![LinkedInsight Logo](logo.png)

**LinkedInsight** is a Python-based tool designed to analyze LinkedIn company profiles and detect trends such as employee headcount changes and median tenure over time. Inspired by the idea of uncovering hidden insights from LinkedIn data (even without official company announcements), LinkedInsight provides actionable metrics, visualizations, and sharing capabilities.

## Features

- **Employee Trend Analysis**: Calculate headcount growth/decline percentages over a specified period.
- **Data Visualization**: Generate detailed graphs of employee headcount trends using Matplotlib.
- **Data Persistence**: Save and load employee data to/from JSON files for persistence across sessions.
- **LinkedIn Sharing**: Share insights directly on LinkedIn (requires LinkedIn API integration).
- **Simulated Data Collection**: Simulate employee headcount changes for testing purposes (replace with real LinkedIn API data in production).

## Installation

### Prerequisites
- Python 3.6 or higher
- Required Python libraries:
  - `matplotlib` (for graphing)
  - `python-dateutil` (for date handling)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/makalin/linkedinsight.git
   cd linkedinsight
   ```
2. Install the required dependencies:
   ```bash
   pip install matplotlib python-dateutil
   ```
3. (Optional) For LinkedIn API integration, install the `requests` library:
   ```bash
   pip install requests
   ```

## Usage

### Basic Example
The following example demonstrates how to use LinkedInsight to simulate employee data, analyze trends, visualize results, and share insights.

```python
from linkedinsight import LinkedInsight
from datetime import datetime

# Initialize LinkedInsight for a company
insight = LinkedInsight("AcmeCorp")

# Set start and end dates for analysis
start_date = datetime(2023, 3, 1)
end_date = datetime(2025, 3, 1)

# Simulate data collection (replace with real LinkedIn API data in production)
insight.simulate_data_collection(start_date, end_date)

# Set median tenure
insight.set_median_tenure(3.1)

# Display insights
insight.display_insights()

# Plot headcount trends
insight.plot_insights()

# Save data to a JSON file
insight.save_data()

# Set LinkedIn API token (replace with real token)
insight.set_linkedin_token("your_linkedin_access_token")

# Share insights on LinkedIn
insight.share_on_linkedin("Check out the latest employee trend analysis for AcmeCorp!")
```

### Sample Output
- **Console Output**:
  ```
  Company: AcmeCorp
  Total Headcount Growth: -43.0% over 6 months
  Median Tenure: 3.1 years
  Data saved to employee_data.json
  LinkedIn API token set. Ensure it has 'w_member_social' scope for sharing.
  Simulating LinkedIn Share API request...
  Sharing: {
    "author": "urn:li:person:YOUR_PERSON_URN",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
      "com.linkedin.ugc.ShareContent": {
        "shareCommentary": {
          "text": "Check out the latest employee trend analysis for AcmeCorp!\nHeadcount Trend: -43.0%"
        },
        "shareMediaCategory": "NONE"
      }
    },
    "visibility": {
      "com.linkedin.ugc.Visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
      }
    }
  }
  ```

- **Graph Output**: A Matplotlib window will display a graph showing the employee headcount trend over time.

## LinkedIn API Integration

LinkedInsight includes support for sharing insights on LinkedIn via the LinkedIn Share API. To enable this:

1. **Register an App**:
   - Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/).
   - Create an app and request the `w_member_social` scope for sharing posts.

2. **Obtain an Access Token**:
   - Use OAuth 2.0 to obtain an access token. Follow LinkedIn's [authentication guide](https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow).
   - Replace `"your_linkedin_access_token"` with the obtained token in the `set_linkedin_token` method.

3. **Update the Share Method**:
   - Replace the simulated `share_on_linkedin` method with a real API call using the `requests` library. Example:
     ```python
     import requests
     headers = {"Authorization": f"Bearer {self.linkedin_token}", "Content-Type": "application/json"}
     response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=share_data)
     print(response.json())
     ```
   - Update the `author` field in `share_data` with your LinkedIn Person URN.

**Note**: Ensure compliance with LinkedIn's API terms of service and rate limits.

## Project Structure

```
linkedinsight/
│
├── linkedinsight.py    # Main script with the LinkedInsight class
├── employee_data.json  # Saved employee data (generated after running save_data)
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows PEP 8 style guidelines and includes appropriate error handling.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by a post by Ugur Umutluoglu on X, highlighting the potential of LinkedIn data for trend analysis.
- Built with Python, Matplotlib, and the LinkedIn API.

## Contact

For questions or suggestions, please open an issue on GitHub or reach out to [makalin@gmail.com](mailto:makalin@gmail.com).
