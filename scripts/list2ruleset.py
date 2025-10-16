import json, re, sys, os

def parse_list(src):
    domains, suffixes, keywords = [], [], []
    with open(src, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            m = re.match(r'^(DOMAIN|DOMAIN-SUFFIX|DOMAIN-KEYWORD)\s*,\s*([^,\s#]+)', s, re.I)
            if not m:
                continue
            typ, val = m.group(1).upper(), m.group(2)
            if typ == "DOMAIN":
                domains.append(val)
            elif typ == "DOMAIN-SUFFIX":
                suffixes.append(val)
            elif typ == "DOMAIN-KEYWORD":
                keywords.append(val)
    rules = []
    if domains:   rules.append({"domain": domains})
    if suffixes:  rules.append({"domain_suffix": suffixes})
    if keywords:  rules.append({"domain_keyword": keywords})
    return {"version": 1, "rules": rules}

def convert_one(basename):
    src = f"{basename}.list"
    if not os.path.exists(src):
        print(f"skip {src} (not found)")
        return False
    obj = parse_list(src)
    out_json = f"{basename}-source.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_json}")
    return True

if __name__ == "__main__":
    # 支持传参：python scripts/list2ruleset.py emby tiktok
    targets = sys.argv[1:] or ["emby", "tiktok"]
    for name in targets:
        convert_one(name)
