#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Radio
# Generated: Sat Jan  7 21:57:54 2017
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
        grc_wxgui.top_block_gui.__init__(self, title="FM Radio")

        ##################################################
        # Variables
        ##################################################
        self.fm_center_freq = fm_center_freq = 96.3e6
        self.samp_rate = samp_rate = 9e6
        self.fm_min_freq = fm_min_freq = 88.1e6
        self.fm_max_freq = fm_max_freq = 108.1e6
        self.fm_channel_width = fm_channel_width = 200e3
        self.fm_channel_freq = fm_channel_freq = fm_center_freq
        self.fm_audio_gain = fm_audio_gain = 3
        self.fft_size = fft_size = 512

        ##################################################
        # Blocks
        ##################################################
        self.notebook_main = self.notebook_main = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_main.AddPage(grc_wxgui.Panel(self.notebook_main), "Controls")
        self.Add(self.notebook_main)
        self.notebook_radio = self.notebook_radio = wx.Notebook(self.notebook_main.GetPage(0).GetWin(), style=wx.NB_TOP)
        self.notebook_radio.AddPage(grc_wxgui.Panel(self.notebook_radio), "Spectrum Analysis")
        self.notebook_main.GetPage(0).Add(self.notebook_radio)
        _fm_channel_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fm_channel_freq_text_box = forms.text_box(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_fm_channel_freq_sizer,
        	value=self.fm_channel_freq,
        	callback=self.set_fm_channel_freq,
        	label='Station',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fm_channel_freq_slider = forms.slider(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_fm_channel_freq_sizer,
        	value=self.fm_channel_freq,
        	callback=self.set_fm_channel_freq,
        	minimum=fm_min_freq,
        	maximum=fm_max_freq,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.notebook_main.GetPage(0).GridAdd(_fm_channel_freq_sizer, 1, 1, 1, 39)
        _fm_audio_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fm_audio_gain_text_box = forms.text_box(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_fm_audio_gain_sizer,
        	value=self.fm_audio_gain,
        	callback=self.set_fm_audio_gain,
        	label='Volume',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._fm_audio_gain_slider = forms.slider(
        	parent=self.notebook_main.GetPage(0).GetWin(),
        	sizer=_fm_audio_gain_sizer,
        	value=self.fm_audio_gain,
        	callback=self.set_fm_audio_gain,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.notebook_main.GetPage(0).GridAdd(_fm_audio_gain_sizer, 2, 1, 1, 39)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_radio.GetPage(0).GetWin(),
        	baseband_freq=fm_channel_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=fft_size,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='FM Station',
        	peak_hold=True,
        )
        self.notebook_radio.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/fm_channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_wx_sink_c_0 = fosphor.wx_sink_c(
        	self.notebook_radio.GetPage(0).GetWin()
        )
        self.fosphor_wx_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_wx_sink_c_0.set_frequency_range(fm_channel_freq, samp_rate)
        self.notebook_radio.GetPage(0).Add(self.fosphor_wx_sink_c_0.win)
        self.fm_osmosdr_source = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.fm_osmosdr_source.set_sample_rate(samp_rate)
        self.fm_osmosdr_source.set_center_freq(fm_channel_freq, 0)
        self.fm_osmosdr_source.set_freq_corr(0, 0)
        self.fm_osmosdr_source.set_dc_offset_mode(2, 0)
        self.fm_osmosdr_source.set_iq_balance_mode(0, 0)
        self.fm_osmosdr_source.set_gain_mode(False, 0)
        self.fm_osmosdr_source.set_gain(0, 0)
        self.fm_osmosdr_source.set_if_gain(20, 0)
        self.fm_osmosdr_source.set_bb_gain(20, 0)
        self.fm_osmosdr_source.set_antenna('', 0)
        self.fm_osmosdr_source.set_bandwidth(0, 0)
          
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((fm_audio_gain, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fm_center_freq - fm_channel_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.fm_osmosdr_source, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.fm_osmosdr_source, 0), (self.fosphor_wx_sink_c_0, 0))    
        self.connect((self.fm_osmosdr_source, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    

    def get_fm_center_freq(self):
        return self.fm_center_freq

    def set_fm_center_freq(self, fm_center_freq):
        self.fm_center_freq = fm_center_freq
        self.set_fm_channel_freq(self.fm_center_freq)
        self.analog_sig_source_x_0.set_frequency(self.fm_center_freq - self.fm_channel_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_wx_sink_c_0.set_frequency_range(self.fm_channel_freq, self.samp_rate)
        self.fm_osmosdr_source.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_fm_min_freq(self):
        return self.fm_min_freq

    def set_fm_min_freq(self, fm_min_freq):
        self.fm_min_freq = fm_min_freq

    def get_fm_max_freq(self):
        return self.fm_max_freq

    def set_fm_max_freq(self, fm_max_freq):
        self.fm_max_freq = fm_max_freq

    def get_fm_channel_width(self):
        return self.fm_channel_width

    def set_fm_channel_width(self, fm_channel_width):
        self.fm_channel_width = fm_channel_width

    def get_fm_channel_freq(self):
        return self.fm_channel_freq

    def set_fm_channel_freq(self, fm_channel_freq):
        self.fm_channel_freq = fm_channel_freq
        self._fm_channel_freq_slider.set_value(self.fm_channel_freq)
        self._fm_channel_freq_text_box.set_value(self.fm_channel_freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.fm_channel_freq)
        self.fosphor_wx_sink_c_0.set_frequency_range(self.fm_channel_freq, self.samp_rate)
        self.fm_osmosdr_source.set_center_freq(self.fm_channel_freq, 0)
        self.analog_sig_source_x_0.set_frequency(self.fm_center_freq - self.fm_channel_freq)

    def get_fm_audio_gain(self):
        return self.fm_audio_gain

    def set_fm_audio_gain(self, fm_audio_gain):
        self.fm_audio_gain = fm_audio_gain
        self._fm_audio_gain_slider.set_value(self.fm_audio_gain)
        self._fm_audio_gain_text_box.set_value(self.fm_audio_gain)
        self.blocks_multiply_const_vxx_0.set_k((self.fm_audio_gain, ))

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
