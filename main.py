from website import create_app

app=create_app()

if __name__=='__main__':
    app.run(debug=False,port=8082,host='0.0.0.0')
 
