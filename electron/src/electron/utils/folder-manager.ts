import fs from 'fs/promises';
import path from 'path';
import { CACHE_FOLDER_PATH, POLLING_INTERVAL } from '../constants/index.js';
import { TReadFolderRecursivelyReturnValue } from '../types/index.js';

export async function readFolderRecursively(
  dirPath: string
): Promise<TReadFolderRecursivelyReturnValue[]> {
  const results = [];
  const items = await fs.readdir(dirPath, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(dirPath, item.name);
    const stat = await fs.stat(fullPath);

    if (item.isDirectory()) {
      results.push({
        name: item.name,
        type: 'directory',
        children: await readFolderRecursively(fullPath),
        timestamp: stat.mtimeMs,
      });
    } else {
      results.push({
        name: item.name,
        type: 'file',
        path: fullPath,
      });
    }
  }

  return results;
}

export function pollFolder() {
  setInterval(async () => {
    const size = await getFolderSize(CACHE_FOLDER_PATH);
    console.log(size);
  }, POLLING_INTERVAL);
}

async function getFolderSize(dirPath: string) {
  let totalSize = 0;

  const items = await fs.readdir(dirPath, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(dirPath, item.name);
    const stat = await fs.stat(fullPath);

    if (item.isDirectory()) {
      totalSize += await getFolderSize(fullPath);
    } else {
      totalSize += stat.size;
    }
  }

  return totalSize;
}
