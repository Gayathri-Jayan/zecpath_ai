import os
import json

from parsers.resume_extractor import extract_resume
from loguru import logger

INPUT_FOLDER = "data/resumes"
OUTPUT_FOLDER = "data/output_json"

logger.add("logs/extraction_logs.txt")

for file_name in os.listdir(INPUT_FOLDER):

    file_path = os.path.join(INPUT_FOLDER, file_name)

    try:
        result = extract_resume(file_path)
        from parsers.resume_extractor import save_text_outputs

        save_text_outputs(
            file_name,
            result["raw_text"],
            result["cleaned_text"]
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name + ".json"
        )

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        logger.success(f"{file_name} processed successfully")

    except Exception as e:

        logger.error(f"{file_name} failed: {str(e)}")