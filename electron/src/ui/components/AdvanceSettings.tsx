import { IconAdjustmentsHorizontal } from '@tabler/icons-react';
import { Collapse } from './templates';

export function AdvanceSettings() {
  return (
    <Collapse icon={<IconAdjustmentsHorizontal />} title="Advanced Settings">
      <p>
        Click the "Sign Up" button in the top right corner and follow the
        registration process.
      </p>
    </Collapse>
  );
}
