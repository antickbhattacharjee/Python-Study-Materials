import re

flag = False
domain_list = (".com", ".org", ".net", ".edu", ".gov", ".io", ".co", ".info", 
               ".biz", ".xyz", ".me", ".tv", ".cc", ".us", ".uk", ".ca", ".in")

link = input("Enter a link to check: ").strip()

if link.startswith("https://"):
    # ✅ Must end with '/'
    if not link.endswith("/"):
        print("❌ Link must end with '/'")
    else:
        domain_found = False
        for d in domain_list:
            if link.endswith(d + "/"):  # ✅ Ensure domain + '/'
                domain_found = True
                domain = d
                break

        if domain_found:
            domain_index = link.rfind(domain)
            link_body = link[8:domain_index]  # extract between 'https://' and domain

            # ❌ Prevent empty domain body (e.g. "https://.com/")
            if link_body == "" or link_body == ".":
                print("❌ Link contains invalid domain name")
            else:
                allowed_chars = "-._~:/?#@!$&'()*+,;=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                invalid_found = False
                for ch in link_body:
                    if ch not in allowed_chars:
                        invalid_found = True
                        break

                if not invalid_found:
                    if re.search(r"(.)\1{3,}", link):
                        print("⚠️ Suspicious: Link contains repeated characters more than 3 times")
                    else:
                        flag = True
                else:
                    print("❌ Link contains invalid characters")
        else:
            print("❌ Link does not end with a valid domain + '/'")
else:
    print("❌ Link does not start with 'https://'")

if flag:
    print("✅ Link is valid")
else:
    print("🔍 Link is suspicious or invalid")
