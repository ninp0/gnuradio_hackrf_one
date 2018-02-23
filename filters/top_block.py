#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Feb 22 17:15:51 2018
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6
        self.transition = transition = samp_rate/8
        self.tap2 = tap2 = 1
        self.tap1 = tap1 = 1
        self.tap0 = tap0 = 1
        self.cutoff = cutoff = samp_rate/8

        ##################################################
        # Blocks
        ##################################################
        _tap2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap2_sizer,
        	value=self.tap2,
        	callback=self.set_tap2,
        	label='tap2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap2_sizer,
        	value=self.tap2,
        	callback=self.set_tap2,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap2_sizer)
        _tap1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap1_sizer,
        	value=self.tap1,
        	callback=self.set_tap1,
        	label='tap1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap1_sizer,
        	value=self.tap1,
        	callback=self.set_tap1,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap1_sizer)
        _tap0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap0_sizer,
        	value=self.tap0,
        	callback=self.set_tap0,
        	label='tap0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap0_sizer,
        	value=self.tap0,
        	callback=self.set_tap0,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap0_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _transition_sizer = wx.BoxSizer(wx.VERTICAL)
        self._transition_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_transition_sizer,
        	value=self.transition,
        	callback=self.set_transition,
        	label='transition',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._transition_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_transition_sizer,
        	value=self.transition,
        	callback=self.set_transition,
        	minimum=samp_rate/1000,
        	maximum=samp_rate/2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_transition_sizer)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, ((tap0,tap1,tap2)))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        _cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	label='cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	minimum=samp_rate/1000,
        	maximum=samp_rate/2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cutoff_sizer)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((tap2, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((tap1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((tap0, ))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.wxgui_scopesink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.set_transition(self.samp_rate/8)
        self.set_cutoff(self.samp_rate/8)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self._transition_slider.set_value(self.transition)
        self._transition_text_box.set_value(self.transition)

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self._tap2_slider.set_value(self.tap2)
        self._tap2_text_box.set_value(self.tap2)
        self.fir_filter_xxx_0.set_taps(((self.tap0,self.tap1,self.tap2)))
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.tap2, ))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self._tap1_slider.set_value(self.tap1)
        self._tap1_text_box.set_value(self.tap1)
        self.fir_filter_xxx_0.set_taps(((self.tap0,self.tap1,self.tap2)))
        self.blocks_multiply_const_vxx_0_0.set_k((self.tap1, ))

    def get_tap0(self):
        return self.tap0

    def set_tap0(self, tap0):
        self.tap0 = tap0
        self._tap0_slider.set_value(self.tap0)
        self._tap0_text_box.set_value(self.tap0)
        self.fir_filter_xxx_0.set_taps(((self.tap0,self.tap1,self.tap2)))
        self.blocks_multiply_const_vxx_0.set_k((self.tap0, ))

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self._cutoff_slider.set_value(self.cutoff)
        self._cutoff_text_box.set_value(self.cutoff)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
