import { AdvanceSettings, UserTasks } from '../components';
import styles from './AppMain.module.css';

export function AppMain() {
  return (
    <main className={`${styles.main} ${styles['dotted-background']}`}>
      <UserTasks />

      <textarea
        className="textarea mx-auto resize-none h-32 w-full max-w-lg xl:max-w-none order-3 xl:order-2"
        placeholder="You can generate images by entering prompts here."
      ></textarea>

      <AdvanceSettings />
    </main>
  );
}
