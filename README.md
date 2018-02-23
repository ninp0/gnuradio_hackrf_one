OSX:
Install MacPorts
Set default python to be MacPorts python 2.7
test that 'import gnuradio' works from python console
sudo port install gnuradio +full
sudo port install hackrf
hackrf_info (make sure this command returns a detected hackrf one)
sudo port install gr-osmosdr +full
sudo port install gr-fosphor

FM Radio:
![fm_radio](https://github.com/ninp0/gnu_radio_hackrf_one/blob/master/screenshots/fm_radio.png)
