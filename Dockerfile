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

# expose port for application
EXPOSE 8001

# start fastapi application
CMD ["python", "app/main.py"]
