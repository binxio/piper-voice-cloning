for i in *.mp3; do
  ffmpeg -i "$i" -ac 1 -ar 16000 "${i%.*}.wav"
done
