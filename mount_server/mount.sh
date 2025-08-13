# Unauthorized
curl -X GET http://localhost:5000/session/acquire \
     -H "Authorization: cf49d44c-06ea-410a-aac8-b21ab8863b87"

# OK
sn="$(curl -X GET http://localhost:5000/session/acquire | jq -r '.session_name')"
echo $sn

curl -X POST http://localhost:5000/mount/location \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"lat": 45.3832643, "lon": 10.6685857, "height": 19}'

# OK
curl -X POST http://localhost:5000/mount/target \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"alt":0,"az":0}'

