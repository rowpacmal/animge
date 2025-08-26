import { useEffect, useState } from 'react';
import { AppFooter, AppHeader, AppMain } from './layout';
import { IconDownload } from '@tabler/icons-react';

function App() {
  const [isDownloading, setIsDownloading] = useState(true);

  useEffect(() => {
    const evtSource = new EventSource(
      'http://localhost:8000/api/v1/downloads/model'
    );
    evtSource.onmessage = (event) => {
      if (event.data === 'DONE') {
        setIsDownloading(false);
        evtSource.close();
      }
    };
    return () => evtSource.close();
  }, []);

  return (
    <>
      {isDownloading ? (
        <div className="flex flex-col justify-center items-center gap-4 h-full w-full">
          <div className="loading loading-ring w-[240px] text-info"></div>

          <div role="alert" className="alert alert-info">
            <IconDownload />
            <span>Downloading resources, please wait...</span>
          </div>
        </div>
      ) : (
        <>
          <AppHeader />
          <AppMain />
          <AppFooter />
        </>
      )}
    </>
  );
}

export default App;
