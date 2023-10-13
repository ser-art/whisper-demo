# import fire
import whisper
import time
import streamlit as st
from tempfile import NamedTemporaryFile
from audio_recorder_streamlit import audio_recorder
import librosa


# @st.cache_resource()
# def load_model(model_name="base"):
#     return whisper.load_model(model_name, device="cpu")


def transcribe(file_path, model_name="base"):
    duration = librosa.get_duration(path=file_path)

    # Print results
    # st.text(f"File: {file_path}")
    st.markdown(f"**Model: {model_name}.**")

    # Load the model
    st.text("Loading the model...")
    model = whisper.load_model(model_name, device="cpu")

    # audio = whisper.load_audio(file_path)
    # audio = whisper.pad_or_trim(audio)

    # mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # # detect the spoken language

    # options = whisper.DecodingOptions(fp16=False)
    # result = whisper.decode(model, mel, options)

    # print(result)

    st.text("Transcribing...")

    # Start timing
    start_time = time.time()

    # Transcribe
    result = model.transcribe(file_path, fp16=False)

    # End timing
    end_time = time.time()

    # Time per duration
    st.markdown(
        f"**Time per duration: {(end_time - start_time) / duration * 60:.2f} seconds per minute!**"
    )

    st.markdown(
        f"**Time taken for transcription: {end_time - start_time:.2f} seconds!**"
    )
    st.markdown(f"**Audio duration: {duration:.2f} seconds.**")

    st.markdown(f"**Transcription: {result['text']}.**")


def main():
    st.title("SigmaBank Whisper Support")

    # st.markdown(
    #     """Press the button below to start recording, to stop recording just stop speaking.
    #     Wait untill the audio is uploaded before pressing the transcribe button."""
    # )

    # audio_bytes = audio_recorder()
    # if audio_bytes:
    #     st.audio(audio_bytes, format="audio/wav")

    # File uploader for audio files
    uploaded_file = st.file_uploader(
        "Choose an audio file", type=["mp3", "wav", "flac"]
    )

    # if uploaded_file:
    #     st.audio(
    #         uploaded_file.read(), format="audio/wav"
    #     )  # Adjust the format accordingly

    model = st.selectbox("Select a model", ["tiny", "base", "small"])

    # Button to transcribe the audio
    if st.button("Transcribe"):
        if uploaded_file:
            with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())

            transcribe(tmp_file.name, model)
        else:
            st.warning("Please upload an audio file first.")


if __name__ == "__main__":
    main()
