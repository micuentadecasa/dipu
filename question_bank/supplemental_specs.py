"""Ten new source-backed question specifications for each syllabus topic."""

from .supplemental_specs_01_10 import TOPIC_SPECS as _TOPICS_01_10
from .supplemental_specs_11_20 import TOPIC_SPECS as _TOPICS_11_20
from .supplemental_specs_21_30 import TOPIC_SPECS as _TOPICS_21_30
from .supplemental_specs_31_40 import TOPIC_SPECS as _TOPICS_31_40

TOPIC_SPECS = {
    **_TOPICS_01_10,
    **_TOPICS_11_20,
    **_TOPICS_21_30,
    **_TOPICS_31_40,
}
