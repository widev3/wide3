curl -X POST http://localhost:5000/mount/location \
     -H "Content-Type: application/json" \
     -d '{"lat": 23.43, "lon": 45, "height": -23}'

curl -X POST http://localhost:5000/mount/ \
     -H "Content-Type: application/json" \
     -d '{"target":{"alt":0,"az":0},"offset":{"az":-100}, "behavior":"transit"}'