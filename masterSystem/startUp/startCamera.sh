#A script to go into the auzsi_communications folder
#and start the camera

#sudo ../auvsi_communications/camera/camera.sh $1
#Open the port to recieve pictures
#sudo python3 ../auvsi_communications/camera/groundstation.py 1000 &
#sleep 2
#Tell the pi to take photos
sudo sshpass -p "auvsirpi" ssh -o "StrictHostKeyChecking=no" pi@raspberrypi -- "cd ~/auvsi_communications/camera && python3 rpi.py 1000"
