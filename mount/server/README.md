# STANTER: STANdard mounT ServER 

## mount API

### POST /mount/location/
**body**
* `{"lat": lat, "lon": lon, "height": height}`

**example**
```bash
curl -X POST http://localhost:5000/mount/location \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"lat": 17.546, "lon": 15.786, "height": 12}'
```

**responses**
* `{"message": "OK"}`, 200
* `{"error": "Missing required field lat"}`, 400
* `{"error": "Missing required field lon"}`, 400
* `{"error": "Empty body"}`, 400
* `{"error": "Missing required field height"}`, 400
* `{"error": "Already moving"}`, 403

---

### POST /mount/target
**body**
* `{"ra": ra, "dec": dec}`
* `{"az": az, "alt": alt}`

**responses**
* `{"message": "OK", "target": {"ra": ra_value,"dec": dec_value}}`, 200
* `{"error": "Empty body"}`, 400
* `{"error": "Missing required field target.dec"}`, 400
* `{"error": "Missing required field target.ra"}`, 400
* `{"error": "Missing required field target.az"}`, 400
* `{"error": "Missing required field target.alt"}`, 400
* `{"error": "Target should be in ra/dec or alt/az"}`, 400
* `{"error": "Neither ra/dec nor alt/az"}`, 400
* `{"error": "Already moving"}`, 403

**example**
```bash
curl -X POST http://localhost:5000/mount/target \
     -H "Content-Type: application/json" \
     -H "Authorization: $sn" \
     -d '{"az":"181d33m","alt":"11d19m"}'
```

---

### POST /mount/offset
**body**
* `{}`

**responses**
* `{"message": "OK", "offset": {"ra": ra_value,"dec": dec_value}}`, 200
* `{"error": "Empty body"}`, 400
* `{"error": "'absolute', 'relative' or 'timedelta'"}`, 400
* `{"error": "Already moving"}`, 403

---

### GET /mount/run?bh=
**responses**
* `{"message": "OK"}`, 200
* `{"error": "Mount location is not set"}`, 400
* `{"error": "Mount target is not set"}`, 400
* `{"error": "Missing required argument bh"}`, 400
* `{"error": "bh must be 'follow', 'transit' or 'route'"}`, 400
* `{"error": f"Mount offset must be set when bh is {bh}"}`, 400

---

### GET /mount/stop
**responses**
* `{"message": "OK"}`, 200
* `{"error": "Already stopped"}`, 403