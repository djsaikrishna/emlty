FROM python:3.10
WORKDIR /app
COPY . .
COPY requirements.txt reuqirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
