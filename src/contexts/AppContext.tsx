import { createContext, useState } from 'react';
import { GoogleGenAI } from '@google/genai';

const AppContext = createContext<{ googleGenAI: GoogleGenAI | null }>({
  googleGenAI: null,
});

function AppProvider({ children }: { children: React.ReactNode }) {
  const [googleGenAI] = useState<GoogleGenAI>(
    new GoogleGenAI({ apiKey: import.meta.env.VITE_GEMINI_API_KEY })
  );

  return (
    <AppContext.Provider value={{ googleGenAI }}>
      {children}
    </AppContext.Provider>
  );
}

export { AppContext, AppProvider };
