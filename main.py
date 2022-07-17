from qbittorrent import Client


qb = Client("http://127.0.0.1:8080/")

qb.login("admin", "adminadmin")

URL = input("torrent file:\n")
torrent_file = open(str(URL), "rb")

print("Downloading ...")

qb.download_from_file(torrent_file)