FROM python:3.10-slim

# Set work directory
WORKDIR /python-docker

# Install dependencies
COPY requirements.txt requirements.txt

# Install system dependencies and clean up apt cache
RUN apt-get update && apt-get install git -y
RUN apt-get update && apt-get install -y ffmpeg

# Install python dependencies
RUN pip install -r requirements.txt
RUN pip install "git+https://github.com/openai/whisper.git"

# Copy project files
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]