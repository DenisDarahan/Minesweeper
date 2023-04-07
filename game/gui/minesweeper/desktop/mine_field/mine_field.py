from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.properties import ObjectProperty


class MineField(RecycleView):
    mine_field: RecycleGridLayout = ObjectProperty()

    parent_layout: BoxLayout

    def __init__(self, parent_layout: BoxLayout, width: int, height: int, data: list, **kwargs):
        self.parent_layout = parent_layout
        super().__init__(**kwargs)

        self.data = data
        self.mine_field.cols = width
        self.mine_field.rows = height
