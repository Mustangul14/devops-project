FROM ubuntu:22.04
WORKDIR /app
COPY sysinfo.sh /app/sysinfo.sh
RUN apt-get update && apt-get install -y procps net-tools iproute2 && chmod +x /app/sysinfo.sh
ENV INTERVAL=5
CMD ["/app/sysinfo.sh"]

