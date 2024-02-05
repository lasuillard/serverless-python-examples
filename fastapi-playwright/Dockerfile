FROM mcr.microsoft.com/playwright/python:v1.41.1-jammy

ARG FUNCTION_DIR="/function"

WORKDIR "${FUNCTION_DIR}"

RUN pip install --no-cache-dir awslambdaric

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
