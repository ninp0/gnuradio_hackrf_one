OSX:
Install MacPorts: https://guide.macports.org/chunked/installing.html

Install the Rest:
```
$ sudo port install python27
$ sudo port install wxgtk-2.8
$ sudo port select --set python python27
$ sudo port select --set python2 python27
$ sudo port uninstall gnuradio && sudo port install gnuradio +ctrlport +docs +grc +jack +performance +counters +portaudio +qtgui +sdl +swig +uhd +wavelet +wxgui +zeromq
sudo port install hackrf
hackrf_info (make sure this command returns a detected hackrf one)
sudo port install gr-osmosdr +airspy +bladeRF +docs +fcdproplus +hackrf +rtlsdr +sdrplay +soapysdr +swig +uhd
sudo port install gr-fosphor
```

test that 'import gnuradio' works from python console
```
$ which python
/opt/local/bin/python

$ python
Python 2.7.14 (default, Sep 27 2017, 12:15:00)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import gnuradio
>>>
```

FM Radio:
![fm_radio](https://github.com/ninp0/gnuradio_hackrf_one/blob/master/screenshots/fm_radio.png)
