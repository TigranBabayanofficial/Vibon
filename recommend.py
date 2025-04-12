
from models.video import Video
import random

def get_recommended_videos(user_id):
    return random.sample(Video.query.all(), min(5, Video.query.count()))
