from pylab import *


class Orbit:
    DURATION = 98.8 * 60


class Charts:

    @classmethod
    def enter_idle_state(self, output_file='enteridlestate.pdf'):
        clf()
        figure(figsize=(7, 3.5))
        rcParams['font.family'] = 'serif'
        duration_seconds = linspace(1, 255, 255)

        plot(duration_seconds,
             CommTransmitter.idle_state_energy(duration_seconds) * 1000.0,
             'r', label="Idle state energy")

        grid(True)
        title("Idle state duration vs consumed energy")
        xlabel("Idle state duration [seconds]")
        ylabel("Consumed energy [mWh]")
        ylim(0, 250)
        xlim(1, 255)
        fill_between(duration_seconds, 100, 250, facecolor='red', alpha=0.2)
        text(60, 175, "DANGER ZONE!", color='red')

        savefig(output_file, bbox_inches="tight")

    @classmethod
    def set_periodic_message(self,
                             message_length,
                             bitrate,
                             output_file='periodicmessage.pdf'):
        clf()
        figure(figsize=(7, 3.5))
        rcParams['font.family'] = 'serif'
        interval_minutes = linspace(1, 15, 60)

        colors = ['r', 'g', 'b', 'm', 'c', 'k']
        for repeat_count in reversed(range(1, 7)):
            plot(interval_minutes,
                 CommTransmitter.periodic_mean_power(message_length,
                                                     interval_minutes,
                                                     bitrate,
                                                     repeat_count) * 1000.0,
                 colors[repeat_count - 1],
                 label="repeat_count=" + str(repeat_count))
        hold(True)
        grid(True)
        title("Mean power consumption of transmitter for PeriodicMessage")
        xlabel("Interval [minutes]")
        ylabel("Mean power [mW]")
        ylim(0, 550)
        xlim(1, 15)
        fill_between(interval_minutes, 100, 550, facecolor='red', alpha=0.2)
        text(4, 250, "DANGER ZONE!", color='red')
        legend(bbox_to_anchor=(1, 0.25), loc=4)

        savefig(output_file, bbox_inches="tight")


class Check:

    @classmethod
    def in_range(self, value, low, high):
        try:
            len(value)

            output_values = []
            for index in range(0, len(value)):
                output_values.append(self.in_range(value[index], low, high))
            return output_values
        except TypeError:
            pass

        if value >= low and value <= high:
            return True
        return False


class CommTransmitter:
    TX_PREAMBLE_TIME = 0.5
    TX_PEAK_PWR = 3.0

    def __init__(self):
        pass

    @classmethod
    def total_tx_time(self, message_length, bitrate):
        return ((message_length * 8) / bitrate) + self.TX_PREAMBLE_TIME

    @classmethod
    def periodic_mean_power(self,
                            message_length,
                            interval_minutes,
                            bitrate=1200,
                            repeat_count=1):
        if not Check.in_range(value=interval_minutes, low=1, high=255):
            raise ValueError('Interval in minutes out of range')

        tx_time = self.total_tx_time(message_length, bitrate) * repeat_count
        return (tx_time / (interval_minutes * 60.0)) * self.TX_PEAK_PWR

    @classmethod
    def idle_state_energy(self, duration):
        return (duration / 3600.0) * self.TX_PEAK_PWR


class CommReceiver:
    RX_MEAN_POWER = 0.51

    def __init__(self):
        pass

    @classmethod
    def mean_power_consumption(self):
        return self.RX_MEAN_POWER

    @classmethod
    def energy_consumption_per_orbit(self):
        return (Orbit.DURATION / 3600.0) * self.RX_MEAN_POWER
