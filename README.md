# OpenTelemetry and A2A sample

本リポジトリは『[A2AサーバをOpenTelemetryで計装する](https://zenn.dev/kimitsu/articles/otel-and-a2a)』のサンプルコードです。

```
uv run opentelemetry-instrument --traces_exporter otlp --metrics_exporter None --logs_exporter None --service_name a2a-server uv run server.py
```

```
uv run opentelemetry-instrument --traces_exporter otlp --metrics_exporter None --logs_exporter None --service_name a2a-client uv run client.py
```
