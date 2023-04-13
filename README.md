# Pystreaming
A python streaming learning material 

## Install Kafka (redpanda) 
```shell
docker compose up -d
brew install redpanda-data/tap/redpanda
rpk cluster info --brokers 127.0.0.1:19092
```