FULL_NAME="Eight Thermocouples DAQ"
LINK="https://sequentmicrosystems.com/products/eight-thermocouples-daq-8-layer-stackable-hat-for-raspberry-pi"

import sm_tc
API = sm_tc.SMtc(0)
DOMAIN = "SMtc"
NAME_PREFIX = "smtc"
SM_MAP = {
    #"button": {
    #    "contact_cnt_rst": {
    #        "chan_no": 4,
    #        "com": {
    #            "set": "rstContactCounter",
    #        },
    #    }
    #},
    "select": {
        "type": {
            "chan_no": 8,
            "com": {
                "get": "get_sensor_type",
                "set": "set_sensor_type",
            },
            "option_map": {
                "B": 0,
                "E": 1,
                "J": 2,
                "K": 3,
                "N": 4,
                "R": 5,
                "S": 6,
                "T": 7,
            }
        },
    },
    "sensor":  {
        "temp": {
                "chan_no": 8,
                "uom": "°C",
                "com": {
                    "get": "get_temp",
                },
        },
    },
}
