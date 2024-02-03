FROM python:3.12-bookworm

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    # Deps for google-chrome-stable
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libcurl4 \
    libdbus-1-3 \
    libdrm2 \
    libexpat1 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libu2f-udev \
    libvulkan1 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    wget \
    xdg-utils \
    && apt-get clean

# Get Google Chorme (chrome-for-testing)
# https://googlechromelabs.github.io/chrome-for-testing/
ARG CHROME_VERSION="121.0.6167.85"
RUN curl --location --output /tmp/google-chrome.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROME_VERSION}/linux64/chrome-linux64.zip" \
    && unzip -j /tmp/google-chrome.zip -d /opt/google-chrome/ \
    && ln -s /opt/google-chrome/chrome /usr/bin/google-chrome \
    && rm -rf /tmp/*

# Get ChromeDriver
# https://googlechromelabs.github.io/chrome-for-testing/
ARG CHROMEDRIVER_VERSION="121.0.6167.85"
RUN curl --location --output /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip -j /tmp/chromedriver.zip -d /opt/chromedriver/ \
    && ln -s /opt/chromedriver/chromedriver /usr/bin/chromedriver \
    && rm -rf /tmp/*

ARG FUNCTION_DIR="/function"
WORKDIR "${FUNCTION_DIR}"

RUN pip install --no-cache awslambdaric

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["main.handler"]
