from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = "smk2025"

# --------- Helper functions ---------
def read_users():
    users = []
    try:
        with open('users.csv','r',newline='') as f:
            reader = csv.DictReader(f)
            for row in reader: users.append(row)
    except FileNotFoundError:
        pass
    return users

def write_users(users):
    with open('users.csv','w',newline='') as f:
        fieldnames=['username','password']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def read_transaksi():
    transaksi=[]
    try:
        with open('transaksi.csv','r',newline='') as f:
            reader = csv.DictReader(f)
            for row in reader: transaksi.append(row)
    except FileNotFoundError:
        pass
    return transaksi

def write_transaksi(transaksi):
    with open('transaksi.csv','w',newline='') as f:
        fieldnames=['id','item','harga','jumlah','total']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transaksi)

# --------- Routes ---------
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        users=read_users()
        for u in users:
            if u['username']==username and u['password']==password:
                session['user']=username
                return redirect(url_for('dashboard'))
        return "Login gagal, periksa username/password"
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        users=read_users()
        users.append({'username':username,'password':password})
        write_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

# Tambah transaksi
@app.route('/dashboard/tambah', methods=['GET','POST'])
def tambah_transaksi():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method=='POST':
        item = request.form['item']
        try:
            harga = int(request.form['harga'].replace('.',''))
            jumlah = int(request.form['jumlah'])
        except ValueError:
            return "Harga atau jumlah invalid"
        total = harga * jumlah
        transaksi = read_transaksi()
        # ID unik walau ada hapus
        if transaksi:
            new_id = str(max(int(t['id']) for t in transaksi)+1)
        else:
            new_id = '1'
        transaksi.append({'id':new_id,'item':item,'harga':harga,'jumlah':jumlah,'total':total})
        write_transaksi(transaksi)
        return redirect(url_for('daftar_transaksi'))
    return render_template('tambah_transaksi.html', user=session['user'])

# Daftar transaksi
@app.route('/dashboard/daftar')
def daftar_transaksi():
    if 'user' not in session:
        return redirect(url_for('login'))
    transaksi = read_transaksi()
    # konversi ke int supaya total bisa dijumlahkan
    for t in transaksi:
        t['harga'] = int(t['harga'])
        t['jumlah'] = int(t['jumlah'])
        t['total'] = int(t['total'])
    return render_template('daftar_transaksi.html', transaksi=transaksi, user=session['user'])

# Hapus transaksi
@app.route('/delete/<id>')
def delete_transaksi(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    transaksi = read_transaksi()
    transaksi = [t for t in transaksi if t['id'] != id]
    write_transaksi(transaksi)
    return redirect(url_for('daftar_transaksi'))

# Edit transaksi
@app.route('/dashboard/edit/<id>', methods=['GET','POST'])
def edit_transaksi(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    transaksi = read_transaksi()
    t = next((x for x in transaksi if x['id']==id), None)
    if not t: return "Transaksi tidak ditemukan"
    if request.method=='POST':
        t['item'] = request.form['item']
        try:
            t['harga'] = int(request.form['harga'].replace('.',''))
            t['jumlah'] = int(request.form['jumlah'])
        except ValueError:
            return "Harga atau jumlah invalid"
        t['total'] = t['harga'] * t['jumlah']
        write_transaksi(transaksi)
        return redirect(url_for('daftar_transaksi'))
    return render_template('edit_transaksi.html', transaksi=t, user=session['user'])

if __name__=="__main__":
    app.run(debug=True)
