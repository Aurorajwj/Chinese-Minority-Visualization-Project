from app import create_app

app=create_app()#用create_app()生成一个实例

if __name__ == '__main__':
    #  print(English.query.count())
    app.run()