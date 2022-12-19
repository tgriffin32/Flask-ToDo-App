# init file makes website a python package so we can import from it
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)     # runs app and updates app when changes made
    