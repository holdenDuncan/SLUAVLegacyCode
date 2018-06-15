sudo python3 ~/interop/SLUAVProgramming/auvsi_communications/camera/groundstation.py 1000 &
groundPID=$!
./startCam.sh
./startWatching.sh
./beginTelemetry.sh &
EXIT=1
trap EXIT=0 SIGINT #sets up ^c to exit cleanly
while :
do
    echo "Use Ctrl C to exit"
    sleep 10
    if [ $EXIT -eq 0 ]
    then
    break
    fi
done
./stopWatching.sh
sudo kill $groundPID
