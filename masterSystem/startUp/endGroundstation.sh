#A script to kill any ports currently bound to a instance of groundstation.py **** &

sudo kill -q $(pgrep python3)
