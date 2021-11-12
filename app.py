from flask import Flask, request, render_template, g
from flask.json import jsonify
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def redirect():
    return redirect('https://ytmp3.sivaj.pl/')


@app.route('/download',)
def download():
    url = request.form.get('url')
    print(url)
    video = YouTube(url)
    stream = video.streams.order_by('abr').get_audio_only()
    filename = stream.default_filename.replace(' ', '-')
    stream.download(output_path='./static/', filename=filename)

    return jsonify(
        url='/static/' + filename
    )
