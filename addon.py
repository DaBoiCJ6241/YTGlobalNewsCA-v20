from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL0 = "https://live.corusdigitaldev.com/groupb/live/6512f46a-8730-4668-af48-83159f3c706d/live.isml/live-audio_1=96000-video=2499968-261185081.ts"
URL1 = "https://www.youtube.com/feeds/videos.xml?channel_id=UChLtXXpo4Ge1ReTEboVvTDg"#GLOBALNEWS
URL1 = "https://www.youtube.com/feeds/videos.xml?channel_id=UCkiP0kvvwqUWlttRLCq88gw"#GLOBALTV
URL3 = "https://www.youtube.com/feeds/videos.xml?channel_id=UCxUD8G1jO8T-Ef2tuADCZOA"#16x9

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': "https://live.corusdigitaldev.com/groupb/live/6512f46a-8730-4668-af48-83159f3c706d/live.isml/live-audio_1=96000-video=2499968-261185081.ts",
            'thumbnail': "https://i0.wp.com/media.globalnews.ca/videostatic/349/131/Global%20News__946999.png?w=500&quality=70&strip=all", 
            'is_playable': True},
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('GN_episodes'),
            'thumbnail': "https://s2.wp.com/wp-content/themes/vip/shaw-globalnews/_img/logos/news_2x.png"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('GTV_episodes'),
            'thumbnail': "https://yt3.ggpht.com/a/AGF-l786nHHRDz4Acb-e65W4t8svk9n3G296lR6RqA=s288-c-k-c0xffffffff-no-rj-mo"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('SBN_episodes'),
            'thumbnail': "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fshawglobalnews.files.wordpress.com%2F2016%2F01%2F16x9-cj.jpg%3Fquality%3D70%26strip%3Dall%26w%3D720%26h%3D480%26crop%3D1&f=1"},

   ]
    return items

@plugin.route('/GN_episodes/')
def GN_episodes():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/GTV_episodes/')
def GTV_episodes():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/SBN_episodes/')
def SBN_episodes():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
if __name__ == '__main__':
    plugin.run()
