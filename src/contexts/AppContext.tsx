import { createContext } from 'react';

const AppContext = createContext({});

function AppProvider({ children }: { children: React.ReactNode }) {
  return (
    <AppContext.Provider
      value={
        {
          // Define context values here.
        }
      }
    >
      {children}
    </AppContext.Provider>
  );
}

export { AppContext, AppProvider };
