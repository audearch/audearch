from web.controllers import app, index, upload, upload_file

app.add_api_route('/', index)
app.add_api_route('/upload', upload)
