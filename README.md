	  ________.______________ __________ ________   ______________________ ___  
	 /  _____/|   \_   _____/ \______   \\_____  \  \_____  \__    ___/   |   \ 
	/   \  ___|   ||    __)    |    |  _/ /   |   \  /   |   \|    | /    ~    \
	\    \_\  \   ||     \     |    |   \/    |    \/    |    \    | \    Y    /
	 \______  /___|\___  /     |______  /\_______  /\_______  /____|  \___|_  / 
	        \/         \/             \/         \/         \/              \/  

GIF Booth needs a new name

How to install

1) Git clone onto Raspberry Pi
2) Configure `settings.config`
3) Configure `gitbooth.config` and move to `/boot` partition
4) `sudo cp init.d/GIFBooth.sh /etc/init.d/GIFBooth.sh`
5) `sudo chmod +x /etc/init.d/GIFBooth.sh`
6) `sudo update-rc.d GIFBooth.sh defaults`
7) Reboot!
