FROM python:3.8.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV MONGO_URI="mongodb url"
ENV FRONTEND_URL="http://localhost:3000"
ENV ANALYTICS_API_KEY="https://www.apianalytics.dev/"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

