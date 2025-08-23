import { IconSettings } from '@tabler/icons-react';

export function AppHeader() {
  return (
    <header className="navbar bg-base-100 shadow-sm">
      <div className="flex-1">
        <h1 className="text-2xl uppercase">
          An<span className="text-primary">img</span>e
        </h1>
      </div>

      <div className="flex-none">
        <button className="btn btn-square btn-ghost">
          <IconSettings size={24} />
        </button>
      </div>
    </header>
  );
}
