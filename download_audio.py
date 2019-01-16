from pathlib import Path, PosixPath
import urllib.request

home_directory = str(Path.home())
storing_path = home_directory + '/audios/'
links_file = PosixPath('./links.txt')


def init_location(path):
    p = Path(path)
    if not p.exists():
        p.mkdir()


def get_audio_file_name(path):
    last_slash_index = path.rfind('/')
    return path[last_slash_index + 1:len(path) - 1]


def download_audio(file_):
    if type(file_) is not PosixPath:
        raise TypeError("Parameter 'file_' must be PosixPath object.")
    with file_.open() as f:
        links = f.readlines()
        for link in links:
            audio_name = get_audio_file_name(link)
            print("Downloading: " + audio_name)
            urllib.request.urlretrieve(link, storing_path + audio_name)
    print('Finished!')


if __name__ == '__main__':
    init_location(storing_path)
    download_audio(links_file)
