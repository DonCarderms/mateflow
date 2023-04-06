#!/bin/bash

PGADMIN_DEFAULT_EMAIL=gtadmin@domain.com
PGADMIN_DEFAULT_PASSWORD=gtroot

cat > /pgadmin4/servers.json << EOF
{
    "Servers": {
        "1": {
            "Name": "Localhost",
            "Group": "Servers",
            "Host": "seu_host",
            "Port": 8080,
            "MaintenanceDB": "postgres",
            "Username": "gtadmin",
            "SSLMode": "prefer"
        }
    }
}
EOF
