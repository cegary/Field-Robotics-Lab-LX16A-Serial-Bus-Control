**For demo: **

use demo_code.py



**Installs (if not pre-installed):**

pip install pygame

python3.10 -m pip install pylx16a 

sudo apt update && sudo apt upgrade -y

sudo apt install bluetooth bluez bluez-tools blueman python3-pip -y


**Activate bluetooth:**

sudo systemctl start bluetooth

sudo systemctl enable bluetooth



**Put PS5 controller in pairing mode:**

Hold PS (PlayStation) + Create (small button next to touchpad) until the light bar starts flashing.



**Scan:**

Bluetoothctl

scan on

find controller MAC address

pair XX:XX:XX:XX:XX:XX

trust XX:XX:XX:XX:XX:XX

connect XX:XX:XX:XX:XX:XX

exit



**Verify: **
ls /dev/input/



**run:**
python3 demo_code.py

