default_zone_db = "db.esi.dz"
default_name = "cdn.esi.dz."
nameserver = "213.179.173.3"
zones = {
    "alger": "213.179.173.10",
    "oran": "213.179.173.14",
    "constantine": "213.179.173.18",
    "laghouat": "213.179.173.22",
    "adrar": "213.179.173.26",
}
template = """ 
; esi.dz
$TTL    604800

$ORIGIN {}
@       IN      SOA  ns1.esi.dz. esi.dz. (
                              2         ; serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@	IN       NS  ns1.esi.dz.

ns1 IN       A   {}

@   IN  A  {}
"""

for zone, ipv4 in sorted(zones.items()):
    with open("./{}.{}".format(default_zone_db, zone), "w+") as f:
        f.write(template.format(default_name, nameserver, ipv4))
