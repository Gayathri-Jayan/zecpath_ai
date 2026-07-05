from screening_ai.stt_service import speech_to_text

from screening_ai.transcript_processor import process_transcript


def stt_pipeline(audio_file):

    transcript = speech_to_text(

        audio_file
    )

    result = process_transcript(

        transcript["text"]
    )

    return result