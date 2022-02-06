import zipfile as zp
with zp.ZipFile('TableBattlesFallujah.vmod', 'r') as zip: zip.extractall('Source')