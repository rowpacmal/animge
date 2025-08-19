import { useEffect, useState } from 'react';
import useTextToImage from './hooks/useTextToImage';
import PromptBox from './components/ui/PromptBox';
import AppHeader from './components/ui/AppHeader';

function App() {
  const { generatedImage, isGenerating, errorMessage, generateImage } =
    useTextToImage();
  const [image, setImage] = useState<string | null>(null);
  const [promptInput, setPromptInput] = useState(
    'Magical girl, fighting a monster'
  );
  const [seedInput, setSeedInput] = useState(0);
  const [isRandomSeed, setIsRandomSeed] = useState(false);
  const [imageWidth, setImageWidth] = useState(1024);
  const [imageHeight, setImageHeight] = useState(1024);

  useEffect(() => {
    if (!generatedImage) {
      return;
    }

    const blob = new Blob([generatedImage], { type: 'image/jpeg' });
    const objectUrl = URL.createObjectURL(blob);
    setImage(objectUrl);

    return () => {
      URL.revokeObjectURL(objectUrl);
    };
  }, [generatedImage]);

  function randomSeed() {
    setSeedInput(Math.floor(Math.random() * 1000000000));
  }

  return (
    <>
      <AppHeader />

      <main className='flex flex-col items-center justify-center gap-4'>
        <div className='flex gap-4'>
          <div className='flex flex-col gap-4'>
            {isGenerating && <p>Generating image...</p>}
            {errorMessage && <p className='text-red-500'>{errorMessage}</p>}

            <PromptBox
              promptInput={promptInput}
              setPromptInput={setPromptInput}
            />

            <div className='flex gap-4'>
              <label className='flex items-center gap-4'>
                <span>Random seed?</span>

                <input
                  className='mr-2'
                  type='checkbox'
                  checked={isRandomSeed}
                  onChange={(e) => setIsRandomSeed(e.target.checked)}
                />
              </label>

              <input
                className='border border-gray-300 rounded py-2 px-4 w-32'
                type='number'
                value={seedInput}
                onChange={(e) => setSeedInput(parseInt(e.target.value))}
              />

              <button
                className='bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded disabled:opacity-50 disabled:cursor-not-allowed'
                onClick={() => {
                  if (isRandomSeed) {
                    randomSeed();
                  }
                  generateImage(
                    promptInput,
                    imageWidth,
                    imageHeight,
                    seedInput
                  );

                  console.log(seedInput);
                }}
                disabled={isGenerating}
              >
                Generate
              </button>
            </div>
          </div>

          <div className='bg-gray-950'>
            {image && (
              <img
                className='mt-4 max-w-96'
                src={image}
                alt='Generated image'
              />
            )}
          </div>
        </div>
      </main>
    </>
  );
}

export default App;
