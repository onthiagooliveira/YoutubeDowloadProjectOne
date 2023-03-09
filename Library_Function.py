# Importing the module
from pytube import YouTube

# Folder that will store the video
download_save = "F:/YoutubeDowloadFiles"

# Message to user input
view_msg = 'Youtube videos Dowload | Thiago Alves'
user_input_message = 'Insert video link: \n'


# Function that requesting the  link to the video link
def Requesting_link_and_Execute_dowload():
    user_input_link = input(user_input_message)
    try:
        yt = YouTube(user_input_link)

        # Name of video
        name = yt.title

        #Captions

        # Setting video resolution
        yt = yt.streams.get_highest_resolution()

        # Downloading and saving locally
        yt = yt.download(output_path=download_save)
        print(f'\nSuccesful download.')
        print(f'{name}')
        print(f'Save in {download_save}')

    except:
        print("Connection Error")