import requests
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_VERSION = "v19.0"
WEBHOOK = "https://chat.googleapis.com/v1/spaces/AAQARW0Ay7s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9Y7d0p62A5I6phFsmp1WjkCxi-aeYoqqi093MfOAmHY"

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

today = datetime.date.today()
if today.month < 12:
    eom = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)
else:
    eom = datetime.date(today.year, 12, 31)
days_left = (eom - today).days + 1
total_days = eom.day

rows = []

for acc in accounts:
    acc_id = acc["account_id"]
    name = acc["account_name"]

    # Get MTD spend, leads, purchases
    insights_url = (
        f"https://graph.facebook.com/{API_VERSION}/act_{acc_id}/insights"
        f"?fields=spend,actions"
        f"&date_preset=this_month"
        f"&access_token={ACCESS_TOKEN}"
    )
    resp = requests.get(insights_url)
    spend = leads = purchases = 0
    if resp.status_code == 200:
        data = resp.json().get("data", [{}])[0]
        spend = float(data.get("spend", 0))
        actions = {a["action_type"]: float(a["value"]) for a in data.get("actions", [])} if "actions" in data else {}
        leads = int(actions.get("lead", 0))
        purchases = int(actions.get("omni_purchase", 0) or actions.get("purchase", 0))
    else:
        print(f"Insights error for {acc_id}: {resp.text}")

    # Get sum of ad set daily budgets
    adset_url = (
        f"https://graph.facebook.com/{API_VERSION}/act_{acc_id}/adsets"
        f"?fields=daily_budget"
        f"&limit=100"
        f"&access_token={ACCESS_TOKEN}"
    )
    adset_resp = requests.get(adset_url)
    daily_budget = 0
    if adset_resp.status_code == 200:
        adsets = adset_resp.json().get("data", [])
        daily_budget = sum(int(a["daily_budget"]) / 100 for a in adsets if a.get("daily_budget"))
    else:
        print(f"Adset error for {acc_id}: {adset_resp.text}")

    spend_remaining = round(daily_budget * days_left, 2)
    cpl = round(spend / leads, 2) if leads else ""
    cpp = round(spend / purchases, 2) if purchases else ""
    cost_per_conv = round(spend / (leads + purchases), 2) if (leads + purchases) else ""

    rows.append([
        name, daily_budget, spend, spend_remaining, leads, purchases, cpl, cpp, cost_per_conv
    ])

# Build markdown table
header = ["Account Name", "Daily Budget", "Spend", "Spend Remaining", "Leads", "Purchases", "CPL", "CPP", "Cost/Conv"]
table_md = "| " + " | ".join(header) + " |\n"
table_md += "| " + " | ".join(["---"] * len(header)) + " |\n"
for row in rows:
    table_md += "| " + " | ".join(str(x) for x in row) + " |\n"

message = {
    "text": f"*Paid Media Account Summary*\n\n{table_md}"
}

resp = requests.post(WEBHOOK, json=message)
print("Google Chat webhook status:", resp.status_code)
print(resp.text) 