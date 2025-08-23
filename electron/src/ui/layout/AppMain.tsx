import { IconPhotoFilled } from '@tabler/icons-react';
import { AdvanceSettings, UserTasks } from '../components';
import styles from './AppMain.module.css';

export function AppMain() {
  return (
    <main className={`${styles.main} ${styles['dotted-background']}`}>
      <div className="order-1">
        <UserTasks />
      </div>

      <div className="flex flex-col gap-4 w-full max-w-lg mx-auto xl:max-w-none order-3 xl:order-2">
        <textarea
          className="textarea resize-none h-32 w-full"
          placeholder="You can generate images by entering prompts here."
        ></textarea>

        <div className="flex justify-between">
          <div></div>

          <button className="flex gap-4 btn btn-secondary">
            <IconPhotoFilled />
            <span>Generate Image</span>
          </button>
        </div>
      </div>

      <div className="order-2 xl:order-3">
        <AdvanceSettings />
      </div>
    </main>
  );
}
