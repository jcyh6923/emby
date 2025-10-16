import json, sys, re

src = "emby.list"
dst = "emby-source.json"

domains = []
domain_suffix = []
domain_keyword = []

with open(src, "r", encoding="utf-8") as f:
    for line in f:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        # 支持：DOMAIN,xxx / DOMAIN-SUFFIX,xxx / DOMAIN-KEYWORD,xxx
        m = re.match(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD)\s*,\s*([^,\s#]+)', s, re.I)
        if not m: 
            continue
        typ, val = m.group(1).upper(), m.group(2)
        if typ == "DOMAIN":
            domains.append(val)
        elif typ == "DOMAIN-SUFFIX":
            domain_suffix.append(val)
        elif typ == "DOMAIN-KEYWORD":
            domain_keyword.append(val)

rules = []
if domains:
    rules.append({"domain": domains})
if domain_suffix:
    rules.append({"domain_suffix": domain_suffix})
if domain_keyword:
    rules.append({"domain_keyword": domain_keyword})

obj = {"version": 1, "rules": rules}

with open(dst, "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
print(f"wrote {dst} with {len(rules)} rule blocks.")
