FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /src/
WORKDIR /src
RUN apt update && apt install -yy mtr nmap dnsutils whois tcpdump
RUN pip install --upgrade pip && pip install -r requirements.txt

