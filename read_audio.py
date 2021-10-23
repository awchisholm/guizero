import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"InstallVirtualBox.webm")
my_clip.audio.write_audiofile(r"InstallVirtualBox.mp3")