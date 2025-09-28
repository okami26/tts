FROM python:3.12-slim

WORKDIR /app

COPY req.txt .

COPY voice.wav .

RUN pip install --no-cache-dir -r req.txt

ENV COQUI_TOS_AGREED=1

COPY . .

EXPOSE 8010

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]


