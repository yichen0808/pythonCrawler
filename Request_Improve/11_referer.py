import requests
# 网站源代码缺少
url = "https://www.pearvideo.com/video_1806629"
contId = url.split('_')[1]
# print(contId)
# 找到视频json
url_video = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.899837181409587"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
    #防盗链
    "referer":"https://www.pearvideo.com/video_1806629"
}
videoContent = requests.get(url_video,headers=headers)
videoJson = videoContent.json()
# 获取视频json
srcUrl = videoJson['videoInfo']['videos']['srcUrl']
replaceContent = videoJson['systemTime']
tureUrl = srcUrl.replace(replaceContent,"cont-"+contId)
# 下载视频
with open(f"{contId}.mp4",mode='wb') as f:
    f.write(requests.get(tureUrl).content)

