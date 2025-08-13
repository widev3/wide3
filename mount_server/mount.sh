# get session_name
sn="$(curl -X GET http://localhost:5000/session/acquire | jq -r '.session_name')"
echo $sn

# set mount location
curl -X POST http://localhost:5000/mount/location \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"lat": 45.3833, "lon": 10.668056, "height": 145}'

# set mount target
curl -X POST http://localhost:5000/mount/target \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"ra":"18h55m","dec":"-26d17m"}'

