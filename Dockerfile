FROM nginx:latest
COPY dist/  /usr/share/nginx/html/
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y --fix-missing python3 python3-pip python3.11-venv 
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip3 install flask pymysql flask_cors cryptography
COPY backend/ /usr/share/nginx/
# CMD ["python3", "/usr/share/nginx/app.py"]