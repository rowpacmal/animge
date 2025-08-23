import { IconHistory } from '@tabler/icons-react';
import { Collapse } from './templates';

export function UserTasks() {
  return (
    <Collapse icon={<IconHistory />} title="User Tasks">
      <p>
        Click the "Sign Up" button in the top right corner and follow the
        registration process.
      </p>
    </Collapse>
  );
}
