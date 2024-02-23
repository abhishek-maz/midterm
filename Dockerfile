FROM python:3.8-slim

WORKDIR /app

COPY midterm.py .

RUN pip install Flask

EXPOSE 8080
CMD ["python", "midterm.py"]