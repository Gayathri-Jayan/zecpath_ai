import re


# -----------------------------------
# Degree Types
# -----------------------------------

DEGREES = [

    "btech",
    "b.tech",
    "mtech",
    "m.tech",
    "bca",
    "mca",
    "bsc",
    "msc",
    "mba"
]


# -----------------------------------
# Fields of Study
# -----------------------------------

FIELDS = [

    "computer science",
    "information technology",
    "electronics",
    "mechanical",
    "civil",
    "artificial intelligence",
    "data science"
]


# -----------------------------------
# Certification Categories
# -----------------------------------

CERTIFICATION_CATEGORIES = {

    "aws": "cloud",

    "google": "cloud",

    "ibm": "data analytics",

    "deloitte": "cybersecurity",

    "infosys": "technology"
}


# -----------------------------------
# Extract Degrees
# -----------------------------------

def extract_degrees(text):

    text = text.lower()

    found = []

    for degree in DEGREES:

        if degree in text:

            found.append(degree)

    return list(set(found))


# -----------------------------------
# Extract Fields
# -----------------------------------

def extract_fields(text):

    text = text.lower()

    found = []

    for field in FIELDS:

        if field in text:

            found.append(field)

    return list(set(found))


# -----------------------------------
# Extract Graduation Years
# -----------------------------------

def extract_graduation_years(text):

    pattern = r"(20\d{2})"

    years = re.findall(pattern, text)

    return list(set(years))


# -----------------------------------
# Extract Institutions
# -----------------------------------

def extract_institutions(text):

    institutions = []

    lines = text.split("\n")

    keywords = [

        "university",

        "college",

        "school",

        "institute"
    ]

    for line in lines:

        for keyword in keywords:

            if keyword in line.lower():

                institutions.append(line.strip())

    return list(set(institutions))


# -----------------------------------
# Extract Certifications
# -----------------------------------

def extract_certifications(text):

    certifications = []

    lines = text.split("\n")

    certification_keywords = [

        "certification",

        "certificate",

        "virtual experience"
    ]

    for line in lines:

        for keyword in certification_keywords:

            if keyword in line.lower():

                certifications.append(line.strip())

    return list(set(certifications))


# -----------------------------------
# Certification Categories
# -----------------------------------

def categorize_certification(certification):

    certification = certification.lower()

    for keyword, category in CERTIFICATION_CATEGORIES.items():

        if keyword in certification:

            return category

    return "general"


# -----------------------------------
# Build Academic Profile
# -----------------------------------

def build_academic_profile(text):

    degrees = extract_degrees(text)

    fields = extract_fields(text)

    institutions = extract_institutions(text)

    years = extract_graduation_years(text)

    certifications = extract_certifications(text)

    structured_certifications = []

    for cert in certifications:

        structured_certifications.append({

            "name": cert,

            "category": categorize_certification(cert)
        })

    return {

        "degrees": degrees,

        "fields_of_study": fields,

        "institutions": institutions,

        "graduation_years": years,

        "certifications": structured_certifications
    }