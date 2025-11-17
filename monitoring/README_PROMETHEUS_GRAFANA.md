

## Grafana + Prometheus

In this project, Prometheus is used as the main monitoring and metrics collection system. It gathers real-time data from the application and infrastructure components, including CPU usage, memory consumption, network activity, and custom application metrics. Prometheus stores these time-series metrics and provides a powerful query language (PromQL) for analysis.

Grafana is integrated as the visualization layer on top of Prometheus. It connects to the Prometheus data source and displays the collected metrics through interactive dashboards. These dashboards provide clear insights into system performance, service health, and resource utilization. Grafana also enables alerting, helping detect issues early and supporting fast troubleshooting.

Together, Prometheus and Grafana deliver a complete monitoring and observability solution within the DevOps project, helping ensure system stability, performance visibility, and proactive incident detection.