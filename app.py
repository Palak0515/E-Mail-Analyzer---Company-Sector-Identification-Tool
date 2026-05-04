from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    emails = data.get("emails", "").splitlines()

    results = []
    invalid_count = 0

    free_domains = ["gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com","protonmail.com"]
    educational_domains = ["ac.in", "edu"]

    for email in emails:
        email = email.strip()
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not re.match(email_pattern, email):
            invalid_count += 1
            continue

        username, domain = email.split("@", 1)
        person = username.replace(".", " ").replace("_"," ").title()
        if domain in free_domains:
            domain_type = "Free Webmail"
        elif any(ed in domain for ed in educational_domains):
            domain_type = "Educational"
        elif ".org" in domain:
            domain_type = "Organization"
        elif ".gov" in domain:
            domain_type = "Government"
        else:
            domain_type = "Corporate"

        university = "Not Found"
        if "iit" in domain:
            university = "Indian Institute of Technology"
        elif "mit" in domain:
            university = "MIT"
        elif "harvard" in domain:
            university = "Harvard University"
        elif "stanford" in domain:
            university = "Stanford University"

        company = "Unknown" if domain in free_domains else domain.split(".")[0].capitalize()

        results.append({"email": email,
                        "domain": domain,
                        "domain_type": domain_type,
                        "person": person,
                        "university": university,
                        "company": company})

    df = pd.DataFrame(results)
    df.to_excel("email_results.xlsx", index=False)

    return jsonify({"total_valid": len(results),
                    "total_invalid": invalid_count,
                    "data": results})

@app.route("/download")
def download():
    return send_file("email_results.xlsx",as_attachment=True,download_name="email_results.xlsx",mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    app.run(debug=True)