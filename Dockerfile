FROM python:3.11-slim

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
COPY src/addons/commands/entrypoint.sh /src/addons/commands/entrypoint.sh

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


RUN chmod +x /src/addons/commands/entrypoint.sh

ENTRYPOINT ["/src/addons/commands/entrypoint.sh"]
