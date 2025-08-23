import styles from './AppMain.module.css';

export function AppMain() {
  return (
    <main className={`${styles.main} ${styles['dotted-background']}`}>
      Main
    </main>
  );
}
