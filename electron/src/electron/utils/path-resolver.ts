import path from 'path';
import { app } from 'electron';
import { isDev } from './is-dev.js';

export function getPreloadPath() {
  return path.join(
    app.getAppPath(),
    isDev() ? '.' : '..',
    '/dist-electron/preload.cjs'
  );
}
