# get session_name
sn="$(curl -X GET http://localhost:5000/session/acquire | jq -r '.session_name')"
echo $sn

# set mount location
curl -X POST http://localhost:5000/mount/location \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"lat": 45.3833, "lon": 10.668056, "height": 145}'

# set mount target by ra/dec
curl -X POST http://localhost:5000/mount/target \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"ra":"8h8m6s","dec":"-14d39m13s"}'

# set mount target by alt/az
curl -X POST http://localhost:5000/mount/target \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"alt":"21d37m","az":"141d54m"}'

# set mount offset
curl -X POST http://localhost:5000/mount/offset \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"timedelta": 60}'

# run the mount
curl -X GET http://localhost:5000/mount/run?bh=route \
     -H "Authorization: $sn"

# release session
curl -X GET http://localhost:5000/session/release \
     -H "Authorization: $sn"