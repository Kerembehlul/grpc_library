# gRPC Library System

Bu proje, bir üniversite çevrim içi kütüphane sistemi için gRPC tabanlı API ve istemci-sunucu uygulamalarını içermektedir.  
Protocol Buffers (Protobuf) ile tanımlanan API, Python ile yazılmış sunucu ve istemci uygulamaları ile test edilmiştir.

---

## İçerik

- `.proto` dosyası: `university.proto`  
- Sunucu uygulaması: `server/server.py`  
- İstemci uygulaması: `client/client.py`  
- gRPC stub dosyaları: `generated/` (GitHub'a dahil edilmemiştir)  
- Test komutları ve çıktıların yer aldığı dosya: `grpcurl-tests.md`  
- Teslim raporu: `DELIVERY.md`

---

## Kullanılan Teknolojiler

- Python 3.x  
- gRPC ve Protocol Buffers  
- grpcio, grpcio-tools, grpcio-reflection Python paketleri  

---

## Kurulum ve Çalıştırma

1. Gerekli Python paketlerini yükleyin:

```bash
pip install grpcio grpcio-tools grpcio-reflection
```
.proto dosyasından Python stub dosyalarını oluşturun:
```bash
python -m grpc_tools.protoc -I. --python_out=./generated --grpc_python_out=./generated university.proto
```

Sunucuyu çalıştırın:
```bash
PYTHONPATH=. python server/server.py
```

Başka bir terminalde istemciyi çalıştırın:
```bash
PYTHONPATH=. python client/client.py
```
