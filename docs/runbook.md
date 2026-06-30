# Runbook

I designed this demo for offline review.

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests
python -m trend_wave_demo.cli --sample data_samples/market_snapshot.csv
```

No build step, credential file, or network service is required.

## 中文摘要

本演示只需 Python 标准库即可进行离线检查，不需要构建、不需要密钥、不需要网络服务。
