class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # private, but no getters or setters so referencing directly is fine
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

        # The hint video said that unmuting needs to cause the volume to return
        # to the pre-muted volume, so we need to store that information
        # somewhere. I know that we're not supposed to "add any extra methods
        # to the class" but I hope this is fine, because otherwise I don't think
        # I know how to make the stateless mute() method remember something
        self.__mute_vol_memory: int = 0

    def power(self):
        """
        Method to turn Television on and off, where `self.__status = True` is
        considered "on" and `self.__status = False` is considered "off"
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self):
        """
        Method to mute and unmute volume
        """
        if self.__status:
            if self.__muted:
                # UNMUTE
                # TV always starts unmuted so first 0 should never come up
                # Set volume to pre-muted volume then unmute
                self.__volume = self.__mute_vol_memory
                self.__muted = False
            else:
                # MUTE
                # Commit to memory what the current volume is
                self.__mute_vol_memory = self.__volume

                # Then actually mute the volume
                self.__volume = 0
                self.__muted = True

    def channel_up(self):
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase the volume
        """
        if self.__status:
            # Unmute if muted
            if self.__muted:
                self.mute()
            # No wrap-around at max volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
        
    def volume_down(self):
        """
        Method to decrease the volume
        """
        if self.__status:
            # Unmute if muted
            if self.__muted:
                self.mute()
            # No wrap-around at min volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to show the TV status.
        :return: TV status
        """
        # Muted status doesn't matter, values will be correct either way
        return (
            f'Power = {self.__status}, Channel = {self.__channel}, '
            f'Volume = {self.__volume}'
        )

# Channel logic - should wrap around both directions
#####################################################################
# Default   -   NFL    -    Cartoon Network    -    Discovery Channel
#    0           1                 2                     3

# Volume logic - should NOT wrap around
########################
#   0       1      2