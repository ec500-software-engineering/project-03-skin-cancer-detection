from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from googlemapEx import get_position, get_nearby_results, get_place_details, get_photo_html, get_phone_number, get_rating
import webbrowser
import os
import aiModule
import videoModule

marker_list = []
learn_link_list = ["https://www.youtube.com/watch?v=AmU1zMuBwJY"
                   ,"https://www.youtube.com/watch?v=wNpfo5DzHnE"
                   ,"https://www.youtube.com/watch?v=c3znU3_96P4"
                   ,"https://www.youtube.com/watch?v=lLCgur8bsyA"
                   ,"https://www.youtube.com/watch?v=wVg2KKeLj28"
                   ,"https://www.youtube.com/watch?v=CEZYXcrvvAA"
                   ,"https://www.youtube.com/watch?v=ODKAWmgKWPM"]

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class LearnDialog(FloatLayout):
    learn = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MapViewDialog(FloatLayout):
    find = ObjectProperty(None)
    cancel = ObjectProperty(None)
    mapview = ObjectProperty()
    address = ObjectProperty()
    # mapview = MapView(zoom=11, lat=50.6394, lon=3.057)

class AboutUsDialog(FloatLayout):
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.detect, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_learn(self):
        content = LearnDialog(learn=self.learn, cancel=self.dismiss_popup)
        self._popup = Popup(title="Learn", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_us(self):
        content = AboutUsDialog(cancel=self.dismiss_popup)
        self._popup = Popup(title="Credits", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def detect(self, path, filename, ):
        try: 
            output = aiModule.test(os.path.join(path, filename[0]))       
            result = "Type: " + output[0] + "\nPossibility: " + str(output[1])
            recommandation = "\nRecommandation: " + videoModule.processResult(output)
            self.text_input.text = result + recommandation
            self.dismiss_popup()
        except IndexError:
            print("please select FILE")

    def learn(self, num):
        webbrowser.open(learn_link_list[num])
        print(num)

    def show_map(self):
        content = MapViewDialog(find=self.find, cancel=self.dismiss_popup)
        self._popup = Popup(title="Map", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def find(self, address, mapview, marker):
        print(address.text)
        rm_all_markers(mapview)
        try:
            position = get_position(address.text)
            
            mapview.center_on(position[0], position[1])
            mark(position, mapview, marker)
            mapview.zoom = 16
            for result in get_nearby_results(position, 5000, "Dermatologist"):
                position = get_position(result)
                mark(position, mapview, marker, result)
        except IndexError:
            address.text = "Please enter a valid position"
    
class SkinDetectionApp(App):
    def build(self):
        return Root()


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('LearnDialog', cls=LearnDialog)
Factory.register('MapViewDialog', cls=MapViewDialog)
Factory.register('AboutUsDialog', cls=AboutUsDialog)

def mark(position, mapview, marker, result = []):
    LAT, LON = position
    if not result:
        # m = marker(lat = LAT, lon = LON, source = "Map-Marker-PNG-Pic_3_1.png")
        bubble = Bubble(orientation = "horizontal", padding = 5)
        text = "[b]Self[/b]"
        label = Label(text = text, markup = True, halign = "center")
        bubble.add_widget(label)
        m = MapMarkerPopup(lat=LAT,lon=LON,popup_size = (100, 50),source = "Map-Marker-PNG-Pic_3_1.png")
        m.add_widget(bubble)
    else:
        place_detail = get_place_details(result["place_id"])
        photo = get_photo_html(result)
        phone = get_phone_number(place_detail)
        name = result["name"]
        rating = get_rating(result)

        # m = marker(lat = LAT, lon = LON) marker has been replaced by mapmarkerpopup
        bubble = Bubble(orientation = "vertical", padding = 5)
        if photo:
            image = AsyncImage(source = photo, mipmap = True)
            bubble.add_widget(image)
        if len(name) > 30:
            index1 = name.find(",")
            index2 = name.find(" ", int(len(name)/2))
            if index1 > 15:
                name = name[:index1] + "\n" + name[index1:]
            elif index2 > 20:
                name = name[:index2] + "\n" + name[index2:]
   
        text = "[b]" + name + "[/b]\n" + "Phone Number: " + phone + "\n" + "Rating: " + rating
        label = Label(text = text, markup = True, halign = "center")
        bubble.add_widget(label)
        m = MapMarkerPopup(lat=LAT,lon=LON,popup_size = (250, 230))
        m.add_widget(bubble)
    marker_list.append(m)
    mapview.add_marker(m)

def rm_all_markers(mapview):
    for m in marker_list:
        mapview.remove_marker(m)
    marker_list.clear()
        
    

if __name__ == '__main__':
    Window.fullscreen = True
    SkinDetectionApp().run()
