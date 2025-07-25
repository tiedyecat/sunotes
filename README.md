# Facebook Ads Reporting Script

This script generates a summary report for Facebook Ads accounts and sends it to a Google Chat webhook.

## Setup

1. **Python Installation**: Python 3.11+ is already installed on your system
2. **Dependencies**: Install required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

## Configuration

1. **Environment Variables**: Copy the `.env` file and update it with your credentials:
   - Replace `your_facebook_access_token_here` with your actual Facebook Graph API access token
   - The Google Chat webhook URL is pre-configured, but you can update it if needed
   - `DRY_RUN=true` means the script will only print to console (safe for testing)

2. **Alternative Configuration**: You can also set environment variables directly:
   ```bash
   export ACCESS_TOKEN="your_facebook_access_token_here"
   export DRY_RUN="false"
   ```

## Usage

### Test Mode (Default - Recommended)
```bash
python3 facebook_ads_report.py
# or explicitly
python3 facebook_ads_report.py --dry-run
```
This will generate and display the report in your console without sending it to Google Chat.

### Send to Google Chat
```bash
python3 facebook_ads_report.py --send
```
This will generate the report and send it to the configured Google Chat webhook.

### Help
```bash
python3 facebook_ads_report.py --help
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

4. **Output Options**:
   - **Dry Run Mode**: Prints the report to console for review
   - **Send Mode**: Posts the report to the configured Google Chat webhook

## Security

- The `.env` file contains sensitive information and is excluded from git tracking
- Never commit your actual access tokens to version control
- Make sure your Facebook access token has the necessary permissions to read insights and ad set data from the accounts listed in the script
- Always test with dry run mode first before sending to chat