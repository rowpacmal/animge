import { createContext } from 'react';

const AppContext = createContext<unknown>({});

function AppProvider({ children }: { children: React.ReactNode }) {
  return <AppContext.Provider value={{}}>{children}</AppContext.Provider>;
}

export { AppContext, AppProvider };
