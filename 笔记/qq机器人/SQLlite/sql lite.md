



## 建立数据库



```js
let db = new sqlite3.Database(':memory:', (err) => {
    if (err) {
        return console.error(err.message)
    }

    console.log('Connected to the in-memory SQlite database.')
})
```

这里使用了`:memory:`关键字，这个关键字指创建一个**临时的内存数据库**。当程序结束，或者数据库连接关闭时，该内存数据库的所有数据将被清空。这种数据库类型经常用于需要快速访问和操作数据，但并不需要持久化数据的情况。形象地说，它就像是程序运行时的"临时记忆"。



如果希望持久化保存数据，可以使用下面的方法：

```js
let db = new sqlite3.Database('database.db', (err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log("Connected to the sqlite database.");
});
```

## 获取结果（db.run）

`db.run`和`db.get`都是用来执行SQL命令的，但它们用于不同的场景并返回不同的结果。

`db.run`用于执行不返回数据的SQL命令（例如，INSERT，UPDATE，DELETE，CREATE TABLE等）。这个方法在查询执行后调用回调函数，并且传递给回调函数可能出现的错误信息。它不会将结果集传递给回调函数。

示例：

```javascript
db.run("INSERT INTO tbl (col1, col2) VALUES (?, ?)", val1, val2, function(err) {
    if (err) {
      return console.log(err.message);
    } 
    console.log(`A row has been inserted with rowid ${this.lastID}`);
});
```

`db.get`用于执行返回单个结果的SQL命令（例如 SELECT）。这个方法在查询执行后调用回调函数，并传递给回调函数可能出现的错误信息和结果集。如果结果集中包含多条记录，只有第一条记录会被返回。

示例：

```javascript
db.get("SELECT * FROM tbl WHERE id = ?", id, function(err, row) {
    if (err) {
        return console.log(err.message);
    }  
    console.log(row.col1, row.col2);
});
```

如果你的SELECT查询可能返回多行数据，你应该使用`db.all`，这个方法会将结果集中的所有记录作为数组传递给回调函数。

示例：

```javascript
db.all("SELECT * FROM tbl", [], (err, rows) => {
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        console.log(row.col1, row.col2);
    });
});
```



## 创建表

```sql
CREATE TABLE YingxueUser(
	qq    INT PRIMARY KEY,
	exp   INT NOT NULL,
	nickname  TEXT NOT NULL,
	last_login_time date Not NUll, 
	level INT  ,
	money INT,
	

);
```



## 删除表

```sql
DROP TABLE YingxueUser;
```


## 插入

```sql
INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );

cursor.execute('insert into user(id,name) values(1,"MRSOFT")')
cursor.execute('insert into user(id,name) values(2,"Andy")')
cursor.execute('insert into user(id,name) values(3,"SiRi")')
————————————————
版权声明：本文为CSDN博主「Moonpie小甜饼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_44653420/article/details/124018901

```