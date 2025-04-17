# pull python base image
FROM python:3.10-slim

# specify working directory
WORKDIR /app

# update pip
RUN pip install --upgrade pip

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# start fastapi application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
