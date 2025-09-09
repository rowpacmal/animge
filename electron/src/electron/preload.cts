const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electron", {
  getTempFolder: () => ipcRenderer.invoke("getTempFolder"),
});