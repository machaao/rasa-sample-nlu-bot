FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

ADD ./actions /app/actions/
ADD ./data /app/data/
ADD ./models /app/models/
ADD ./start.sh /app/start.sh
ADD ./domain.yml /app/
ADD ./config.yml /app/
ADD ./credentials.yml /app/
ADD ./connectors/MachaaoConnector.py /app/connectors/MachaaoConnector.py

RUN chmod +x /app/start.sh

ENTRYPOINT []
CMD /app/start.sh