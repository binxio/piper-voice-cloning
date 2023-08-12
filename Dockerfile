# Start with Python 3.9 base image
FROM python:3.9

# Copy the model files from your local system to the docker container
COPY model/model.onnx /model/model.onnx
COPY model/model.onnx.json /model/model.onnx.json

# Set the working directory to /output
# This is where the result.wav will be written
WORKDIR /output

# Install piper-tts
RUN pip install piper-tts

# Default command
CMD echo $INPUT_STRING | piper -m /model/model.onnx --output_file ./output.wav

