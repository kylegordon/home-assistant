"""
Simple pollen sensor that reports on the current pollen level in the UK.
Does not work outside the UK. PRs happily accepted!
"""
from homeassistant.const import ATTR_LATITUDE, ATTR_LONGITUDE
from homeassistant.helpers.entity import Entity

REQUIREMENTS = ['pypollen==0.1.3']

# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Pollen sensor."""

    if None in (hass.config.latitude, hass.config.longitude):
        _LOGGER.error("Latitude or longitude not set in Home Assistant config")
        return False

    add_devices([PollenSensor(hass)], True)


class PollenSensor(Entity):
    """Representation of a Pollen sensor."""

    def __init__(self, hass):
        """Initialize the sensor."""

        from pypollen import Pollen
        #self._state = Pollen(51.7546407,-1.2510746).pollencount
        self._state = Pollen(hass.config.latitude, hass.config.longitude)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Pollen Level"

    @property
    def state(self):
        """Return the state of the sensor."""

        return self._state.pollencount
