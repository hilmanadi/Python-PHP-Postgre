print("content-type: text/html\n\n" )
import psycopg2

try:
    conn = psycopg2.connect(host="localhost", user="postgres", password="bellato50", database="test")
    cur = conn.cursor()
    pasien = cur.execute("SELECT * from akses,pasien")
    past = cur.fetchall()
    pastt = len(past)

    nama1_1 = [""]*pastt
    nama1_2 = [""]*pastt
    alamat1_1 = [""]*pastt
    alamat1_2 = [""]*pastt
    alamat2_1 = [""]*pastt
    alamat2_2 = [""]*pastt
    alamat3_1 = [""]*pastt
    alamat3_2 = [""]*pastt
    alamat4_1 = [""]*pastt
    alamat4_2 = [""]*pastt
    rp1_1 = [""]*pastt
    rp1_2 = [""]*pastt
    rp2_1 = [""]*pastt
    rp2_2 = [""]*pastt
    rp3_1 = [""]*pastt
    rp3_2 = [""]*pastt
    rp4_1 = [""]*pastt
    rp4_2 = [""]*pastt
    gj1_1 = [""]*pastt
    gj1_2 = [""]*pastt
    gj2_1 = [""]*pastt
    gj2_2 = [""]*pastt
    gj3_1 = [""]*pastt
    gj3_2 = [""]*pastt
    gj4_1 = [""]*pastt
    gj4_2 = [""]*pastt

    opnknci = open("C:\Users\ASUS\Desktop\workfile.txt", 'r')
    kncii = opnknci.read()

    def splitbiner(w):
        splits = -((-len(w)) // 2)
        return w[:splits:], w[splits:]

    def decode_binary_string(s):
        return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))

    def split_bits(val,n):
        parts,mask = [],(1<<n)-1
        parts = [0]*4
        while val:
            parts.insert(4,val&mask)
            parts.pop(0)
            val >>=n
        parts.reverse()
        return parts

    pasien = map(list, past)

    for index, a in enumerate(pasien):
        # nama
        pasien[index][4] = "".join('{0:08b}'.format(x, 'b') for x in bytearray(a[4]))
        nm = pasien[index][4].zfill(128)
        # alamat
        pasien[index][8] = "".join('{0:08b}'.format(x, 'b') for x in bytearray(a[8]))
        almt = pasien[index][8].zfill(512)
        # riwayat penyakit
        pasien[index][11] = "".join('{0:08b}'.format(x, 'b') for x in bytearray(a[11]))
        rp = pasien[index][11].zfill(512)
        # gejala
        pasien[index][12] = "".join('{0:08b}'.format(x, 'b') for x in bytearray(a[12]))
        gj = pasien[index][12].zfill(512)

        gjj = int(gj,2)
        rpp = int(rp,2)
        almtt = int(almt,2)
        a = split_bits(almtt,128)
        g = split_bits(gjj,128)
        r = split_bits(rpp,128)

        al1 = bin(a[0])[2:].zfill(128)
        al2 = bin(a[1])[2:].zfill(128)
        al3 = bin(a[2])[2:].zfill(128)
        al4 = bin(a[3])[2:].zfill(128)

        ket1 = bin(r[0])[2:].zfill(128)
        ket2 = bin(r[1])[2:].zfill(128)
        ket3 = bin(r[2])[2:].zfill(128)
        ket4 = bin(r[3])[2:].zfill(128)

        gejala1 = bin(g[0])[2:].zfill(128)
        gejala2 = bin(g[1])[2:].zfill(128)
        gejala3 = bin(g[2])[2:].zfill(128)
        gejala4 = bin(g[3])[2:].zfill(128)
        #pecah biner
        nama1, nama2 = splitbiner(nm)
        alm1,alm2 = splitbiner(al1)
        alm3,alm4 = splitbiner(al2)
        alm5,alm6 = splitbiner(al3)
        alm7,alm8 = splitbiner(al4)
        rp1, rp2 = splitbiner(ket1)
        rp3, rp4 = splitbiner(ket2)
        rp5, rp6 = splitbiner(ket3)
        rp7, rp8 = splitbiner(ket4)
        gj1, gj2 = splitbiner(gejala1)
        gj3, gj4 = splitbiner(gejala2)
        gj5, gj6 = splitbiner(gejala3)
        gj7, gj8 = splitbiner(gejala4)

        keys = "".join('{0:08b}'.format(x, 'b') for x in bytearray(kncii))
        kunci = keys.zfill(128)
        knci1, knci2 = splitbiner(kunci)

        nama1_1[index] = int(nama1, 2)
        nama1_2[index] = int(nama2, 2)
        alamat1_1[index] = int(alm1, 2)
        alamat1_2[index] = int(alm2, 2)
        alamat2_1[index] = int(alm3, 2)
        alamat2_2[index] = int(alm4, 2)
        alamat3_1[index] = int(alm5, 2)
        alamat3_2[index] = int(alm6, 2)
        alamat4_1[index] = int(alm7, 2)
        alamat4_2[index] = int(alm8, 2)
        rp1_1[index] = int(rp1, 2)
        rp1_2[index] = int(rp2, 2)
        rp2_1[index] = int(rp3, 2)
        rp2_2[index] = int(rp4, 2)
        rp3_1[index] = int(rp5, 2)
        rp3_2[index] = int(rp6, 2)
        rp4_1[index] = int(rp7, 2)
        rp4_2[index] = int(rp8, 2)
        gj1_1[index] = int(gj1, 2)
        gj1_2[index] = int(gj2, 2)
        gj2_1[index] = int(gj3,2)
        gj2_2[index] = int(gj4,2)
        gj3_1[index] = int(gj5,2)
        gj3_2[index] = int(gj6,2)
        gj4_1[index] = int(gj7,2)
        gj4_2[index] = int(gj8,2)
        knci1_1 = int(knci1,2)
        knci1_2 = int(knci2,2)

    ROUNDS = 32

    def geserkiri(value, shift):
        tmp_bin = bin(value)[2:].zfill(64)
        binary = []
        for i in tmp_bin:
            binary.append(i)
        for i in range(shift):
            binary.append(binary.pop(0))
        result = ''.join(binary)
        return int(result, 2)

    def geserkanan(value, shift):
        tmp_bin = bin(value)[2:].zfill(64)
        binary = []
        for i in tmp_bin:
            binary.append(i)
        for i in range(shift):
            binary.insert(0, binary.pop())
        result = ''.join(binary)
        return int(result, 2)

    def speck_block(x, y, k):
        x = geserkanan(x, 8)
        x += y
        while x > 18446744073709551615:
            x -= (18446744073709551615 + 1)
        x ^= k
        y = geserkiri(y, 3)
        y ^= x
        result = [x, y]
        return result

    def speck_key(key, key_schedule):
        a = key[0]
        b = key[1]
        key_schedule[0] = b
        for i in range(ROUNDS-1):
            tmp_res = speck_block(a, b, i)
            a = tmp_res[0]
            b = tmp_res[1]
            key_schedule[i+1] = b
        return key_schedule

    def proses_enkripsi(plaintext, key_schedule, ciphertext):
        ciphertext[0] = plaintext[0]
        ciphertext[1] = plaintext[1]
        for i in range(ROUNDS):
            tmp_res = speck_block(ciphertext[0], ciphertext[1], key_schedule[i])
            ciphertext[0] = tmp_res[0]
            ciphertext[1] = tmp_res[1]
        return ciphertext

    def enkrip(pl1,pl2,k1,k2):
        plaintext = [0] * 2
        key = [0] * 2
        ciphertext = [0] * 2
        key_schedule = [0] * ROUNDS

        plaintext[0] = pl1
        plaintext[1] = pl2
        key[0] = k1
        key[1] = k2
        key_schedule = speck_key(key, key_schedule)
        ciphertext = proses_enkripsi(plaintext, key_schedule, ciphertext)
        pt1 = bin(plaintext[0])[2:].zfill(64)
        pt2 = bin(plaintext[1])[2:].zfill(64)
        enkripsi1 = hex(ciphertext[0]).rstrip("L").lstrip('0x') or "0"
        enkripsi2 = hex(ciphertext[1]).rstrip("L").lstrip('0x') or "0"
        e1 = enkripsi1.zfill(16)
        e2 = enkripsi2.zfill(16)
        enkripp = e1 + e2
        return enkripp

    def runprogram():
        for index, a in enumerate(pasien):
           nama = enkrip(nama1_1[index],nama1_2[index],knci1_1,knci1_2)
           alamat1 = enkrip(alamat1_1[index],alamat1_2[index],knci1_1,knci1_2)
           alamat2 = enkrip(alamat2_1[index], alamat2_2[index],knci1_1,knci1_2)
           alamat3 = enkrip(alamat3_1[index], alamat3_2[index],knci1_1,knci1_2)
           alamat4 = enkrip(alamat4_1[index], alamat4_2[index],knci1_1,knci1_2)
           riwayat1 = enkrip(rp1_1[index],rp1_2[index],knci1_1,knci1_2)
           riwayat2 = enkrip(rp2_1[index], rp2_2[index],knci1_1,knci1_2)
           riwayat3 = enkrip(rp3_1[index], rp3_2[index],knci1_1,knci1_2)
           riwayat4 = enkrip(rp4_1[index], rp4_2[index],knci1_1,knci1_2)
           gejalaa1 = enkrip(gj1_1[index],gj1_2[index],knci1_1,knci1_2)
           gejalaa2 = enkrip(gj2_1[index], gj2_2[index],knci1_1,knci1_2)
           gejalaa3 = enkrip(gj3_1[index], gj3_2[index],knci1_1,knci1_2)
           gejalaa4 = enkrip(gj4_1[index], gj4_2[index],knci1_1,knci1_2)

           alamatsemua = alamat1+alamat2+alamat3+alamat4
           riwayatsemua = riwayat1+riwayat2+riwayat3+riwayat4
           gejalasemua = gejalaa1+gejalaa2+gejalaa3+gejalaa4

           tambah_pasien = ("update pasien "
                                     "set nama = %s, alamat =%s,ket_rekam_medik=%s,gejala=%s"
                                     "where no_pasien  = %s"
                             )
           add_pasien = (nama,alamatsemua,riwayatsemua,gejalasemua,pasien[index][3])
           cur.execute(tambah_pasien, add_pasien)
           conn.commit()

    runprogram()
except psycopg2.Error as error :
    print("koneksi ke database error"), error