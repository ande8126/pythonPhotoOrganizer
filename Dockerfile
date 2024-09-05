FROM python
WORKDIR /pythonPhotoOrganizer
RUN apt-get update && \
    apt-get install -y libmediainfo0v5 &&  \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "main.py"]