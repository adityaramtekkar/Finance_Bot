# utils/categorizer.py
def categorize_expense(description):
    description = description.lower()
    if "uber" in description or "ola" in description:
        return "Travel"
    elif "swiggy" in description or "zomato" in description:
        return "Food"
    elif "rent" in description:
        return "Rent"
    elif "amazon" in description or "myntra" in description:
        return "Shopping"
    else:
        return "Other"
