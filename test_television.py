import pytest
from television import *

class Test:
    def setup_method(self):
        self.tvl = Television()

    def teardown_method(self):
        del self.tvl

    def test_init(self):
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tvl.power()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'

        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        # Shouldn't be able to change channels when power is off
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Confirm channel_up() increases channel when power is on
        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # Confirm ability to wrap around channels by going past channel 3
        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # Shouldn't be able to change channels when power is off
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Confirm channel_down() decreases channel when power is on
        self.tvl.power()
        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # Confirm ability to wrap around channels by going past channel 0
        self.tvl.channel_down()
        self.tvl.channel_down()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 2, Volume = 0'

    def test_volume_up(self):
        # Shouldn't be able to change volume when power is off
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Confirm volume_up() increases volume when power is on
        self.tvl.power()
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # Confirm volume_up() unmutes and continues increasing volume
        self.tvl.mute()
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'

        # Shouldn't be able to wrap around volume
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # Shouldn't be able to change volume when power is off
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Confirm volume_down() decreases volume when power is on
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # Confirm volume_down() unmutes and continues decreasing volume
        self.tvl.mute()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Shouldn't be able to wrap around volume
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'
