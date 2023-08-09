const { app, BrowserWindow } = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
      width: 1072,
      height: 576,
      backgroundColor: '#FFF',
      titleBarStyle: 'hidden',
    })
  
    win.loadFile('index.html')
  }



  
  app.whenReady().then(() => {
    createWindow()
  })