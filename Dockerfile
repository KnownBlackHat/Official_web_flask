FROM ubuntu:22.04
RUN apt update -y && apt install python3.11 python3-pip -y
WORKDIR /root
COPY . .
RUN python3.11 -m pip install -r requirements.txt
ENTRYPOINT ["python3.11"]
CMD ["webserver.py"]
