FROM python:3.8

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 80 

#STREAMLIT CONFIG
RUN mkdir ~/.streamlit

RUN cp config.toml ~/.streamlit/config.toml 

RUN cp credentials.toml ~/.streamlit/credentials.toml 

#ENTRYPOINTS
ENTRYPOINT [ "streamlit", "run" ]

CMD ["app.py"]