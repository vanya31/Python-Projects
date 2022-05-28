# importing the module
from pytube import YouTube

# where to save
path = input("Enter Destination Path:")

# link of the video to be downloaded
link = input("Enter YouTube Link:")

try:
    # object creation using YouTube
    # which was imported in the beginning
    obj = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
obj = YouTube(link)
mp4files = obj.filter('mp4')

# to set the name of the file
obj.set_filename('Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = obj.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(path)
except:
    print("Some Error!")
print('Task Completed!')
