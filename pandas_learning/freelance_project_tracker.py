import pandas as pd

projects = pd.DataFrame({
    'project': ['Web Scraper','Excel Automation','Data Analysis','SQL Setup','Dasjboard'],
    'budget': [8000, 5000, 15000, 10000, 12000],
    'hours_spent': [10,5,20,15,18],
    'status': ['In Progress','Completed','In Progress','Completed','In Progress]
    })

# Add categories using lambda
# 1. Rate per hour
# 2. Project size (Small/Medium/Large based on budget)
# 3. Efficiency (budget/hours_spent)
# 4. Filter: High paying projects that are completed

