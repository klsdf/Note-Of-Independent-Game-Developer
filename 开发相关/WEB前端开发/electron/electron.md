# 安装
```shell
 npm install -g cnpm --registry=https://registry.npm.taobao.org
```

查看版本

```shell
npx electron -v
```

打开electron

```shell
npx electron
```



# 基本结构

index.html

```html
<!DOCTYPE html>
<html lang="zh-Ch">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    hello world
</body>
</html>
```



main.js

```js
const {app, BrowserWindow} = require('electron')
const path = require('path')

function createWindow () {

  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  mainWindow.loadFile('index.html')
  // 打开开发工具
  mainWindow.webContents.openDevTools()

}


app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

```

preload.js

```js
window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const dependency of ['chrome', 'node', 'electron']) {
      replaceText(`${dependency}-version`, process.versions[dependency])
    }
  })
```



package.json

```json
{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "author": "",
  "license": "ISC"
}

```





# 渲染流程

electron依赖于Chromium的多线程架构。有一个主进程，也就是package.json中的那个main。剩下的都是渲染进程。









