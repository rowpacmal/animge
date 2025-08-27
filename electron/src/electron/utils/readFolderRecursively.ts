import fs from "fs/promises";
import path from "path";

type TReadFolderRecursivelyReturnValue = {
    name: string;
    type: string;
    children: TReadFolderRecursivelyReturnValue[];
} | {
    name: string;
    type: string;
    path: string;
};

export async function readFolderRecursively(dirPath: string): Promise<TReadFolderRecursivelyReturnValue[]> {
  const results = [];
  const items = await fs.readdir(dirPath, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(dirPath, item.name);
    if (item.isDirectory()) {
      results.push({
        name: item.name,
        type: "directory",
        children: await readFolderRecursively(fullPath),
      });
    } else {
      results.push({
        name: item.name,
        type: "file",
        path: fullPath,
      });
    }
  }

  return results;
}
