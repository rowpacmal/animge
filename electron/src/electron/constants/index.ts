import { app } from 'electron';
import path from 'path';

export const POLLING_INTERVAL = 1000;

export const TEMP_FOLDER_PATH = path.join(
  app.getPath('documents'),
  '/Animge/temp'
);

export const CACHE_FOLDER_PATH = path.join(
  app.getPath('documents'),
  '/Animge/models'
);
