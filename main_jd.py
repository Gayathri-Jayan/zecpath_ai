import json

from ats_engine.jd_parser import build_jd_profile

sample_jd = """

We are hiring a MERN Stack Developer
with 2+ years experience in React.js,
NodeJS, MongoDB and AWS.

Qualification: B.Tech / MCA preferred.

"""

result = build_jd_profile(sample_jd)

print(json.dumps(result, indent=4))