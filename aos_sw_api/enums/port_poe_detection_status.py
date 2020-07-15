from enum import Enum


class PortPoeDetectionStatusEnum(str, Enum):
    PPDS_DISABLE = "PPDS_DISABLE"
    PPDS_SEARCHING = "PPDS_SEARCHING"
    PPDS_DELIVERING = "PPDS_DELIVERING"
    PPDS_FAULT = "PPDS_FAULT"
    PPDS_TEST = "PPDS_TEST"
    PPDS_OTHER_FAULT = "PPDS_OTHER_FAULT"
