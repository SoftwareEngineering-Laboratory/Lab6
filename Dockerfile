FROM python:3.8-alpine
WORKDIR /src
COPY requirements.txt .
COPY . .
RUN pip install --proxy=http://proxy.cafebazaar.org:3128 -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]