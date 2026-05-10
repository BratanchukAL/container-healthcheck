FROM python:3.10-slim


# prepare to install
# ===================================================
RUN apt update && apt install curl -y \
     && apt-get clean
     && rm -rf /var/lib/apt/lists/*


#
# ===================================================
WORKDIR /app/

COPY ./requirements.txt ./
COPY ./deployments/prod/backend_base/requirements.deploy.txt ./


# install python requirements
# ===================================================
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.deploy.txt


# copy SRC
# ===================================================
COPY ./src/ ./
