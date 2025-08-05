curl -X POST http://localhost:5000/mount \
     -H "Content-Type: application/json" \
     -d '{"target":{"alt":0,"az":0},"offset":{"az":100}, "behavior":"transit"}'