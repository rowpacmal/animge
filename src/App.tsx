import useAppStore from './stores/useAppStore';
import reactLogo from '/react.svg';
import viteLogo from '/vite.svg';
import './styles/App.css';

import { InferenceClient } from '@huggingface/inference';
import { useEffect, useState } from 'react';

function App() {
  const count = useAppStore((state) => state.count);
  const increment = useAppStore((state) => state.increment);

  const client = new InferenceClient(import.meta.env.VITE_HF_TOKEN);
  const [img, setImg] = useState<string | null>(null);

  async function test() {
    const response = await client.textToImage({
      model: 'black-forest-labs/FLUX.1-dev',
      inputs: 'a picture of a green bird',
      provider: 'fal-ai',
    });
    console.log(response);

    const objUrl = URL.createObjectURL(response as unknown as Blob);
    setImg(objUrl);

    const img = document.createElement('img');
    img.src = objUrl;
    document.body.appendChild(img);

    // URL.revokeObjectURL(objUrl);
  }

  useEffect(() => {
    return () => {
      URL.revokeObjectURL(img);
    };
  }, [img]);

  return (
    <>
      <div className='flex justify-center items-center'>
        <a href='https://vite.dev' target='_blank'>
          <img src={viteLogo} className='logo' alt='Vite logo' />
        </a>

        <a href='https://react.dev' target='_blank'>
          <img src={reactLogo} className='logo react' alt='React logo' />
        </a>
      </div>

      <h1>Vite + React</h1>

      <div className='card'>
        <button onClick={() => increment()}>count is {count}</button>

        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>

      <p className='read-the-docs'>
        Click on the Vite and React logos to learn more
      </p>

      {img && <img src={img} />}

      <div>
        <button onClick={test}>Test</button>
      </div>
    </>
  );
}

export default App;
