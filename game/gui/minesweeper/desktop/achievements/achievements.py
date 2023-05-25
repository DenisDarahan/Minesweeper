from kivy.properties import ObjectProperty

from ...common import BasePopup
from .rating import RatingContainer


class Achievements(BasePopup):
    rating_container: RatingContainer = ObjectProperty()
