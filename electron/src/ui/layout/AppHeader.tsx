import { IconSettings, IconSparkles } from '@tabler/icons-react';
import styles from './AppHeader.module.css';

export function AppHeader() {
  return (
    <header className={styles.header}>
      <div className={styles['h-container']}>
        <IconSparkles size={32} className={styles.highlight} />

        <h1 className={styles.h1}>
          An<span className={styles.highlight}>img</span>e
        </h1>
      </div>

      <div className={styles['button-container']}>
        <button className={styles.button}>
          <IconSettings size={24} />
        </button>
      </div>
    </header>
  );
}
