# How to run

```bash

docker build -t whisper-benchmark .

docker run --rm --cpus=1 --name whisper-benchmark whisper-benchmark --file-path=audio/audio.mp3 --model-name=tiny

docker run whisper-benchmark --file-path=./audio/audio.mp3 --model-name=tiny
```
