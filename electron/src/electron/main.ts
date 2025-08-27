import { app, BrowserWindow } from 'electron';
import path from 'path';
import { isDev } from './utils.js';
import { getPreloadPath } from './pathResolver.js';

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    autoHideMenuBar: isDev() ? false : true,
    webPreferences: {
      preload: getPreloadPath(),
      webSecurity: isDev() ? false : true,
    }
  });

  mainWindow.maximize();

  if (isDev()) {
    mainWindow.loadURL('http://localhost:5123');
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(app.getAppPath(), '/dist-react/index.html'));
  }
});