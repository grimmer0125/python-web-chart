## Prepare

### Install Python dependencies

`pip/pip3 install -r requirements.txt`

Use Django 2, the latest is 3.
Use Plotly 2.7, the latest is 4.5.0.

### Install Node.js and Yarn and node packages

1. node: >=12. https://nodejs.org/en/
2. yarn: 1.x. https://classic.yarnpkg.com/en/docs/install#mac-stable
3. In `./reactui`, execute `yarn install` to install node.js packages.

`reactui` is created by https://create-react-app.dev/ and uses react hooks, https://zh-hant.reactjs.org/docs/hooks-intro.html.

Rearding building part on react side, extra steps after creating react project were done. Here is the note,

1. `yarn run eject` to generate webpack config file
2. `webpack.config.js`
   1. `runtimeChunk: false`
   2. comment `splitChunks`
   3. regarding output css, `filename: "static/css/[name].css"`
   4. regarding output js, `filename: isEnvProduction ? "static/js/[name].js"`

## Dev (two servers)

1. Start React web server (hot reload): `yarn`, then open `http://localhost:3000` for reactui part. You can set breakpoint on react code in chrome.
2. Start the django dev server (hot reload): `python manage.py runserver` or use VSCode to launch django

### usage

Open http://localhost:3000

## Production (one server)

1. [Produciton] Build output react js, `yarn build` in `./reactui`
2. [Caution] (**Should swtich to produciton build!!**). Start the django dev server: `python manage.py runserver` or use VSCode to launch django

### usage

Open http://127.0.0.1:8000

## Deprecated part

1. http://127.0.0.1:8000 to see automatical-reload time page (just for testing)
2. http://127.0.0.1:8000/chart/mode2
