import urllib.request
from datetime import datetime

# รายชื่อลิงก์ทั้ง 10 ลิงก์
urls = [
    "https://raw.githubusercontent.com/PhyschicWinter9/thai-adblock-list/main/subscription/thai-adblock-list-adblockplus.txt",
    "https://ublocko.github.io/uBO-Filters/uF.txt",
    "https://cdn.jsdelivr.net/gh/deathbybandaid/piholeparser/Subscribable-Lists/ParsedBlacklists/EasyList-Thailand.txt",
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
    "https://easylist-downloads.adblockplus.org/easylist.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro++.txt",
    "https://hblock.molinero.dev/hosts_adblock.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt"
]

merged_rules = set()

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read().decode('utf-8').splitlines()
            for line in data:
                line = line.strip()
                # กรองบรรทัดที่ว่างเปล่า และบรรทัดที่เป็น Comment ออก (เก็บเฉพาะ Rule จริงๆ)
                if line and not line.startswith('!') and not line.startswith('#'):
                    merged_rules.add(line)
    except Exception as e:
        print(f"Error loading {url}: {e}")

# บันทึกเป็นไฟล์ adblock_list.txt
with open("adblock_list.txt", "w", encoding="utf-8") as f:
    f.write("[Adblock Plus 2.0]\n")
    f.write(f"! Title: My Custom Adblock List\n")
    f.write(f"! Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n")
    f.write(f"! Total Rules: {len(merged_rules)}\n")
    for rule in sorted(merged_rules):
        f.write(rule + "\n")
