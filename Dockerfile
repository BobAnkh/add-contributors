FROM python:3.9.1-slim

COPY main.py entrypoint.sh requirements.txt /
RUN chmod +x /entrypoint.sh
RUN chmod +x /main.py
ENTRYPOINT ["/entrypoint.sh"]
