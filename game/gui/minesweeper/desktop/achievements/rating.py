from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock

from game.gui.api import server_api
from ...common import BasePopup
from ..authentication import Authentication


class LoadingImage(Image):
    pass


class RatingRow(BoxLayout):
    line_number: Label = ObjectProperty()
    username: Label = ObjectProperty()
    score: Label = ObjectProperty()

    line_number_text: str = StringProperty()
    username_text: str = StringProperty()
    score_text: str = StringProperty()

    def __init__(self, line_number: str = '', username: str = '', score: str = '', **kwargs):
        super().__init__(**kwargs)

        self.line_number_text = line_number
        self.username_text = username
        self.score_text = score

    def on_line_number_text(self, _self_instance, line_number: str):
        self.line_number.text = line_number

    def on_username_text(self, _self_instance, username: str):
        self.username.text = username

    def on_score_text(self, _self_instance, score: str):
        self.score.text = score


class ListButton(Button):
    button_color = ListProperty()


class RatingTable(BoxLayout):
    table_header: RatingRow = ObjectProperty()
    table_content: RatingRow = ObjectProperty()
    list_up: ListButton = ObjectProperty()
    list_down: ListButton = ObjectProperty()

    parent_layout: BoxLayout

    def __init__(self, parent_layout: BoxLayout, rate_top: list[dict], rate_count: int, **kwargs):
        super().__init__(**kwargs)
        self.parent_layout = parent_layout

        self.table_header.line_number.text = '#'
        self.table_header.username.text = 'Username'
        self.table_header.username.pos_hint = {'center_x': 0.5}
        self.table_header.score.text = 'Score'

        for row in rate_top:
            self.table_content.add_widget(RatingRow(
                line_number=str(row['line_number']),
                username=row['username'],
                score=str(row['game_score'])
            ))

        self.list_up.disabled = rate_top[0]['line_number'] == 1
        self.list_down.disabled = rate_top[-1]['line_number'] == rate_count

    def up_list(self):
        self.parent_layout.load_content(-1)

    def down_list(self):
        self.parent_layout.load_content(1)


class RatingContainer(BoxLayout):
    container: RelativeLayout = ObjectProperty()

    parent_popup: BasePopup = ObjectProperty()

    limit: int = 10
    offset: int = 0
    rate_top: list[dict] = []
    direction: int = 0

    def on_parent(self, _self_instance, _parent_instance):
        self.load_content(0)  # will keep offset 0

    def load_content(self, direction: int):
        # direction up -> -1
        # direction down -> 1
        self.offset = max(self.offset + self.limit * direction, 0)  # filter negative offset

        Clock.schedule_once(lambda _dt: self.container.add_widget(LoadingImage()))
        server_api.rate_top(limit=self.limit, offset=self.offset, on_success=self.rate_success,
                            on_failure=self.rate_failure)

    def rate_success(self, _req: UrlRequest, rate: dict):
        self.container.clear_widgets()
        self.container.add_widget(RatingTable(self, rate['top'], rate['count']))

    def rate_failure(self, req: UrlRequest, _res: dict):
        if req.resp_status == 401:
            self.parent_popup.dismiss()
            Authentication(self.parent_popup.__class__).open()
            return
