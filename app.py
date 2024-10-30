from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="Microforge - O futuro da Biologia Molecular passa por aqui!", 
        description="Produzimos insumos de biologia molecular para laboratórios, 100% nacionais, para facilitar a rotina dos cientistas brasileiros."
    )

if __name__ == '__main__':
    app.run(debug=True)
