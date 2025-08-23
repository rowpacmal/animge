import { AppFooter, AppHeader } from './layout';
import './styles/App.css';

function App() {
  return (
    <>
      <AppHeader />

      <main className="flex-1 p-4 dotted-background">
        <p>Main</p>
      </main>

      <AppFooter />
    </>
  );
}

export default App;
