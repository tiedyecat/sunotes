import requests
import datetime
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_VERSION = "v19.0"
WEBHOOK = "https://chat.googleapis.com/v1/spaces/AAQARW0Ay7s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9Y7d0p62A5I6phFsmp1WjkCxi-aeYoqqi093MfOAmHY"

# Check for dry run mode (default to True for safety)
DRY_RUN = os.getenv("DRY_RUN", "true").lower() in ("true", "1", "yes")

# Override with command line argument
if len(sys.argv) > 1:
    if sys.argv[1] == "--send":
        DRY_RUN = False
    elif sys.argv[1] == "--dry-run":
        DRY_RUN = True
    elif sys.argv[1] == "--help":
        print("Usage: python3 facebook_ads_report.py [--send|--dry-run|--help]")
        print("  --send     Send report to Google Chat")
        print("  --dry-run  Print report to console only (default)")
        print("  --help     Show this help message")
        sys.exit(0)

# Check if access token is configured
if not ACCESS_TOKEN or ACCESS_TOKEN == "your_facebook_access_token_here":
    print("ERROR: ACCESS_TOKEN not configured in .env file")
    print("Please edit the .env file and set your Facebook access token")
    sys.exit(1)

print(f"Running in {'LIVE' if not DRY_RUN else 'DRY RUN'} mode")

accounts = [
    {"account_name": "American Barbell Clubs", "account_id": "768011641837919"},
    {"account_name": "Blue Moon Fitness", "account_id": "3391610954217064"},
    {"account_name": "BodyFuel Fitness", "account_id": "153306196665189"},
    {"account_name": "CLUB4 Airport Blvd", "account_id": "3677625435847606"},
    {"account_name": "CLUB4 Baton Rouge (FL Blvd)", "account_id": "1149138102928190"},
    {"account_name": "CLUB4 Baton Rouge (Jones Creek)", "account_id": "430318089532490"},
    {"account_name": "CLUB4 Coppell", "account_id": "471612331857396"},
    {"account_name": "CLUB4 Flower Mound", "account_id": "734469125480093"},
    {"account_name": "CLUB4 Flowood", "account_id": "720349256965760"},
    {"account_name": "CLUB4 Fort Oglethorpe", "account_id": "418347846562803"},
    {"account_name": "CLUB4 Grand Prairie", "account_id": "25225981710381288"},
    {"account_name": "CLUB4 Gulfport", "account_id": "1159757755047228"},
    {"account_name": "CLUB4 Harvey", "account_id": "794797602567121"},
    {"account_name": "CLUB4 Hernando", "account_id": "2405794156295144"},
    {"account_name": "CLUB4 Hillcrest", "account_id": "283967884736561"},
    {"account_name": "CLUB4 Homewood", "account_id": "820900519856984"},
    {"account_name": "CLUB4 Hoover", "account_id": "426701026402091"},
    {"account_name": "CLUB4 Horn Lake", "account_id": "1134629174377884"},
    {"account_name": "CLUB4 Houma", "account_id": "2528017720706385"},
    {"account_name": "CLUB4 Inverness", "account_id": "444367931272993"},
    {"account_name": "CLUB4 Kenner", "account_id": "315994014491477"},
    {"account_name": "CLUB4 Kingston (Knoxville)", "account_id": "958755499107421"},
    {"account_name": "CLUB4 Knoxville", "account_id": "429960709555331"},
    {"account_name": "CLUB4 Lafayette", "account_id": "1348642135843421"},
    {"account_name": "CLUB4 Lake Charles", "account_id": "1512722452931613"},
    {"account_name": "CLUB4 Lake Harbour", "account_id": "742937718041243"},
    {"account_name": "CLUB4 Longview", "account_id": "1161109311722347"},
    {"account_name": "CLUB4 Madison", "account_id": "1157558445407339"},
    {"account_name": "CLUB4 McKinney", "account_id": "1873494733108567"},
    {"account_name": "CLUB4 Melbourne", "account_id": "2091960307832341"},
    {"account_name": "CLUB4 Meridian", "account_id": "390013037150578"},
    {"account_name": "CLUB4 Murphy", "account_id": "1151816089180077"},
    {"account_name": "CLUB4 Orlando", "account_id": "216239401583608"},
    {"account_name": "CLUB4 Prattville", "account_id": "725278396132912"},
    {"account_name": "CLUB4 Schillinger", "account_id": "3857358031186659"},
    {"account_name": "CLUB4 Shreveport", "account_id": "937226184733455"},
    {"account_name": "CLUB4 Slidell", "account_id": "1559285031582494"},
    {"account_name": "CLUB4 Starkville", "account_id": "6483928041710615"},
    {"account_name": "CLUB4 Tillman's Corner", "account_id": "904491511426823"},
    {"account_name": "CLUB4 Trussville", "account_id": "1056669778768498"},
    {"account_name": "California Athletic Club", "account_id": "430492915277766"},
    {"account_name": "Club Fit", "account_id": "2978635188937841"},
    {"account_name": "Club4", "account_id": "250052719425863"},
    {"account_name": "Focus Fitness Club", "account_id": "493003589707257"},
    {"account_name": "Gentry Gym", "account_id": "1116948612833379"},
    {"account_name": "Glen Swain", "account_id": "146633817605203"},
    {"account_name": "Gold's Gym BC", "account_id": "863908177844455"},
    {"account_name": "Gold's Gym Laval", "account_id": "4240296322862443"},
    {"account_name": "Gold's Gym Ville St-Laurent", "account_id": "514167960371052"},
    {"account_name": "Henry's Gymnasium - Capitol Hill", "account_id": "3245179648899298"},
    {"account_name": "Hidden Gym", "account_id": "2199284363711953"},
    {"account_name": "LEVEL Fitness Pelham", "account_id": "820514018691762"},
    {"account_name": "LEVEL Fitness Thornwood", "account_id": "1171062777200647"},
    {"account_name": "LEVEL Fitness Yorktown", "account_id": "339863677199288"},
    {"account_name": "Level Somers", "account_id": "1102554120713582"},
    {"account_name": "Lubbock CLUB4 Fitness (New)", "account_id": "3513413998952998"},
    {"account_name": "Maximum Health & Fitness", "account_id": "210589141110391"},
    {"account_name": "Physiq Fitness", "account_id": "797120043955249"},
    {"account_name": "Results Gym", "account_id": "2557742534531268"},
    {"account_name": "Satya Yoga", "account_id": "774317683757687"},
    {"account_name": "Shasta Athletic Club", "account_id": "245388930016665"},
    {"account_name": "VillaSport | West Wind | Peacock Gap", "account_id": "248503545341046"},
    {"account_name": "West Seattle Health Club", "account_id": "3658212624277624"},
    {"account_name": "World Gym Beaumont", "account_id": "180438538439013"},
]

print(f"Processing {len(accounts)} accounts...")

today = datetime.date.today()
if today.month < 12:
    eom = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)
else:
    eom = datetime.date(today.year, 12, 31)
days_left = (eom - today).days + 1
total_days = eom.day

rows = []
totals = {"spend": 0, "leads": 0, "purchases": 0}
skipped_accounts = []

# Group for CLUB4 accounts
club4_data = {
    "spend": 0,
    "leads": 0, 
    "purchases": 0,
    "daily_budget": 0,
    "account_count": 0,
    "errors": []
}

for acc in accounts:
    acc_id = acc["account_id"]
    name = acc["account_name"]
    is_club4 = "club4" in name.lower()

    # Get MTD spend, leads, purchases
    insights_url = (
        f"https://graph.facebook.com/{API_VERSION}/act_{acc_id}/insights"
        f"?fields=spend,actions"
        f"&date_preset=this_month"
        f"&access_token={ACCESS_TOKEN}"
    )
    resp = requests.get(insights_url)
    spend = leads = purchases = 0
    insights_error = None
    
    if resp.status_code == 200:
        data = resp.json().get("data", [{}])[0]
        spend = float(data.get("spend", 0))
        actions = {a["action_type"]: float(a["value"]) for a in data.get("actions", [])} if "actions" in data else {}
        leads = int(actions.get("lead", 0))
        purchases = int(actions.get("omni_purchase", 0) or actions.get("purchase", 0))
    else:
        insights_error = resp.json().get("error", {}).get("message", "Unknown error")
        print(f"Insights error for {name}: {insights_error}")

    # Get sum of ad set daily budgets
    adset_url = (
        f"https://graph.facebook.com/{API_VERSION}/act_{acc_id}/adsets"
        f"?fields=daily_budget"
        f"&limit=100"
        f"&access_token={ACCESS_TOKEN}"
    )
    adset_resp = requests.get(adset_url)
    daily_budget = 0
    adset_error = None
    
    if adset_resp.status_code == 200:
        adsets = adset_resp.json().get("data", [])
        daily_budget = sum(int(a["daily_budget"]) / 100 for a in adsets if a.get("daily_budget"))
    else:
        adset_error = adset_resp.json().get("error", {}).get("message", "Unknown error")
        print(f"Adset error for {name}: {adset_error}")

    # Track skipped accounts
    if insights_error or adset_error:
        error_reason = insights_error or adset_error
        if "ads_management" in error_reason.lower() or "ads_read" in error_reason.lower():
            reason = "No permission"
        elif "malformed access token" in error_reason.lower():
            reason = "Invalid token"
        elif "account not found" in error_reason.lower():
            reason = "Account not found"
        else:
            reason = "API error"
            
        skipped_accounts.append({
            "name": name,
            "reason": reason,
            "error": error_reason[:100] + "..." if len(error_reason) > 100 else error_reason
        })
        
        # Skip this account if we have no data
        if insights_error and adset_error:
            continue

    # Add to totals
    totals["spend"] += spend
    totals["leads"] += leads
    totals["purchases"] += purchases

    # Handle CLUB4 accounts - group them together
    if is_club4:
        club4_data["spend"] += spend
        club4_data["leads"] += leads
        club4_data["purchases"] += purchases
        club4_data["daily_budget"] += daily_budget
        club4_data["account_count"] += 1
        if insights_error or adset_error:
            club4_data["errors"].append(f"{name}: {reason}")
    else:
        # Individual account (not CLUB4)
        spend_remaining = round(daily_budget * days_left, 2)
        cpl = round(spend / leads, 2) if leads else ""
        cpp = round(spend / purchases, 2) if purchases else ""
        cost_per_conv = round(spend / (leads + purchases), 2) if (leads + purchases) else ""

        # Format monetary values with dollar signs
        daily_budget_formatted = f"${daily_budget:,.2f}" if daily_budget > 0 else "-"
        spend_formatted = f"${spend:,.2f}" if spend > 0 else "-"
        spend_remaining_formatted = f"${spend_remaining:,.2f}" if spend_remaining > 0 else "-"
        cpl_formatted = f"${cpl:,.2f}" if cpl else "-"
        cpp_formatted = f"${cpp:,.2f}" if cpp else "-"
        cost_per_conv_formatted = f"${cost_per_conv:,.2f}" if cost_per_conv else "-"

        rows.append([
            name, daily_budget_formatted, spend_formatted, spend_remaining_formatted, 
            leads, purchases, cpl_formatted, cpp_formatted, cost_per_conv_formatted
        ])

# Add consolidated CLUB4 entry
if club4_data["account_count"] > 0:
    club4_spend_remaining = round(club4_data["daily_budget"] * days_left, 2)
    club4_cpl = round(club4_data["spend"] / club4_data["leads"], 2) if club4_data["leads"] else ""
    club4_cpp = round(club4_data["spend"] / club4_data["purchases"], 2) if club4_data["purchases"] else ""
    club4_cost_per_conv = round(club4_data["spend"] / (club4_data["leads"] + club4_data["purchases"]), 2) if (club4_data["leads"] + club4_data["purchases"]) else ""

    # Format CLUB4 values
    club4_daily_budget_formatted = f"${club4_data['daily_budget']:,.2f}" if club4_data["daily_budget"] > 0 else "-"
    club4_spend_formatted = f"${club4_data['spend']:,.2f}" if club4_data["spend"] > 0 else "-"
    club4_spend_remaining_formatted = f"${club4_spend_remaining:,.2f}" if club4_spend_remaining > 0 else "-"
    club4_cpl_formatted = f"${club4_cpl:,.2f}" if club4_cpl else "-"
    club4_cpp_formatted = f"${club4_cpp:,.2f}" if club4_cpp else "-"
    club4_cost_per_conv_formatted = f"${club4_cost_per_conv:,.2f}" if club4_cost_per_conv else "-"

    rows.insert(0, [
        f"CLUB4 (All {club4_data['account_count']} Locations)", 
        club4_daily_budget_formatted, 
        club4_spend_formatted, 
        club4_spend_remaining_formatted, 
        club4_data["leads"], 
        club4_data["purchases"], 
        club4_cpl_formatted, 
        club4_cpp_formatted, 
        club4_cost_per_conv_formatted
    ])

# Build markdown table
header = ["Account Name", "Daily Budget", "Spend", "Spend Remaining", "Leads", "Purchases", "CPL", "CPP", "Cost/Conv"]
table_md = "| " + " | ".join(header) + " |\n"
table_md += "| " + " | ".join(["---"] * len(header)) + " |\n"
for row in rows:
    table_md += "| " + " | ".join(str(x) for x in row) + " |\n"

# Create summary section
current_date = datetime.date.today()
month_start = datetime.date(current_date.year, current_date.month, 1)
summary = f"""
**📊 Month-to-Date Summary ({current_date.strftime('%B %d, %Y')})**
*Data from {month_start.strftime('%B %d')} - {current_date.strftime('%B %d, %Y')}*

• Total Spend: ${totals["spend"]:,.2f}
• Total Leads: {totals["leads"]:,}
• Total Purchases: {totals["purchases"]:,}
• Days Remaining: {days_left}
• Accounts Processed: {len(rows)}
• Accounts Skipped: {len(skipped_accounts)}
"""

# Add error summary if there are skipped accounts
error_summary = ""
if skipped_accounts:
    error_summary = "\n**⚠️ Skipped Accounts:**\n"
    for skip in skipped_accounts:
        error_summary += f"• {skip['name']}: {skip['reason']}\n"

message = {
    "text": f"*🎯 Paid Media Account Summary*\n{summary}\n\n{table_md}{error_summary}"
}

if not DRY_RUN:
    print("Sending report to Google Chat...")
    resp = requests.post(WEBHOOK, json=message)
    print("Google Chat webhook status:", resp.status_code)
    if resp.status_code == 200:
        print("✅ Report sent successfully!")
    else:
        print(f"❌ Error sending report: {resp.text}")
else:
    print("\n" + "="*80)
    print("🧪 DRY RUN MODE - Report NOT sent to Google Chat")
    print("="*80)
    print("\nGenerated report:")
    print(message["text"])
    print("\n" + "="*80)
    print("To send this report to Google Chat, run:")
    print("python3 facebook_ads_report.py --send")
    print("="*80) 