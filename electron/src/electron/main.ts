import { app, BrowserWindow, ipcMain } from 'electron';
import path from 'path';
import {
  isDev,
  getPreloadPath,
  readFolderRecursively,
  pollFolder,
} from './utils/index.js';
import { TEMP_FOLDER_PATH } from './constants/index.js';

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    autoHideMenuBar: isDev() ? false : true,
    webPreferences: {
      preload: getPreloadPath(),
      webSecurity: isDev() ? false : true,
    },
  });

  mainWindow.maximize();

  if (isDev()) {
    mainWindow.loadURL('http://localhost:5123');
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(app.getAppPath(), '/dist-react/index.html'));
  }

  pollFolder();
});

ipcMain.handle('getTempFolder', async () => {
  return readFolderRecursively(TEMP_FOLDER_PATH);
});
