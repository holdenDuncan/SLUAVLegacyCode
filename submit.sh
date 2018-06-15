#Calls the auvsi proxy_mavlink.py to handle telemetry
#submission
#Note: Server, user, and password are all currently hard coded

python interop/auvsi/interop/client/tools/interop_cli.py --url http://192.168.0.153:8000 --user testuser --password testpass odlcs --oflc_dir submit/ &
