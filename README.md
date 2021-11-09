A messaging microservice sample 


## build and run

 - build the image

  $ sudo docker build -t sample_ms .


 - run the container

  $ sudo docker run -p 8000:8000 sample_ms


 - send a message

  $ curl --header "Content-Type: application/json"  --request POST --data '{"sender":"1234","recipient":"1", "message":"Hello"}'  http://localhost:8000/api/messages/


 - receive all recipient messages

  $ curl --header "Content-Type: application/json"  http://localhost:8000/api/messages/1/
