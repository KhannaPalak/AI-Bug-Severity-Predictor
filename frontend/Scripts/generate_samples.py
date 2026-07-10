import pandas as pd
import random

modules = [
    "Authentication",
    "Login",
    "Payment Gateway",
    "Shopping Cart",
    "Database",
    "REST API",
    "FastAPI",
    "Docker",
    "Kubernetes",
    "Cloud Storage",
    "Machine Learning",
    "BERT Model",
    "User Profile",
    "Notifications",
    "Email Service",
    "File Upload",
    "Dashboard",
    "Search",
    "Reports",
    "Admin Panel",
]

issues = [
    "crashes unexpectedly",
    "returns HTTP 500",
    "freezes during operation",
    "shows incorrect data",
    "fails to load",
    "times out",
    "throws Null Pointer Exception",
    "consumes excessive memory",
    "uses high CPU",
    "redirects infinitely",
    "fails authentication",
    "loses session",
    "duplicates records",
    "does not save changes",
    "fails after deployment",
]

descriptions = [
    "The issue occurs consistently after repeated usage.",
    "The bug affects production users.",
    "The application becomes unresponsive.",
    "The server logs indicate an internal exception.",
    "The problem started after the latest deployment.",
    "Users cannot complete their workflow.",
    "The issue is reproducible every time.",
    "Memory consumption continuously increases.",
    "API response exceeds timeout limits.",
    "System performance degrades significantly.",
]

rows = []

for i in range(500):

    module = random.choice(modules)
    issue = random.choice(issues)
    desc = random.choice(descriptions)

    rows.append(
        {
            "Title": f"{module} - {issue}",
            "Summary": f"{module} {issue}",
            "Description": f"{module}: {desc}",
        }
    )

df = pd.DataFrame(rows)

df.to_csv("../data/sample_bugs.csv", index=False)

print("✅ 500 sample bug reports generated successfully!")
