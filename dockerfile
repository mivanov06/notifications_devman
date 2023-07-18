FROM python:3.10-slim
RUN mkdir /usr/src/notifications_devman
WORKDIR /usr/src/notifications_devman
COPY requirements.txt /usr/src/notifications_devman
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "main.py"]