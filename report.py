def generate_report(filename, role, percent, matched, missing, suggestions, companies):
    """Generate a text report of resume analysis"""
    report = f"Resume: {filename}\n"
    report += f"Role Applied: {role}\n"
    report += f"Match Percentage: {percent:.1f}%\n\n"

    report += "Matched Skills:\n"
    report += ", ".join(matched) + "\n\n"

    report += "Missing / Other Skills:\n"
    report += ", ".join(missing) + "\n\n"

    report += "AI Suggestions:\n"
    report += ", ".join(suggestions) + "\n\n"

    report += "Recommended Companies:\n"
    report += ", ".join(companies) + "\n"

    return report
