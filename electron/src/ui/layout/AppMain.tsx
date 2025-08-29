import { IconPhotoFilled } from '@tabler/icons-react';
import { useState } from 'react';
import { AdvanceSettings, UserTasks } from '../components';
import styles from './AppMain.module.css';
import { Carousel } from '../components/templates';

export function AppMain() {
  const [images, setImages] = useState<string[]>([]);
  const [prompt, setPrompt] = useState(
    '1boy, bara, solo, male focus, muscular male, random hair style, random hair color, random outfit, random pose, random angle, random background, looking at viewer,'
  );
  const [qualityTags] = useState(
    'masterpiece, high score, great score, absurdres'
  );
  const [negativePrompt] = useState(
    'lowres, bad anatomy, bad hands, text, error, missing finger, extra digits, fewer digits, cropped, worst quality, low quality, low score, bad score, average score, signature, watermark, username, blurry'
  );
  const [width] = useState(896);
  const [height] = useState(1152);
  const [steps] = useState(28);
  const [cfgScale] = useState(5.0);
  // const [seed, setSeed] = useState(0);
  const [batchSize, setBatchSize] = useState(1);
  const [isGenerating, setIsGenerating] = useState(false);

  async function handleGenerateImage() {
    try {
      setIsGenerating(true);
      const response = await fetch(
        'http://localhost:8000/api/v1/pipelines/text-to-image',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            prompt: prompt + ', ' + qualityTags,
            negative_prompt: negativePrompt,
            width,
            height,
            steps,
            cfg_scale: cfgScale,
            seed: Math.floor(Math.random() * 1000000000),
            batch_size: batchSize,
            quality_tags: qualityTags,
          }),
        }
      );
      const data = await response.json();
      // console.log(data);
      // data.paths.forEach(async (path: string) => {
      //   const content: string = `file:///${path.replace(/\\/g, '/')}`;
      //   // console.log(content);
      //   setImages((images) => [...images, content]);
      // });

      setImages(data.paths);
    } catch (error) {
      console.error(error);
    } finally {
      setIsGenerating(false);
    }
  }

  return (
    <main className={`${styles.main} ${styles['dotted-background']}`}>
      <div className={styles['main-container']}>
        <div className="order-1">
          <UserTasks />
        </div>

        <div className="order-2 xl:order-3">
          <AdvanceSettings />
        </div>

        <div className="flex flex-col gap-4 w-full max-w-lg mx-auto xl:max-w-none order-3 xl:order-2">
          <div className="flex flex-col gap-4">
            <div
              className={
                styles['moving-border'] +
                ' relative bg-base-100 rounded-md border border-base-300 p-1 overflow-hidden' +
                (isGenerating ? '' : ' before:hidden')
              }
            >
              <textarea
                className="textarea resize-none h-32 w-full border-secondary focus-visible:outline-secondary relative z-10"
                placeholder="You can generate images by entering prompts here."
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
              ></textarea>
            </div>

            <div className="flex flex-col xl:flex-row justify-between gap-2 px-1">
              <div>
                <select
                  className="select select-secondary w-full xl:w-auto"
                  disabled={isGenerating}
                  value={batchSize}
                  onChange={(e) => setBatchSize(parseInt(e.target.value))}
                >
                  {[1, 2, 3, 4].map((n) => (
                    <option key={n} value={n}>
                      Number of images : {n}
                    </option>
                  ))}
                </select>
              </div>

              <button
                className="flex gap-4 btn btn-secondary"
                onClick={handleGenerateImage}
                disabled={isGenerating}
              >
                <IconPhotoFilled />
                <span>Generate Image</span>
              </button>
            </div>
          </div>

          <div className="flex-1 flex justify-center items-center">
            <Carousel images={images} />
          </div>
        </div>
      </div>
    </main>
  );
}
