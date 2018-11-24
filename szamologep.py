print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('Üdvözöllek az egyszerû számológépben!                                              Ver. 1.0')
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print ('Help: Eloszor add meg, hogy mit szeretnel(Osszeadas, Kivonas, Szorzas, Osztas, Hatvanyozas ) \n majd add meg a tagokat(Ha nincs tobb tag,akkor irj 0 -t! ')
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('')

try:
    All= int(input('Osszeadas(1), Kivonas(2), Szorzas(3), Osztas(4), Hatvanyozas(5): '))
except ValueError:
    print("Kérlek számokat írj be!")
    All=0               #csak azért, hogy ha itt exceptionre fut, akkor 15. sorban lévő while ne szálljon el amiatt, hogy még nincs ilyen változó
# All2=0  # nem kell használat előtt deklarálni a változókat

while int(All) not in (1,2,3,4,5):
    print("Nem a lehetséges műveletek közül választottál")
    try:
        All = int(input('Osszeadas(1), Kivonas(2), Szorzas(3), Osztas(4), Hatvanyozas(5): '))
    except ValueError:
        print("Kérlek számokat írj be!")

print('')
try:
    num1 = int (input('Add meg az elsõ tagot: '))
    num2 = int (input('Add meg a második tagot: '))
except:
    print("Egész számot kellett volna beírnod!")
print('')

try:
    if All == 1:
        All2 = int(num1) + int(num2)
        print (num1, '+' , num2,'=', All2)


    if All == 2:
        All2 = int(num1) - int(num2)
        print (num1, '-' , num2,'=', All2)



    if All == 3:
        All2 = int(num1) * int(num2)
        print (num1, '*' , num2,'=', All2)

    if All == 4:
        try:
            All2 = int(num1) / int(num2)
            print (num1, '/' , num2,'=', All2)
        except ZeroDivisionError:
            print("Hoppá! Nullával osztás")

    if All == 5:
        All2 = int(num1) ** int(num2)
        print (num1, '**' , num2,'=', All2)
except NameError:
    print("Nem adtál meg számokat")
print('')    
print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

input('')
