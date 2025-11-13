FROM python:3.11-slim
WORKDIR /app
COPY sysinfo.py /app/sysinfo.py
RUN pip install --no-cache-dir psutil
ENV INTERVAL=5
CMD ["python","/app/sysinfo.py"]

