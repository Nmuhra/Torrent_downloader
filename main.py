from qbittorrent import Client

qb_adress = input("qb: \n")
qb = Client(str(qb_adress))

qb.login("admin", "adminadmin")

URL = input("torrent file:\n")
torrent_file = open(str(URL), "rb")

print("Downloading ...")

qb.download_from_file(torrent_file)