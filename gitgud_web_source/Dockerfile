FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /src/
WORKDIR /src
RUN apt update && apt install -yy mtr dnsutils whois
RUN pip install --upgrade pip && pip install -r requirements.txt

#removed the heavier packages to decrease buildtime tcpdump nmap 