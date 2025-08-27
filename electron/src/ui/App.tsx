import { useEffect, useState } from 'react';
import { AppFooter, AppHeader, AppMain } from './layout';
import { IconDownload, IconError404 } from '@tabler/icons-react';

function App() {
  const [isDownloading, setIsDownloading] = useState(true);
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    const evtSource = new EventSource(
      'http://localhost:8000/api/v1/downloads/model'
    );
    evtSource.onmessage = (event) => {
      if (event.data.startsWith('DONE')) {
        setIsDownloading(false);
        setIsError(false);
        evtSource.close();
      } else if (event.data.startsWith('ERROR')) {
        setIsDownloading(false);
        setIsError(true);
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
          {isError ? (
            <div className="flex flex-col justify-center items-center gap-4 h-full w-full">
              <div role="alert" className="alert alert-error">
                <IconError404 />
                <span>Failed to download resources</span>
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
      )}
    </>
  );
}

export default App;
