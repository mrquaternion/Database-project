
FROM python:3.12-slim
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

