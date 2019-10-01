
import os
import urllib.request
import zipfile


def multiwoz_download(target_dir="", version="2.0"):
    # Download if necessary
    if version == "2.0":
        url = "https://www.repository.cam.ac.uk/bitstream/handle/1810/280608/MULTIWOZ2.zip?sequence=3&isAllowed=y"
    elif version == "2.1":
        url = "https://www.repository.cam.ac.uk/bitstream/handle/1810/294507/MULTIWOZ2.1.zip?sequence=1&isAllowed=y"
    else:
        raise ValueError(f"Version '{version}' must be '2.0' or '2.1'.")

    if target_dir is None or target_dir == "":
        target_dir = os.path.abspath(os.path.join(".", "data"))
    else:
        if not os.path.exists(target_dir):
            raise ValueError(f"Directory '{target_dir}' does not exist.")

    if version == "2.0":
        file_name = os.path.join(target_dir, "MultiWOZ-2.zip")
        unpacked_dir = os.path.abspath(os.path.join(target_dir, "MultiWOZ-2"))
    elif version == "2.1":
        file_name = os.path.join(target_dir, "MultiWOZ-2.1.zip")
        unpacked_dir = os.path.abspath(os.path.join(target_dir, "MultiWOZ-2.1"))
    else:
        raise ValueError(f"Version '{version}' must be '2.0' or '2.1'.")

    if not os.path.isfile(file_name):
        print(f"Downloading '{url}'' to '{file_name}'...")
        urllib.request.urlretrieve(url, file_name)
    else:
        print(f"The archive '{file_name}' exists already.")

    # Unpack if necessary
    if not os.path.isdir(unpacked_dir):
        print(f"Unpacking...")
        with zipfile.ZipFile(file_name, "r") as zip_ref:
            zip_ref.extractall(unpacked_dir)
    else:
        print("Files were unpacked already.")

    if version == "2.0":
        return os.path.join(unpacked_dir, "MULTIWOZ2 2")
    elif version == "2.1":
        return os.path.join(unpacked_dir, "MULTIWOZ2.1")
    else:
        raise ValueError(f"Version '{version}' must be '2.0' or '2.1'.")


if __name__ == '__main__':
    multiwoz_download(target_dir=os.path.abspath(os.path.join("..", "data")), version="2.1")
