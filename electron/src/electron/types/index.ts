export type TReadFolderRecursivelyReturnValue =
  | {
      name: string;
      type: string;
      children: TReadFolderRecursivelyReturnValue[];
    }
  | {
      name: string;
      type: string;
      path: string;
    };
