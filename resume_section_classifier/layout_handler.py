def normalize_layout(text):

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove multiple spaces
    while "  " in text:
        text = text.replace("  ", " ")

    return text