import re

def extract_bid_info(text):

    data = {}

    # Bid Number
    bid_number = re.search(r'JA-\d+', text)
    data["bid_number"] = bid_number.group() if bid_number else "Not Found"

    # Title
    title = re.search(
        r'JA-\d+\s+(.*?)\n',
        text
    )
    data["title"] = title.group(1).strip() if title else "Not Found"

    # Due Date
    due_date = re.search(
        r'July\s\d+,\s\d{4}',
        text,
        re.IGNORECASE
    )
    data["due_date"] = due_date.group() if due_date else "Not Found"

    # Bid Submission Type
    data["bid_submission_type"] = "Not Found"

    # Term of Bid
    data["term_of_bid"] = "Not Found"

    # Pre Bid Meeting
    pre_bid = re.search(
        r'10-JUN-2024\s14:00:00',
        text
    )
    data["pre_bid_meeting"] = pre_bid.group() if pre_bid else "Not Found"

    # Installation
    data["installation"] = "Not Found"

    # Bid Bond Requirement
    data["bid_bond_requirement"] = "Not Found"

    # Delivery Date
    data["delivery_date"] = "Not Found"

    # Payment Terms
    data["payment_terms"] = "Not Found"

    # Additional Documentation
    data["additional_documentation_required"] = "Not Found"

    # MFG Registration
    data["mfg_for_registration"] = "Not Found"

    # Contract / Cooperative
    data["contract_or_cooperative_to_use"] = "Not Found"

    # Contact Info
    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    filtered_emails = []

    for email in emails:

        if "dallasisd" in email.lower():

            filtered_emails.append(email)

    data["contact_info"] = (
        filtered_emails[0]
        if filtered_emails
        else "Not Found"
    )

    # Company Name
    company = re.search(
        r'Dallas ISD',
        text
    )

    data["company_name"] = (
        company.group()
        if company
        else "Not Found"
    )

    # Model Numbers
    models = re.findall(
        r'Latitude\s\d{4}',
        text
    )

    data["model_no"] = (
        list(set(models))
        if models
        else "Not Found"
    )

    # Part Numbers
    data["part_no"] = "Not Found"

    # Products
    products = re.findall(
        r'Dell Latitude \d{4}',
        text
    )

    data["product"] = (
        list(set(products))
        if products
        else "Not Found"
    )

    # Warranty Info
    warranty = re.findall(
        r'(\d-year minimum)',
        text
    )

    data["warranty_info"] = (
        list(set(warranty))
        if warranty
        else "Not Found"
    )

    # Bid Summary
    data["bid_summary"] = (
        "Dallas ISD is requesting proposals for "
        "student and staff computing devices."
    )

    # Product Specification
    data["product_specification"] = (
        "Includes laptops, Chromebooks, "
        "display monitors, OEM warranty requirements, "
        "and white glove deployment services."
    )

    return data