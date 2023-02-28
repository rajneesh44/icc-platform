class VideoController:
    videos = []
    tutorials = [
        {
            "title":
            "Warne bowling to Ponting with Healy behind the stumps! | Wicket Keeping Masterclass | Part 2 🏏",
            "src": "https://www.youtube.com/embed/V2sg7vF8xa0",
        },
        {
            "title":
            "Virat Kohli: The Complete Batsman | Batting masterclass with Kohli &amp; Nasser Hussain",
            "src": "https://www.youtube.com/embed/m8u-18Q0s7I",
        },
        {
            "title":
            "What&#39;s it like to face a Murali spin delivery? | Muttiah Muralitharan Bowling Masterclass | Part 2",
            "src": "https://www.youtube.com/embed/_86wgCOFi-c",
        },
        {
            "title": "How the New Ball Swings | Wicket to Wicket | BYJU’S",
            "src": "https://www.youtube.com/embed/ylu7kdmakTA",
        }]
    
    def list_videos(self, video_type="videos"):
        if video_type == "tutorials":
            return self.tutorials
        return self.videos

        

