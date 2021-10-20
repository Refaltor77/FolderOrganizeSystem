import os
from pathlib import Path


folders = {
    "html": [".html5", ".html", ".htm", ".xhtml"],
    "images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
    "vidéos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx"],
    "archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip"],
    "audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "text": [".txt", ".in", ".out"],
    "pdf": [".pdf"],
    "python": [".py"],
    "xml": [".xml"],
    "exe": [".exe"],
    "shell": [".sh"]
}


formats = {file_format: directory for directory, file_formats in folders.items()for file_format in file_formats}
def rangement():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(formats[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

    try:
        os.mkdir("autres")
    except:
        pass

    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/autres/' + str(Path(dir)))
        except:
            pass


if __name__ == "__main__":
    rangement()
