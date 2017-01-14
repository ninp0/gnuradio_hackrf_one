#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: AM Radio
# Generated: Sat Jan  7 21:25:24 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="AM Radio")

        ##################################################
        # Variables
        ##################################################
        self.am_center_freq = am_center_freq = 1536e3
        self.samp_rate = samp_rate = 20e6
        self.audio_gain = audio_gain = 3
        self.am_min_freq = am_min_freq = 540e3
        self.am_max_freq = am_max_freq = 1600e3
        self.am_channel_width = am_channel_width = 10e3
        self.am_channel_freq = am_channel_freq = am_center_freq

        ##################################################
        # Blocks
        ##################################################
        self.notebook_main = self.notebook_main = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_main.AddPage(grc_wxgui.Panel(self.notebook_main), "Controls")
        self.Add(self.notebook_main)
        self.notebook_radio = self.notebook_radio = wx.Notebook(self.notebook_main.GetPage(0).GetWin(), style=wx.NB_TOP)
        self.notebook_radio.AddPage(grc_wxgui.Panel(self.notebook_radio), "Spectrum Analysis")
        self.notebook_main.GetPage(0).Add(self.notebook_radio)
        _audio_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain_text_box = forms.text_box(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	label='Volume',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._audio_gain_slider = forms.slider(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.notebook_main.GetPage(0).GridAdd(_audio_gain_sizer, 0, 2, 1, 13)
        _am_channel_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._am_channel_freq_text_box = forms.text_box(
        	parent=self.notebook_radio.GetPage(0).GetWin(),
        	sizer=_am_channel_freq_sizer,
        	value=self.am_channel_freq,
        	callback=self.set_am_channel_freq,
        	label='Station',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._am_channel_freq_slider = forms.slider(
        	parent=self.notebook_radio.GetPage(0).GetWin(),
        	sizer=_am_channel_freq_sizer,
        	value=self.am_channel_freq,
        	callback=self.set_am_channel_freq,
        	minimum=am_min_freq,
        	maximum=am_max_freq,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.notebook_radio.GetPage(0).GridAdd(_am_channel_freq_sizer, 0, 1, 1, 39)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_radio.GetPage(0).GetWin(),
        	baseband_freq=am_channel_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.notebook_radio.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=16,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(am_channel_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (10, ), am_center_freq, samp_rate)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48e3,
        	audio_decim=10,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc3_xx_0 = analog.agc3_cc(1e-1, 1e-2, .7, 1.0, 1)
        self.analog_agc3_xx_0.set_max_gain(65536)
        self.am_low_pass_filter = filter.fir_filter_ccf(int(samp_rate/am_channel_width), firdes.low_pass(
        	1, samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.am_fosphor_wx_sink_c = fosphor.wx_sink_c(
        	self.notebook_main.GetPage(0).GetWin()
        )
        self.am_fosphor_wx_sink_c.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.am_fosphor_wx_sink_c.set_frequency_range(am_channel_freq, samp_rate)
        self.notebook_main.GetPage(0).Add(self.am_fosphor_wx_sink_c.win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.am_low_pass_filter, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.analog_agc3_xx_0, 0), (self.analog_am_demod_cf_0, 0))    
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.am_low_pass_filter, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.am_fosphor_wx_sink_c, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_agc3_xx_0, 0))    

    def get_am_center_freq(self):
        return self.am_center_freq

    def set_am_center_freq(self, am_center_freq):
        self.am_center_freq = am_center_freq
        self.set_am_channel_freq(self.am_center_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.am_center_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.am_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.am_fosphor_wx_sink_c.set_frequency_range(self.am_channel_freq, self.samp_rate)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self._audio_gain_slider.set_value(self.audio_gain)
        self._audio_gain_text_box.set_value(self.audio_gain)
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain, ))

    def get_am_min_freq(self):
        return self.am_min_freq

    def set_am_min_freq(self, am_min_freq):
        self.am_min_freq = am_min_freq

    def get_am_max_freq(self):
        return self.am_max_freq

    def set_am_max_freq(self, am_max_freq):
        self.am_max_freq = am_max_freq

    def get_am_channel_width(self):
        return self.am_channel_width

    def set_am_channel_width(self, am_channel_width):
        self.am_channel_width = am_channel_width

    def get_am_channel_freq(self):
        return self.am_channel_freq

    def set_am_channel_freq(self, am_channel_freq):
        self.am_channel_freq = am_channel_freq
        self._am_channel_freq_slider.set_value(self.am_channel_freq)
        self._am_channel_freq_text_box.set_value(self.am_channel_freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.am_channel_freq)
        self.osmosdr_source_0.set_center_freq(self.am_channel_freq, 0)
        self.am_fosphor_wx_sink_c.set_frequency_range(self.am_channel_freq, self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
