class VideoController:
    videos = []
    tutorials = [
        {
            "title": "Warne bowling to Ponting with Healy behind the stumps! | Wicket Keeping Masterclass | Part 2 🏏",
            "src": "https://www.youtube.com/embed/V2sg7vF8xa0",
            "video_url": "https://firebasestorage.googleapis.com/v0/b/fintech-23925.appspot.com/o/videos%2FWarne%20bowling%20to%20Ponting%20with%20Healy%20behind%20the%20stumps!%20_%20Wicket%20Keeping%20Masterclass%20_%20Part%202%20%F0%9F%8F%8F.mp4?alt=media&token=2a257496-6da3-4d8b-af6f-47bc7c500fe0"
        },
        {
            "title": "Virat Kohli: The Complete Batsman | Batting masterclass with Kohli &amp; Nasser Hussain",
            "src": "https://www.youtube.com/embed/m8u-18Q0s7I",
            "video_url": "https://firebasestorage.googleapis.com/v0/b/fintech-23925.appspot.com/o/videos%2FVirat%20Kohli_%20The%20Complete%20Batsman%20_%20Batting%20masterclass%20with%20Kohli%20.mp4?alt=media&token=79f7741e-c634-410c-a199-cb72ef61f64d"
        },
        {
            "title": "What&#39;s it like to face a Murali spin delivery? | Muttiah Muralitharan Bowling Masterclass | Part 2",
            "src": "https://www.youtube.com/embed/_86wgCOFi-c",
            "video_url": "https://firebasestorage.googleapis.com/v0/b/fintech-23925.appspot.com/o/videos%2FWhat's%20it%20like%20to%20face%20a%20Murali%20spin%20delivery.mp4?alt=media&token=c9308647-4ae1-4d17-bdd0-1261d81e79dd"
        },
        {
            "title": "How the New Ball Swings | Wicket to Wicket | BYJU’S",
            "src": "https://www.youtube.com/embed/ylu7kdmakTA",
            "video_url": "https://firebasestorage.googleapis.com/v0/b/fintech-23925.appspot.com/o/videos%2FCherry-Picking%20_%20How%20the%20New%20Ball%20Swings%20_%20Wicket%20to%20Wicket%20_%20BYJU%E2%80%99S.mp4?alt=media&token=0d879f69-f440-4e24-b170-068b441f9048"
        }]
    
    def list_videos(self, video_type="videos"):
        if video_type == "tutorials":
            return self.tutorials
        return self.videos

        

