
print("=========START=======")

print("=========Percobaan Pertama Type Data=======")
#anggep datane int
data_integer = 9
print("data :",data_integer)
print("bertipe :",type(data_integer))

print("=========Percobaan Kedua Casting=======")
 #misale integer ape tak dadikno float
data_int= 0
print("data :",data_int,"data bertipe :",type(data_int))

data_float= float(data_int)#pasti ndek kene berubahe float
print("data :",data_float,"data bertipe :",type(data_float ))


bilangan_complex= complex(12,27)
print("data :",bilangan_complex,type(bilangan_complex))


# print("=========Percobaan Ketiga input user=======")

# #input user khusus string
# spectra = input("Coba masukkan kata akhi :")
# print("data",spectra,"bertipe :",type(spectra)) 

# #lek pingin input nggae integer cobak pakek iki berlaku sisan gae float kok
# cendana = int(input("masukkan digit bilangan anda :"))
# print("data",cendana,"bertipe :",type(cendana)) 

# #saiki khusus boolean kudu bersabar,dan cobak gawe modifikasi paramater casting
# vector = bool(int(input("masukkan bilangan pembuktian salah benar :")))
# print("data",vector,"bertipe :",type(vector)) 

print("=========Percobaan Keempat Operasi Komparasi input user=======")
a = 4
b = 3

hasil = a > b
print(a,">",b,"=",hasil)

hasil = a < b
print(a,"<",b,"=",hasil)

hasil = a == b
print(a,"=",b,"=",hasil)

hasil = b != b
print(b,"!=",a,"=",hasil)

hasil = a != a
print(a,"!=",b,"=",hasil)

x = 5
y = 4

print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))

print("=========FINISH=======")



