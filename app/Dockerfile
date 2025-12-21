FROM python:3.13

LABEL authors="Evgeny"

RUN pip install requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]