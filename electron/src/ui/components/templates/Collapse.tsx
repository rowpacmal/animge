import { useState } from 'react';

export function Collapse({
  children,
  icon,
  title,
}: {
  children: React.ReactNode;
  icon: React.ReactNode;
  title: string;
}) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="max-w-lg mx-auto">
      <div className="collapse collapse-arrow bg-base-100 border-primary border">
        <input
          type="checkbox"
          checked={isOpen}
          onChange={() => setIsOpen(!isOpen)}
        />

        <div className="collapse-title font-semibold flex items-center gap-2 text-primary">
          {icon} {title}
        </div>

        <div className="collapse-content text-sm">
          <div className="flex flex-col gap-2 overflow-y-auto max-h-[560px] p-1">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}
