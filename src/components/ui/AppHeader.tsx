import { IconInfoCircleFilled, IconSparkles, IconX } from '@tabler/icons-react';
import { useState } from 'react';

function AppHeader() {
  const [isInfoOpen, setIsInfoOpen] = useState(false);

  return (
    <>
      <header className='flex justify-between items-center p-4 bg-gray-950 w-full shadow-lg'>
        <a className='flex items-center' href='/'>
          <IconSparkles size={32} />

          <h1 className='text-3xl font-bold uppercase select-none'>
            An<span className='text-pink-500'>img</span>e
          </h1>
        </a>

        <button
          className='hover:text-pink-500 transition-colors'
          type='button'
          onClick={() => setIsInfoOpen(true)}
        >
          <IconInfoCircleFilled size={32} />
        </button>
      </header>

      {isInfoOpen && (
        <div className='absolute top-0 left-0 w-full h-full bg-gray-950/50 flex justify-center items-center z-50'>
          <div className='bg-gray-950 p-4 rounded shadow-lg'>
            <div className='flex justify-between items-center mb-4'>
              <h2 className='text-2xl font-bold mb-2'>About</h2>

              <button
                type='button'
                onClick={() => setIsInfoOpen(false)}
                className='hover:text-pink-500 hover:scale-[105%] transition-all'
              >
                <IconX size={24} />
              </button>
            </div>

            <p>
              Animge is an AI image generator that uses the{' '}
              <a
                href='https://pollinations.ai'
                target='_blank'
                rel='noreferrer'
              >
                Pollinations AI API
              </a>{' '}
              to generate images based on text prompts.
            </p>

            <p>
              The app is built with{' '}
              <a
                href='https://react.dev/'
                target='_blank'
                rel='noreferrer'
                className='text-pink-500'
              >
                React
              </a>{' '}
              and{' '}
              <a
                href='https://tailwindcss.com/'
                target='_blank'
                rel='noreferrer'
                className='text-pink-500'
              >
                Tailwind CSS
              </a>
              .
            </p>
          </div>
        </div>
      )}
    </>
  );
}

export default AppHeader;
