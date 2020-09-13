FROM gcc:9.2.0

RUN apt update; apt install -y python3-pip
RUN pip3 install online-judge-tools
