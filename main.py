import googleapiclient.discovery
import pandas as pd
DEVELOPER_KEY = "AIzaSyAAi4WcMa3Ld6GPSF3atCUIHNxw3YChfS0"

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

video_id = "22tVWwmTie8"

comments = []

next_page_token = None
while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token
    )

    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        public = item['snippet']['isPublic']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['likeCount'],
            comment['textOriginal'],
            public
        ])

    next_page_token = response.get('nextPageToken')

    if not next_page_token:
        break

# Convert comments to a DataFrame
df = pd.DataFrame(comments, columns=['author', 'updated_at', 'like_count', 'text', 'public'])
for text in df['text']:
     print(text)
print(df.shape[0])