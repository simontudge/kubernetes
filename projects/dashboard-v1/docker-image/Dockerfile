FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8050

CMD ["python", "map.py"]
