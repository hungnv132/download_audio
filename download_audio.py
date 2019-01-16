from pathlib import PosixPath
import urllib.request


def download_audio(file_):
    if type(file_) is not PosixPath:
        raise TypeError("Parameter 'file_' must be PosixPath object.")
    with file_.open() as f:
        links = f.readlines()
        for link in links:
            audio_name = get_audio_file_name(link)
            print("Downloading: " + audio_name)
            urllib.request.urlretrieve(link, audio_name)
    print('Finished!')


def get_audio_file_name(path):
    last_slash_index = path.rfind('/')
    return path[last_slash_index + 1:len(path) - 1]


if __name__ == '__main__':
    file_ = PosixPath('./links.txt')
    download_audio(file_)
