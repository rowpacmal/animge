export function AppFooter() {
  return (
    <footer className="footer sm:footer-horizontal footer-center bg-primary text-gray-50 p-4">
      <aside>
        <p>
          Copyright © {new Date().getFullYear()} - All right reserved by ACME
          Industries Ltd
        </p>
      </aside>
    </footer>
  );
}
