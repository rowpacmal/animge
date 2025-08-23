import {
  IconMoon,
  IconSettings,
  IconSparkles,
  IconSun,
} from '@tabler/icons-react';
import styles from './AppHeader.module.css';
import { useState } from 'react';

export function AppHeader() {
  const [theme, setTheme] = useState(
    document.documentElement.dataset.theme
      ? document.documentElement.dataset.theme === 'light'
        ? 'light'
        : 'dark'
      : 'dark'
  );

  return (
    <header className={styles.header}>
      <div className={styles['h-container']}>
        <IconSparkles className={styles.highlight + ' size-8'} />

        <h1 className={styles.h1}>
          An<span className={styles.highlight}>img</span>e
        </h1>
      </div>

      <div className={styles['button-container']}>
        <button
          className={styles.button}
          onClick={() => {
            // Change data-theme
            if (document.documentElement.dataset.theme === 'light') {
              document.documentElement.dataset.theme = 'dark';
              setTheme('dark');
            } else {
              document.documentElement.dataset.theme = 'light';
              setTheme('light');
            }
          }}
        >
          {theme === 'light' ? <IconSun /> : <IconMoon />}
        </button>

        <button className={styles.button}>
          <IconSettings />
        </button>
      </div>
    </header>
  );
}
