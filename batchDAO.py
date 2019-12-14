import mysql.connector
import dbconfig as cfg

class BatchDAO:
    db=""

    def connectToDB(self):
        self.db = mysql.connector.connect(
        host= cfg.mysql['host'],
        user= cfg.mysql['username'],
        password= cfg.mysql['password'],
        database= cfg.mysql["database"]
        )


    def __init__(self):
        self.connectToDB()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()


    def create(self, values):
        cursor = self.getCursor()
        sql="insert into batch (batch, yield, time) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close()
        return lastRowId

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from batch"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDict(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from batch where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        batch = self.convertToDict(result)
        cursor.close()
        return batch
 
    def update(self, values):
        cursor = self.getCursor()
        sql="update batch set batch= %s, yield=%s, time=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from batch where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()


    def convertToDict(self,result):
        colnames=['id','batch','yield','time']
        item ={}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item


batchDAO = BatchDAO()