import pwn
import re
p = pwn.remote('auto.threatsims.com',5225)
#print(p.recv(4096))
p.recvuntil('Hint3: Tax is not a percentage\n')
while(True):
    s = p.recv(4096)
    print(s.decode('latin'))
    l = []
    if b'Spam' in s:
        print("FOUNDD SPAM")
        result = re.search(b'Memo: (.*)\n', s)
        pay = result.group(1).decode('latin')
        print(pay)
        p.sendline((pay))
        #print(t)
        #k = 'Memo'
        #pwn.log.info('Memo is ')
        #print(s[s.find(b'Memo: '):s.index(b'\n')])
    l = []
    if b'=' in s:
        print("BOOK")
        eq = re.search(b'=(.*)\n',s)
        suma = eq.group(1)
        t = s.split(b'+')
        result = re.findall(b'\d+',s)
        l = result
        print(l)
        pay = 0
        sumica = int(suma)

        for i in l:
            if i != suma:
                print(i)
                pay += int(i)
        send = sumica - pay
        print(send)
        send = round(send)
        p.sendline(str(send))
    # check is worked*rate + overtime*rate/2
    if b'check' in s:
        worked = re.search(b'Hours Worked: (.*)\n',s)
        print(f'THIS {worked}')

        w = worked.group(1)
        rate = re.search(b'Hourly Rate: (.*)\n',s)
        r = rate.group(1)
        over = re.search(b'Overtime: (.*)\n',s)
        o = over.group(1)
        check = int(w)*int(r) + int(o)*(int(r)/2)
        print(int(check))
        p.sendline(str(int(round(check))))
    if b'taxes' in s:
        tax = re.search(b'Tax: (.*)\n',s)
        ta = tax.group(1)
        earn = re.search(b'Earnings: (.*)\n',s)
        ea = earn.group(1)
        pay = float(ta) * float(ea)
        print(int(pay))
        pay = round(pay)
        p.sendline(str(pay))
    if b'TS' in s:
        s = p.recvall()
        print(s)
        pwn.log.info("YOU WON")
        break
