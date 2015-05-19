# Professional diseases database | База данных профессиональных заболеваний
## Deployment | Развертывание
docker build -t diseases .
docker run -d -p 80:80 diseases
