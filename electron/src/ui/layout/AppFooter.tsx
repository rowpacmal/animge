import styles from '../styles/AppFooter.module.css';

export function AppFooter() {
  return (
    <footer
      className={`footer sm:footer-horizontal footer-center ${styles['footer']}`}
    >
      <aside>
        <p>
          Copyright © {new Date().getFullYear()} - All right reserved by ACME
          Industries Ltd
        </p>
      </aside>
    </footer>
  );
}
