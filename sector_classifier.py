def identify_sector(text):
    text = text.lower()

    if any(word in text for word in ["software", "technology", "it", "cloud", "ai"]):
        return "IT / Technology"

    elif any(word in text for word in ["bank", "finance", "investment", "insurance"]):
        return "Finance"

    elif any(word in text for word in ["hospital", "health", "medical", "pharma"]):
        return "Healthcare"

    elif any(word in text for word in ["manufacturing", "factory", "industrial"]):
        return "Manufacturing"

    else:
        return "Unknown"