# -----------------------------------
# Role-Based Rule Configuration
# -----------------------------------

JOB_RULES = {

    "backend developer": {

        "minimum_ats_score": 75,

        "mandatory_skills": [

            "python",

            "django",

            "rest api"
        ],

        "minimum_experience": 2,

        "maximum_experience": 6,

        "preferred_location": "remote",

        "availability": "immediate"
    },

    "data scientist": {

        "minimum_ats_score": 80,

        "mandatory_skills": [

            "python",

            "machine learning",

            "pandas"
        ],

        "minimum_experience": 3,

        "maximum_experience": 8,

        "preferred_location": "hybrid",

        "availability": "immediate"
    }
}


# -----------------------------------
# Get Rules for Job
# -----------------------------------

def get_job_rules(job_role):

    return JOB_RULES.get(

        job_role.lower(),

        {}
    )


# -----------------------------------
# Check Mandatory Skills
# -----------------------------------

def check_skills(

    candidate_skills,

    mandatory_skills
):

    candidate_skills = [

        skill.lower()

        for skill in candidate_skills
    ]

    return all(

        skill.lower() in candidate_skills

        for skill in mandatory_skills
    )


# -----------------------------------
# Experience Validation
# -----------------------------------

def check_experience(

    experience_years,

    min_exp,

    max_exp
):

    return (

        min_exp <= experience_years <= max_exp
    )


# -----------------------------------
# Location Validation
# -----------------------------------

def check_location(

    candidate_location,

    preferred_location
):

    return (

        candidate_location.lower()

        ==

        preferred_location.lower()
    )


# -----------------------------------
# Availability Validation
# -----------------------------------

def check_availability(

    candidate_availability,

    required_availability
):

    return (

        candidate_availability.lower()

        ==

        required_availability.lower()
    )


# -----------------------------------
# Eligibility Decision Logic
# -----------------------------------

def evaluate_candidate(

    candidate,

    job_role
):

    rules = get_job_rules(

        job_role
    )

    score = candidate.get(

        "final_score",

        0
    )

    skills_match = check_skills(

        candidate.get(

            "skills",

            []
        ),

        rules.get(

            "mandatory_skills",

            []
        )
    )

    experience_match = check_experience(

        candidate.get(

            "experience_years",

            0
        ),

        rules.get(

            "minimum_experience",

            0
        ),

        rules.get(

            "maximum_experience",

            100
        )
    )

    location_match = check_location(

        candidate.get(

            "location",

            ""
        ),

        rules.get(

            "preferred_location",

            ""
        )
    )

    availability_match = check_availability(

        candidate.get(

            "availability",

            ""
        ),

        rules.get(

            "availability",

            ""
        )
    )

    # Final Status

    if (

        score >= rules.get(

            "minimum_ats_score",

            0
        )

        and skills_match

        and experience_match

        and location_match

        and availability_match

    ):

        status = "Eligible"

    elif score >= 60:

        status = "Review"

    else:

        status = "Rejected"

    return {

        "candidate_id":

        candidate.get(

            "candidate_id"
        ),

        "job_role":

        job_role,

        "final_score":

        score,

        "mandatory_skills_match":

        skills_match,

        "experience_match":

        experience_match,

        "location_match":

        location_match,

        "availability_match":

        availability_match,

        "eligibility_status":

        status
    }

# -----------------------------------
# Default Eligibility Rules
# -----------------------------------

DEFAULT_RULES = {

    "min_ats_score": 70,

    "mandatory_skills": [],

    "min_experience": 0,

    "max_experience": 10,

    "allowed_locations": [],

    "availability_required": False
}


# -----------------------------------
# Safe Value Helper
# -----------------------------------

def safe_value(value, default):

    return value if value is not None else default


# -----------------------------------
# Skill Matching Check
# -----------------------------------

def check_mandatory_skills(

        candidate_skills,

        required_skills):

    if not required_skills:

        return True

    candidate_skills = [

        s.lower()

        for s in candidate_skills
    ]

    required_skills = [

        s.lower()

        for s in required_skills
    ]

    return all(

        skill in candidate_skills

        for skill in required_skills
    )


# -----------------------------------
# Experience Check
# -----------------------------------

def check_experience(

        candidate_exp,

        min_exp,

        max_exp):

    return min_exp <= candidate_exp <= max_exp


# -----------------------------------
# Location Check
# -----------------------------------

def check_location(

        candidate_location,

        allowed_locations):

    if not allowed_locations:

        return True

    return candidate_location.lower() in [

        loc.lower()

        for loc in allowed_locations
    ]


# -----------------------------------
# Availability Check
# -----------------------------------

def check_availability(

        is_available,

        required):

    if not required:

        return True

    return is_available


# -----------------------------------
# Main Eligibility Function
# -----------------------------------

def evaluate_candidate(

        candidate,

        rules=DEFAULT_RULES):

    ats_score = safe_value(

        candidate.get(

            "final_score"),

        0)

    skills = safe_value(

        candidate.get(

            "skills"),

        [])

    experience = safe_value(

        candidate.get(

            "total_experience"),

        0)

    location = safe_value(

        candidate.get(

            "location"),

        "")

    available = safe_value(

        candidate.get(

            "available"),

        True)

    # Rule Checks

    skill_ok = check_mandatory_skills(

        skills,

        rules["mandatory_skills"]
    )

    exp_ok = check_experience(

        experience,

        rules["min_experience"],

        rules["max_experience"]
    )

    loc_ok = check_location(

        location,

        rules["allowed_locations"]
    )

    avail_ok = check_availability(

        available,

        rules["availability_required"]
    )

    # Decision Logic

    if (

        ats_score >= rules["min_ats_score"]

        and skill_ok

        and exp_ok

        and loc_ok

        and avail_ok

    ):

        status = "Eligible"

    elif ats_score >= (

            rules["min_ats_score"] - 15):

        status = "Review"

    else:

        status = "Rejected"

    return {

        "candidate_id":

            candidate.get(

                "candidate_id"),

        "eligibility_status":

            status,

        "checks": {

            "ats_score":

                ats_score,

            "skill_match":

                skill_ok,

            "experience_match":

                exp_ok,

            "location_match":

                loc_ok,

            "availability_match":

                avail_ok
        }
    }


# -----------------------------------
# Batch Evaluation Pipeline
# -----------------------------------

def evaluate_candidates_batch(

        candidates,

        rules):

    results = []

    for candidate in candidates:

        result = evaluate_candidate(

            candidate,

            rules=DEFAULT_RULES)

        results.append(

            result)

    return results