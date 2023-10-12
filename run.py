# import fire
import whisper
import time
import streamlit as st
from tempfile import NamedTemporaryFile
from audio_recorder_streamlit import audio_recorder


@st.cache_resource()
def load_model(model_name="base"):
    return whisper.load_model(model_name, device="cpu")


def transcribe(file_path, model_name="base"):
    # Print results
    st.text(f"File: {file_path}")
    st.text(f"Model: {model_name}")

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

    # Start timing
    start_time = time.time()

    # Transcribe
    result = model.transcribe(file_path, fp16=False)

    # End timing
    end_time = time.time()

    st.markdown(
        f"**Time taken for transcription: {end_time - start_time:.2f} seconds!**"
    )
    st.markdown(f"**Transcription: {result['text']}.**")


def main():
    st.title("Whisper Transcription Demo")

    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")

    # # File uploader for audio files
    # uploaded_file = st.file_uploader(
    #     "Choose an audio file", type=["mp3", "wav", "flac"]
    # )

    # if uploaded_file:
    #     st.audio(uploaded_file, format="audio/wav")  # Adjust the format accordingly

    model = st.selectbox("Select a model", ["tiny", "base", "small"])

    # Button to transcribe the audio
    if st.button("Transcribe"):
        if audio_bytes:
            with NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_file.write(audio_bytes)

            transcribe(tmp_file.name, model)
        else:
            st.warning("Please upload an audio file first.")


if __name__ == "__main__":
    main()
