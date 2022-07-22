FROM ubuntu:18.04
MAINTAINER Darren Yau

COPY requirements.txt ./

RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
#RUN pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple


RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ADD ./actions /app/actions/
ADD ./data /app/data/
ADD ./models /app/models/
ADD ./config /app/config/
ADD ./connectors /app/connectors
ADD ./start.sh /app/start.sh
ADD ./domain.yml /app/
ADD ./config.yml /app/

RUN chmod +x /app/start.sh

ENTRYPOINT []
CMD /app/start.sh