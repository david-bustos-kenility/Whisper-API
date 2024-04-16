# Terminal 
1. docker build -t whisper-api-img .
2. docker run -p 8000:8000 whisper-api-img
3. Abrir la url: localhost:8000/docs
4. Listo subir el wav file y obtener el transcript.
```bash
curl -X 'POST' \
  'http://localhost:8000/whisper' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@450.mp3;type=audio/mpeg'
```