from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class ColoredBox(BoxLayout):
    def __init__(self, bg_color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*bg_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class CoupeMondeApp(App):
    def build(self):
        # Container lehibe
        root = BoxLayout(orientation='vertical')
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=80)
        header.add_widget(Label(text="COUPE DU MONDE 2026", font_size='22sp', bold=True, color=(0, 1, 1, 1)))
        header.add_widget(Label(text="By Franco", font_size='14sp', italic=True))
        root.add_widget(header)
        
        # Tabs
        tp = TabbedPanel(do_default_tab=False)
        
        # TAB GROUPS
        th_groups = TabbedPanelItem(text='Groups')
        scroll1 = ScrollView()
        group_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        group_layout.bind(minimum_height=group_layout.setter('height'))
        
        data_groups = [
            ("Grp", "Ekipa 1", "Ekipa 2", "Ekipa 3", "Ekipa 4"),
            ("A", "Mexico", "South Africa", "Korea Rep.", "Winner D"),
            ("B", "Canada", "Winner A", "Qatar", "Switzerland"),
            ("C", "Brazil", "Morocco", "Haiti", "Scotland"),
            ("D", "USA", "Paraguay", "Australia", "Winner C"),
            ("E", "Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"),
            ("F", "Netherlands", "Japan", "Winner B", "Tunisia"),
            ("G", "Belgium", "Egypt", "IR Iran", "New Zealand"),
            ("H", "Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"),
            ("I", "France", "Senegal", "Winner 2", "Norway"),
            ("J", "Argentina", "Algeria", "Austria", "Jordan"),
            ("K", "Portugal", "Winner 1", "Uzbekistan", "Colombia"),
            ("L", "England", "Croatia", "Ghana", "Panama")
        ]
        for i, row in enumerate(data_groups):
            bg = (0.2, 0.4, 0.7, 1) if i == 0 else ((0.9, 0.9, 0.9, 1) if i % 2 != 0 else (0.8, 0.8, 0.8, 1))
            box = ColoredBox(bg_color=bg, orientation='horizontal', size_hint_y=None, height=35)
            for item in row:
                box.add_widget(Label(text=item, font_size='9sp', color=(0,0,0,1)))
            group_layout.add_widget(box)
        scroll1.add_widget(group_layout)
        th_groups.add_widget(scroll1)
        tp.add_widget(th_groups)
        
        # TAB CALENDRIER
        th_cal = TabbedPanelItem(text='Calendrier')
        scroll2 = ScrollView()
        cal_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        cal_layout.bind(minimum_height=cal_layout.setter('height'))
        
        cal_data = [
            ("11-Jun", "Mexico vs South Africa", "21:00"), ("12-Jun", "Korea vs Czech", "04:00"), ("12-Jun", "Canada vs Bosnia", "21:00"),
            ("13-Jun", "USA vs Paraguay", "03:00"), ("13-Jun", "Qatar vs Switzerland", "21:00"), ("13-Jun", "Brazil vs Morocco", "24:00"),
            ("14-Jun", "Haiti vs Scotland", "03:00"), ("14-Jun", "Australia vs Turkey", "06:00"), ("14-Jun", "Germany vs Curaçao", "19:00"),
            ("14-Jun", "Netherlands vs Japan", "22:00"), ("15-Jun", "Ivory Coast vs Ecuador", "01:00"), ("15-Jun", "Sweden vs Tunisia", "04:00"),
            ("15-Jun", "Spain vs Cabo Verde", "18:00"), ("15-Jun", "Belgium vs Egypt", "21:00"), ("15-Jun", "Saudi Arabia vs Uruguay", "24:00"),
            ("16-Jun", "Iran vs New Zealand", "03:00"), ("16-Jun", "France vs Senegal", "21:00"), ("16-Jun", "Iraq vs Norway", "24:00"),
            ("17-Jun", "Argentina vs Algeria", "03:00"), ("17-Jun", "Austria vs Jordan", "06:00"), ("17-Jun", "Portugal vs Congo DR", "19:00"),
            ("17-Jun", "England vs Croatia", "22:00"), ("18-Jun", "Ghana vs Panama", "01:00"), ("18-Jun", "Uzbekistan vs Colombia", "04:00"),
            ("18-Jun", "Czech vs South Africa", "18:00"), ("18-Jun", "Switzerland vs Bosnia", "21:00"), ("18-Jun", "Canada vs Qatar", "24:00"),
            ("19-Jun", "Mexico vs Korea", "03:00"), ("19-Jun", "USA vs Australia", "21:00"), ("19-Jun", "Scotland vs Morocco", "24:00"),
            ("20-Jun", "Brazil vs Haiti", "02:30"), ("20-Jun", "Turkey vs Paraguay", "05:00"), ("20-Jun", "Netherlands vs Sweden", "19:00"),
            ("20-Jun", "Germany vs Ivory Coast", "22:00"), ("21-Jun", "Ecuador vs Curaçao", "02:00"), ("21-Jun", "Tunisia vs Japan", "06:00"),
            ("21-Jun", "Spain vs Saudi Arabia", "18:00"), ("21-Jun", "Belgium vs Iran", "21:00"), ("21-Jun", "Uruguay vs Cabo Verde", "24:00"),
            ("22-Jun", "New Zealand vs Egypt", "03:00"), ("22-Jun", "Argentina vs Austria", "19:00"), ("22-Jun", "France vs Iraq", "23:00"),
            ("23-Jun", "Norway vs Senegal", "02:00"), ("23-Jun", "Jordan vs Algeria", "05:00"), ("23-Jun", "Portugal vs Uzbekistan", "19:00"),
            ("23-Jun", "England vs Ghana", "22:00"), ("24-Jun", "Panama vs Croatia", "01:00"), ("24-Jun", "Colombia vs Congo DR", "04:00"),
            ("24-Jun", "Switzerland vs Canada", "21:00"), ("24-Jun", "Bosnia vs Qatar", "21:00"), ("24-Jun", "Scotland vs Brazil", "24:00"),
            ("24-Jun", "Morocco vs Haiti", "24:00"), ("25-Jun", "South Africa vs Korea", "03:00"), ("25-Jun", "Czech vs Mexico", "03:00"),
            ("25-Jun", "Ecuador vs Germany", "22:00"), ("25-Jun", "Curaçao vs Ivory Coast", "22:00"), ("26-Jun", "Tunisia vs Netherlands", "01:00"),
            ("26-Jun", "Japan vs Sweden", "01:00"), ("26-Jun", "Paraguay vs Australia", "04:00"), ("26-Jun", "Turkey vs USA", "04:00"),
            ("26-Jun", "Norway vs France", "21:00"), ("26-Jun", "Senegal vs Iraq", "21:00"), ("27-Jun", "Uruguay vs Spain", "02:00"),
            ("27-Jun", "Cabo Verde vs Saudi Arabia", "02:00"), ("27-Jun", "New Zealand vs Belgium", "05:00"), ("27-Jun", "Egypt vs Iran", "05:00"),
            ("27-Jun", "Panama vs England", "23:00"), ("27-Jun", "Croatia vs Ghana", "23:00"), ("28-Jun", "Colombia vs Portugal", "01:30"),
            ("28-Jun", "Congo DR vs Uzbekistan", "01:30"), ("28-Jun", "Algeria vs Austria", "04:00"), ("28-Jun", "Jordan vs Argentina", "04:00")
        ]
        
        current_date, toggle = "", True
        for d, l, o in cal_data:
            if d != current_date:
                current_date = d
                toggle = not toggle
            bg = (0.9, 0.8, 0.3, 1) if toggle else (0.7, 0.7, 0.7, 1)
            box = ColoredBox(bg_color=bg, orientation='horizontal', size_hint_y=None, height=45)
            for item in [d, l, o]:
                box.add_widget(Label(text=item, font_size='10sp', color=(0,0,0,1)))
            cal_layout.add_widget(box)
            
        scroll2.add_widget(cal_layout)
        th_cal.add_widget(scroll2)
        tp.add_widget(th_cal)
        
        root.add_widget(tp)
        return root

if __name__ == '__main__':
    CoupeMondeApp().run()
