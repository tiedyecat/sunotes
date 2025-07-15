# Facebook Ads Reporting Script

This script generates a summary report for Facebook Ads accounts and sends it to a Google Chat webhook.

## Setup

1. **Python Installation**: Python 3.11+ is already installed on your system
2. **Dependencies**: The `requests` library is already available

## Configuration

Before running the script, you need to update the following in `facebook_ads_report.py`:

1. **Facebook Access Token**: Replace `"REPLACE_WITH_YOUR_ACCESS_TOKEN"` with your actual Facebook Graph API access token
2. **Google Chat Webhook**: The webhook URL is already configured, but you can update it if needed

## Usage

Run the script with:
```bash
python3 facebook_ads_report.py
```

## What the Script Does

1. **Fetches Account Data**: For each account in the list, it retrieves:
   - Month-to-date spend
   - Number of leads
   - Number of purchases
   - Daily budget from active ad sets

2. **Calculates Metrics**:
   - Spend remaining (daily budget × days left in month)
   - Cost per lead (CPL)
   - Cost per purchase (CPP)
   - Cost per conversion

3. **Generates Report**: Creates a markdown table with all the metrics

4. **Sends to Google Chat**: Posts the report to the configured Google Chat webhook

## Note

Make sure your Facebook access token has the necessary permissions to read insights and ad set data from the accounts listed in the script.