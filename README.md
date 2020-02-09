## Prepare

### Install Python dependencies

`pip/pip3 install -r requirements.txt`

### Install Node.js and Yarn and node packages

1. node: >=12. https://nodejs.org/en/
2. yarn: 1.x. https://classic.yarnpkg.com/en/docs/install#mac-stable
3. In `./reactui`, execute `yarn install` to install node.js packages.

## Dev (two servers)

1. Start React web server: `yarn`, then open `http://localhost:3000` for reactui part.
2. Start the django server: `python manage.py runserver` or use VSCode to launch django

### usage

Open http://localhost:3000

## Production (one server)

1. Build output react js, `yarn build` in `./reactui`
2. Start the django server: `python manage.py runserver` or use VSCode to launch django

### usage

Open http://127.0.0.1:8000/chart/mode1

## Deprecated part

1. http://127.0.0.1:8000 to see automatical-reload time page (just for testing)
2. http://127.0.0.1:8000/chart/mode2
