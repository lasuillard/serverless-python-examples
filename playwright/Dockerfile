FROM mcr.microsoft.com/playwright/python:v1.41.1-jammy as build-image

ARG FUNCTION_DIR="/function"

WORKDIR "${FUNCTION_DIR}"

RUN pip install --no-cache awslambdaric

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
