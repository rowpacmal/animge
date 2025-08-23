import { AppHeader } from './components';
import './styles/App.css';

function App() {
  return (
    <>
      <AppHeader />

      <main className="flex-1">
        <p>Main</p>
      </main>

      <footer>
        <p>Footer</p>
      </footer>
    </>
  );
}

export default App;
