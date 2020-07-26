FROM python:3.7.8-slim

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY main.py /main.py

ENTRYPOINT python /main.py