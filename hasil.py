# Coding by guweh Romi Afrizal
from xyz import *
from time import sleep as jeda
from datetime import datetime

#--- TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#--- CEK HASIL FACEBOOK
def hasil_fb():
	tulis(Panel(f"{Te}{U} •{P} 01 {O}Cek hasil akun {H}OK \n{U} •{P} 02 {O}Cek hasil akun {K}CP \n{U} •{P} 03 {O}Hapus hasil crack \n{U} •{M} 00 {O}Kembali",style='#FF0022'))
	rom = input('%s╰─%s Pilih %s>%s '%(p,o,m,k))
	if rom in['']:
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		os.system("python run.py")
	elif rom in['1','01']:
		dirs = os.listdir('OK')
		print ('')
		for file in dirs:
			print("%s╰─%s> %s%s"%(p,m,h,file));jeda(0.07)
		try:
			tulis(Panel(f"{Te}{U} •{O} Masukan file [ cth{M}: {K}{waktu}.txt{O} ]",style='#FF0022'))
			file = input("%s╰─%s masukan file %s:%s "%(p,o,m,h));jeda(0.2)
			if file in['']:
				exit("%s╰─%s isi yang benar kentod"%(p,m))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s╰─ %sfile tidak ada "%(p,m))
		except UnboundLocalError:
			print("%s╰─ %sfile tidak ada "%(p,m))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {H}{file_nm} {O}jumlah {M}: {H}{len(totalok)}",style='#FF0022'))
		print(f'{h}')
		os.system('cat OK/%s'%(file));jeda(0.07)
		exit('\n')
	elif rom in['2','02']:
		dirs = os.listdir('CP')
		print ('')
		for file in dirs:
			print("%s╰─%s> %s%s"%(p,m,k,file));jeda(0.07)
		try:
			tulis(Panel(f"{Te}{U} •{O} Masukan file [ cth{M}: {K}{waktu}.txt{O} ]",style='#FF0022'))
			file = input("%s╰─%s masukan file %s:%s "%(p,o,m,h));jeda(0.2)
			if file in['']:
				exit("%s╰─ %sisi yang benar kentod"%(p,m))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s╰─ %sfile tidak ada "%(p,m))
		except UnboundLocalError:
			print("%s╰─ %sfile tidak ada "%(p,m))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {K}{file_nm} {O}total {M}: {K}{len(totalcp)}",style='#FF0022'))
		print(f'{k}')
		os.system('cat CP/%s'%(file));jeda(0.07)
		exit('\n')
	elif rom in['3','03']:
		os.system('rm -rf CP/*.txt && rm -rf OK/*.txt')
		jalan (f'{p}╰─{h} berhasil menghapus hasil crack ');jeda(2)
		os.system("python run.py")
	elif rom in['0','00']:
		os.system("python run.py")
	else:
		print ('\n%s╰─%s isi yang benar'%(p,m));jeda(2)
		os.system("python run.py")
