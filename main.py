from flask import Flask, request
import requests
import connection

app = Flask(__name__)

db_connection = connection.Connection().getConnection()

#Template response gagal
resultFailed = {
        'status' : 'error',
        'message' : 'cek ulang body request'
    }   

#Post data
@app.route('/api/post_data', methods=['POST'])
def postData():
    f = request.form
    nama = f['nama']        
    pengarang = f['pengarang']
    tahun_terbit = f['tahun_terbit']
    #Cek tipe data
    if((isinstance(nama, str)) and (isinstance(pengarang, str)) and (isinstance(tahun_terbit, str))):
        try:
            query = f"INSERT INTO buku (judul_buku, pengarang, tahun_terbit) VALUES ('{nama}','{pengarang}','{tahun_terbit}')"
            cursor = db_connection.cursor()
            cursor.execute(query=query)
            db_connection.commit()
            cursor.close()

            result_json = {
                'status' : 'success',
                'message' : 'berhasil tambahkan data',
                'data' : {
                    'nama' : nama,
                    'pengarang' : pengarang,
                    'tahun terbit': tahun_terbit
                }
            }
        except Exception as e:
            print(e)
            result_json = resultFailed
    else:
        print("here")
        result_json = resultFailed
    
    return result_json


#Get Data
@app.route('/api/get_all_data', methods=['GET'])
def getAllData():
    #Cek tipe data
    try:
        
        query = f"SELECT * FROM buku"
        cursor = db_connection.cursor()
        cursor.execute(query=query)
        data_buku = cursor.fetchall()
        db_connection.commit()
        cursor.close()

        result_json = {
            'status' : 'success',
            'message' : 'berhasil ',
            'data' : data_buku
        }
    except Exception as e:
        print(e)
        result_json = resultFailed
    
    return result_json

#Delete Data
@app.route('/api/delete_data', methods=['DELETE'])
def deleteData():
    f = request.form
    buku_id = f['id']
    try:
        buku_id_int = int(buku_id)
    except:
        return resultFailed
    
    try:
        query = f"DELETE FROM buku WHERE buku_id = {buku_id}"
        cursor = db_connection.cursor()
        cursor.execute(query=query)
        db_connection.commit()
        cursor.close()

        result_json = {
            'status' : 'success',
            'message' : 'berhasil hapus buku',
            'id_buku' : buku_id
        }
    except Exception as e:
        print(e)
        result_json = resultFailed
    
    return result_json

if __name__ == '__main__':
    app.run(host='10.0.2.3', port=8001)